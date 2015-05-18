toNum :: Char -> Int
toNum x = fromEnum x - fromEnum 'a'
encrypt :: String -> String -> String
encrypt message password =
  map (toEnum . (+97) . (`mod` 26) . (uncurry (-)))
  . zip (map toNum message)
  $ (concat . repeat . map toNum $ password)


