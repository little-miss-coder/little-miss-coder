#recursive gcd

def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x%y)

def main():
    num1 = int(input('Enter number 1: '))
    num2 = int(input('Enter number 2: '))

    print(f'The GCD of {num1} and {num2} is {gcd(num1, num2)}.')

main()
