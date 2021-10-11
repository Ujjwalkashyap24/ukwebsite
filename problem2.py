letter = '''<|name|>
your are selected
<|date|>'''
name = input("enter your name:\n")
date = input("enter your date")
letter = letter.replace("<|name|>",name)
letter = letter.replace("<|date|>",date)
print(letter)