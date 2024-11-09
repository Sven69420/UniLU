-- Problem A
-- Part 1
combinations :: Int -> [a] -> [[a]]
combinations 0 _ = [[]]
combinations _ [] = []
combinations k (x:xs)
  | k < 0 = []
  | otherwise = [ x:ys | ys <- combinations (k-1) xs ] ++ combinations k xs


-- Part 2
type Candidate = (String, [String])

allHaveSkill :: String -> [Candidate] -> Bool
allHaveSkill skill = all (\(_, skills) -> skill `elem` skills)

candidates1 :: [Candidate]
candidates1 = [("Alice", ["Python", "Java"]), ("Charlie", ["Python", "C++"])]

candidates2 :: [Candidate]
candidates2 = [("Alice", ["Python", "Java"]), ("Bob", ["JavaScript"])]


-- Part 3
validTeamCombinations :: [Candidate] -> String -> [[String]]
validTeamCombinations candidates skill =
    let
        -- Step 1: Filter candidates with the required skill and extract names
        namesWithSkill = [ name | (name, skills) <- candidates, skill `elem` skills ]

        -- Step 2: Generate combinations for all possible team sizes
        teamSizes = [1 .. length namesWithSkill]
        teams = concatMap (`combinations` namesWithSkill) teamSizes
    in
        teams

candidates3 :: [Candidate]
candidates3 = [("Alice", ["Python", "Java"]), ("Bob", ["JavaScript"]), ("Charlie", ["Python", "C++"])]

candidates4 :: [Candidate]
candidates4 = [("Alice", ["Python"]), ("David", ["Python", "JavaScript"])]


-- Part 4
countValidTeams :: [Candidate] -> String -> Int
countValidTeams candidates skill = length (validTeamCombinations candidates skill)


-- Problem B
-- Part 1
relevantLocations :: [[Int]] -> [Int]
relevantLocations garden = foldr f [] indexedGarden
  where
    flatGarden     = concat garden -- flatten 2d garden into 1d list
    lastIdx        = length flatGarden - 1 -- index of last element
    indexedGarden  = zip [0..] flatGarden -- pair each element with its index
    f (idx, val) acc
      | idx == 0 || idx == lastIdx || val == 1 = idx : acc -- include starting, ending and ripe strawberry locations
      | otherwise = acc


-- Part 2
gardenacci :: Int -> Integer
gardenacci n
    | n < 0 = error "Negative index not allowed"
    | n == 0 = 1
    | n == 1 = 1
    | n == 2 = 1
    | otherwise = go 3 1 1 1  -- Starting recursion from index 3 with initial values
  where
    go :: Int -> Integer -> Integer -> Integer -> Integer
    go i gPrev1 gPrev2 gPrev3
        | i > n     = gPrev1 -- return result if desired index is reached
        | otherwise = let gCurrent = gPrev1 + gPrev3
                          gPrev1'  = gCurrent -- update previous values for next iteration
                          gPrev2'  = gPrev1
                          gPrev3'  = gPrev2
                      in go (i + 1) gPrev1' gPrev2' gPrev3' -- recursion call with updated values


-- Part3
numberPaths :: Int -> [[Int]] -> Integer
numberPaths n garden =
  let
    relevantPos = relevantLocations garden -- use previous function to get list of relevant positions
    segments = zip relevantPos (tail relevantPos) -- create pairs of consecutive relevant positions
    totalPaths = foldl (\acc (start, end) -> -- fold over segments to compute total paths
      let
        d = end - start 
        forbiddenPositions = [p - start | p <- relevantPos, p > start, p < end] -- adjust forbidden positions relative to segment start
        ways = numWays d forbiddenPositions 
      in
        acc * ways) 1 segments -- multiply number of ways with each segment
  in
    totalPaths -- returns total



