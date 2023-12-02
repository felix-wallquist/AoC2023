max_cube = {"red": 12, "green": 13, "blue": 14}
possible = True
num_possible = 0
game_iteration = 1

with open("input.txt") as input:
    for line in input:
        games = line.split(": ")[1].split(";")

        for i in range(0, len(games)):
            games[i] = games[i].strip()

        for game in games:
            game = game.replace(",", "").split()
            for key in list(max_cube.keys()):

                if key in game:
                    index = game.index(key)

                    if int(game[index-1]) > max_cube.get(key):
                        possible = False

        if possible:
            num_possible += game_iteration
        possible = True
        game_iteration += 1

print(num_possible)
