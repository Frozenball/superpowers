from superpowers import patch, _
patch()

[1, 2, 3].map(_ * 3 + 3).map(lambda x: print(x))
['Hello', 'World'].map(_.upper).map(print)
[1, 2, 3, 4, 5].filter(_ > 3).map(print)
