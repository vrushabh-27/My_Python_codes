## Dictionary

#- Dictionary is mutable

#1.0 Initialize Dictionary
my_dict={}
my_dict_1=dict()
print('1.',my_dict)
print('2.',my_dict_1)

#2.0 Creating Dictionary
dict1={1:'python',2:'java'}
dict2=dict({1:'one',2:'two'})
print('1.',dict1)
print('2.',dict2)

#3.0 Changing an element
dict3={'one':'python','two':'data science'}
print('1. This is dict3',dict3)

#Changing the value 'data science' to 'machine learning'
dict3['two']='machine learning'
print('2.',dict3)

#4.0 Adding key and value
dict3['three']='analysis'
print('3.',dict3)

#5.0 Delete element
dict4={'one':'python1','two':'data science','three':'analysis'}
print('1.',dict4)
#print('2.',dict4.pop('two'))  #remove key and value
print('3.',dict4)

#6.0 pop element from dictionary
a=dict4.pop('two')
print('4.',a)
print('5.',dict4)

#7.0 popitem function (pops last element)
dict4={'one':'python1','two':'data science','three':'analysis'}
print('1.',dict4)
#b=dict4.popitem()
#print('2.',b)
print('3.',dict4)

#8.0 Copy function
dict4={'one':'python1','two':'data science','three':'analysis'}
dict5=dict4.copy()
print(dict5)

#9.0 Clearing a dictionary
dict5.clear()
print('5.',dict5)

#10.0 get function (returns value for given key)
dict5={'one':'python1','two':'data science','three':'analysis'}
print(dict5.get('one'))


#11.0 Print keys from dictionary
print('1.',dict5.keys())

#12.0 Print values from dictionary
print('2.',dict5.values())

#13.0 fromkeys function (create a dictionary from a sequesnce of keys)
keys={'one','two','three'}
value=['great']
dict6=dict.fromkeys(keys,value)
print('1.',dict6)

# changing dictionary
value.append('number')
print('2.',dict6)



