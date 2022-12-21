import pandas as pd

df = pd.read_csv("pokemon_data.csv")

print(df.head(3)) #top 3 rows ("tail" for bottom)

#for txt files separated by tabs
#df_txt = pd.read_csv("pokemon_data.txt", delimiter="\t")

#read headers
df.columns

print(df[['Name', "HP", "Type 1"]]) #prints name column

#prints first 4 rows of the data
print(df.head(4))

#prints first row specifically can also use [1:5]
print(df.iloc[1])

#how to iterate
for index, row in df.iterrows():
   print(index, row['Name'])

#finding specific data that is not integer based but more based off the info
print(df.loc[df['Type 1'] == "Fire"])

#get specific data form specific column
print(df.iloc[2, 1])

#sorting values What to sort by\/     whether ascending or not
df.sort_values(["Type 1", "HP"], ascending=[1, 0])

#CHANGING DATA
df["Total"] = df["HP"] |+df["Attack"] +df["Defense"] 
print(df.head(5))

#dripping column
df.drop(columns = ["Total"])
            #all rows      #columns
df["Total"] = df.iloc[:, 4:10].sum(axis=1)
#another way to add a new column

#to restructure or sort the data by columns 
cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
#puts total in the middle (purely visual)

