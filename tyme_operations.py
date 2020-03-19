import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("ArtJan2018resumido.csv")
df = pd.DataFrame(data)

df['Date'] = df['pubDate'].str.extract('(../../..)', expand=True)
df["Date"] = pd.to_datetime(df['Date'])
plt.plot(df["articleWordCount"], df["source"], "-")
_ = plt.xticks(rotation=45)
plt.show()
