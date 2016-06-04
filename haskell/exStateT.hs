--import qualified
import Control.Monad.Identity
import Control.Monad.Error
import Control.Monad.Reader
import Control.Monad.State
import Control.Monad.Writer
import Data.Maybe
import Data.Either
import qualified Data.Map as Map

type Name = String

data Exp =  Lit Integer
         |  Var Name
         |  Plus Exp Exp
         |  Abs Name Exp
         |  App Exp Exp
         deriving (Show)

data Value = IntVal Integer
         |   FunVal Env Name Exp
         deriving (Show)

type Env = Map.Map Name Value

eval0 :: Env -> Exp -> Value
eval0 env (Lit i)           = IntVal i
eval0 env (Var n)           = fromJust (Map.lookup n env)
eval0 env (Plus e1 e2 )     = let IntVal i1 = eval0 env e1
                                  IntVal i2 = eval0 env e2
                              in IntVal (i1+i2)

eval0 env (Abs n e)         = FunVal env n e
eval0 env (App e1 e2)       = let val1 = eval0 env e1
                                  val2 = eval0 env e2
                              in case val1 of
                                   FunVal env' n body ->
                                     eval0 (Map.insert n val2 env') body

exampleExp = Lit 12 `Plus` (App (Abs "x" (Var "x")) (Lit 4 `Plus` Lit 2))
--main = print $ eval0 Map.empty exampleExp

type Eval1 a = Identity a
runEval1 :: Eval1 a -> a
runEval1 ev = runIdentity ev

eval1 :: Env -> Exp -> Eval1 Value
eval1 env (Lit i)           = return $ IntVal i
eval1 env (Var n)           = return $ fromJust $ Map.lookup n env
eval1 env (Plus e1 e2)      = do IntVal i1 <- eval1 env e1
                                 IntVal i2 <- eval1 env e2
                                 return $ IntVal (i1+i2)
eval1 env (Abs n e)         = return $ FunVal env n e
eval1 env (App e1 e2)       = do val1 <- eval1 env e1
                                 val2 <- eval1 env e2
                                 case val1 of
                                   FunVal env' n body ->
                                     eval1 (Map.insert n val2 env') body


-- main = print $ runEval1 $ eval1 Map.empty exampleExp
{--
instance (Error e) => Monad (Either e) where
  return         = Right
  Left  l >>= _  = Left l
  Right r >>= k  = k r
  fail msg       = Left (strMsg msg)

class (Monad m) => MonadError e m | m -> e where
  throwError :: e -> m a
  catchError :: m a -> ( e -> m a) -> m a

class (Monad m) => MonadReader r m | m -> r where
  ask   :: m r
  local :: (r -> r) -> m a -> m a
--} 

type Eval2 a = ErrorT String Identity a
runEval2 :: Eval2 a -> Either String a
runEval2 ev = runIdentity (runErrorT ev)

eval2a        :: Env -> Exp -> Eval2 Value
eval2a env (Lit i)        = return $ IntVal i
eval2a env (Var n)        = return $ fromJust $ Map.lookup n env
eval2a env (Plus e1 e2)   = do IntVal i1 <- eval2a env e1
                               IntVal i2 <- eval2a env e2
                               return $ IntVal (i1+i2)

eval2a env (Abs n e)      = return $ FunVal env n e
eval2a env (App e1 e2)    = do val1 <- eval2a env e1
                               val2 <- eval2a env e2
                               case val1 of
                                 FunVal env' n body ->
                                   eval2a (Map.insert n val2 env') body


--main = print $ runEval2 $ eval2a Map.empty exampleExp

eval2b :: Env -> Exp -> Eval2 Value
eval2b env (Lit i) = return $ IntVal i
eval2b env (Var n) = case Map.lookup n env of
                       Just x -> return x
                       Nothing -> throwError "notInScope"
eval2b env (Plus e1 e2) = do e1' <- eval2b env e1
                             e2' <- eval2b env e2
                             case (e1', e2') of
                               (IntVal i1, IntVal i2) ->
                                 return $ IntVal (i1+i2)
                               _ -> throwError "typeError"
eval2b env (Abs n e) = return $ FunVal env n e
eval2b env (App e1 e2) = do val1 <- eval2b env e1
                            val2 <- eval2b env e2
                            case val1 of
                              FunVal env' n body ->
                                eval2b (Map.insert n val2 env') body
                              _ -> throwError "typeError"
--main = print $ runEval2 $ eval2b Map.empty exampleExp
exampleExp2 = Plus (Lit 1) (Abs "x" (Var "x"))
--main = print $ runEval2 $ eval2b Map.empty exampleExp2
exampleExp3 = Var "x"
--main = print $ runEval2 $ eval2b Map.empty exampleExp3

type Eval3 a = ReaderT Env (ErrorT String Identity) a
runEval3 :: Env -> Eval3 a -> Either String a
runEval3 env ev = runIdentity (runErrorT (runReaderT ev env))

eval3 :: Exp -> Eval3 Value
eval3 (Lit i) = return $ IntVal i
eval3 (Var n) = do env <- ask
                   case Map.lookup n env of
                     Nothing -> throwError "unBound var"
                     Just x  -> return x

eval3 (Plus e1 e2) = do e1' <- eval3 e1
                        e2' <- eval3 e2
                        case (e1',e2') of
                          (IntVal i1, IntVal i2) ->
                            return $ IntVal (i1+i2)
                          _ -> throwError "typeError"

eval3 (Abs n e) = do env <- ask
                     return $ FunVal env n e

eval3 (App e1 e2) = do val1 <- eval3 e1
                       val2 <- eval3 e2
                       case val1 of
                         FunVal env' n body ->
                           local ( const (Map.insert n val2 env')) (eval3 body)
                         _ -> throwError "typeError"


--main = print $ runEval3 Map.empty $ eval3 exampleExp

type Eval4 a = ReaderT Env (ErrorT String (StateT Integer Identity)) a
runEval4 :: Env -> Integer -> Eval4 a -> (Either String a, Integer)
runEval4 env st ev = runIdentity ( runStateT (runErrorT (runReaderT ev env))  st)

tick :: (Num s, MonadState s m) => m ()
tick = do st <- get
          put (st+1)

eval4 (Lit i) = do tick
                   return $ IntVal i
eval4 (Var n) = do tick
                   env <- ask
                   case Map.lookup n env of
                     Nothing -> throwError ("unBoundError")
                     Just x -> return x
eval4 (Plus e1 e2) = do tick
                        e1' <- eval4 e1
                        e2' <- eval4 e2
                        case (e1', e2') of
                          (IntVal i1, IntVal i2) ->
                            return $ IntVal (i1+i2)
                          _ -> throwError "typeError"

eval4 (Abs n e) = do tick
                     env <- ask
                     return $ FunVal env n e

eval4 (App e1 e2) = do tick
                       val1 <- eval4 e1
                       val2 <- eval4 e2
                       case val1 of
                         FunVal env' n body ->
                           local (const (Map.insert n val2 env')) (eval4 body)
                         _ -> throwError "typeError"

main = print $ runEval4 Map.empty 0 $ eval4 exampleExp
