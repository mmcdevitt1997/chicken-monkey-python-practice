import random
number = list()
for i in range(100):
    number.append(random.randrange(1, 100))
    if (i % 7 == 0 and i % 5 == 0):
        print("ChickenMonkey")
    elif(i % 7 == 0):
        print("Monkey")
    elif(i % 5 == 0):
          print("Chicken")
    else:
       print(i)
