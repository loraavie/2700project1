"""
Project 1 CSC2700
Names: Lora Elliott and Shubheksha Acharya
"""

#Small function to allow the program to gracefully terminate at will.
def quit_on_demand():
    print("You are now exiting the quiz... \n")
    quit()

#Use: for giving the answer to yes or no questions
def y_or_n(inp):
    inv_input=0
    while True:
        if(inp.upper()=="YES" or inp.upper()=="Y"):
            ans = True
            return 5
        elif(inp.upper()=="NO" or inp.upper()=="N"):
            ans = False
            return 0
        elif(inp.upper()=="QUIT"):
            quit_on_demand()
        inv_input +=1
        if inv_input>4:
            print("You have entered invalid input too many times. Now terminating...")
            quit_on_demand()
        inp = input("Invalid Input: try again")
        y_or_n(inp)

'''
Used for questions that have multiple answer choices. Takes a response of a, b, or c
'''
def options(opt):
    inv_count = 0
    while True:
        if opt.upper()=="A":
            return 'a'
        elif opt.upper()=="B":
            return 'b'
        elif opt.upper()=="C":
            return 'c'
        elif opt.upper()=="QUIT":
            quit_on_demand()
        inv_count+=1
        if inv_count > 4:
            print("You have entered invalid input too many times. Now terminating...")
            quit_on_demand()
        opt = input("Invalid answer. Please Try again.")


"""
Use: for giving the answer to how much questions 
ex: 'how often do you do this' 'how much does this apply to you'
ideal input is a scale 1-5
q: represents the question you want to ask
"""
def how_much(q):
    print(q)
    inv_count = 0;
    while True:
        try:
            inp = int(input("Enter an integer input from 1-5:"))
            # if inp.lower() == "quit":
            #     quit_on_demand()
            if inp>=1 and inp<6:
                return inp
        except:
            input("Your input was not a number. Try again.")
            inv_count+=1
            if inv_count>4:
                print("You have entered invalid input too many times. Now terminating...")
                quit_on_demand()


"""Loops until an input number is reached. If quiz has 5 questions
inp = 5. Can either be modified to have questions directly inside each case or """
def game_loop(inp):

    res1 = 1
    res2 = 1
    res3 = 1
    x = 0
    while x<inp:
        match x:
            case 0:
                print("Question 1")
                q = "How often would you say that you find yourself lost in thought or distracted by your surroundings?\n"
                q+= "Please enter a number from 1-5, with 1 meaning never and 5 meaning all the time."
                inpu= how_much(q)
                res2= res1+inpu
            case 1:
                print("Question 2")
                q= "Would you consider yourself to be a strong leader? Type y or n to answer.\n"
                res1 += y_or_n(input(q))
            case 2:
                print("Question 3")
                q = "When given the option of what to do with your day, what would you pick?\n"
                q += "A: Study and catch up on work.\n"
                q += "B: Spend Time with family and friends\n"
                q += "C: Hit the gym and relax after. \n"
                ans = options(input(q))
                if ans == 'a':
                    res1+=5
                elif ans == 'b':
                    res2+=5
                elif ans == 'c':
                    res3+=5
            case 3:
                print("question 4")
                q = "You are at the convenient store and want to get a little treat. Which one do you get?\n"
                q += "A: A frozen drink (Slushie/ICEE)\n"
                q += "B: A candy bar. \n"
                q += "C: A bag of chips \n"
                ans = options(input(q))
                if ans == 'a':
                    res2+=5
                elif ans == 'b':
                    res1+=5
                elif ans == 'c':
                    res3+=5
            case 4:
                print("question 5")
                q = "Whenever you have an assignment to complete, when do you start on it?\n"
                q+= "Please enter a number from 1-5, with 1 meaning immediately and 5 meaning right before it is due."
                inpu= how_much(q)
                if inpu<3:
                    res1+=5
                elif inpu>3:
                    res2+=5
                else:
                    res3+=5
            case 5:
                print("question 6")
                q = "What is your favorite color out of the given options?\n"
                q += "A: Green\n"
                q += "B: Red \n"
                q += "C: Blue \n"
                ans = options(input(q))
                if ans == 'a':
                    res3+=5
                elif ans == 'b':
                    res1+=5
                elif ans == 'c':
                    res2+=5
            case 6:
                print("question 7")
                q= "Whenever you pick out your outfit in the morning is comfort the most important thing to you? \nType y or n to answer.\n"
                res3 += y_or_n(input(q))
            case 7:
                print("question 8")
                q = "Which of these holidays do you like the best?\n"
                q += "A: Christmas\n"
                q += "B: Halloween \n"
                q += "C: Valentines Day \n"
                ans = options(input(q))
                if ans == 'a':
                    res1+=5
                elif ans == 'b':
                    res3+=5
                elif ans == 'c':
                    res2+=5
            case 8:
                print("question 9")
                q = "Imagine you are driving and see something on the side of the road that interests you. How likely are you to stop?\n"
                q+= "Please enter a number from 1-5, with 1 meaning not at all and 5 meaning completely."
                inpu= how_much(q)
                if inpu>3:
                    res3+=5
                elif inpu<3:
                    res1+=5
                else : res2+=3
            case 9:
                print("question 10")
        x=x+1
    if res1>=res2 and res1>=res3:
        ending1()
    elif res2>=res1 and res2>=res3:
        ending2()
    elif res3>=res1 and res3>=res2:
        ending3()

def ending1():
    print("You are most like Blossom. Blossom is intelligent, level-headed, and responsible.\n She is also friendly and outgoing type of person. ")
def ending2():
    print("You are most like Bubbles. Bubbles is sweet-natured and optimistic.\n She tends to be driven by strong emotions"
          " whether they be happy or sad ones. ")
def ending3():
    print("You are most like Buttercup. Buttercup is tough and a bit hotheaded. \n "
          "She is more impulsive, but makes up for it with her strength.")


print("Welcome to our personality quiz. Answer a few questions to find out which Powerpuff Girl you are.")
print("To end the game, enter quit at any time.")

game_loop(10)
while True:
    play_again = input("If you would like to take the quiz again, enter y. \nEnter anything else to exit.\n")
    if play_again == "y" or play_again == "Y":
        game_loop(10)
    else:
        print("Thank you for playing! Goodbye.")
        quit()

