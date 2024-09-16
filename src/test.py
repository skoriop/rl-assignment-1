from game import Game


n = 5
h = 10
game = Game(n, h)

total_reward = 0
print("Use 'w', 'a', 's', 'd' to move around the current level")
print("Use 'k' and 'j' to move up and down levels")
print("Use 'q' to quit")
print()
print(f"n = {n}, h = {h}")
while True:
    print()
    print(f"Turns Played: {game.turn}")
    print(f"Current Position: {game.position[:2]} at level {game.position[2]}")
    print(f"Total Reward: {total_reward}")
    print()
    if game.position[:2] == (n, n):
        break
    move = input("Move: ")[:1]
    if move == "q":
        break
    else:
        if move == "w":
            new_position = (game.position[0], game.position[1] + 1, game.position[2])
        elif move == "a":
            new_position = (game.position[0] - 1, game.position[1], game.position[2])
        elif move == "s":
            new_position = (game.position[0], game.position[1] - 1, game.position[2])
        elif move == "d":
            new_position = (game.position[0] + 1, game.position[1], game.position[2])
        elif move == "k": 
            new_position = (game.position[0], game.position[1], game.position[2] + 1)
        elif move == "j":
            new_position = (game.position[0], game.position[1], game.position[2] - 1)
        else:
            print("Invalid input!")
            continue
        try:
            position, reward = game.move(new_position)
        except Exception as e:
            print(e)
            continue
        total_reward += reward
    
    
