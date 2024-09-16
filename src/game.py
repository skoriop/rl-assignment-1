import numpy as np

class Game:   
    def __init__(self, n: int, h: int):
        self.n = n
        self.h = h
        self.position = (1, 1, 1)
        self.turn = 0
    """
    Returns (new position, reward) and throws an exception if the move is invalid
    """
    def move(self, new_position: tuple[int, int, int]) -> tuple[tuple[int, int, int], float]:
        if self.position[:2] == (self.n, self.n) or not self.__check(new_position):
            print(self.position)
            print(new_position)
            raise Exception("Invalid move!")
        
        # if the player is moving around in the same level, there is a chance of getting reset
        if new_position[:2] != self.position[:2]:
            rng = np.random.default_rng()
            # print(f"self.level_probability(new_position[2]): {self.__level_probability(new_position[2])}")
            if rng.random() < self.__level_probability(new_position[2]):
                new_position = (1, 1, new_position[2])

        self.position = new_position
        self.turn += 1
        
        if self.position[:2] == (self.n, self.n):
            return (self.position, self.__final_reward(new_position[2]))
        else:
            return (self.position, self.__move_reward(new_position[2]))
    """
    haha
    """
    def check(self, new_position: tuple[int, int, int]) -> bool:
        return self.__check(new_position) 
    
    def __check(self, new_position: tuple[int, int, int]) -> bool:
        if new_position[0] < 1 or new_position[0] > self.n:
            return False
        if new_position[1] < 1 or new_position[1] > self.n:
            return False
        if new_position[2] < 1 or new_position[2] > self.h:
            return False
        if abs(new_position[0] - self.position[0]) + abs(new_position[1] - self.position[1]) + abs(new_position[2] - self.position[2]) != 1:
            return False
        return True
    
    def __level_probability(self, h: int) -> float:
        return 1 - np.exp(-1.0 * h / (self.h ** 2))

    def __final_reward(self, h: int) -> float:
        return 100.0 * h
    
    def __move_reward(self, h: int) -> float:
        return -1.0 / h
    
    def is_terminal(self, new_position: tuple[int, int, int]) -> bool:
        return new_position[:2] == (self.n, self.n)
