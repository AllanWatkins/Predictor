import pdct_io as io
import pdct_scraper as scrape
import blobber as iob

import json
import numpy as np
import pandas as pd

# Find the winner from a row of the results table
# row is a series (aka like from a df)
def findWinner (row) :
    if row["home_score"] > row["away_score"] :
        return row["home_team"]
    elif row["home_score"] < row["away_score"] :
        return row["away_team"]
    elif row["home_score"] == row["away_score"] :
        return "tie"

# populate the winner column in the provided dataframe based on the home_score and away_score
def addWinner(df) :
    new_col = []
    for row in df.iterrows() :
        new_col.append(findWinner(row[1]))
    df["winner"]=new_col
    return df

# Check the results table and return a boolean list of whether you made the right prediction
# df (dataframe) - results table (must include a "winner" column)
# prediction_col (string) - column containing the predictions you want to check.
def didIWin(df, prediction_col) :
    new_col = []
    for index, row in df.iterrows() :
        iWon = row["winner"] == row[prediction_col]
        new_col.append(iWon)
    return new_col

##############################################################################################

# read in a week
results_df = scrape.scrapeWeek(2018,3)

# write to CosmosDB
iob.writeResults(results_df)

# calculate the winner of each game
results_df = addWinner(results_df)


# Create a set of predictions (basically the home team in each case)
pred_allan = pd.DataFrame()
pred_allan = results_df.loc[results_df["week"]=="week1",["home_team","away_team"]]
pred_allan["allan"] = pred_allan["home_team"]
pred_allan["week"] = "week1"
pred_allan["home_team"] = pred_allan["home_team"].astype(str)
pred_allan["away_team"] = pred_allan["away_team"].astype(str)
pred_allan["allan"] = pred_allan["allan"].astype(str)
pred_allan["week"] = pred_allan["week"].astype(str)

# Create a set of predictions (basically the away team in each case)
pred_chris = pd.DataFrame()
pred_chris = results_df.loc[results_df["week"]=="week1",["home_team","away_team"]]
pred_chris["chris"] = pred_chris["away_team"]
pred_chris["week"] = "week1"
pred_chris["home_team"] = pred_chris["home_team"].astype(str)
pred_chris["away_team"] = pred_chris["away_team"].astype(str)
pred_chris["chris"] = pred_chris["allan"].astype(str)
pred_chris["week"] = pred_chris["week"].astype(str)

#merge the predictions into the results_df
results_df = pd.merge(results_df, pred_chris, how="outer")
results_df = pd.merge(results_df, pred_allan, how="outer")
results_df = results_df.replace(np.nan, "No Prediction")

results_df["allan_results"] = didIWin(results_df, "allan")
results_df["chris_results"] = didIWin(results_df, "chris")

results_dict = results_df.to_dict(orient="index")
results_json = json.dumps(results_dict, indent=4)
