import pandas as pd
import tabula

data = tabula.read_pdf("./data_folder/sample.pdf", lattice=True, pages = 'all')

dfs = []
# for df in dfs:
#     print(df[0])
for df in data:
    # print(df.iat[1,0])
    # print(df.iloc[1,0:3])
    dfs.append(df)

print(dfs[0])
print(dfs[0].iloc[1,0:3])