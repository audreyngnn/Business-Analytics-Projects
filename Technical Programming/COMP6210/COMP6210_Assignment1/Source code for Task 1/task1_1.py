# -*- coding: utf-8 -*-
"""
@author: Khuat Son Tra Nguyen
"""

from pymongo import MongoClient
import re

#DATA EXTRACTION
# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['A01-01']
collection = db['Olympic_Athletes']

# Query and extract data
query = {
    "$and": [
        {"edition": {"$regex": r"^(198|199|200|201|2020).*Summer Olympics$"}},
        {"medal": {"$in": ["Gold", "Silver", "Bronze"]}},
        {"athlete_id": {"$exists": True}},
        {"country_noc": {"$exists": True}},
        {"edition": {"$exists": True}},
        {"event": {"$exists": True}},
        {"medal": {"$exists": True}}
    ]
}


results = collection.find(query)

# Write to athletes.txt
with open('athletes.txt', 'w', encoding = "utf-8") as f:
    for athlete in results:
        year = re.search(r'\d{4}', athlete['edition']).group()
        line = f"{athlete['athlete_id']}\t{athlete['country_noc']}\t{year}\t{athlete['event']}\t{athlete['medal']}\n"
        f.write(line)

print("Data extraction complete. Check athletes.txt")