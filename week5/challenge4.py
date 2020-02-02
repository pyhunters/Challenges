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

@zaid 

def plnd(x):
  y=""
  i=-1
  while i>=-len(x):
    y=y+x[i]
    i-=1
  if y==x :
    print(f"the word '{x}' is palindrome. ")
  else:
    print(f"the word '{x}' is not palindrome. ")
    
t=input("please insert your word to check if it is palindrome or not:  ")
plnd(t)

############## extra ################

(lambda txt : print('palindrome') if txt == txt[::-1] else print('no palindrome')(input('Enter a word ')
