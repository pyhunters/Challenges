
'''
hello Dear hunters Todays' our challenge is : 

Write a Python program to create the multiplication table (from 1 to 10) of a number that has been taken from the user . 

أكتب برنامج يقوم بإنشاء جدول الضرب من 1 الى 10 لعدد يقوم بإدخاله المستخدم 

مثال 

input  
6          
output 
                                             
6 x 1 = 6                                                               
6 x 2 = 12                                                              
6 x 3 = 18                                                              
6 x 4 = 24                                                              
6 x 5 = 30                                                              
6 x 6 = 36                                                              
6 x 7 = 42                                                              
6 x 8 = 48                                                              
6 x 9 = 54                                                              
6 x 10 = 60

'''





#------------------ @start:zaid------------------------------

n=int(input("please insert the number you want to know its multiples:  "))
m=1
while m<11:
  print(f"{m}x{n}=  ".format(),m*n)
  m+=1

#-------------------- @end:zaid------------------------------



#------------------ @start:hadeel------------------------------



#-------------------- @end:hadeel------------------------------




#------------------ @start:khalid------------------------------
a = int(input("Please enter a number to see it's multiplication table: \n"))
while True:
    print(f"{a} x 1 = {a} \n"
          f"{a} x 2 = {a*2} \n"
          f"{a} x 3 = {a*3} \n"
          f"{a} x 4 = {a*4} \n"
          f"{a} x 5 = {a*5} \n"
          f"{a} x 6 = {a*6} \n"
          f"{a} x 7 = {a*7} \n"
          f"{a} x 8 = {a*8} \n"
          f"{a} x 9 = {a*9} \n"
          f"{a} x 10 = {a*10} \n")
    break
#-------------------- @end:khalid------------------------------



#------------------ @start:عبدالرحمن------------------------------



#-------------------- @end:عبدالرحمن------------------------------


#------------------ @start:ممدوح------------------------------

num = int(input('Enter number: '))
i=1
while i < 11:
    print(num, ' * ', i, ' = ', num * i)
    i+=1

#-------------------- @end:ممدوح------------------------------