numWays :: Int -> [Int] -> Integer
numWays d forbiddenPositions =
  let
    forbiddenSet = forbiddenPositions  -- List of forbidden positions
    dp = map dpValue [0..d] -- dynamic map for positions 0 to d
    dpValue 0 = 1 -- base case
    dpValue i
      | i `elem` forbiddenSet = 0 -- fobidden results in 0 ways
      | otherwise =
        let a = if i - 1 >= 0 then dp !! (i - 1) else 0 -- 1 step move
            b = if i - 3 >= 0 then dp !! (i - 3) else 0 -- 3 step move
        in a + b -- total ways to reach position i
  in
    dp !! d -- returns total




-- Test Cases
testA1 :: Bool
testA1 = combinations 2 ["Alice", "Bob", "Charlie"] == [["Alice", "Bob"], ["Alice", "Charlie"], ["Bob", "Charlie"]]

testB1 :: Bool
testB1 = allHaveSkill "Python" candidates1

testB2 :: Bool
testB2 = not (allHaveSkill "JavaScript" candidates2)  -- Expected: True (since Alice doesn't have "JavaScript")

testC1 :: Bool
testC1 = validTeamCombinations candidates3 "Python" == [["Alice"], ["Charlie"], ["Alice", "Charlie"]]

testC2 :: Bool
testC2 = validTeamCombinations candidates4 "Python" == [["Alice"], ["David"], ["Alice", "David"]]

testD1 :: Bool
testD1 = countValidTeams candidates3 "Python" == 3

testD2 :: Bool
testD2 = countValidTeams candidates4 "JavaScript" == 1

testE1 :: Bool
testE1 = numberPaths 2 [[0,0],[0,1]] == 2

testE2 :: Bool
testE2 = numberPaths 3 [[0,0,0],[1,0,0],[1,0,0]] == 4

testE3 :: Bool
testE3 = numberPaths 5 [[0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,1,0,0,0],
                        [0,0,0,0,0],
                        [0,0,1,1,0]] == 1681


-- created for debugging purposes 
garden420 :: [[Int]]
garden420 = [[0, 0, 0, 0, 0],
             [0 ,1 ,1 ,1, 0],
             [0, 1, 1, 1, 0],
             [1, 1, 1, 0, 0],
             [0, 0, 0, 0, 0]]

gardenTestResult :: Bool
gardenTestResult = relevantLocations garden420 == [0,6,7,8,11,12,13,15,16,17,24]

gardenacciTest1 :: Bool
gardenacciTest1 = gardenacci 0 == 1

gardenacciTest2 :: Bool
gardenacciTest2 = gardenacci 2 == 1

gardenacciTest3 :: Bool
gardenacciTest3 = gardenacci 10 == 28


-- Main
main :: IO ()
main = do
  putStrLn "--------------------"
  putStrLn $ "Test A1 Passed: " ++ show testA1
  putStrLn "--------------------"
  putStrLn $ "Test B1 Passed: " ++ show testB1
  putStrLn $ "Test B2 Passed: " ++ show testB2
  putStrLn "--------------------"
  putStrLn $ "Test C1 Passed: " ++ show testC1
  putStrLn $ "Test C2 Passed: " ++ show testC2
  putStrLn "--------------------"
  putStrLn $ "Test D1 Passed: " ++ show testD1
  putStrLn $ "Test D1 Passed: " ++ show testD2
  putStrLn "--------------------"
  putStrLn $ "Test E1 Passed: " ++ show testE1
  putStrLn $ "Test E2 Passed: " ++ show testE2
  putStrLn $ "Test E3 Passed: " ++ show testE3
  putStrLn "--------------------"
  putStrLn $ "Garden Test Match Expected Result: " ++ show gardenTestResult ++ " (" ++ show (relevantLocations garden420) ++ ")" -- expected [0,6,7,8,11,12,13,15,16,17,24]
  putStrLn "--------------------"
  putStrLn $ "Test passed: " ++ show gardenacciTest1 ++ " | Gardenacci 0: " ++ show (gardenacci 0)
  putStrLn $ "Test passed: " ++ show gardenacciTest2 ++ " | Gardenacci 2: " ++ show (gardenacci 2)
  putStrLn $ "Test passed: " ++ show gardenacciTest3 ++ " | Gardenacci 10: " ++ show (gardenacci 10)
  putStrLn "--------------------"
