import Data.List (union)
import Control.Monad
problem_1' = sum (union [3,6..999] [5,10..999])

fibs = 1 : 1 : zipWith (+) fibs (tail fibs) 
problem_2' = sum [ x | x <- takeWhile (<= 1000000) fibs, even x]


problem_22 = sumEvenFibsLessThan 1000000

sumEvenFibsLessThan n = (a+b-1) `div` 2
  where
    n2 = n `div` 2
    (a,b) = foldr f (0,1)
            . takeWhile ((<= n2) . fst)
            . iterate times2E $ (1,4)
    f x y | fst z <= n2 = z
          | otherwise = y
          where z = x `addE` y
addE (a,b) (c,d) = (a*d+b*c-4*ac, ac+b*d)
  where ac = a*c

times2E (a,b) = addE (a,b) (a,b)

tmp1 = iterate times2E $ (1,4)
tmp2 = iterate times2E (1,4)



readFiveLines :: IO [Int]
readFiveLines = replicateM 5 readLn

addIndex :: [Int] -> [(Int, Int)]
addIndex xs = zip xs [0..]

findMaxIndx :: [Int] -> Int
findMaxIndx xs = snd(maximum (addIndex xs))

loop :: ()
loop = loop

main :: IO ()
main = do xs <- readFiveLines
          putStrLn ( show (findMaxIndx xs))
