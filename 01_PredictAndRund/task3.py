import re

reg = re.compile("www.google.de|com")
print(reg.match("www.google.com"))

reg = re.compile("www\.google\.(de|com)")
print(reg.match("www.google.de"))
print(reg.match("wwwwgoogle.de"))

string = "Niko Stein"

reg = re.compile("Nikolai Stein")
print(reg.match(string))

reg = re.compile("Niko Stein")
print(reg.match(string))

reg = re.compile("Niko|Nikolai Stein")
print(reg.match(string))

reg = re.compile("(Niko | Nikolai) Stein")
print(reg.match(string))

reg = re.compile("(Niko|Nikolai) Stein")
print(reg.match(string))

string = "\."

reg = re.compile(".")
print(reg.match(string))
print(reg.findall(string))

reg = re.compile("\.")
print(reg.match(string))
print(reg.search(string))

reg = re.compile("\\\\")
print(reg.match(string))

reg = re.compile("\\\\.")
print(reg.match(string))
reg = re.compile("\\\\\.")
print(reg.match(string))
#verstehe nicht warum hier das gleiche heraus kommt.

text = "This book on tennis cost $3.99 at Walmart."

reg = re.compile("is")
match = re.findall(reg, text)
print(match)

reg = re.compile("\d")
match = re.findall(reg, text)
print(match)
