max_cube = {"red": 0, "green": 0, "blue": 0}
sum = 0

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
                        max_cube[key] = int(game[index-1])

        game_sum = 1
        for key in list(max_cube.keys()):
            game_sum *= max_cube.get(key)
            max_cube[key] = 0
        sum += game_sum

print(sum)
