#hanoi game

'''
1: move (n-1) disks from peg 1 to peg 2
2: move the biggest disk from peg 1 to peg 3
3: move (n-1) disks from peg 2 to peg 3
'''

#global
count_steps = 0

def move_disk(num, from_peg, to_peg, temp_peg):
    global count_steps
    if num > 0:
        move_disk(num-1, from_peg, temp_peg, to_peg)
        print(f'Move a disk from peg {from_peg} to peg {to_peg}')
        count_steps+=1
        move_disk(num-1, temp_peg, to_peg, from_peg)

def main():
    num_disks = 5
    from_peg = 1
    temp_peg = 2
    to_peg = 3

    move_disk(num_disks, from_peg, to_peg, temp_peg)
    print(f'It takes {count_steps} steps')

main()
