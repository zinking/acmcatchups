--import qualified
import Data.Map as M

type History = [String]

data Result = Result (Maybe String) Bool DB

data Command = Command { name  :: String,
                         key   :: Maybe String,
                         value :: Maybe String
                       }
data DB = DB (M.Map String String)

cmdKey c = let Just s = key   c in s
cmdValue c = let Just s = value c in s

runSetCmd :: Command -> DB -> IO (Maybe String, DB)
runSetCmd c db@(DB map) = do
  let newMap = M.insert (cmdKey c) (cmdValue c) map
  return  (Nothing, DB newMap)

runGetCmd :: Command -> DB -> IO (Maybe String, DB)
runGetCmd c db@(DB map) = return  (M.lookup (cmdKey c) map, db)

execCmd :: DB -> Command -> IO Result
execCmd db c@(Command name key value ) = do
  (output, newDB) <- case name of
    "set" -> runSetCmd c db
    "get" -> runGetCmd c db
    _     -> return (Nothing, db)
  return  $ Result output end newDB
  where
    end = case name of
               "end" -> True
               _     -> False

getCmd = getLine >>= return . parseCmd

parseCmd :: String -> Command
parseCmd s =
  case words s of
    (name:key:value:_) -> Command name (Just key) (Just value)
    (name:key:[])      -> Command name (Just key) Nothing
    (name:[])          -> Command name Nothing Nothing

displayResult :: Result -> IO Result
displayResult r@(Result (Just s) _ _) = putStrLn s >> return r
displayResult r                       = return r

continue :: Result -> IO ()
continue (Result _ end db) = if end then return () else repl db

repl state = getCmd >>= execCmd state >>= displayResult >>= continue

main = repl(DB M.empty)
