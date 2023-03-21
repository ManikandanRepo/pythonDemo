

num1 = 10.00

num2 = -222
print(abs(num2))
print(int(num1))

help(print)

print("Manikandan ", "Srinivasan", sep='$ ')

print(max(100,120,130))

def mod_5(x):
    return x % 5

print(max(100,121,132, key=mod_5))
#help(max)

def smash_candies(candycount):
    print("Splitting ", candycount, "candy" if candycount == 1 else "candies")
    return print(candycount % 3)


smash_candies(91)
smash_candies(1)

print(int(True)+int(False)+int(True))
print(bool(-10))

names = ['zebra','Mani', "Srini", "Trichy", "Testing"]

print(names[-2:])

print(len(names))

print(sorted(names))

print(names)

numbers = [1, 2, 3, 4]
print(sum(numbers))
print(max(numbers))

print(num1.imag)
print(num2.imag)

help(names.append)

names.append('Manachanallur')
print(names)

names.pop()
print(names)

print('Trichy is in position ',names.index('Trichy')+1)

print('Trichy' in names)

tuple1 = (1, 2, 3)

x = -0.125

print(x.as_integer_ratio())

help(x.as_integer_ratio)

numerator, denominator = x.as_integer_ratio()

print (numerator / denominator)

total_coins = 10

print("T0tal number of coins", total_coins , "coin" if total_coins == 1 else "coins")

total_coins = 1

print("T0tal number of coins", total_coins , "coin" if total_coins == 1 else "coins")

t = (1,2,3)

print("tuple is:" , t)

x= t + (4 , 5)
print(x)

print (len(t) , " " , len(names))

help(str)

numonly = "1234567890"
alphanum = "121231asaA"
specialNum = "1.234!@"
fractioNum = "1/2E"
decNum = "1.2345"

print(numonly.isdigit())
print(alphanum.isdigit())
print(specialNum.isdigit())
print(fractioNum.isdigit())

print("-------------")

print(numonly.isnumeric())
print(alphanum.isnumeric())
print(specialNum.isnumeric())
print(fractioNum.isnumeric())

print("-----------")

print(numonly.isdecimal())
print(alphanum.isdecimal())
print(specialNum.isdecimal())
print(fractioNum.isdecimal())
print(decNum.isdecimal())

print(dir(str))