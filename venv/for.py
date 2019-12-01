for var in range(0, 8):
    print(var)


count = 0
while count < 5:
    print(count)
    count += 1 #same like count=1

for var in range(1, 10):
    if var % 2 == 0:
        print(var)
        break #exit a for loop or a while loop
    print("Not an even number")

print("out of the loop")

for var in range(10):
    if var % 2==0:
        print("in if scope")
        continue #stay in the loop
    print(var)

print("out of the loop")

my_list = [2, 12, 1986, 22, 2, 1987, 24, 5, 2012, 9892, 542, 23, 82, 90, 561, 673, 41, 87, 25, 45]

for number in my_list:
    if number > 500:
        continue
    if number % 2 == 0:
        print(number)
