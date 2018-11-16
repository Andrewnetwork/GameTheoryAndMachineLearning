# Checkers.py
# Andrew Ribeiro 
# November 2018 

# CS = {E,R,B,RK,BK}
# CS_enum = {0,1,2,3,4}

import numpy as np
from random import randint
import math

class Checkers:
    def __init__(self,initialState = None, initialTurn = None):
        if initialState == None:
            # State array. 
            self.state = [1]*12 + [0]*8 + [2]*12
            self.rows = 8
            self.columns = 8
            self.RSet = set([1,3])
            self.BSet = set([2,4])
            self.pieceSets = {1:self.RSet , 2:self.BSet}

        else:
            raise NotImplemented
        
        if initialTurn == None:
            self.turn = randint(1,2)
        else:
            self.turn = initialTurn

    def getDenseLabelMatrix(self):
        return np.matrix(list(range(self.rows*self.columns))).reshape(self.rows,self.columns)
    
    def getSparseLabelMatrix(self):
        nl = []
        alternate = True

        for i in range(32):
            if alternate:
                nl.append(0)
                nl.append(i)
            else:
                nl.append(i)
                nl.append(0)

            if((i+1) % 4 == 0): 
                alternate = not alternate

        return np.matrix(nl).reshape(8,8)

    # Returns a numpy matrix.
    def getMatrix(self):
        nl = []
        alternate = True

        for i in range(32):
            if alternate:
                nl.append(0)
                nl.append(self.state[i])
            else:
                nl.append(self.state[i])
                nl.append(0)

            if((i+1) % 4 == 0): 
                alternate = not alternate

        return np.matrix(nl).reshape(8,8)

    def move(self,pos):
        """Move a game piece. Equivalent to swapping two elements in the state tuple.

        Keyword arguments:
        pos -- ([0,63],[0,63]) 

        Output: 
        false -- Move failed because it is invalid.
        true  -- Move succeeded.
        """

        if self.isValidMove(pos):
            # Convert position from full board labeling to dense labeling. 
            p0 = pos[0] - math.ceil(pos[0]/2)
            p1 = pos[1] - math.ceil(pos[1]/2)

            # Swap positions. 
            self.state[p0],self.state[p1] = self.state[p1],self.state[p0]
            return True
        else:
            return False

    def diagonalMoves(self,i):
        colP = self.columns+1
        colM = self.columns-1

        # Superset of the diagonals. 
        candidates = [i - colP, i - colM, i + colM, i + colP]

        # Filters.
        rowCond = lambda z,y: abs(math.floor(z/self.columns) - math.floor(y/self.columns)) == 1
        boundaryCond = lambda z: z >= 0 and z < self.rows*self.columns

        return set([x for x in candidates if rowCond(i,x) and boundaryCond(x)])

    def isValidMove(self,pos):
        # There are two types of moves, a jump and swap with an empty space. 
        
        matItter = self.getMatrix().flat
        # If the move is a diagonal move.
        if pos[0] in self.diagonalMoves(pos[1]):
            bothB = matItter[pos[0]] in self.BSet and matItter[pos[1]] in self.BSet
            bothR = matItter[pos[0]] in self.RSet and matItter[pos[1]] in self.RSet

            # If both pieces aren't the same color. 
            if not (bothB or bothR):
                #TODO: Handle jump logic. 
                return True
            else:
                # Both pieces are the same color. Invalid move. 
                return False
        else:
            return False
        
    def validMoves(self):
        """Returns a set of allowable moves."""
        validMovesOut = []

        idx = 0
        for i in self.getMatrix().flat:
            # If the piece belongs to the current turn player, check for valid diagonal moves.
            if i in self.pieceSets[self.turn]:
                for dm in self.diagonalMoves(idx):
                    if self.isValidMove((idx,dm)):
                        validMovesOut.append((idx,dm))
            idx += 1
        
        return validMovesOut
        
            
    