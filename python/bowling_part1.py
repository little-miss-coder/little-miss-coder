#This is part one of the bowling example
#This is to open a new .txt file and insert scores to it

def main():
    result = open('result.txt','w')

    print('***Submit empty name field to exit program***')
    name = input("Enter the participant's name: ")

    #while loop, hitting enter without entry will exit loop
    while name != '':
        result.write(name +'\n')
        score =(input(f"Enter the score: "))
        result.write(score +'\n')
        name = input("Enter the participant's name: ")
        
    print('***Thanks for submitting scores!***')


    #close file
    result.close()

if __name__=='__main__':
    main()


'''
OUTPUT IN PROGRAM:
***Submit empty name field to exit program***
Enter the participant's name: Maria
Enter the score: 290
Enter the participant's name: Laura
Enter the score: 200
Enter the participant's name: Max
Enter the score: 290
Enter the participant's name: Mitch
Enter the score: 80
Enter the participant's name: Echo
Enter the score: 150
Enter the participant's name: Corey
Enter the score: 97
Enter the participant's name:
***Thanks for submitting scores!***
'''
'''
OUTPUT IN .TXT FILE
Maria
290
Laura
200
Max
290
Mitch
80
Echo
150
Corey
97
'''
