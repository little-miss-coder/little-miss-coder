#This is part 2 of the bowling example, to get and display results

def main():
    result=open('result.txt', 'r')
    highscores=open('highscore.txt', 'r+') #r+ to read and write

    print('*'*12 + 'ALL SCORES' + '*'*12)
    highscore = 0
    name = result.readline()
    count = 0  
    while name != '':
        score = int(result.readline())
        name = name.rstrip('\n')
        print (f'{name:20} {score:>13}')

        if score > highscore:
            highscore = score;
            highscores.truncate() #this is to delete current entries if a new high score is achieved
            highscores.write(name + '\n')
            highscores.write(str(score) + '\n')
        elif score == highscore:
            highscores.write(name + '\n')
            highscores.write(str(score) + '\n')
        else:
            pass
        name = result.readline()
        count +=1 

    #close files
    result.close()
    highscores.close()

    print (f'\n\n{"Total Participants":20} {count:>13}') 
    printscores() 

def printscores():

    print('*'*12 + 'HIGH SCORE' + '*'*12)
    hs = open('highscore.txt', 'r')
    print('Winner(s):')
    name = hs.readline()
    while name != '':
        score = int(hs.readline())
        name = name.rstrip('\n')
        print(name)
        
        name = hs.readline()

    print(f'Score: {score}')
    print('*'*34)

    hs.close()



if __name__=='__main__':
    main()


'''
OUTPUT:
************ALL SCORES************
Maria                          300
Max                            190
Echo                            70
Corey                          300
Lexie                           40


Total Participants               5 
************HIGH SCORE************
Winner(s):
Maria
Corey
Score: 300
**********************************
'''


