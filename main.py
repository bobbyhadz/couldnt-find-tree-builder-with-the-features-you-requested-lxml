from bs4 import BeautifulSoup


markup = """<html><head><title>Example html doc</title></head>
<body>
<p class="title"><b>bobbyhadz.com</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(markup, "lxml")

print(soup.title)
print('-' * 50)
print(soup.title.name)
print('-' * 50)
print(soup.p)
print('-' * 50)
print(soup.find_all('a'))

