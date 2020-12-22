import sys
from collections import deque

def join_deck(p):
    return '.'.join(str(c) for c in p)

class Game :
    def __init__(self):
        self.p1 = deque()
        self.p2 = deque()
        self.games_played = set()
        self.winner = 0 

    def parse(self):
        for l in open(sys.argv[1]) :
            if l.startswith("Player 1:"):
                p = self.p1
            elif l.startswith("Player 2:"):
                p = self.p2
            elif 1<len(l) :
                p.append(int(l))

    def game_string(self):
        return join_deck(self.p1)+'|'+join_deck(self.p2)

    def play(self) :
        while self.p1 and self.p2 and not self.winner :
            # recurse prevention
            gs = self.game_string()
            if gs in self.games_played :
                self.winner = 1
                break
            else:
                self.games_played.add(gs)
        
            c1 = self.p1.popleft()
            c2 = self.p2.popleft()
            if c1 <= len(self.p1) and c2 <= len(self.p2) :
                sg = Game()
                for c in range(c1) :
                    sg.p1.append(self.p1[c]) 
                for c in range(c2) :
                    sg.p2.append(self.p2[c])
                res = sg.play()
            else :
                res = 1
                if c1 < c2 :
                    res = 2
        
            # normal
            if res == 2 :
                self.p2.append(c2)
                self.p2.append(c1)
            else :
                self.p1.append(c1)
                self.p1.append(c2)
        
        if not self.winner :
            if self.p1 : self.winner=1
            else: self.winner=2

        return self.winner
        
g = Game()
g.parse()   
w = g.play()
if w == 1 : winner = g.p1
else : winner = g.p2

s = sum((len(winner)-i)*v for i,v in enumerate(winner))
print(winner, s)

