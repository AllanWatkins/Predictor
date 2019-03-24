import json

directory = "C:\\Users\\allan\\"
filename = "jets1.json"
my_file = directory + filename

team = {
    "name":"New York Jets",
    "game1":{
        "venue":"home",
        "opponent":"Denver Broncos",
        "date":"01012019",
        "my_score":24,
        "their_score":17
    },
    "game2":{
        "venue":"away",
        "opponent":"LA Rams",
        "date":"24122018",
        "my_score":10,
        "their_score":14
    }
}

print(type(team))
print(team)
bob = json.dumps(team, indent=4)
print(type(bob))

with open(my_file,'w') as outfile:
    json.dump(team,outfile, indent=4)

with open(my_file) as infile:
    team1 = json.load(infile)