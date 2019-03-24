import pdct_io as io
import pdct_scraper as scrape
import json
import numpy as np
import pandas as pd

# Return a dictionary for an initialised team node
# shortname (string) is used for the JSON filename - so no spaces
# longname (string) is the "pretty" name for visualisation
# conference and division (strings) are informational
def buildNode(shortname, longname, conference="TBC", division="TBC") :
    return {
        "name" : shortname,
        "fullname" : longname,
        "division" : conference + " " + division,
        "fixtures" : {}
    }

# Return a dictionary for an initialised fixture
# home (boolean) - True = home fixture, False = away fixture)
# versus (string) - the shortname of the opposition
# week (integer) - the week number
# season (integer) - the year of the season in question
def buildFixture(versus, week, season=2019, home=True) :
    return {
        "opposition" : versus,
        "week" : week,
        "season" : season,
        "home" : home
    }

jets = buildNode("NYJ", "New York Jets", "AFC", "East")

#print(json.dumps(jets,indent=4))

io.writeNode(jets)

jets1 = io.readNode("NYJ")
#fixture1 = buildFixture("Jags", 11, 2018, True)
#print(json.dumps(fixture1,indent=4))
#io.addFixture("NYJ",fixture1)

#fixture2 = buildFixture("NYG", 3, 2018, False)
io.addFixture(team="NYJ",season=2019, week=1, opposition="NYG", home=False)
io.addFixture(team="NYJ", season=2019, week=2, opposition="JAX", home=True)
#print(json.dumps(jets1,indent=4))