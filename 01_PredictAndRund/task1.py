import re

text = "This book on tennis cost $3.99 at Walmart."

reg1 = re.compile("ten")
match = reg1.match(text)
print(match)

reg2 = re.compile("this")
match = reg2.match(text)
print(match)

reg3 = re.compile("This")
match = reg3.match(text)
print(match)

reg4 = re.compile("cost")
match = reg4.match(text)
print(match)
match = reg4.search(text)
print(match)

match = reg1.search(text)
print(match)
