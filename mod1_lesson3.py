#finding the exponential of a number
print('Finding the exponential of a number')

#allow users to enter their integer
x = int(input('Enter your number:'))
y = int(input('Enter your number:'))

#check if the power is 0
if y==0:
    print(1)

#if power is not 0
else:
    x = x**y

    print(x)
    