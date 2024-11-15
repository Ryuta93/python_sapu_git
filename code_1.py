#問題2-1
year = 1000

if year % 400 == 0:
    print('閏年です')
elif year % 100 == 0:
    print('平年です')
elif year % 4 == 0:
    print('閏年です')
else:
    print('平年です')