import random

class RPSBoard(object):
    def __init__(self):
        #tracks opponents moves
        self._opp_moves = [0,0,0]#rock, paper, scissors
        #tracks how many times lost from making a move
        self._reg_moves = [0,0,0]#rock, paper, scissors
        #tracks what opponents do after each move
        self._opp_predictions = [[0,0,0],[0,0,0],[0,0,0]]#rps
        self._opp_prev = ""
        self._move_dict = {0:"r", 1:"p", 2:"s"}
        self._ind_dict = {"r":0, "p":1, "s":2}
        self._beat_dict = {"s":"r", "p":"s", "r":"p"}
        self._poss_ans = {"r", "p", "s", "x"}

    def _ai_move(self):
        move = ""
        poss_opp_moves = []
        if self._opp_prev != "":
            for index in range(3):
                if self._opp_predictions[self._ind_dict[self._opp_prev]][index] == max(self._opp_predictions[self._ind_dict[self._opp_prev]]):
                    poss_opp_moves.append(index)
        else:
            poss_opp_moves = [0, 1, 2]
        for opp_move in poss_opp_moves:
            for index in poss_opp_moves:
                if opp_move != index:
                    if self._opp_moves[index] >= self._opp_moves[opp_move]:
                        break
            else:
                move = self._beat_dict[self._move_dict[opp_move]]
                break
        else:
            maxes = []
            temp_arr = []
            for opp_move in poss_opp_moves:
                temp_arr.append(self._opp_moves[opp_move])
            for opp_move in poss_opp_moves:
                if self._opp_moves[opp_move] == max(temp_arr):
                    maxes.append(opp_move)
            mins = []
            maxv = [self._reg_moves[mx] for mx in maxes]
            for maxn in maxes:
                if self._reg_moves[maxn] == max(maxv):
                    mins.append(maxn)
            move = self._move_dict[random.choice(mins)]
        return move
    
    def _test_move(self, ai, pl):
        if ai == pl:
            return 0
        elif (ai == "r" and pl == "s") or (ai == "s" and pl == "p") or (ai == "p" and pl == "r"):
            return 1
        else:
            return -1
    
    def play(self):
        ai_score = 0
        pl_score = 0
        first = True
        while True:
            answer = raw_input("Play rock, paper, or scissors. [r/p/s/x for exit]")
            while answer not in self._poss_ans:
                answer = raw_input("Sorry, didn't quite get that")
            if answer == "x":
                break
            ai_answer = self._ai_move()
            result = self._test_move(ai_answer, answer)
            self._reg_moves[self._ind_dict[answer]] += result
            self._opp_moves[self._ind_dict[answer]] += 1
            if not first:
                self._opp_predictions[self._ind_dict[self._opp_prev]][self._ind_dict[answer]] += 1
            print("You played " + answer + "!")
            print("Computer played " + ai_answer + "!")
            if result == 1:
                print("Computer wins!")
                ai_score += 1
            elif result == -1:
                print("You win!")
                pl_score += 1
            else:
                print("It's a tie!")
            print("Current score: C" + str(ai_score) + "-P" + str(pl_score))
            self._opp_prev = answer
            first = False

brd = RPSBoard()

brd.play()
