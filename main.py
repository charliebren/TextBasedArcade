import random
#main.py
#by: Charlie Brenckle
#An arcade with two games. After gaining tickets you can go to the prize table to claim prizes.

class Prize:
    def __init__(self,name,ticketVal):
        self.name = name
        self.ticketVal = ticketVal

prize1 = Prize("Teddy Bear",4)
prize2 = Prize("Tatoo",2)
prize3 = Prize("Spider",5)
prize4 = Prize("Turtle",12)
prize5 = Prize("Slime",3)
prize6 = Prize("Dog",6)

prizes = [prize1,prize2,prize3,prize4,prize5,prize6]
def caesarCipher(cipher, message):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    toReturn = ""
    for i in range(len(message)):
        subMessage = message[i:i+1]
        currentPos = 0
        if subMessage != " ":
            for j in range(len(alphabet)):
                if(alphabet[j] == subMessage.upper()):
                    currentPos = j

            currentPos += cipher

            if currentPos >= len(alphabet):
                currentPos -= len(alphabet)

            toReturn = toReturn + alphabet[currentPos]

        else:
            toReturn = toReturn + " "

    return toReturn

def playCaesarCipher():
    print("Welcome to Caesar Cipher!! The rules are simple. A hidden message will be given to you in the form of a")
    print("Caesar Cipher. Your goal is to translate the sentence. If you type in a message that is incorrect, it will")
    print("be translated in to the cipher to give hints about the correct answer. Every time you type anything but the")
    print("correct message, the amount of tickets you can win will decrease until you are at zero. Good Luck!")

    cipher = random.randint(0,25)
    possibleMessages = ["Hello friend", "How are you", "What is your name", "How old are you", "Python is cool"]

    randPos = random.randint(-1,len(possibleMessages) - 1)
    randMessage = possibleMessages[randPos]

    cipheredMessage = caesarCipher(cipher, randMessage)


    print("Your ciphered message is: " + cipheredMessage)

    ticketsWon = 50
    gameOver = False
    while(ticketsWon > 0 and gameOver == False):
        answer = input("Enter answer or letters for hints: ")
        if(answer.lower() == randMessage.lower()):
            gameOver = True
            print("Congratulations, you got it!")
        else:
            cipheredAnswer = caesarCipher(cipher, answer)
            print("Wrong answer, but this is your answer ciphered: " + cipheredAnswer)
            ticketsWon -= 1
    if ticketsWon == 1:
        print("You have won 1 ticket!")
    elif ticketsWon == 0:
        print("I am sorry but you did not win any tickets")
    else:
        print("You have won " + str(ticketsWon) + " tickets!")

    return ticketsWon



def playMathGame():
    print("Welcome to Math Game! In this game you will be given a bunch of math equations. Everytime you get one right,")
    print("the amount of tickets you will gain goes up. The first time you enter an answer incorrectly, the game is over.")
    print("Good luck and have fun! P.S. Round to the nearest whole number")

    easyQs = ["2+2","3-2","4+5","5+9","9-6","2+6"]
    easyQsAnswers = [4,1,9,14,3,8]
    mediumQs = ["5*2","4/2","5-7","7*5","8/2","10*20"]
    mediumQsAnswers = [10,2,-2,35,4,200]
    hardQs = ["7/3","22*11","-5*70","-3*-4","50*60","111*7"]
    hardQsAnswers = [2,242,-350,12,3000,777]

    numQs = 5

    ticketsWon = 0
    gameOver = False
    i = 0
    print("Lets start with some easy questions!")
    while(gameOver == False and i<numQs):
        randVal = random.randint(-1,len(easyQs)-1)
        answer = int(input("What is the answer to " + easyQs[randVal] + ": "))
        if(answer == easyQsAnswers[randVal]):
            print("Correct!")
            ticketsWon += 1
            i += 1
        else:
            print("I am sorry but that is incorrect")
            gameOver = True

    if(gameOver == False):
        print("Good job! Now lets do a bit more challenging questions!")
    i=0
    while (gameOver == False and i < numQs):
        randVal = random.randint(-1, len(mediumQs) - 1)
        answer = int(input("What is the answer to " + mediumQs[randVal] + ": "))
        if (answer == mediumQsAnswers[randVal]):
            print("Correct!")
            ticketsWon += 2
            i += 1
        else:
            print("I am sorry but that is incorrect")
            gameOver = True

    if(gameOver == False):
        print("Wow you\'re good at this! Hardest question coming up!")

    i=0
    while (gameOver == False and i < numQs):
        randVal = random.randint(-1, len(hardQs) - 1)
        answer = int(input("What is the answer to " + hardQs[randVal] + ": "))
        if (answer == hardQsAnswers[randVal]):
            print("Correct!")
            ticketsWon += 3
            i += 1
        else:
            print("I am sorry but that is incorrect")
            gameOver = True

    if(ticketsWon > 1):
        print("Congratulations!! You have won " + str(ticketsWon) + " tickets!")
    elif(ticketsWon == 1):
        print("Congratultions! You won 1 ticket!")
    else:
        print("I am sorry but you did not win any tickets. Next time you\'ve got this!!")

    return ticketsWon
