from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# Function to web scrape NFL regular season results from NFL.com for multiple weeks
# season (integer) - the year the season started as an integer
# weeks (list of integers) - the week numbers requested

def scrapeResults(season=2019, weeks=[1]) :
    full_results = {}
    for week in weeks :
        full_results["week" + str(week)] = scrapeWeek(season, week)
    return(full_results)

# Function to web scrape NFL regular season results from NFL.com for a specific week
# season (integer) - the year the season started as an integer
# week (integer) - the week number as an integer

def scrapeWeek(season, week) :
    # Generate the url for the results page based on the naming schema of nfl.com
    url = "http://www.nfl.com/schedules-uk/" + str(season) + "/REG" + str(week)

    # Generate a Beautiful Soup object from the url
    html = urlopen(url)
    soup = BeautifulSoup(html,'lxml')

    # filter to find all the html elements that represent a result
    games = soup.find_all("div", attrs={"class":"list-matchup-row-team"})

    # iterate over each result, loading the team names and scores to create a list of result dictionaries
    results = pd.DataFrame()
    for game in games :
        this_result = {}
        for row in game.contents :
            if row == "\n" :
                continue
            elif row["class"][0] == "team-name" :
                if row["class"][1] == "home" :
                    this_result["home_team"] = str(row.contents[0])
                elif row["class"][1] == "away" :
                    this_result["away_team"] = str(row.contents[0])
            elif row["class"][0] == "team-score" :
                if row["class"][1] == "home" :
                    this_result["home_score"] = str(row.contents[0])
                elif row["class"][1] == "away" :
                    this_result["away_score"] = str(row.contents[0])
        results = results.append(this_result, ignore_index=True)
    results["week"] = str(week)
    results["season"] = str(season)
    return results