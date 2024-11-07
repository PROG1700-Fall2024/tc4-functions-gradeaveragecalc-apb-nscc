############################################
# Tech Check 4 - Provided Starter File
# Take this provided single-grade entry program and re-work it to use a function, to allow the customized entry of 6 different course grades, and
# to calculate a final grade point average for all six courses.
############################################

# Student Name: Alex Barr W0487099

#Initialization

classes = ["PROG1700", "NETW1700", "OSYS1200", "WEBD1000", "DBAS1007"]
numericGrade = 0.0 #Moved this here so it doesn't get messed up if I change main() too much
finalGrade = [] #To hold final grades in corresponding indexes to classes list
GPA = 0.0 #Final Grade Point Average (Normally I wouldn't use abbreviations/acronyms but everyone knows what a GPA is)

#Introduction Message Function
def ProgramIntroduction():
    print("Grade Point Calculator\n")
    print("Valid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0.\n")

#Get Letter Grade from user
def GetLetterGrade(_program): 
    return input(f"Please enter a letter grade for {_program}: ").upper()

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
        #else TODO ERROR CHECKING WILL GO HERE  
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

    for i in range(len(classes)): #Putting the main part of this code in a for loop, will do another loop below for the final output
        #Gather user inputs
        letterGrade = GetLetterGrade(classes[i])
        modifier = GetModifier()
        print("")

        # Determine base numeric value of the grade
        numericGrade = ConvertLetterToNumber(letterGrade)
        
        # Determine whether to apply a modifier
        numericGrade = Modifier(modifier, letterGrade, numericGrade)

    # Output final message and result, with formatting
    print("The numeric value is: {0:.1f}".format(numericGrade))

#PROGRAM EXECUTION STARTS HERE
main()