from sage.all import *
a = int(input('>'))
print(matrix(Zmod(2),[a,a+1,a+2]))
exit()