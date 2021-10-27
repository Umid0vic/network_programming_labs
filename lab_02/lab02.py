#lab 2 - Network Programming - Python: Containers
#created by Osman Said 2021-10-26


players = {}
top_players = {}
file = open('score2.txt')

for line in file.readlines():
    upp, number, firstName, lastName, points = line.split()
    key = firstName+ ' ' +lastName
    if key in players:
    	new_points = players[key] + int(points)
    	players[key] = new_points
    else:
    	players[firstName+ ' ' +lastName] = int(points)

print('#####Players with their score#####')
highest = max(players, key=players.get)

for k, v in players.items():
	print(k, v)
	if v == players[highest]:
		top_players[k] = v

print('#####Top players#####')
print(top_players)

