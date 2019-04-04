# -*- coding: utf-8 -*-
import requests

# test = raw_input()
url = 'https://post-rps-server.herokuapp.com?weapon='
# r = requests.post("https://post-rps-server.herokuapp.com?weapon=rock")
# print(r.json())

sumRes = { 'Lose': 0, 'Win': 0, 'Draw': 0 }

while (sumRes['Lose'] < 3) and (sumRes['Win'] < 3):
    print "input your weapon(rock,paper,scissors) >>",
    user = raw_input()
    if user not in ['rock', 'paper', 'scissors']:
        continue
    response = requests.post(url + user)
    server = response.json()['server_weapon']
    result = response.json()['result']
    print "Server: " + server
    print "You: " + user
    print "Result: " + result
    sumRes[result] += 1

print "#### finish ####"
print "Win: %d" % sumRes['Win']
print "Lose: %d" % sumRes['Lose']
print "Draw: %d" % sumRes['Draw']

if sumRes['Win'] == 3:
    print "You Win!"
else:
    print "You Lose!"
