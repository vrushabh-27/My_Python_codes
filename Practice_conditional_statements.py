## Practice

#1.check if number is positive, if yes then add 5 to it and print the output
num = 8
if num > 0:
    print('Number is positive and\nNumber + 5 =',num+5)


#2.check if number is negative number if yes multiply it by 10 print the output
num = -5
if num < 0:
    print('Number is negative and\nNumber * 10 =',num*10)


#3.if number is positive add 10 to that number if it is negative multiply by 10
#and print the output accordingly
num = 8
num = -5
if num > 0:

    print('Number is positive and \n Number + 10 =',num+10)
else:
    
    print('Number is negative and\n Number * 10 =',num*10)

#4.If number is multiple of 2 print a message
num = 8
#num = 5
if num%2 == 0 :
    print(num,' is multiple of 2')
else:
    print(num,' is not multiple of 2')


#5.now check if number is multiple of 3
#if yes add 100 to the number 
#if not then return its square
    
#num = 9
num = 7

if num%3 == 0:
    print('Number is multiple of 3 and \n Number + 100 =',num+100)
else:
    print('Number is not multiple of 3 and\n Square of number =',num*num)

#6.write a program such that if input is positive number 
#output is same positive number, if input is negative number still output
#is positive number Take input from user

num=int(input('Enter a number: '))

if num > 0:
    print('Number is positive and its absolute value is: ',num)

else:
    print('Number is negative and its absolute value is: ',-num)

#7.take a sides of quadrilateral from user and check if it is a square or not

s1=int(input('Enter side 1: '))
s2=int(input('Enter side 2: '))
s3=int(input('Enter side 3: '))
s4=int(input('Enter side 4: '))

if s1==s2==s3==s4 :
    print('The quadrilateral is square.')

else:
    print('The quadrilateral is not square.')

#8.in the above question find area if it is a square
s1=int(input('Enter side 1: '))
s2=int(input('Enter side 2: '))
s3=int(input('Enter side 3: '))
s4=int(input('Enter side 4: '))

if s1==s2==s3==s4 :
    area=s1*s1
    print('The quadrilateral is square with area= ',area,'mm^2')

else:
    print('The quadrilateral is not square.')
    
#9.Take positive Radius of circle and find its area. Message if negative

rad=int(input('Enter the radius of circle: '))

if rad>0:
    area=3.142*rad*rad
    print('The area of circle is: ',area,'mm^2')

else:
    print('The radius of circle can not be negative.')
