import json

directory = ".\\data\\"

# take a predictor node dictionary and write it as a file
# object is a node object
def writeNode(node) :
    # define the location of the file as the name of the team
    filename = node["name"] + ".json"
    my_file = directory + filename

    # dump the dictionary as a JSON file
    with open(my_file, "w") as outfile :
        json.dump(node, outfile, indent=4)

# read a JSON file in as a dictionary
# team is a string (name of team = name of JSON file)
def readNode(team) :
    my_file = directory + team + ".json"

    with open(my_file) as infile :
        return json.load(infile)

# add a fixture to a team's record
# team is a string (name of team = name of JSON file)
# data is dictionary of the fixture
def addFixture(team, season, week, opposition, home) :
    existing = readNode(team)
    if season not in existing["fixtures"].keys() :
        existing["fixtures"][season] = {}
        #print("adding season " + season)
        #print(json.dumps(existing,indent=4))
    if week not in existing["fixtures"][season].keys() :
        #print("adding fixture for week " + week)
        existing["fixtures"][season][week] = {
            "opposition" : opposition,
            "home" : home
        }
    writeNode(existing)
