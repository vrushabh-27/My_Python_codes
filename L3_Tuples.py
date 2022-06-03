##Tuples##
'''
-Tuple is same as list but they are not mutable.
-in tuple we use "()" brackets
'''
#1.0 Initiating Tuple
my_tuple=()
my_tuple_1=tuple()
print(my_tuple)
print(my_tuple_1)

#2.0 Creating a tuple
tuple1=(1,2,3)
tuple2=tuple(('Hello','Welcome',3))
print(type(tuple2))
print(tuple1)
print(tuple2)

tuple3='Example',6
print(tuple3)
print(type(tuple3))

#3.0 Print tuple_1
tuple_1=(1,2,3)
print(tuple_1)

#4.0 Print 'Hello', 'all'
tuple_2=tuple(('Hello','welcome','all','here'))
print(tuple_2[0:3:2])

#5.0 Print '1' from tuple_3
tuple_3=(1,2,3,['new','string',1])
print(tuple_3[0])

#6.0 Print tuple_2
print(tuple_2[:])

#7.0 Print 'string' from tuple_3
print(tuple_3[3][1])

#8.0 Replace 'start' with 'change'
tuple3=(1,2,3,['start','done','string','done'])
tuple3[3][0]='change'
print(tuple3)

#9.0 Count 5 in tuple4
tuple4=(1,2,3,['new','string',9,9,9],1,1,5,5)
print(tuple4.count(5))

#10.0 Find index of list in tuple4
print(tuple4.index(['new','string',9,9,9]))
