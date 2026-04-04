import os
import pandas as pd

#extract key words from raw text (Job description) for machine learning model
#which signal in the data is important 

#make sure the script can find the file from other folders (avoid import error)
#__file__ = full path of the current file (feature_engineering.py) - use os.path.abspath to get the exact location of the file
#first os.path.dirname() removes the file name → goes to ml/
#second os.path.dirname() goes up one level → jmip/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "data", "Cleaned_DS_jobs.csv")
df = pd.read_csv(file_path)

#list of skills to look for in the job description
skills = ["python", "sql", "aws", "machine learning", "docker", "c++", "java", "javascript", "react", "node.js", "ruby", "php", "tensorflow", "pytorch", "numpy", "pandas", "scikit-learn", "git"]

#extract the skills fromn the job description
def extract_skills(text):
    text = str(text).lower()
    return [skill for skill in skills if skill in text]

print(df.columns) 


df["skills"] = df["Job Description"].apply(extract_skills)

print(df[["Job Description", "skills"]].head())


#create binary columns for each skill (1 if the skill is present in the job description, 0 otherwise)
for skill in skills:
    df[skill] = df["Job Description"].str.lower().str.contains(skill).astype(int)

print(df[["Job Description"] + skills].head(50))