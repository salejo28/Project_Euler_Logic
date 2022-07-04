def moduleNum(num):
  array = []
  for i in range(1, 21):
    array.append(num % i)
  array2 = []
  for number in array:
    if number == 0:
      array2.append(number)
  # len([elem for elem in array if elem != 0])
  if len(array2) == 20:
    return True
  return False  

def getSmallestDivder(): 
  num = 1
  array = []
  while(num <= 232792561):
    module = moduleNum(num)
    if (module == True):
      array.append(num)

    num += 1

  return array

dividers = getSmallestDivder()

print(dividers)