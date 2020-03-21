#Practice Quiz: Understanding the Problem in Troubleshooting and Debugging Techniques Week1

'''
The compare_strings function is supposed to compare just the alphanumeric content of two strings, 
ignoring upper vs lower case and punctuation. But something is not working. 
Fill in the code to try to find the problems, then fix the problems.
'''


import re
def compare_strings(string1, string2):
  #Convert both strings to lowercase 
  #and remove leading and trailing blanks
  string1 = string1.lower()
  string2 = string2.lower()

  #Ignore punctuation
  punctuation = r"[,|.|?|'|!]"
  string1 = re.sub(punctuation, r"", string1)
  string2 = re.sub(punctuation, r"", string2)

  #DEBUG CODE GOES HERE
  print("Compare String1 : {} and \n String2 : {}".format(string1,string2))

  return string1 == string2

print(compare_strings("Have a Great Day!", "Have a great day?")) # True
print(compare_strings("It's raining again.", "its raining, again")) # True
print(compare_strings("Learn to count: 1, 2, 3.", "Learn to count: one, two, three.")) # False
print(compare_strings("They found some body.", "They found somebody.")) # False