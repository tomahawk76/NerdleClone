import random
import pyinputplus as pyinp

def main():
    comboPicker = random.randrange(1,2) #1 is addition, #2 is subtraction, #3 is multiplication, #4 is division
    if comboPicker == 1:
        combo1()
    if comboPicker == 2:
        #combo2()

    def combo1():
        arithmeticPicker = random.randrange(1,2)
        num1 = random.randint(100,300)
        num2 = random.randint(10,99)
        if arithmeticPicker == 1:
            for tries in range(1,10,1):
                guess = pyinp.inputStr("What is your guess?")
                if num1 > num2:
                    generatedAnswer = num1 + num2
                    generatedEquation = str[num1, "+", num2, "=", generatedAnswer]
                    print(generatedEquation)
                    if guess == generatedEquation:
                        print("Correct!")
                else:
                    generatedAnswer = num2 + num1
                    generatedEquation = str[num2, "+", num1, "=",generatedAnswer]
                    print(generatedEquation)
                    if guess == generatedEquation:
                        print("Correct!")

if __name__ == "__main__":
    main()