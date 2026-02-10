import pandas as pd
import openpyxl

df = pd.read_excel("deployment.xlsx")

failed = df[df["status"] == "Failed"]


print(df.columns)
print(df)

