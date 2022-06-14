##Patterns

#square pattern
a=int(input('Enter a number: '))

for i in range (a):
    for j in range (a):
        print('#',end=' ')
    print()
    
######################################################################################################################

# first column
a=int(input('Enter a number: '))

for i in range (a):
    for j in range (a):
        if j==0:
            print('#',end=' ')
    print()
    
#######################################################################################################################

#first and last column
a=int(input('Enter a number: '))

for i in range (a):
    for j in range (a):
        if j==0 or j==4:
            print('#',end=' ')
        else:
            print(' ',end=' ')
    print()
    
######################################################################################################################

#top and bottom row
a=int(input('Enter a number: '))

for i in range (a):
    for j in range (a):
        if i==0 or i==4:
            print('#',end=' ')
        else:
            print(' ',end=' ')
    print()
    
####################################################################################################################

#digonal (left to right)
a=int(input('Enter a number: '))

for i in range (a):
    for j in range (a):
        if i==j:
            print('#',end=' ')
        else:
            print(' ',end=' ')
    print()
    
######################################################################################################################

#digonal (right to left)
a=int(input('Enter a number: '))

for i in range (a):
    for j in range (a):
        if i+j==4:
            print('#',end=' ')
        else:
            print(' ',end=' ')
    print()

#########################################################################################################################

#cross (x) pattern
a=int(input('Enter a number: '))

for i in range (a):
    for j in range (a):
        if i==j or i+j==4:
            print('#',end=' ')
        else:
            print(' ',end=' ')
    print()

##########################################################################################################################

#plus (+)pattern
a=int(input('Enter a number: '))

for i in range (a):
    for j in range (a):
        if i==2 or j==2:
            print('#',end=' ')
        else:
            print(' ',end=' ')
    print()

########################################################################################################################

#hollow square pattern
a=int(input('Enter a number: '))

for i in range (a):
    for j in range (a):
        if i==0 or j==0 or i==4 or j==4:
            print('#',end=' ')
        else:
            print(' ',end=' ')
    print()

#######################################################################################################################

#right angle triangle
a=int(input('Enter a number: '))

for i in range (a):
    for j in range (i+1):
        print('#',end=' ')
    print()
    
                ##OR##
    
a=int(input('Enter a number: '))
for i in range (a):
    print('# '*(i+1))

#################################################################################################################

#inverted right angle triangle

a=int(input('Enter a number: '))

for i in range (a):
    for j in range (a-i):
        print('#',end=' ')
    print()
    
                ##OR##
    
a=int(input('Enter a number: '))
for i in range (a):
    print('# '*(a-i))

#################################################################################################################

#equilateral triangle
a=int(input('Enter a number: '))

for i in range (a):
    print(' '*(a-i+1),'# '*(i+1))


##OR
n=int(input('Enter a number: '))
k=n-1

for i in range (n):
    for j in range (k):
        print(' ',end='')
    k=k-1
    for i in range (i+1):
        print('# ',end='')
    print()

    

#################################################################################################################

#diamond shape
a=int(input('Enter a number: '))

for i in range (1,a+1):
    print(' '*(a-i), end='')
    print('* '*i)

#inverted triangle
k=a-1
for i in range (k):
    print(' '*i,'* '*(k-i) )
    
################################################################################################################

#hollow triangle
a=int(input('Enter a number: '))

for i in range (a):
    for j in range (a):
        if i==4 or j==0 or i==j:
            print('#',end=' ')
        else:
            print(' ',end=' ')
    print()

#hollow square with diagonal

a=int(input('Enter a number: '))

for i in range (a):
    for j in range (a):
        if i==0 or j==0 or i==(a-1) or j==(a-1) or i==j or i+j==(a-1):
            print('#',end=' ')
        else:
            print(' ',end=' ')
    print()

    

