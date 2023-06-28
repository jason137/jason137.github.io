-- comment

{-
    block comment
-}

double :: Num a => a -> a
double x = x + x

quad :: Num a => a -> a
quad x = double (double x)

half_length :: [a] -> Int
half_length xs = length(xs) `div` 2

halve :: [a] -> ([a], [a])
halve xs = (take k xs, drop k xs)
    where k = half_length(xs)

qsort :: Ord a => [a] -> [a]
qsort [] = []
qsort (x: xs) = qsort smaller ++ [x] ++ qsort larger
    where
        smaller = [a | a <- xs, a <= x]
        larger = [b | b <- xs, b > x]

factors :: Int -> [Int]
factors n = [k | k <- [1..n], n `mod` k == 0]

prime :: Int -> Bool
prime n = factors n == [1, n]

primes_below :: Int -> [Int]
primes_below n = [k | k <- [2..n], prime k]

prime_facs :: Int -> [Int]
prime_facs n = [k | k <- factors n, k <= sqrt fromIntegral n, prime k]
