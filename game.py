import random

def game():        #this function is used for showing main menu and working in that part
    name = ''      #when program starts, name is initially an empty string
    password = ''   #when program starts, password is initially an empty string
    while True:     #to make program shows the main menu constantly
        print ("--- Welcome to 'Guess the Number' Game V.0.3 ---")
        print("1. Login")
        print("2. Sign Up (Limited to 1 user)")
        print ("3. Description")
        while True:    #while True it will work in the main menu
            option = raw_input()
            if option == '1':    #if user selects first option which is  login
                option_1(name,password)   #function namely option_1 is called
                break               #break is used to get out of this while loop to see the main menu
            elif option == '2':         #if user selects second option which is sign up
                name,password = option_2(name,password)   #name and password are updated from function option_two
                break             #break is used to get out of this while loop to see the main menu
            elif option == '3':           #if user selects third option which is description
                option_3()                #function option_3 is called
                break                  #break is used to get out of this while loop to see the main menu
            else:            #this part for the condition when user enters number which is not in the main menu
                print 'Please enter a valid number!'

def option_1(name,password):   #it takes two parameters which are name and password to check if name and password are correct or not
    if name == '':      #if name is an empty string, it means that there is no user signed up
        print ("Warning! There is no users :( Please sign up first" + "\nGoing back to main menu...")
    else:
        user = raw_input('Please enter your username:')
        passw = raw_input('Please enter your password:')
        if user == name and passw == password:   #check if user write her/his user name and password correctly or not
            print "Game starts..."
            point = 100      #user's initial point
            while True:
                if point <= 0:  #if point is neegative or equal to zero, it prints statement below and finish this while loop so that point starts from 100
                    break
                generated_number = random.randint(0, 100)  # number is randomly chosen betweeon 0 and 100 which both are included
                print "Let's start with a new number" + "\nYour Point: 100" + "\nGuess the number:"
                while True:
                    if point <= 0:    #if point is neegative or equal to zero, it prints statement below and finish this while loop
                        print "< Your Point is ZERO >" + "\n--------------------------------" + "\n----- < Game Over > -----" + \
                            "\n--------------------------------"
                        break
                    else:     #if point is bigger than zero, then it asks user's guessed number
                        guessed_number = raw_input()
                        if int(guessed_number) == generated_number:  # it checks if user's number is the same as randomly generated one
                            point += 25  # and update the point value
                            print "Your Point: " + str(point) + "\nCongratulations, that's right you got +25 points" + \
                                  "\nLet's start with a new number"
                        else:  # if user's number is not same as generated number then we have four options
                            if int(guessed_number) < (generated_number / 2.0):  # if guessed_number is less than the half of the generated number
                                point -= 10     #and update the point value
                                print "Your Point: " + str(point) + "\nThe number you guess is too low, you loss 10 points" + \
                                "\n You still have a chance. Try Again!"
                            elif (generated_number / 2.0) < int(guessed_number) < (generated_number):  # if typed number is less than the half of the generated number
                                point -= 5        #and update the point value
                                print "Your Point: " + str(point) + "\nThe number you guess is low. You lose 5 points" + \
                                "\n You still have a chance. Try Again!"
                            elif int(guessed_number) > (generated_number * 2):  # if the typed number is bigger than the two times generated number
                                point -= 10          #and update the point value
                                print "Your Point: " + str(point) + "\nThe number you guess is too high, you lose 10 points" + \
                                      "\n You still have a chance. Try Again!"
                            elif (generated_number * 2) > int(guessed_number) > (generated_number):  # if typed number is less than two times generated number and bigger than the generated number
                                point -= 5       #and update the point value
                                print "Your Point: " + str(point) + "\nThe number you guess is high, you lose 5 points" + \
                                      "\n You still have a chance. Try Again!"
            else:    #if user name or password is not same as the name and password saved in 'sign up' part
                print "Information is invalid!"

def option_2(name,password):  #takes two parameters because name and password should be saved
    if name == '':  #if name is an empty string user is asked to enter her/his name and password
        name_exp = "Please enter your user name:"
        user_name = raw_input(name_exp)    #name of the user is assigned as user_name
        password_exp = "Please enter your password:"
        user_password = raw_input(password_exp)    #password of the user is assigned as user_name
        return user_name,user_password      #user name and password is saved and returned
    else:
        print ("You have already signed up, you can't sign up more than 1 user!" + "\nGoing back to main menu..")
        return name, password       #user name and password is saved and return

def option_3():   #print the statement if user selects "description"
        print "This project is 'ENGR 101 - Introduction to Programming' course's mini project 01." \
          "The project is a game played by one player by sign up and login system." \
          "The player should assume the randomly generated number and accordingly he/she will earn or lose points."

game()