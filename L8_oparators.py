## Operators

#Arithmatic operators
a=10
b=2

print('Addition',a+b)
print('Subtraction',a-b)
print('Multiplication',a*b)
print('Division',a/b)
print('Remainder',a%b)
print('Exponential',a**b)

#Assignment operators
print()
print("Assignment operators")
a=5
add,sub,mul,div,rem,expo=0,0,0,1,1,1

#add=add+a
add+=a
print('1.',add)
sub-=a
print('2.',sub)
mul*=a
print('3.',mul)
div/=a
print('4.',div)
rem%=a
print('5.',rem)
expo**=a
print('6.',expo)

#Comparison opearators
print()
print('Comparision operators')
a=5
b=10
#true if equal
print('1.',a==b)

#true not equal
print('2.',a!=b)

#true if a is greater than b
print('3.',a>b)

#true if b is greater than a
print('3.',b>a)

#true if a is greater than or equal to b
print('4.',a>=b)

#true if a is less than or equal to b
print('5.',a<=b)

#Logical opearators
print()
print('Logical operators')
a=5
b=0

#true if both are true
print('1.',a and b)

#true if either one is true
print('2.',a or b)

#returns opposite of value
print('3.',not a)
print('4.',not b)

#Identity operators
print()
print('Identity operators')
a=[1,2,3]
b=[2,3,4]

#true if a and b are equal
print('5.',a is b)

#True if a and b are not equal
print('6.',a is not b)

#true if 2 in a
print('7.', 2 in a)

#true if 2 in not b
print('8.',2 not in b)


