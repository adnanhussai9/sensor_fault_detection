import pymongo
import pandas as pd
import json

client=pymongo.MongoClient("mongodb+srv://adna9:mongodbpassword@cluster0.s6xua.mongodb.net/test")

DATA_FILE_PATH= "https://raw.githubusercontent.com/avnyadav/sensor-fault-detection/main/aps_failure_training_set1.csv"
DATABASE_NAME= "aps"
COLLECTION_NAME= "sensor"

if __name__ == "__main__":
    df= pd.read_csv("https://raw.githubusercontent.com/avnyadav/sensor-fault-detection/main/aps_failure_training_set1.csv")
    print(f"Raows and Columns:{df.shape}")

    #Convert dataframe to json so that we can dump these record in mpngo db
    df.reset_index(drop=True, inplace= True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    #insert converted json to mongodb
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