def main():
    print("Welcome to the Brenckle arcade. You will be asked how many tokens you would like to have and then get to play")
    print("either two of the games in the arcade. Based on how well you do in the game will decide how many tickets")
    print("you get after finishing the game. You can use those tickets to obtain prizes to bring home after it is over.")
    print("Also you can quit at anytime and go straight to the prize table. Good luck and have fun!")

    tokens = int(input("How many tokens would you like to start with? "))
    tickets = 0
    caesarTokenVal = 3
    mathTokenVal = 2
    quit = False

    print()
    while(tokens>0 and quit == False):
        print("Tokens:", tokens)
        print("Tickets:", tickets)
        print()
        print("Caesar Cipher: 3 tokens")
        print("Math game: 2 tokens")
        print("Enter caesar to play \"Caesar Cipher\", enter math to play \"Math Game\", enter q to quit/prize table")
        answer = str(input("What would you like to do? "))
        answer = answer.lower()

        if answer == "caesar":
            tokens -= caesarTokenVal
            tickets += playCaesarCipher()
        elif answer == "math":
            tokens -= mathTokenVal
            tickets += playMathGame()
        elif answer == "q":
            quit = True
        else:
            print("I am sorry that is not a valid answer")


    print("Welcome to the prize table!")
    print("Congratulations on winning tickets!")
    prizesTakingHome = "You are taking home: "
    #PTH stands for Prizes Taking Home
    minLenOfPTH = len(prizesTakingHome)
    while (tickets > 0):
        print("You have: " + str(tickets) + " tickets left")
        print()
        print("Here are your options for prizes: ")
        for i in range(len(prizes)):
            print(str(i) + ") " + prizes[i].name + " " + str(prizes[i].ticketVal))

        prizeId = int(input("Enter the prize Id, the number at the beginning, of the prize you want(-1 if you want to quit)"))
        if prizeId == -1:
            tickets = 0
        elif prizeId >= len(prizes):
            print("I am sorry, this is an invalid prize Id")
        else:
            quantity = int(input("How many do you want? "))
            if prizes[prizeId].ticketVal * quantity > tickets:
                print("I am sorry, you do not have enough tickets")
            else:
                tickets = tickets - prizes[prizeId].ticketVal * quantity
                if quantity == 1:
                    prizesTakingHome = prizesTakingHome + str(quantity) + " " + prizes[prizeId].name + ", "
                else:
                    prizesTakingHome = prizesTakingHome + str(quantity) + " "+ prizes[prizeId].name + "s, "

    print()
    if len(prizesTakingHome) > minLenOfPTH:
        print(prizesTakingHome[0:len(prizesTakingHome) - 2])


    print("Thank you for playing!")
    input("Press <enter> to quit")

main()