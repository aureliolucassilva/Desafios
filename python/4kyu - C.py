# Link -> https://www.codewars.com/kata/51fda2d95d6efda45e00004e

import math

class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, exerciseRank):
        rank = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
        idxUser = rank.index(self.rank)
        idxExercise = rank.index(exerciseRank)

        if idxUser == 15:
            return

        if idxExercise == idxUser - 1:
            self.progress += 1
        elif idxExercise == idxUser:
            self.progress += 3
        elif idxExercise > idxUser:
            d = idxExercise - idxUser
            self.progress += 10 * d * d

        if self.progress >= 100:
            nextRank = math.floor(self.progress / 100)
            idxUser += nextRank
            self.rank = rank[idxUser]
            extraProgress = self.progress - 100 * nextRank
            self.progress = extraProgress

            if self.rank == 0:
                self.rank = 1
            elif self.rank == 8:
                self.progress = 0
