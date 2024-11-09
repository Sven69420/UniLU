-- Problem A: Magical Potion Mixing
mixPotions :: [a] -> [a] -> [a]
mixPotions [] ys = ys -- in case first list is empty
mixPotions xs [] = xs -- in case second list is emtpy
mixPotions (x:xs) (y:ys) = x : y : mixPotions xs ys -- recursion if both lists are non-empty

-- Test cases, ignore
testA1 :: Bool
testA1 = mixPotions ["Unicorn Horn", "Dragon Scale", "Phoenix Feather"] ["Mermaid's Tear", "Goblin Ear"]
       == ["Unicorn Horn", "Mermaid's Tear", "Dragon Scale", "Goblin Ear", "Phoenix Feather"]

testA2 :: Bool
testA2 = mixPotions ["Pixie Dust"] ["Fairy Wing", "Elf Ear", "Goblin Tooth"]
       == ["Pixie Dust", "Fairy Wing", "Elf Ear", "Goblin Tooth"]



-- Problem B: Digital Root
digitalRoot :: Int -> Int
digitalRoot n
  | n < 10    = n -- test if number is a single digit
  | otherwise = digitalRoot (sumDigits n) -- call helper function

-- Helper function
sumDigits :: Int -> Int
sumDigits 0 = 0 -- sum of 0 is 0
sumDigits n = (n `mod` 10) + sumDigits (n `div` 10) -- adds last digit to the sum of the remaining digits

-- List mapping
digitalRootList :: [Int] -> [Int]
digitalRootList = map digitalRoot

-- Test cases, ignore
testB1 :: Bool
testB1 = digitalRoot 3 == 3

testB2 :: Bool
testB2 = digitalRoot 1408 == 4

testB3 :: Bool
testB3 = digitalRootList [2, 23, 654, 12, 39, 12347] == [2, 5, 6, 3, 3, 8]



-- Problem C: Tower of Hanoi
hanoi :: Int -> Int
hanoi 1 = 1
hanoi n = 2 * hanoi (n-1) + 1

{-
Strategy:
  Recursion

Base Case:
  for n = 1, only one move is needed, hence 1 = 1

Recursive Cases:
  for every n > 1, the minimum number of needed moves can be calculated:
    - "hanoi (n-1)": moving the top n-1 disks to the extra rod (takes n - 1 moves)
    - "+ 1": moving the largest disk to the destination rod (takes exactly 1 move)
    - "2 *": moving the n-1 disks from the extra rod the the destination rod (also takes n - 1 moves, hence we multiply "hanoi (n-1)" by 2)
-}

-- Test cases, ignore
testC1 :: Bool
testC1 = hanoi 3 == 7

testC2 :: Bool
testC2 = hanoi 14 == 16383



-- Probelm D: Music Theory
-- Infinite list of piano keys
infiniteKeys :: [String]
infiniteKeys = cycle baseKeys -- generate and cycle through infinite list of given base keys
  where
    baseKeys = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

-- Step conversion function (from string to integer list)
patternToSteps :: String -> Maybe [Int]
patternToSteps = mapM charToStep
  where
    charToStep 'W' = Just 2 -- 'W' represents a whole step
    charToStep 'H' = Just 1 -- 'H' represents a half step
    charToStep _   = Nothing -- returns 'Nothing' for invalid pattern (therefore '-> Maybe [Int]')

-- Custom elemIndex function (since we are limited to "Prelude" import, which is automatically imported by Haskell, not needed with Data.List (elemIndex) import)
myElemIndex :: Eq a => a -> [a] -> Maybe Int
myElemIndex x xs = myElemIndexHelper x xs 0
  where
    myElemIndexHelper _ [] _ = Nothing
    myElemIndexHelper y (z:zs) n
      | y == z    = Just n
      | otherwise = myElemIndexHelper y zs (n + 1)

-- Custom intercalate function (since we are limited to "Prelude" import, not needed with Data.List (intercalate) import)
myIntercalate :: String -> [String] -> String
myIntercalate _ []  = ""
myIntercalate _ [x] = x
myIntercalate sep (x:xs) = x ++ sep ++ myIntercalate sep xs

-- Music scale generation function
musicScale :: String -> String -> String
musicScale root pattern =
  -- finds index of root note
  case myElemIndex root baseKeys of 
    -- if no root note found, throw error
    Nothing -> error "Invalid root note" 
    Just startIndex ->
      -- converts string into list of steps (Int)
      case patternToSteps pattern of 
        -- if pattern contains an invalid character, throw error
        Nothing -> error "Invalid pattern" 
        Just steps ->
          -- compute cumulative sum of steps
          let positions = scanl (+) 0 steps
              -- gets absolute index in "baseKeys" and wraps around list if index exceeds list length
              indices = map (\pos -> (startIndex + pos) `mod` length baseKeys) positions
              -- builds list of notes corresponding to the index
              notes = map (baseKeys !!) indices 
          -- joins the notes with hyphens '-'
          in myIntercalate "-" notes 
  where
    baseKeys = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

-- Test case, ignore
testD1 :: Bool
testD1 = musicScale "G" "WWHWWWH" == "G-A-B-C-D-E-F#-G"




{-
-- Output test code passes / failures (should all return 'True')
main :: IO ()
main = do
  putStrLn "--------------------"
  putStrLn $ "Test A1 Passed: " ++ show testA1
  putStrLn $ "Test A2 Passed: " ++ show testA2
  putStrLn "--------------------"
  putStrLn $ "Test B1 Passed: " ++ show testB1
  putStrLn $ "Test B2 Passed: " ++ show testB2
  putStrLn $ "Test B3 Passed: " ++ show testB3
  putStrLn "--------------------"
  putStrLn $ "Test C1 Passed: " ++ show testC1
  putStrLn $ "Test C2 Passed: " ++ show testC2
  putStrLn "--------------------"
  putStrLn $ "Test D1 Passed: " ++ show testD1
  putStrLn "--------------------"
-}