'''
Write a function to count the numbers of scores are in the ranges 90 – 100, 80 – 89,
70 – 79, 60 – 69, below 60 and show the output with a good format.
'''


def main():
    scores = get_list()

    average= get_avg(scores)

    low = get_min(scores)
    high = get_max(scores)
    get_grades(scores)
    score_count(scores)

    print()
    print(f'{"Average Score:":<15}' + f'{average:>10.2f}')
    print(f'{"Highest Score:":<15}' + f'{high:>10}')
    print(f'{"Lowest Score:":<15}' + f'{low:>10}')
    

def get_list():
    #open file with scores
    infile = open('data.txt', 'r')

    nums = infile.readlines()

    infile.close()

    #convert to int
    for index in range(len(nums)):
        nums[index] = int(nums[index])

    return nums

def get_avg(nums):

    total = 0
    for index in range(len(nums)):
        total += nums[index]

    avg = total/(len(nums))

    return avg

def get_min(nums):
    smallest = min(nums)
    return smallest

def get_max(nums):
    largest = max(nums)
    return largest

def get_grades(nums):

    A = 0; B = 0; C = 0; D = 0; F = 0

    for index in range(len(nums)):
        if nums[index] >= 90:
            A +=1
        elif nums[index] >=80:
            B+=1
        elif nums[index] >= 70:
            C += 1
        elif nums[index] >=60:
            D += 1
        else:
            F +=1

    print(f'{"Grade:":<15}' + f'{"Count:":>10}')
    print(f'{"A (90-100)":<15}' + f'{A:>10}')
    print(f'{"B (80-89)":<15}' + f'{B:>10}')
    print(f'{"C (70-79)":<15}' + f'{C:>10}')
    print(f'{"D (60-69)":<15}' + f'{D:>10}')
    print(f'{"F (<60)":<15}' + f'{F:>10}')

def score_count(nums):
    nums.sort() #sort appending
    nums.reverse() #sort highest to lowest

    print()
    print(f'{"Score:":<15}' + f'{"Count:":>10}')
    for index in range(len(nums)):
        #if its the same as the last num, skip printing so there's no repeats
        if nums[index] == nums[index-1]: 
            pass
        else:
            print(f'{nums[index]:<15}' + f'{nums.count(nums[index]):>10}')

    print(f'{"Total Scores:":<15}' + f'{len(nums):>10}')
            


if __name__=='__main__':
    main()


'''
OUTPUT:
Grade:             Count:
A (90-100)              9
B (80-89)              32
C (70-79)              11
D (60-69)               4
F (<60)                 1

Score:             Count:
98                      1
95                      2
93                      1
90                      5
88                     10
85                      4
83                      5
82                      5
80                      8
77                      5
75                      4
72                      2
68                      1
66                      2
60                      1
55                      1
Total Scores:          57

Average Score:      81.75
Highest Score:         98
Lowest Score:          55

'''
