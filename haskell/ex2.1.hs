--import qualified
import Data.Map as M
import Control.Monad.State

type History = [String]

data Result = Result (Maybe String) Bool DB

data Command = Invalid | End | Get String | Set String String
data DB = DB (M.Map String String)


execCmd :: DB -> Command -> IO Result
execCmd db@(DB map) c@(Set key val) = do
  let newMap = M.insert key val map
  return $ Result Nothing False (DB newMap)
execCmd db@(DB map) c@(Get key) = do
  return $ Result (M.lookup key map) False db
execCmd db c@End = do
  return $ Result Nothing True db
execCmd db c@Invalid = do
  return $ Result Nothing False db

getCmd = getLine >>= return . parseCmd

parseCmd :: String -> Command
parseCmd s =
  case words s of
    ("set":key:value:_) -> Set key value
    ("get":key:_)       -> Get key
    ("end":_)           -> End
    _                   -> Invalid

displayResult :: Result -> IO Result
displayResult r@(Result (Just s) _ _) = putStrLn s >> return r
displayResult r                       = return r

continue :: Result -> IO ()
continue (Result _ end db) = if end then return () else repl db

repl state = getCmd >>= execCmd state >>= displayResult >>= continue

main = repl(DB M.empty)
