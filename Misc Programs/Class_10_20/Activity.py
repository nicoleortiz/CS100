o = open('copyMyself.txt', 'w')
l = open('aboutMe.txt', 'r')
o.write(l.read())
l.close()
o.close()