fizzbuzz :: Int -> Int -> [String]
fizzbuzz start end = map fizzbuzziter [start .. end]
    where
      fizzbuzziter :: Int -> String
      fizzbuzziter i
        | (i `mod` 15 == 0) = "FizzBuzz"
        | (i `mod` 3 == 0) = "Fizz"
        | (i `mod` 5 == 0) = "Buzz"
        | otherwise = show i

main = sequence (map putStrLn (fizzbuzz 1 100))
