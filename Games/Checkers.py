# Checkers.py
# Andrew Ribeiro 
# November 2018 

# CS = {E,R,B,RK,BK}
# CS_enum = {0,1,2,3,4}

class Checkers:
    def __init__(self,initialState = None):
        if(initialState == None):
            self.state = [1]*12 + [0]*8 + [2]*12
            
    