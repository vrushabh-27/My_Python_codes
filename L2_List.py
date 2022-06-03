# List in Python

#-A list in Python is used to store the sequence of  various types of data.
#-Lists are mutable type it means we can modify its elements after it is created.
#-List is created by placing elements inside square brackets[] separated by comma.

#1.0 Initilising list

list_0=[]
print(list_0)

#2.0 Creating a list

list_1=[1,2,3,'Hello',4,5]
print(list_1)

list_2=list([5,6,'Hi',7])
print(list_2)
list_3=[0,1,2,3,4,5,6]

#3.0 Index function, (list[starting index : ending index : skipping value])

print(list_1[:])        # To print all elements of list
print(list_2[3])        # To print the value of element at 3rd index
print(list_3[0:4])      # To print the values from index 0 to 3
print(list_1[::-1])     # To print list in reverse order
print(list_1[-2:-5:2])
print(list_1[0:5:2])    # To print using skipping index 2
print(list_1[3][3])     # To print alphabet of string using index place

#4.0 append function (for adding one element at the end of the list

list_1=[1,2,3,'Hello',4,5]
list_2=list([5,6,'Hi',7])
list_3=[0,1,2,3,4,5,6]

list_2.append(10)       # To add element in the list
print(list_2)

list_2.append([11,12])  # To add two elements as one argument
print(list_2)

#5.0 extend function (for adding multiple elements to list)

list_2.extend([13])
print(list_2)

list_2.extend([14,15])  # To add two elements as two arguments
print(list_2)

#6.0 insert function

list_3.insert(3,'Good') # To add a element at a particular index
print(list_3)

#7.0 index function

print(list_2.index('Hi'))

#8.0 count function

print(list_1.count('Hello'))
print(list_1.count(3))

#9.0 len function

a=len(list_1)
print(a)
print(len(list_1))

#10.0 reverse function
list_3.reverse()
print(list_3)
'''
#11.0 sort function

list4=[6,2,8,1,10,4,7,3,0,5,9]
'''
#list4.sort()   #change the list by sort in ascending order
#print(sorted(list4))   #only print i ascending order
#print(list4)

list4.sort(reverse=True)   #sort in descending order
print(sorted(list4,reverse=True))
print(list4)

#12.0 copy function
list5=list4.copy()
print('list5 is',list5)

#13.0 pop function (use index)

a=(list4.pop(2))
print(a)
print(list4)

#14.0 remove function (for removing an element in the list use value)

list4.remove(7)
print(list4)

#15.0 del function (for deleting an element in list use index)

del (list4[2])
print(list4)

#16.0 clear function (for clearing the list)

list4.clear()
print(list4)

#17.0 replace an element in list

list5=[6,2,8,1,10,4,7,3,0,5,9]
list5[-2]='5 is replacing'
list5[3]=35
print(list5)


