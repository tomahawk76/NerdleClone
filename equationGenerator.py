import random

def addGen():
    for i in range(0,4850):
        num1 = random.randint(10,99)
        num2 = random.randint(10,99)
        plus = "+"
        equal = "="

        #Checks to make sure no numbers 100 or over are added
        if num1 + num2 >= 100: 
            print("Nope")
        #Checks to make sure only numbers under 100 and the actual solutions are added
        elif num1 + num2 <= 99:
            f = open(r"C:\Users\student\Desktop\Equations\addition.txt", 'a')
            #Handles formatting based on which number is larger
            if num1 > num2:
                sum = num1 + num2
                if sum < 100 and sum > 9:
                    f.write(str(num1)+ plus + str(num2) + equal + str(sum) + "\n")
            elif num1 < num2:
                sum = num1 + num2
                if sum < 100 and sum > 9:
                    f.write(str(num2)+ plus + str(num1) + equal + str(sum) + "\n")

def subGen():
    for i in range(0,4850):
        num1 = random.randint(10,99)
        num2 = random.randint(10,99)
        sub = "-"
        equal = "="
        #Checks to make sure no numbers 100 or over are added
        #Checks to make sure no numbers 100 or over are added
        if num1 > num2:
            sum = num1 - num2
        elif num1 < num2:
            sum = num2 - num1
        if sum >= 100:
            print("Nope")
        #Checks to make sure only numbers under 100 and the actual solutions are added
        elif sum <= 99:
            f = open(r"C:\Users\student\Desktop\Equations\subtraction.txt", 'a')
            #Handles formatting based on which number is larger
            if num1 > num2:
                sum = num1 - num2
                if sum < 100 and sum > 9:
                    f.write(str(num1)+ sub + str(num2) + equal + str(sum) + "\n")
            elif num1 < num2:
                sum = num2 - num2
                if sum < 100 and sum > 9:
                    f.write(str(num2)+ sub + str(num1) + equal + str(sum) + "\n")

def multGen():
    for i in range(0,4850):
        num1 = random.randint(10,99)
        num2 = random.randint(2,9)
        mult = "*"
        equal = "="
        if num1 > num2:
            sum = num1 * num2
        elif num1 < num2:
            sum = num2 * num1
        if sum >= 1000:
            print("Nope")
        #Checks to make sure only numbers under 100 and the actual solutions are added
        elif sum >= 100:
            f = open(r"C:\Users\student\Desktop\Equations\multiplication.txt", 'a')
            #Handles formatting based on which number is larger
            if num1 > num2:
                sum = num1 * num2
                if sum < 1000 and sum > 100:
                    f.write(str(num1)+ mult + str(num2) + equal + str(sum) + "\n")
            elif num1 < num2:
                sum = num2 * num2
                if sum < 1000 and sum > 100:
                    f.write(str(num2)+ mult + str(num1) + equal + str(sum) + "\n")
    


addGen()
subGen()
multGen()