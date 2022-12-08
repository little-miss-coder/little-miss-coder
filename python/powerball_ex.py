#powerball example
#this program gets randomized and non repeating numbers for the powerball
#user has option to enter their own numbers to tell them if they won

import random

#global values. 
max_num = 69
pb_max = 29 #this is so you can change what number you want it to go up to
num_drawn = 5 #this is for the amount of numbers drawn


def main():
    #get 5 winners
    winners = random.sample(range(1, max_num), k = num_drawn)
    winners.sort() #sort the list
    
    #get one powerball number
    powerball = random.choice(range(1, pb_max))

    #make sure its not the same
    for index in range(num_drawn):
        if powerball == winners[index]:
            powerball = random.choice(range(1, pb_max))
        else:
            pass
        
    #sort to ascending order    
    winners.sort()

    
    print('Would you like to check your numbers?')
    choice = input('y for yes anything else for no: ')
    if choice == 'y':
        compare_nums(winners, powerball)
    else:
        pass
    
    
    print()
    print('*'*40)
    print('The powerball numbers are: ')
    for r in range(num_drawn):
        print(winners[r], end = '\t')
    print(f'\nPowerball #{powerball}')
    print('*'*10 + 'Thanks for playing!' + '*'*10)


'
#compare users numbers to the powerball numbers        
def compare_nums(list1, pb):
    user_list= [] #create list to store users numbers

    #get numbers and add to list
    for index in range(num_drawn):
        num = int(input(f'Enter #{index+1}: '))
        while num > max_num:
            print('Only numbers 1-69 are valid.')
            num = int(input(f'Enter #{index+1}: '))
        user_list.append(num)

    user_pb = int(input('Enter your powerball number: '))
    while user_pb > pb_max:
        print('Only numbers 1-26 are valid.')
        user_pb = int(input(f'Enter your powerball number: '))

    #sort ascending
    user_list.sort()


    print('*'*40)
    print('Your numbers: ')
    for r in range(num_drawn):
        print(user_list[r], end = '\t')
    print(f'\nYour powerball: #{user_pb}')
    print()

        
    same_nums = [] #define empty list to store same numbers in

    for index in range(num_drawn):
        if list1[index] in user_list: #SEARCH for each item
            same_nums.append(list1[index])
        else:
            pass
    
    if len(same_nums) > 0:
        print('Congrats! Same number(s): ', end=' ')
        for r in range(len(same_nums)):
            print(same_nums[r], end = '\t')
        print()
    else:
        print('Sorry, you do not have any winning numbers')
            
    if pb == user_pb:
        print('Congrats! You have the winning powerball number of {pb}!')
    else:
        print(f'Sorry, the winning powerball number was {pb}.')

        
if __name__=='__main__':
    main()


'''
OUTPUT:

****************************************
The powerball numbers are: 
1	16	24	56	57	
Powerball #7
**********Thanks for playing!**********


Would you like to check your numbers?
y for yes anything else for no: y
Enter #1: 30
Enter #2: 90
Only numbers 1-69 are valid.
Enter #2: 9
Enter #3: 17
Enter #4: 24
Enter #5: 49
Enter your powerball number: 4
****************************************
Your numbers: 
9	17	24	30	49	
Your powerball: #4

Congrats! Same number(s):  9	
Sorry, the winning powerball number was 26.

****************************************
The powerball numbers are: 
9	16	38	55	68	
Powerball #26
**********Thanks for playing!**********


'''
