age = int(36)
height = 1,76
complexNumber = complex()

triangleBase = input('What is the base of the triangle: ')
triangleHeight = input('What is the height of the triangle: ')
print('Area of the triangle: ', (int(triangleBase) * int(triangleHeight)) / 2)

triangleSideA = input('What is the first side of the triangle: ')
triangleSideB = input('What is the second side of the triangle: ')
triangleSideC = input('What is the third side of the triangle: ')
print('Area of the triangle: ', (int(triangleSideA) * int(triangleSideB) * int(triangleSideC)) / 2)
print('Perimeter of the triangle: ', (int(triangleSideA) + int(triangleSideB) + int(triangleSideC)))

rectangleWidth = input('What is the width of the rectangle: ')
rectangleHeight = input('What is the height of the rectangle: ')
print('Area of the rectangle: ', int(rectangleWidth) * int(rectangleHeight))
print('Perimeter of the rectangle: ', 2 * (int(rectangleWidth) + int(rectangleHeight)))

circleRadius = input('What is the radius of the circle: ')
print('Area of the circle: ', 3.14 * int(circleRadius) ** 2)
print('Circumference of the circle: ', 2 * 3.14 * int(circleRadius))

print('Euclidean distance between point (2, 2) and point (6,10): ' + str(((2 - 6) ** 2 + (2 - 10) ** 2) ** 0.5))
print('Slope of the line: ' + str((2 - 6) / (2 - 10)))

print('The value of x to make y=0 for the quadratic equation y = x**2 + 6x + 9: is: ', 'x = ' + str((-6 + (9 ** 0.5)) / 2))

print(len('python') == len('dragon'))

print(''''on' is found in both 'python' and 'dragon':''' + str('on' in 'python' and 'on' in 'dragon'))

print(''''jargon in 'I hope this course is not full of jargon':''' + str('jargon' in 'I hope this course is not full of jargon'))

print(str(float(len('python'))))

print('triangleSideA is even: ' + str(int(triangleSideA) % 2 == 0))

print('Check if the floor division of 7 by 3 is equal to the int converted value of 2.7: ' + str(7 // 3 == int(2.7)))

print('''Check if type of '10' is equal to type of 10: ''' + str(type(10)) == type(10))

print('''Check if int('9.8') is equal to 10: ''' + str(int(9.8) == 10))

numberOfHours = int(input('How many hours did you work this week? '))
hourlyRate = int(input('What is your hourly rate? '))
print('Your weekly earning: ' + str(numberOfHours * hourlyRate))

age = int(input('Enter your current age? '))
print('If you live until 100 years old you have this many seconds left to live: ' + str((100 - age) * 365 * 24 * 60 * 60))

for i in range(1,6):
    print(i, end=' ')
    for j in range(0,4):
        print(str(i ** j), end=' ')
    print()

    
