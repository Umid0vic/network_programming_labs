#lab 2 - Network Programming
#created by Osman Said 2021-10-26

dic = {}
lista = []
file = open('score2.txt')

for line in file.readlines():
    upp, number, firstName, lastName, points = line.split()
    key = firstName+ ' ' +lastName
    if key in dic:
    	new_points = dic[key] + int(points)
    	dic[key] = new_points
    else:
    	dic[firstName+ ' ' +lastName] = int(points)

print(dic)

