#1.take two int inputs from the user, print greatest among them

num1=int(input('Enter number 1: '))
num2=int(input('Enter number 2: '))

if num1>num2:
	print('The greater number is: ',num1)
else:
	print('The greater number is: ',num2)

######################################################################################################

#2.ask the user their Marks and grade accordingly

#Below 25 - F

#25 to 45 - E

#45 to 50 - D

#50 to 60 - C

#60 to 80 - B

#Above 80 - A

marks=int(input('Enter your marks: '))

if marks<25:
	print('Your grade is F')

elif 25<= marks<45:
	print('Your grade is E')

elif 45<=marks<50:
	print('Your grade is D')

elif 50<= marks<60:
	print('Your grade is C')

elif 60<= marks<80:
	print('Your grade is B')

else: 
	print('Your grade is A ')

#######################################################################################################

#3.take age as input from 3 users check who is oldest among them

a1=int(input('Enter your age a1: '))
a2=int(input('Enter your age a2: '))
a3=int(input('Enter your age a3: '))

if a1>a2 and a1>a3:
	print('a1 is the oldest',a1)
elif a2>a1 and a2>a3:
	print('a2 is the oldest',a2)
else:
	print('a3 is the oldest',a3)

                           ##OR##

age_list=(a1,a2,a3)
x=max(age_list)
print('The oldest is',x)

######################################################################################################

#4.take age as input from 3 users check who is youngest among them

a1=int(input('Enter your age a1: '))
a2=int(input('Enter your age a2: '))
a3=int(input('Enter your age a3: '))

if a1<a2 and a1<a3:
	print('a1 is the youngest',a1)
elif a2<a1 and a2<a3:
	print('a2 is the youngest',a2)
else:
	print('a3 is the youngest',a3)

#OR

age_list=(a1,a2,a3)
x=min(age_list)
print('The youngest is',x)

#####################################################################################################

#5.take salary and no of years of service in a company as input from the user	
#company decided to give bonus of 5% to employee,
#if his/her year of service is more than 5 years

#print total amount and bonus amount.


salary=int(input('Enter your salary: '))
service=int(input('Enter your service years: '))

if service>=5:
	bonus=salary*0.05
	print('Total amount: ',salary+bonus,'Bonus; ',bonus)
else:
	print('Total amount: ',salary,'You are not eligible for bonus')

####################################################################################################

#6.Ask user for quantity of a product he purchased,

#A shop will give discount of 10% 

#if the cost of purchased quantity is more than 1000

#Suppose, one unit will cost 100.

#Judge and print discount for user and total cost.


n=int(input('Enter no. of items purchased: '))

total=n*100

if total>1000:
	discount=total*0.1
	print('Total amount: ',total,' Net amount: ',total-discount,' Discount: ',discount)
else:
	print('Total amount: ',total,' Net amount: ',total,' Discount: No discount')

###################################################################################################

#7.take Number of classes held and Number of classes attended and medical
#fitness as input from user, Allow him to attend exam if percentage 75. 

nh=int(input('enter no. of classes held: '))
na=int(input('enter no. of classes attended: '))
fitness=input('Are you medically fit?  Answer yes or no')

attend=(na/nh)*100

if attend>=75 and fitness=='yes':
	print('Your are allowed for exam.')
else:
	print('Your are not allowed for exam.')

####################################################################################################
#8.take input as month from user(take only first six month)

#output should be no. of days in that month



print('The available months are:\njan(0)\nfeb(1)\nmar(2)\napr(3)\nmay(4)\njun(5)')

months=('jan','feb','mar','apr','may','jun')

days=(31,28,31,30,31,30)

a=int(input('Enter the numer given against the month: '))

print('The no. of days in the month of',months[a],' are ',days[a])

                              ##OR##

dict1={'jan':31,'feb':28,'mar':31,'apr':30,'may':31,'jun':30}
b=input('Enter a month: ')
print('The no. of days in month ',b,' are',dict1[b])

                              ##OR##

if b=='jan' or b=='mar' or b=='may':
        print('The no. of days in month ',b,'are 31')
elif b=='apr' or b=='jun' :
        print('The no. of days in month ',b,'are 30')
else:
        print('The no. of days in month ',b,'are 28')


##################################################################################################

#9.take 10 inputs from the user, print greatest among them.


a1=int(input('Enter your age a1: '))
a2=int(input('Enter your age a2: '))
a3=int(input('Enter your age a3: '))
a4=int(input('Enter your age a4: '))
a5=int(input('Enter your age a5: '))
a6=int(input('Enter your age a6: '))
a7=int(input('Enter your age a7: '))
a8=int(input('Enter your age a8: '))
a9=int(input('Enter your age a9: '))
a10=int(input('Enter your age a10: '))

age_list=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]

x=max(age_list)

print('The oldest is ',x)


