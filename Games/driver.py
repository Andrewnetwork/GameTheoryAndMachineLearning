from Checkers import *
from random import randint
a = Checkers()


print(a.getMatrix())
print(a.move(a.validMoves()[0]))
print(a.getMatrix())

#print(a.getDenseLabelMatrix())
#print(a.getSparseLabelMatrix())

#loc = 7
#print("Adjacent diagonals to {0}: {1}".format(loc,str(a.diagonalMoves(loc))))
#print(a.state)
#print(a.getSparseLabelMatrix())
#print(a.getMatrix())
#print(a.validMoves())