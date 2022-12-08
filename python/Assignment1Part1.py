#Assignment 1 Part 1
#Maria Gilipsky

def packageA(hours):
    if hours <= 20:
        charge = 29.95
    else:
        charge = ((hours - 20) * 2) + 29.95

    return charge

def packageB(hours):
    if hours <= 40:
        charge = 49.95
    else:
        charge = (hours - 40) + 49.95

    return charge

def packageC():
    return 69.95 #no math because its unlimited hours

def getPackage():
    package = input('Enter your package (A, B, or C): ').upper() #.upper() so if they enter lowercase 'a' 'b' or 'c' it still works
    while package != "A" and package != "B" and package != "C":
        package = input("Invalid package. Please enter 'A', 'B', or 'C' : ").upper()

    return package

def getHours():
    hrs = int(input('Please enter your hours: '))

    while hrs < 0:
        hrs = int(input('Cannot have hours less than 0. Please enter your hours: '))

    return hrs

def compare(): #REVISED
    pckg = getPackage()
    hours = getHours()

    #get all rates
    costA = packageA(hours)
    costB = packageB(hours)
    costC = packageC()

    #find lowest rate
    lowest = min(costA, costB, costC)

    if pckg == 'A':
        if lowest == costA:
            print(f'You have the best rate.')
        else:
            savingsB = costA - costB
            savingsC = costA - costC
            print(f'You would save ${savingsB:.2f} with package B.')
            print(f'You would save ${savingsC:.2f} with package C.')
            
        print(f'Your current bill is ${costA:.2f}.')
        
    elif pckg == 'B':
        if lowest == costB:
            print(f'You have the best rate.')
        else:
            savingsA = costB - costA
            savingsC = costB - costC
            print(f'You would save ${savingsA:.2f} with package A.')
            print(f'You would save ${savingsC:.2f} with package C.')
            
        print(f'Your current bill is ${costB:.2f}.')
        
    else:
        savings = costC-lowest
        if lowest == costC:
            print(f'You have the best rate.')
        else:
            savingsA = costC - costA
            savingsB = costC - costB
            print(f'You would save ${savingsA:.2f} with package A.')
            print(f'You would save ${savingsB:.2f} with package B.')
            
        print(f'Your current bill is ${costC:.2f}.')    
        

def main():
    compare()


if __name__ == '__main__':
    main()

'''
REVISED OUTPUT:

Enter your package (A, B, or C): a
Please enter your hours: 500
You would save $480.00 with package B.
You would save $920.00 with package C.
Your current bill is $989.95.


Enter your package (A, B, or C): b
Please enter your hours: 50
You have the best rate.
Your current bill is $59.95.

Enter your package (A, B, or C): c
Please enter your hours: 10
You would save $40.00 with package A.
You would save $20.00 with package B.
Your current bill is $69.95.


'''


