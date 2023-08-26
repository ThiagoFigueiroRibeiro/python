# Given 3 sides of a triangle, let's test if it exists
# and if it is Scalene, Isoceles or Equilateral.

def triangle_test():
    
    print ('Testing your triangle')
    a = float(input('Enter the first side of the triangle:'))
    b = float(input('Enter the second side of the triangle:'))
    c = float(input('Enter the third side of the triangle:'))
    if (a>b+c or b>a+c or c>b+a):
        print('These measurements cannot build a triangle')
    elif(a==b and b==c and c==a):
        print('This is an Equilateral triangle')
    elif(a==b or b==c or c==a):
        print('This is an Isoceles triangle')
    else:
        print('This triangle has three different sides (Scalene)')

    return 0
    
triangle_test()