import re

text = "This book on tennis cost $3.99 at Walmart."

reg2 = re.compile("$This")
match = reg2.search(text)
print(match)

reg2 = re.compile("^This")
match = reg2.search(text)
print(match)

reg2 = re.compile("This^")
match = reg2.search(text)
print(match)

reg2 = re.compile("This$")
match = reg2.search(text)
print(match)

reg2 = re.compile("Walmart\.$")
match = reg2.search(text)
print(match)

#
