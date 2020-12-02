#There is no magic number, from 0 - max value
def num_one(message):
    while True:
        try:
            num_one = int(input(message))
        except ValueError:
            print("Choose  a number between 0 to max value")
            continue
        else:
            return num_one
            break
        #Avoid the calculator to crash.
def num_two(message):
    while True:
        try:
            num_two = int(input(message))
        except ValueError:
            print("Choose  a number between 0 to max value")
            continue
        else:
            return num_two
            break


        #MAIN STARTS HERE:
while True:

    val1 = num_one("Enter 1st number: ")
    op = input("Enter operator (+ , -, *, /): ")

    val2 = num_two("Enter 2nd number: ")

    if op == "+":
        sum = (val1+val2)
        if  sum < 50:
            print ("Less Then Fifty")
        elif sum == 50:
            print ("Fifty")
        elif sum > 50 and sum <= 99:
            print ("Almost Hundred")
        elif sum == 100:
            print ("Spot On")
        elif sum > 100:
            print ("Missed The Spot!")
    elif op == "-":
        sum = (val1-val2)
        if  sum < 50:
            print ("Less Then Fifty")
        elif sum == 50:
            print ("Fifty")
        elif sum > 50 and sum <= 99:
            print ("Almost Hundred")
        elif sum == 100:
            print ("Spot On")
        elif sum > 100:
            print ("Missed The Spot!")
    elif op == "*":
        sum = (val1*val2)
        if  sum < 50:
            print ("Less Then Fifty")
        elif sum == 50:
            print ("Fifty")
        elif sum > 50 and sum <= 99:
            print ("Almost Hundred")
        elif sum == 100:
            print ("Spot On")
        elif sum > 100:
            print ("Missed The Spot!")
    elif op == "/":
        sum = (val1/val2)
        if  sum < 50:
            print ("Less Then Fifty")
        elif sum == 50:
            print ("Fifty")
        elif sum > 50 and sum <= 99:
            print ("Almost Hundred")
        elif sum == 100:
            print ("Spot On")
        elif sum > 100:
            print ("Missed The Spot!")

    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        continue
    else:
        print("Goodbye")
        break
    #22:58
