############################################
# Tech Check 4 - Provided Starter File
# Take this provided single-grade entry program and re-work it to use a function, to allow the customized entry of 6 different course grades, and
# to calculate a final grade point average for all six courses.
############################################

# Student Name: Alex Barr W0487099

#Introduction Message Function
def ProgramIntroduction():
    print("Grade Point Calculator\n")
    print("Valid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0.\n")

#Get Letter Grade from user
def GetLetterGrade():
    return input("Please enter a letter grade : ").upper()

#Get Modifier from user
def GetModifier():
    return input("Please enter a modifier (+, - or nothing) : ")

#Modifier Math
def Modifier(_modifier, _letterGrade, _numericGrade):
    if _modifier == "+":
        if _letterGrade != "A" and _letterGrade != "F": # Plus is not valid on A or F
            _numericGrade += 0.3
        elif _modifier == "-":
            if _letterGrade != "F":     # Minus is not valid on F
                _numericGrade -= 0.3
    return _numericGrade

#Convert letter grade to number
def ConvertLetterToNumber(_letterGrade:str):
    if _letterGrade == "A":
        _numericGrade = 4.0
    elif _letterGrade == "B":
        _numericGrade = 3.0
    elif _letterGrade == "C":
        _numericGrade = 2.0
    elif _letterGrade == "D":
        _numericGrade = 1.0
    elif _letterGrade == "F":
        _numericGrade = 0.0
    else:
        #If an invalid entry is made
        #print("You entered an invalid letter grade.") #come back to this later
        pass #TODO ERROR CHECKING WILL GO HERE    
    return _numericGrade

# main() FUNCTION
def main():

    ProgramIntroduction() #Show introduction and instruction messages

    numericGrade = 0.0

    #Gather user inputs
    letterGrade = GetLetterGrade()
    modifier = GetModifier()

    # Determine base numeric value of the grade
    numericGrade = ConvertLetterToNumber(letterGrade)
    
    # Determine whether to apply a modifier
    numericGrade = Modifier(modifier, letterGrade, numericGrade)

    # Output final message and result, with formatting
    print("The numeric value is: {0:.1f}".format(numericGrade))

#PROGRAM EXECUTION STARTS HERE
main()