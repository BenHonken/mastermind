import random
colorlist=['Red', 'Yellow', 'Green', 'Blue', 'Black', 'White']
code=[]
numlist=[1,2,3,4,5,6]
while len(code)<4:
    color=colorlist[random.randint(0, len(colorlist)-1)]
    code.append(color)
solved=False
turn=1
print("The computer has generated a code consisting of four colors.  Duplicates are allowed.  You have 12 guesses to crack it.")
while solved==False and turn<13:
    print('It is turn', turn,'now.')
    n=0
    print('1. Red')
    print('2. Yellow')
    print('3. Green')
    print('4. Blue')
    print('5. Black')
    print('6. White')
    print('Enter 4 digits corresponding to the colors for your guess.')
    guess=input('Enter exactly 4 digits with no spaces. Only enter the digits listed. ')
    guesscheck=False
    while guesscheck==False:
        badchars=0
        if len(guess)!=4:
            guess=input('Please enter exactly 4 digits. ')
        for char in guess:
            char=int(char)
            if char not in numlist:
                badchars+=1
        if badchars>0:
            guess=input('Please only input numbers between 1-6.  All other input will cause an error.  ')
        else:
            guesscheck=True
    guesslist=[]
    guesslist.append(colorlist[int(guess[0])-1])
    guesslist.append(colorlist[int(guess[1])-1])
    guesslist.append(colorlist[int(guess[2])-1])
    guesslist.append(colorlist[int(guess[3])-1])
    if guesslist==code:
        solved=True
        print('You win!  You got the code in', turn, 'guesses!')
        playagain=input('Would you like to play again? y/n ')
        if playagain=='y':
            solved=False
            code=[]
            while len(code)<4:
                color=colorlist[random.randint(0, len(colorlist)-1)]
                code.append(color)
            turn=1
    else:
        m=0
        exact=0
        wrongplace=0
        total=0
        copy=[]
        copy.append(code[0])
        copy.append(code[1])
        copy.append(code[2])
        copy.append(code[3])        
        while m<4:
            if guesslist[m]==copy[m]:
                exact+=1
            m+=1
        m=0
        while m<4:
            if guesslist[m] in copy:
                copy.remove(guesslist[m])
                total+=1
            m+=1
        if total==1:
            print('You have 1 match!')
        else:
            print('You have', total, 'matches!')
        if exact==1:
            print('You have 1 exact match!')
        else:
            print('You have', exact, 'exact matches!')
    if turn==12:
        print('You ran out of turns!  The code was', code)
        playagain=input('Would you like to play again? y/n ')
        if playagain=='y':
            solved=False
            code=[]
            while len(code)<4:
                color=colorlist[random.randint(0, len(colorlist)-1)]
                code.append(color)
            turn=1
    turn+=1
