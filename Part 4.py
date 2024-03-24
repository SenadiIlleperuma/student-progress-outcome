# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 

# Student ID: 20220678
 
# Date: 2023-4-20


#Initialising Variables.
progress = 0
trailer = 0
retriever = 0
exclude = 0
part_4_dict = {}
progression_List = ""

print("\n\n====================================================================================================")
print("                                     Student Progress Outcome                                       ")
print("====================================================================================================\n\n")

def Part4_Dict():
    print("====================================================================================================")
    print("                                             Dictionary                                             ")
    print("====================================================================================================\n")
    for a in part_4_dict:
        print(a,": ",part_4_dict[a])

while True:
    try:
        stuID = input("Please enter Students ID : ")    #Geting the StudentID from the user.
        Pass = int(input("\nPlease enter your credit at pass: "))
        # Check if 'Pass' is out of range or not a multiple of 20, and if so, prompt the user to enter it again
        if Pass > 120 or Pass < 0 or (Pass % 20 != 0):
            print('Out of range\n')
            continue

        Defer = int(input("Please enter you credit at Defer: "))
        # Check if 'Defer' is out of range or not a multiple of 20, and if so, prompt the user to enter it again
        if Defer > 120 or Defer < 0 or (Defer % 20 != 0):
            print('Out of range\n')
            continue

        Fail = int(input("Please enter you credit at Fail: "))
        # Check if 'Fail' is out of range or not a multiple of 20, and if so, prompt the user to enter it again
        if Fail > 120 or Fail < 0 or (Fail % 20 != 0):
            print('Out of range\n')
            continue
    except:
        # If the user enters a non-integer value, print an error message and prompt them to enter it again
        print("Integer Required\n")
        continue

    # Check if the sum of 'Pass', 'Defer', and 'Fail' is not equal to 120, and if so, prompt the user to enter the credits again
    if Pass + Defer + Fail != 120:
        print("Total incorrect!\n")
        continue
    else:
        if Pass == 120:
            print("Progress\n")
            progress += 1
            progression_List = "Progress"

        elif Pass >= 100:
            print("Progress (Module Trailer)\n")
            trailer += 1
            progression_List = "Progress (Module Trailer)"
    
        elif (Pass >= 40 and Fail <= 60) or (Defer >= 60 and Fail <= 60):
            print("Do not Progress – module retriever\n")
            retriever += 1
            progression_List = "Module Retriever"

        else:
            print("Exclude\n")
            exclude += 1
            progression_List = "Exclude"
        

    #Assiging Dictionary.
    part_4_dict[stuID] = progression_List + " - " +str(Pass) + "," + str(Defer) + "," + str(Fail)



    print('Would you like to enter another set of data ?')
    option = input("Enter 'y' for yes or 'q' to quit and view results: ")
    print()

    if option == 'y':
        continue
    elif option == 'q':
        Part4_Dict()
        break
    else:
        print("Invalid input!")
        break
