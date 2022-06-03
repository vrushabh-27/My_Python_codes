##Practice set for list##

##1.print welcome python1

list11 = ['welcome',1,2,3,'python1',6,5,13,'python2','python3',10.5]

print(list11[0],list11[4])
print(list11[-11],list11[-7])
a=list11[0]
b=list11[4]
print(a,b)
print(list11[0:5:4])
print(list11[-11:-6:4])

##2.table of 2 and 3

list12 =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print(list12[1::2]) #table of 2
print(list12[2::3]) #table of 3

##3.add 'end' after python1 in list11

list11 = ['welcome',1,2,3,'python1',6,5,13,'python2','python3',10.5]

list11.insert(5,'end')
print(list11)


##3.1 reverse list 'new'

new = [10,29,1,2,3,7,9,0,4,55]

print(new[::-1])
new.reverse()
print(new)

##4.only print sorted list in ascending and descending order

new = [10,29,1,2,3,7,9,0,4,55]

print(sorted(new))
print(sorted(new,reverse=True))

##5.changing the list to sort descending order

new = [10,29,1,2,3,7,9,0,4,55]

new.sort(reverse=True)
print(new)

##6.deleting 3 from list 'new' (use index)

new = [10,29,1,2,3,7,9,0,4,55]

del (new[4])
del(new[-6])
print(new)

new.pop(4)
new.pop(-6)
print(new)

##7.remove 29 from list 'new' (use values)

new = [10,29,1,2,3,7,9,0,4,55]

new.remove(29)
print(new)

##8.pop 9 from list 'new' (uses index and returns the value)

new = [10,29,1,2,3,7,9,0,4,55]

r=new.pop(6)
new.pop(-4)
print(new)
print(r)

##9.copy new list

new = [10,29,1,2,3,7,9,0,4,55]

newList=new.copy()
print(newList)

##10. count '2' in list a

a=[1,2,12,2,2,2,3,3,4,4,5,5,6,6,7,7,8,9,9,5,6,5,7,6,7,6,3,4,5]

print(a.count(2))

##11.clear list

a=[1,2,12,2,2,2,3,3,4,4,5,5,6,6,7,7,8,9,9,5,6,5,7,6,7,6,3,4,5]

a.clear()
print(a)

del(a[:])
print(a)

##12.append "cup" in list11

list11 = ['welcome',1,2,3,'python1',6,5,13,'python2','python3',10.5]

list11.append("cup")
print(list11)

##13.extend "tea" in list12

list12 =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

list12.extend(['tea'])
print(list12)

##14.add 32,41,55 in list 'new'

new = [10,29,1,2,3,7,9,0,4,55]

new.extend([32,41,55])
print(new)

new.append([32,41,55])
print(new)

new.insert(3,[32,41,55])
print(new)

###15.add 22,32,42 as one index in list'new'

new = [10,29,1,2,3,7,9,0,4,55]

new.append([22,32,42])
new.insert(0,[22,32,42])
print(new)

##16.replace '29' by 'done' in list 'new'

new = [10,29,1,2,3,7,9,0,4,55]

new[1]='done'
print(new)

