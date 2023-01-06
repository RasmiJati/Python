letter = '''
Dear <|Name|>,
Greeting from ABC company.
\tYou are selected!
Have a great day!!
Thanks and regards
John
Date: <|Date|>
'''
name = input("Enter Your name: \n")
date = input("Enter date: \n")
letter = letter.replace("<|Name|>",name)
letter = letter.replace("<|Date|>",date)
print(letter)

# letter = '''
# Dear name,
# Greeting from ABC company.
# \tYou are selected!
# Have a great day!!
# Thanks and regards
# John
# Date: date>
# '''
# name = input("Enter Your name: \n")
# date = input("Enter date: \n")
# letter = letter.replace("name",name)
# letter = letter.replace("date",date)
# print(letter)