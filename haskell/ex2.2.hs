--import qualified
import Data.Map as M
import Control.Monad.State

type History = [String]
data Command = Invalid | End | Get String | Set String String
data DB = DB (M.Map String String)
data Result = Result (Maybe String) Bool


execCmd :: Command -> State DB Result
execCmd (Set key val) = do
  DB map<- get
  let newMap = M.insert key val map
  let result = Result Nothing False
  put (DB newMap)
  state $ \s -> (result, DB newMap)
execCmd (Get key) = do
  DB map <- get
  let result = Result (M.lookup key map) False
  state $ \s -> (result, s)
execCmd End = do
  let result = Result Nothing True
  state $ \s -> (result, s)
execCmd Invalid = do
  let result = Result (Just "Invaid Cmd") False
  state $ \s -> (result, s)
 
getCmd = getLine >>= return . parseCmd

parseCmd :: String -> Command
parseCmd s =
  case words s of
    ("set":key:value:_) -> Set key value
    ("get":key:_)       -> Get key
    ("end":_)           -> End
    _                   -> Invalid

displayResult :: Result -> IO Result
displayResult r@(Result (Just s) _ ) = putStrLn s >> return r
displayResult r                      = return r

repl db = do
  cmd <- getCmd
  let st = execCmd cmd
  let (r,s) = runState st db
  Result _ end  <- displayResult r
  if end
    then return ()
    else repl s

main = repl (DB M.empty)

