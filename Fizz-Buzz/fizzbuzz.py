def fizzbuzz(start, end, num1, num2):
    for num in range(start,end+1):
        if num % num1 == 0 and num % num2 == 0:
            print('FIZZ-BUZZ - Number: {} is a Multiple of both {} & {}'.format(num,num1,num2))
        elif num % num1 == 0:
            print('FIZZ - Number: {} is a Multiple of {}'.format(num,num1))
        elif num % num2 == 0:
            print('BUZZ - Number: {} is a Multiple of {}'.format(num,num2))
        else:
            print('{}'.format(num))

while True:
    start = input("Please Enter a Start Number: ")
    try:
        start = int(start)
        break
    except:
        print('Try again')

while True:
    end = input("Please Enter a End Number: ")
    try:
        end = int(end)
        break
    except:
        print('Try again')

while True:
    num1 = input("Please Enter First Multiple: ")
    try:
        num1 = int(num1)
        break
    except:
        print('Try again')

while True:
    num2 = input("Please Enter Second Multiple: ")
    try:
        num2 = int(num2)
        break
    except:
        print('Try again')

fizzbuzz(start,end,num1,num2)