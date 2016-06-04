--import qualified
import Data.Map as M
import Control.Monad.State
import System.Random

threeCoins :: StdGen -> (Bool, Bool, Bool)
threeCoins gen =
  let (fstCoin, newGen) = random gen
      (sndCoin, newGen') = random newGen
      (trdCoin, newGen'') = random newGen'
  in (fstCoin, sndCoin, trdCoin)

type Stack = [Int]

--pop :: Stack -> (Int,Stack)
--pop (x:xs) = (x,sx)

--push :: Int -> Stack -> ((), Stack)
--push a xs = ((), a:xs)

pop :: State Stack Int
pop = state $ \(x:xs) -> (x,xs)

push :: Int -> State Stack ()
push a = state $ \xs -> ((), a:xs)

stackManip :: State Stack Int
stackManip = do
  push 3
  a <- pop
  pop
  
