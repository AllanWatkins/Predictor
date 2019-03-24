from azure.storage.blob import BlockBlobService, PublicAccess
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity

# Create the BlockBlobService that is used to call the Blob service for the storage account
#block_blob_service = BlockBlobService(account_name='predictomatic', account_key='H2LyENOrQJ+QxAHMt3eU6+n4/VMJ3wBFzL9j/eAwf6QYQfkOJKV2r+ArDKYkz1/tToztH/Wp+kDEvfhRlUqaiQ==')

#my_table = "results"

#table_service = TableService(account_name='predictomatic', account_key='H2LyENOrQJ+QxAHMt3eU6+n4/VMJ3wBFzL9j/eAwf6QYQfkOJKV2r+ArDKYkz1/tToztH/Wp+kDEvfhRlUqaiQ==')
#table_service.create_table(my_table)

# Send a set of results to CosmosDB
# results_df (dataframe) - a set of results/fixtures/predictions

#def transBool() :

def writeResults(results_df) :
    # change the type of any non-string columns to string
    for i in [col for col in results_df.columns if type(col) != str] :
        results_df[col] = results_df[col].astype(str)
    results_df["PartitionKey"] = results_df["season"] + "-" + results_df["week"]
    results_df["RowKey"] = results_df["home_team"] + "-at-" + results_df["away_team"]
    print("OK")
    table_service = TableService(account_name='predictomatic', account_key='H2LyENOrQJ+QxAHMt3eU6+n4/VMJ3wBFzL9j/eAwf6QYQfkOJKV2r+ArDKYkz1/tToztH/Wp+kDEvfhRlUqaiQ==')
    for key, value in results_df.iterrows() :
        linq = "PartitionKey eq \'" + value["PartitionKey"] + "\\ and RowKey eq \\\'" + value["RowKey"] + "\\\'"
        print(linq)
        if len(list(table_service.query_entities("results", filter=linq))) == 0 :
            table_service.insert_entity("results", value.to_dict())



#with TableService(account_name='predictomatic', account_key='H2LyENOrQJ+QxAHMt3eU6+n4/VMJ3wBFzL9j/eAwf6QYQfkOJKV2r+ArDKYkz1/tToztH/Wp+kDEvfhRlUqaiQ==') as table_service :