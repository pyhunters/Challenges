 '''

لديكم هذه القائمة تحتوي على عناصر 
my_list = ['HKU3K','KJI8TE','IIUH1I','I7YUI','OPRE9','5JGU','ER4TB','HY0OH']

المطلوب ترتيب هذه القائمة تصاعديًا 
ليكون المخرج كالتالي 

['HY0OH','IIUH1I','HKU3K','ER4TB','5JGU','I7YUI','KJI8TE','OPRE9']

'''
	
#------------------ @start:missx------------------------------	

my_list = ['HKU3K','KJI8TE','IIUHI','I7YUI','OPRE9','5JGU','ER4TB','HY0OH']

my_list.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))
print(my_list)

#------------------ @start:missx------------------------------



#------------------ @start:zaid------------------------------

L = ['HKU3K','KJI8TE','IIUH1I','I7YUI','OPRE9','5JGU','ER4TB','HY0OH']
S=[]
C=[]
for i in L:
  for z in i:
    if z.isdigit():
      S.append(z)
S.sort()
for x in S:
  for y in L:
    if x in y:
      C.append(y)
print("L=",C)

#-------------------- @end:zaid------------------------------



#------------------ @start:hadeel------------------------------












#-------------------- @end:hadeel------------------------------




#------------------ @start:khalid------------------------------

bad_list = ['HKU3K','KJI8TE','IIUH1I','I7YUI','OPRE9','5JGU','ER4TB','HY0OH']
good_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for t in bad_list:
    for letter in t:
        if letter.isdigit():
            index_num = int(letter)
            good_list[index_num] = t
x = 0
for item in good_list:
    x +=1
    try:
        good_list.remove(x)
    except:
        continue
print(good_list)

#-------------------- @end:khalid------------------------------



#------------------ @start:عبدالرحمن------------------------------











#-------------------- @end:عبدالرحمن------------------------------


#------------------ @start:ممدوح------------------------------
my_list = ['HKU3K', 'KJI8TE', 'IIUH1I',
           'I7YUI', 'OPRE9', '5JGU', 'ER4TB', 'HY0OH']
x = 0
d={}
while x < len(my_list):
    letter = my_list[x]
    for p in letter:
        if p.isnumeric() == True:
            d[p]=d.get(p,letter)
    x += 1
sortd=sorted(d.items(),reverse=False)
mysorted_list=[]
for i in sortd:
	mysorted_list.append(i[1])
print(mysorted_list)

#-------------------- @end:ممدوح------------------------------

#------------------ @start:العنود------------------------------










#-------------------- @end:العنود------------------------------

#------------------ @start:أحمد------------------------------










#-------------------- @end:أحمد------------------------------
