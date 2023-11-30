import Data.List
import Data.List.Split

parseInput2 :: [String] -> [[Int]]
parseInput2 = aux [] []
  where
    aux acc1 acc [] = acc1 : acc
    aux acc1 acc (line : lines) =
      case reads line of -- The read typeclass turns strings to their corresponding types
        [(n, "")] -> aux (n : acc1) acc  lines
        _         -> aux [] (acc1 : acc) lines

parseLines :: [String] -> [[Int]]
parseLines = (map . map) read . splitOn [""]

solver1 :: [[Int]] -> Int
solver1 elves = maximum $ map sum elves

solver2 :: [[Int]] -> Int
solver2 elves = sum $ take 3 $ sortBy (flip compare) (map sum elves)
  
main :: IO ()
main = do
  contents <- readFile "../inputs/1.txt"
  let parsed = parseLines $ lines contents
  print (solver1 parsed)
  print (solver2 parsed)

-- main :: IO ()
-- main =
--   readFile "../inputs/1.txt" >>= \contents ->
--     let parsed = parseInput $ lines contents
--     in print (solver1 parsed)
--     >> print (solver2 parsed)
