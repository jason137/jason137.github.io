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
