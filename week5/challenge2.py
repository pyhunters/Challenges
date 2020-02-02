'''
 Write a Python program to reverse a string. 

المطلوب كتابة دالة تستقبل string وتقوم بإعادة ترتيب عناصرها من النهاية للبداية وتقوم بارجاع الشكل الأخير 

Sample String : "1234abcd"
Expected Output : "dcba4321"
'''

@missx 


def reverse_str(string):
  my_list = list(string)
  my_list.reverse()
  return ''.join(my_list)

str_ = '1234abcd'
print(reverse_str(str_))
#output :dcba4321




def reverse(string):  
    return string[::-1]

str_ = '1234abcd'
print(reverse(str_))
#output :dcba4321



