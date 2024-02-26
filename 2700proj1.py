"""
Use: for giving the answer to yes or no questions
"""
def y_or_n(inp):

    if(inp.upper()=="YES" or inp.upper()=="Y"):
        ans = True
        return 5
    elif(inp.upper()=="NO" or inp.upper()=="N"):
        ans = False
        return 0
    else:
        inp = input("Invalid Input: try again")
        y_or_n(inp)


"""Loops until an input number is reached. If quiz has 5 questions
inp = 5. Can either be modified to have questions directly inside each case or """
def game_loop(inp):
    #each res is the counter for each ending. The one with the highest will be the result. 
    res1 = 0
    res2 = 0
    res3 = 0
    res4 = 0
    x = 0
    while x<inp:
        match x:
            case 0:
                print("question 1")
            case 1:
                print("question 2")
            case 2:
                print("question 3")
            case 3:
                print("question 4")
            case 4:
                print("question 5")
        x=x+1
      
game_loop(4)
