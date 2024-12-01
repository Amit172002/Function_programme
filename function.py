# prime number or not 1st way
def prime(val):
    for den in range(2,val//2+1):
        if val%den == 0:
            return 'not a prime number'
    return 'prime number'
num = 15
print(prime(num))

# compare two number 

def compare(num1,num2):
    if num1 > num2:
        return 'num1 is greater'
    return 'num2 is greater'
print(compare(11,15))

# prime number or not 2nd way
def prime(val):
    for den in range(2,int((val)**(0.5))+1):
        if val%den == 0:
            return 'not a prime number'
    return 'prime number'
num = 18
print(prime(num))

# prime number or not 2nd way
def prime_num(n,fact_count=0):
    for den in range(1,n+1):
        if n%den == 0:
            fact_count +=1
    return fact_count == 2
num = 16
print('prime number' if prime_num(num) else 'not a prime number')

# Armstrong Number
def Armstrong_num(n,power , res = 0):
    while n != 0:
        res = res+(n%10)**power
        n //=10
    return res
num = 153
print('Armstong number' if Armstrong_num(num,len(str(num)))==num else 'Not a armstrong number')

# Factorial Number
def factorial_number(n,fact=1):
    for val in range(1,n+1):
        fact = fact*val
    return fact
num = 5
print(factorial_number(num))

# Add all digit in a number :
def dig_sum(n,res = 0):
    while n != 0:
        res = res + n%10
        n //=10
    return res
num = 56781
print(dig_sum(num))
    
# multiply all digit in a number :
def mul_sum(n,res = 1):
    while n != 0:
        res = res*(n%10)
        n //=10
    return res
num = 23
print(mul_sum(num))

# Disarum number
def Disarum_num(n,power , res = 0):
    while n != 0:
        res = res+(n%10)**power
        n //=10
        power -=1
    return res
num = 136
print('Disarum number' if Disarum_num(num,len(str(num)))==num else 'Not a Disarum number')


# Happy number
def sq(n,res = 0):
        while n != 0:
            rem = n%10
            res = res+rem**2
            n //=10
        return res
def Happy_num(dig):
    while dig > 9:
        dig = sq(dig)
    return dig==1 or dig==7

num = 19
print('Happy number'if Happy_num(num) else "Not A Happy Number")


# reverse Number
def reverse_num(n, rev=0):
    while n != 0:
        rev = rev*10 + (n%10)
        n //= 10
    return rev
num = 8576
print(reverse_num(num))

# palindrome or not
def palindrome_num(n , rev=0):
    while n != 0:
        rev = rev*10 + (n%10)
        n //=10
    return rev
num = 218812
print('palindrome number' if palindrome_num(num) == num else 'not a palindrome')


# convert into int to binary
def convert_int_binary(n , pos = 1,res =0):
    while n != 0:
        res = res + (n%2)*pos
        pos *=10
        n //=2
    return res
num = 17
print(convert_int_binary(num))

# convert into binary to int
def convert_binary_int(n, pos= 0, res = 0):
    while n != 0:
        res = res + (n%10)*2**(pos)
        pos += 1
        n //=10
    return res
num = 10001
print(convert_binary_int(num))


# EMIRP Number or not
def Reverse_num(n, rev = 0):
    while n != 0:
        rev = rev * 10 + (n%10)
        n //=10
    return rev
def prime(x):
    for den in range(2,x//2+1):
        if x%den == 0:
            return False
    return True

num = 13
dup = Reverse_num(num)
print('EMirp Number' if dup != num and prime(num) and prime(dup) else 'not a emirp number')


# Fascnating Number
def fasc_number(n):
    calc = str(n)*1+str(n*2)+str(n*3)
    for x in range(1,10):
        if str(x) not in calc:
            print('not a Fascnating number')
            break
    else:
        print("fascnating number")

num= 192
fasc_number(num)

# strong number
def factorial(n,fact=1):
    for val in range(1,n+1):
        fact = fact*val
    return fact
def strong_number(x,res=0):
    while x!=0:
        rem = x%10
        res = res + factorial(rem)
        x //=10
    return res
num = 145
print("strong number" if strong_number(num)== num else "not a strong number")


# palyprime or not
def reverse_num(n,rev=0):
    while n!=0:
        rem = n%10
        rev = rev*10 +rem
        n //=10
    return rev
def prime_num(x):
    for den in range(2,x//2+1):
        if x%den == 0:
            return False
    return True

def palyprime(y):
    if prime_num(y) and reverse_num(y)==y:
        return 'palyprime number'
    return 'not a palyprime number'

    
num = 11
print(palyprime(num))

