import re

reg = re.compile("h?t?t?p?s?:?/?/?www(\.[a-z]+\-?[a-z]+)+\.[a-z]+/?([a-z]+/)*")

m = reg.match("www.google.com")
print(m)

m = reg.match("https://www.youtube.com")
print(m)

m = reg.match("http://www.uni-wuerzburg.de")
print(m)

m = reg.match("www.wiwi.uni-wuerzburg.de/wiba/startseite/")
print(m)

m = reg.match("http://www.uni.sau-haufen.mutte.servustv/ich/kein/bock/mehr/")
print(m)

