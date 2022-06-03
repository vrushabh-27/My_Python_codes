##==Practice questions of tuples==##



##1. Initialize empty tuple
my_Tuple=()
my_Tuple_1=tuple()

print(my_Tuple)
print(my_Tuple_1)

##2. Create a tuple of few integer values (dont use tuple function)
myTuple=(9,8,7,6,5,4,3,2,1,0)
myTuple=9,8,7,6,5,4,3,2,1,0
print(myTuple)

##3. Create a tuple of few string values
myTuple1=('Hi','this','is','Vrushabh')
mtTuple1=tuple(('Hi','this','is','Vrushabh'))
print(myTuple1)



##4. Print 'welcome'

new1=(1,2,3,4,'welcome')

print(new1[4])
print(new1[-1])

##5. Create a tuple of few integer values using tuple function

myTuple3=tuple((1,2,3,4))

print(myTuple3)

##6. Create  a tuple as tuple11, with list,string,tuple,45.21 and integer datatypes

tuple11=(['Hiii',27],'string',('abc',21),45.21,123)

tuple11=tuple((['Hiii',27],'string',('abc',21),45.21,123))
print(tuple11)


##7. Print hello , all , python

new2 = tuple(('hello','welcome','all','here',29.32,'python','end'))

print(new2[0],new2[2],new2[5])
print(new2[-7],new2[-5],new2[-2])
a=new2[0]
b=new2[2]
c=new2[5]
print(a,b,c)


##8. Print all the elements from the tuple new2

new2 = tuple(('hello','welcome','all','here',29.32,'python','end'))

print(new2)
print(new2[:])
print(new2[0:7])
print(new2[::-1])


##9. Print last element from the tuple

new2 = tuple(('hello','welcome','all','here',29.32,'python','end'))

print(new2[-1])
print(new2[6])
a=len(new2)
print(new2[a-1])


##10. Print 'all' from new2

new2 = tuple(('hello','welcome','all','here',29.32,'python','end'))

print(new2[2])
print(new2[-5])
print(new2[2:3])
print(new2[-5:-4])

print(new2[new2.index('all')])

##11. Print index of 'end'

new2 = tuple(('hello','welcome','all','here',29.32,'python','end'))

print(new2.index('end'))




#12. Print index of first list

tuple1 = ("Orange",2, [10, 20, 30], ['a','b','c'],(5, 15, 25))

print(tuple1.index([10, 20, 30]))

#13. Print 1st list from the tuple1

tuple1 = ("Orange",2, [10, 20, 30], ['a','b','c'],(5, 15, 25))

print(tuple1[2])
print(tuple1[-3])

#14. Change '20' to 'start'

tuple1 = ("Orange",2, [10, 20, 30], ['a','b','c'],(5, 15, 25))

tuple1[2][1]='start'
tuple1[2][-2]='start'
tuple1[-3][1]='start'
tuple1[-3][-2]='start'
print(tuple1)

#15. Replace '15' to '9' in tuple1

tuple1 = ("Orange",2, [10, 20, 30], ['a','b','c'],(5, 15, 25))

x="We can not change the values in the tuple as it is a immutable data type."
print(x)

#16. Print second list from tuple1

tuple1 = ("Orange",2, [10, 20, 30], ['a','b','c'],(5, 15, 25))

print(tuple1[3])
print(tuple1[-2])

#17. Print tuple from tuple1

tuple1 = ("Orange",2, [10, 20, 30], ['a','b','c'],(5, 15, 25))

print(tuple1[4])
print(tuple1[-1])

#18. Change 10 to 'start2'

tuple1 = ("Orange",2, [10, 20, 30], ['a','b','c'],(5, 15, 25))

tuple1[2][0]='start2'
tuple1[2][-3]='start2'
tuple1[-3][0]='start2'
tuple1[-3][-3]='start2'
print(tuple1)

#19. Print 45.21 from tuple11(code should run for all students)

tuple11=(['Hiii',27],'string',('abc',21),45.21,123)

a=tuple11.index(45.21)
print(tuple11[a])
print(tuple11[tuple11.index(45.21)])

#20. Print the number of elements in first list in tuple1.

tuple1 = ("Orange",2, [10, 20, 30], ['a','b','c'],(5, 15, 25))

print(len(tuple1[2]))

#21. Print the count of 'b' in second list in tuple1.

tuple1 = ("Orange",2, [10, 20, 30], ['a','b','c'],(5, 15, 25))

print(tuple1[3].count('b'))


