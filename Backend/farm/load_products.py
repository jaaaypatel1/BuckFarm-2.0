import pandas as pd
import json

with open("products.json") as f:
    data = json.load(f)


df = pd.DataFrame(data)
df.head()
df.columns

### SQL Connection

import sqlite3

conn = sqlite3.connect("db.sqlite3")
c = conn.cursor()

