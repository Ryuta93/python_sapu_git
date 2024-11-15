# 問題2-1
"""year = 1000

if year % 400 == 0:
    print('閏年です')
elif year % 100 == 0:
    print('平年です')
elif year % 4 == 0:
    print('閏年です')
else:
    print('平年です')"""
    
# 問題2-2 FizzBuzz
for number in range(1, 101):
    if number % 15 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)