import pyinputplus as pyinp
import random

def main():

    print("Welcome to Nerdle! \n")
    print("----------------------------------------\n")
    print("All equations have to be 8 characters long! \n")

    def Addition(prompt):
        with open('addition.txt') as f:
            lines = f.read().splitlines()
        myline = random.choice(lines)
        print(myline)
        while prompt != myline or len(prompt) != 8:
            prompt = pyinp.inputStr("Incorrect! Take another guess with 8 characters!\n")
        if prompt == myline and len(prompt) == 8:
            print("Correct!")
        

    def Subtraction(prompt):
        with open('subtraction.txt') as f:
            lines = f.read().splitlines()
        myline = random.choice(lines)
        print(myline)
        while prompt != myline or len(prompt) != 8:
            prompt = pyinp.inputStr("Incorrect! Take another guess with 8 characters!\n")
        if prompt == myline and len(prompt) == 8:
            print("Correct!")
    
    def Multiplication(prompt):
        with open('multiplication.txt') as f:
            lines = f.read().splitlines()
        myline = random.choice(lines)
        print(myline)
        while prompt != myline or len(prompt) != 8:
            prompt = pyinp.inputStr("Incorrect! Take another guess with 8 characters!\n")
        if prompt == myline and len(prompt) == 8:
            print("Correct!")
        
    
    # 1 = Addition, 2 = Subtraction, 3 = Multiplication, 4 = Division
    picker = random.randint(1,3)
    if picker == 1:
        print("Addition")
        Addition(pyinp.inputStr("Take a guess!\n"))
    if picker == 2:
        print("Subtraction")
        Subtraction(pyinp.inputStr("Take a guess!\n"))
    if picker == 3:
        print("Multiplication")
        Multiplication(pyinp.inputStr("Take a guess!\n"))
    
    
if __name__ == "__main__":
    main()

