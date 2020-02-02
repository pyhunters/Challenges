'''
Write a Python function that checks whether a passed string is palindrome or not. Go to the editor
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

المطلوب عمل دالة تحدد ما إذا كانت الكلمة المدخلة يمكن قرائتها من البداية للنهاية كما يمكن قرائتها من النهاية للبداية

'''

@missx 
def palindrome(string):
  return string == string[::-1]

print(palindrome('خوخ'))
True

