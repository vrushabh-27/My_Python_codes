## Practice on Dictionary
#1.initialize dictionary(without using dictionary function)
myDict={}
print('1.',myDict)

#2.initialize elements(using dictionary function)
myDict_1=dict()
print('2.',myDict_1)

dict13 = {1:'python' , 2:'java',3:'new',4:'last',5:'end'}
#3.print new from dict13
print(dict13[3])
print(dict13.get(3))
#a=dict13.pop(3)
#print(a)

#4.change 'last' to 'hello'
dict13 = {1:'python' , 2:'java',3:'new',4:'last',5:'end'}
dict13[4]='hello'
print(dict13)

#5.add a new pair where, key=10 and value = 'lecture'
dict13 = {1:'python' , 2:'java',3:'new',4:'last',5:'end'}
dict13[10]='lecture'
print(dict13)

#6.pop last pair
dict13 = {1:'python' , 2:'java',3:'new',4:'last',5:'end'}
#dict13.popitem()
print(dict13)

dict13.pop(5)
print(dict13)

#7.delete second pair
dict13 = {1:'python' , 2:'java',3:'new',4:'last',5:'end'}
b=dict13.pop(2)
print(b)
print(dict13)

#8.print keys from dictionary
dict13 = {1:'python' , 2:'java',3:'new',4:'last',5:'end'}
print(dict13.keys())

#9.print values from dictionary
dict13 = {1:'python' , 2:'java',3:'new',4:'last',5:'end'}
print(dict13.values())

#10.clear dict
dict13 = {1:'python' , 2:'java',3:'new',4:'last',5:'end'}
#dict13.clear()
print(dict13)

#11.creat dictionary by using 1,2,3,4 as keys and 'is integer' as value
keys={1,2,3,4}
value=['is integer']
newDict=dict.fromkeys(keys,value)
print(newDict)


