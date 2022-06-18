import pandas as pd
import csv
df = pd.read_csv("final.csv")
del df["hyperlink"]
df = df.rename({
'planet_type': 'gas_giant_or_rocky'
}, axis='columns')
df.to_csv('c130Main.csv')