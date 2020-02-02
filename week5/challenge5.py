'''
لمطلوب عمل دالة لامدا تقوم بإعادة اصغر رقم في قائمة ما 
مثلًا : 
my_list = [8,5,7] 

المخرج يكون : 
5 

بلإضافة الى دالة تقوم بإعادة اكبر رقم في قائمة ما مثال : 

my_list = [8,5,7] 

المخرج يكون : 
8
'''

@missx 
my_list= [1,2,3]
result = lambda x : f'maxNum: {max(x)} \nminNum {min(x)}'
print(result(my_list))


النتيجة
 
maxNum: 3 
minNum: 1






@mmdouh 

#max function 
my_list = [8, 5, 7]
maxnumber = my_list[0]
for i in range(len(my_list)):
    if maxnumber < my_list[i]:
        maxnumber = my_list[i]
        i += 1
print(maxnumber)

#min function 
my_list = [8, 5, 7]
mininumber = my_list[0]
for i in range(len(my_list)):
    if mininumber > my_list[i]:
        mininumber = my_list[i]
        i += 1
print(mininumber)






@zaid 

L=[8,5,7]
m=L[0]

for i in L:
  if i>m:
    m=i

print("maximum is:  ",m)
  
for i in L:
  if i<m:
    m=i

print("minimum is:  ",m)






@khalied 

#max function 

my_list = [1, 5, 3, 4, -1]
i = my_list[0]
x = my_list[0]
for item in my_list:
    if item < i:
        i = item
for item in my_list:
    if item > x:
        x = item
print(f"The samllest number is {i} \nand the maximum number is {x}")


#min function 

a = 'FxmmMxox'
lower = 0
for letter in a:
    if letter.islower():
        lower += 1
cap = len(a) - lower
print(f"The number of capital numbers are {cap} \nand the number of lower numbers {lower}")
