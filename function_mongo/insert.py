from configparser import ConfigParser
from pymongo import MongoClient
import pandas as pd

import json

config = ConfigParser()
config.read('config.ini')

client = MongoClient(config['MONGO']['URI'])
database = client[config['MONGO']['DATABASE']]
collection = database[config['MONGO']['COLLECTION']]

nome_arquivo = ''

csv_data = pd.read_csv(f"{nome_arquivo}.csv", sep = ",")
json_data = csv_data.to_json(orient = "records")
parsed = json.loads(json_data)

insert = collection.insert_many(parsed)
insert.inserted_ids


