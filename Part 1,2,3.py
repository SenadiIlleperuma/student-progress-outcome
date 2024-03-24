# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 

# Student ID: 20220678
 
# Date: 2023-4-20


#Initialising Variables.
progress = 0
trailer = 0
retriever = 0
exclude = 0
data = []
part_4_dict = {}

print("\n\n====================================================================================================")
print("                                     Student Progress Outcome                                       ")
print("====================================================================================================\n\n")

stuID = input("Please enter Students ID : ")    #Geting the StudentID from the user.

print('\n Part 1\n Part 2\n Part 3\n')
print("Type as Showned.\n")
user = input("Select your option: ")


def part1_Main():   #Printing the Histogram.
    print("====================================================================================================")
    print("                                        Horizontal Histogram                                        ")
    print("====================================================================================================\n")
    print('Progress ', progress, '   :', '*' * progress)
    print('Trailer ', trailer, '    :', '*' * trailer)
    print('Retriever ', retriever, '  :', '*' * retriever)
    print('Excluded ', exclude, '   :', '*' * exclude)
    print()
    print(progress + trailer + retriever + exclude, 'outcome in total.\n')    #printing the total outcomes.
    print("====================================================================================================")


def part2_List():   #Functions for the List
    print("====================================================================================================")
    print("                                        Horizontal Histogram                                        ")
    print("====================================================================================================\n")
    print('Progress ', progress, '   :', '*' * progress)
    print('Trailer ', trailer, '    :', '*' * trailer)
    print('Retriever ', retriever, '  :', '*' * retriever)
    print('Excluded ', exclude, '   :', '*' * exclude)
    print()
    print(progress + trailer + retriever + exclude, 'outcome in total.\n')      #printing the total outcomes.
    print("")

    #Printing the List.
    print("====================================================================================================")
    print("                                                List                                                ")
    print("====================================================================================================\n")
    for i in data:
        print(i)   


def part3_TextFile():   #Function for the TextFile
    print("====================================================================================================")
    print("                                        Horizontal Histogram                                        ")
    print("====================================================================================================\n")
    print('Progress ', progress, '   :', '*' * progress)
    print('Trailer ', trailer, '    :', '*' * trailer)
    print('Retriever ', retriever, '  :', '*' * retriever)
    print('Excluded ', exclude, '   :', '*' * exclude)
    print()
    print(progress + trailer + retriever + exclude, 'outcome in total.\n')      #printing the total outcomes.
    print("====================================================================================================")


    #Writing the data for the TextFile.
    outFile = open('data.txt', 'w')  
    for i in data:
        outFile.write(i + '\n')
    outFile.close()  

    #Reading the data from TextFile.
    fileData = open('data.txt', 'r')
    read = fileData.read()
    print(read)
    fileData.close()


while True:
    try:
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
            data.append(f"Progress - {Pass}, {Defer}, {Fail}")

        elif Pass >= 100:
            print("Progress (module trailer)\n")
            trailer += 1
            data.append(f"Progress (module trailer) - {Pass}, {Defer}, {Fail}")
    
        elif (Pass >= 40 and Fail <= 60) or (Defer >= 60 and Fail <= 60):
            print("Do not Progress – module retriever\n")
            retriever += 1
            data.append(f"Do not Progress - module retriever - {Pass}, {Defer}, {Fail}")

        else:
            print("Exclude\n")
            exclude += 1
            data.append(f"Exclude - {Pass}, {Defer}, {Fail}")
            

    print('Would you like to enter another set of data ?')
    option = input("Enter 'y' for yes or 'q' to quit and view results: ")
    print()

    if option == 'y':
        continue
    elif option == 'q':
        if user == 'Part 1':
            part1_Main()
        elif user == 'Part 2':
            part2_List()
        elif user == 'Part 3':
            part3_TextFile()
        break
    else:
        print("Invalid input!")
        break
