
import Control.Monad (forever)
import Control.Monad.Trans.Class (lift)
import Control.Monad.Trans.State
import Data.Map as M

loop :: StateT (Map String String) IO r
loop = forever $ do
    l <- lift getLine
    case (words l) of
        ["get", key]      -> do
            mval <- gets (M.lookup key)
            lift $ putStrLn $ case mval of
                Nothing  -> "Invalid key"
                Just val -> val
        ["set", key, val] -> modify (M.insert key val)
        _                 -> lift $ putStrLn "Invalid command"

repl :: IO r
repl = evalStateT loop M.empty

main = repl
