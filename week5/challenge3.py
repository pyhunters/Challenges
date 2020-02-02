'''
Write a Python function that takes a list and returns a new list with unique elements of the first list. 

المطلوب عمل دالة تقوم باستقبال قائمة ثم إعادة قائمة تحتوي ع نفس العناصر بدون تكرار 

Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]

'''

@missx 

def unique(list_):
  return list(set(list_))

print(unique([1,2,2,3,3,4,4]))
#output :[1, 2, 3, 4]

