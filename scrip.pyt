firstDigit = range(256)
secondDigit = range(256)
thirdDigit = range(256)
fourthDigit = range(256)
for x in firstDigit:
  for y in secondDigit:
    for z in thirdDigit:
        for o in fourthDigit:
            first = str(x)
            second = str(y)
            third = str(z)
            fourth = str(o)
            print(first + "." + second + "." + third + "." + fourth)