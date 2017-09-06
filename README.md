# Superpowers
Sane map() for lists for unsane people.

## Usage

The following is valid code after using this library:

````python
from superpowers import patch, _
patch()

[1, 2, 3].map(_ * 3 + 3)._(print)
# [6, 9, 12]
['Hello', 'World'].map(_.upper).mkString(', ')._(print)
# HELLO, WORLD
[1, 2, 3, 4, 5].filter(_ > 3).map(print)
# 4
# 5
(1000).together(3001).together(1000)._(range)._(list).map(str).mkString(', ').together('are big numbers')._(print)
# 1000, 2000, 3000 are big numbers
````
