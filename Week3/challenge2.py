
'''
Write a Python program to count the number of even and odd numbers from a series of numbers. 

أكتب برنامج يعد كم عدد زوجي وكم عدد فردي بين الاعداد 0 الى 10 


Output : 
Number of even numbers : 6
Number of odd numbers : 5

'''




#------------------ @start:zaid------------------------------

n=[0,1,2,3,4,5,6,7,8,9,10]
e=0
o=0

#use this
i=0
while i<len(n):
  if (n[i]%2)==0 :
    e+=1
  else :
    o+=1
  i+=1
  
#or this——————————————————
for m in range(len(n)):
  if (n[m]%2)==0 :
    e+=1
  else :
    o+=1
  
print(f"there are {e} even numbers, and {o} odd numbers in the domain [0,{len(n)-1}]")

#-------------------- @end:zaid------------------------------



#------------------ @start:hadeel------------------------------



#-------------------- @end:hadeel------------------------------




#------------------ @start:khalid------------------------------



#-------------------- @end:khalid------------------------------



#------------------ @start:عبدالرحمن------------------------------



#-------------------- @end:عبدالرحمن------------------------------


#------------------ @start:ممدوح------------------------------

odd = []
even = []
i=0
while i < 11:
    if i % 2 == 0:
        odd.append(i)
    else:
        even.append(i)
    i += 1
print('Number of even numbers: ', len(even))
print('Number of odd numbers:', len(odd))

#-------------------- @end:ممدوح------------------------------








