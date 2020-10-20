import pandas as pd 
import boto3
import json

def calc_scores():
    url = 'https://www.pro-football-reference.com/boxscores/'

    # get boxscores
    list_of_dfs = pd.read_html(url, skiprows=1)

    # We just want scores, remove rushing/receiving stats
    res = list_of_dfs[::2]

    #rename columns
    for i in res:
        i.rename(columns = {0 :'team', 1 : 'score', 2: 'margin'}, inplace = True)

    # calculate margin of victory for each df
    for i in res:
        i.loc[0, 'margin'] = i['score'][0] - i['score'][1]
        i.loc[1, 'margin'] = i['score'][1] - i['score'][0] 

    # flatten the list of data frames into a a single data frame
    df = pd.concat(res)
    df = df.reset_index(drop=True)
    json_mov = df.to_json(orient="records")
 
    return json_mov

def handler(event, context):
    df = calc_scores()

    return {
        'statusCode': 200,
        'body': json.dumps(df, indent=4)
    }