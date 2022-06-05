## Sets
'''
-set is mutable and has only unique immutable elements.
-A set is created by placing all the items (elements) inside curly
braces {},separated by comma, or by using the built-in set()function.
-It can have any number of items and they may be of different
types (integer, float, tuple, string etc.)
-But a set cannot have mutable elements like lists, sets or
dictionaries as its elements.
'''

#1.0 Initializing set
mySet1=set()
print(type(mySet1))
print(mySet1)

#2.0 Initializing elements in set
my_set2={1.3,'Hello',(1,2,3),6,6}
print('2.',type(my_set2))
print('3.',len(my_set2))
print('4.',my_set2)

#3.0 Adding elements to set
set9={1,2,3}
print(set9)
set9.add('x')
print(set9)

#4.0 Update sets
set1={2,3,4,5}
set2={4,5,6,7}
set1.update(set2,{33,44,55},'b')
print(set1)
#5.0 Remove an element(it will throw a key error ,if element is not present)
set1={2,3,4,5}
set1.remove(3)
print(set1)

#6.0 Discard an element (it will not throw a key error ,if element is not present)
set1.discard('a')
print(set1)

#7.0 pop function
a=set1.pop()
print(a)
print(set1)

#8.0
set1={2,3,4,5}
print('Maximum value is:')
print(max(set1))
print('Minimum value is:')
print(min(set1))
print('Sum of values is:')
print(sum(set1))

#9.0 Empty the set
set1.clear()
print(set1)

#10.0 Other methods in set
set1={2,3,4,5}
set2={4,5,6,7}
print('1.',set1)
print('2.',set2)

#11.0 Union (It is all items of both sets)
print('3.',set1.union(set2))
print('3.',set1|set2)

#12.0 Intersection (It is common itemsof the both sets)
print('4.',set2.intersection(set1))
print('4.',set1&set2)

#13.0 Difference set1-set2
print('5.',set1.difference(set2))
print('5.',set1-set2)

# set2-set1
print('6.',set2.difference(set1))
print('6.',set2-set1)

#14.0 Symmetric difference (It is uncommon items of both sets)
print('7.',set1.symmetric_difference(set2))
print('7.',set1^set2)

#15.0 Boolean oprators of sets
superset={0,1,2,3,4,4,4,5,6,7,8,9}
s1={2,3,4,5}
s2={4,5,6,7}
print('8. Superset is:',superset)
print('9. s1 is:',s1)
print('10. s2 is:',s2)

#find an element in set
print('11. if 6 is in s1: ',6 in s1)
print('11. if 6 is not in s1: ',6 not in s1)

# if symmetric
print('12. if s1 and s2 symmetric ?  ',s1==s2)

# if not symmetric
print('13. if s1 and s2 not symmetric ? ',s1!=s2)

# if s1 is a subset of superset,
print('14. if s1 is a subset of superset ? ',s1.issubset(superset))
print('14. if s1 is a subset of superset ? ',s1<=superset)

# if s1 is a proper subset of superset
print('15. if s1 is a proper subset of superset ? ',s1<superset)

# if s2 is a subset of s1
print('16. if s2 is a subset of s1 ? ',s2.issubset(s1))
print('16. if s2 is a subset of s1 ? ',s2<=s1)

# if s2 is a proper subset of s1
print('17. if s2 is a proper subset of s1 ? ',s2<s1)

# if 'superset' is a superset of s1
print('18. if superset is a superset of s1 ? ',superset.issuperset(s1))
print('18. if superset is a superset of s1 ? ',superset>=s1)

