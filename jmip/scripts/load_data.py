import sys
import os
import pandas as pd
from models import Job
from database import SessionLocal

#load the csv file, convert each rows in to Job object and insert into the database

df = pd.read_csv("data/Cleaned_DS_jobs.csv")
#convert dataFrame in to a dict
data = df.to_dict(orient="records")
#create a session
db = SessionLocal()

#bulk_insert is faster than iterrows() / multiple rows vs one row at a time
db.bulk_insert_mappings(Job, data)


# interrows() from panda turns table into something I can loop through.
# for index, row in df.iterrows():
#     job = Job(
#         job_title = row["title"],
#         description = row["description"],
#         salary = row["salary"],
#         company = row["company"],
#         industry = row["industry"],
#         location = row["location"],
#         rating = row["rating"]
#     )   

db.commit()
db.close()