## Practice on Sets

#1.creat an empty set
set_1=set()
print('1.',set_1)

#2.create a set with multiple values,repetitions and all possible data type, print the set
set_2={1,2,1,3,4,5,6,6,'Hi',12.3,(1,2,3)}
print(type(set_2))
print('2.',set_2)

##3.add 100 in the set
set_2.add(100)
print('3.',set_2)

#4.add 23,'little',[11,'done',33],('a','b',10),{'d','f'},{71:'one',72:'two'},set1
set1={1,2,3,4}
set_2.update('23','little',[11,'done',33],('a','b',10),{'d','f'},{71:'one',72:'two'},set1)
print(set_2)

#5. delete tuple and 50 from set
set_2.remove((1,2,3))
set_2.discard(50)
print(set_2)
#6.delete first element from set
set_2.pop()
print(set_2)

set1 = {1,2,3,4,7,9}  
set2 = {1,4,5,6,11,3}

#7.print  all elements of these sets
print(set1.union(set2))
print(set1|set2)

#8.print the common elements of these sets
print(set1.intersection(set2))
print(set1&set2)

#9.print the uncommon elements of both set1 and set2
print(set1.symmetric_difference(set2))
print(set1^set2)

#10.print difference of set2 and set1
print(set2.difference(set1))
print(set2-set1)

s1 = {1,3,4,11}
s2 = {3,2,4,5,6}
s3 = {2,3,4,5,6,8,9,1,10,11,12,20}

#11.check if 4 is present in s1
print(4 in s1)

#12.check if s1 and s2 are same
print(s1==s2)

#13.check if s1 is subset of s3
print(s1<=s3)
print(s1.issubset(s3))

#14.check if s2 is proper set of s3
print(s2<s3)
