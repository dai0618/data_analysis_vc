import os
import pandas as pd
import tabula
import glob

def modify_table(data):
    # 変に同じセル内で改行を行わないように置換している。
    df = data[0].replace("\r", "", regex=True)
    column = len(df.columns)

    # 列の名前を題〜期から変更
    for i in range(0,column,1):
        df.rename(columns={df.columns[i]:str(i)}, inplace=True)

    return df

def process_table():
    new_df = pd.DataFrame(index=[], columns=[])
    for pdf_data in glob.glob("./data_folder/*.pdf"):
        company_name_df = pd.DataFrame(os.path.splitext(os.path.basename(pdf_data)[0]))
        table_data = tabula.read_pdf(pdf_data, lattice=True, pages = 'all')
        df = modify_table(table_data)
        new_df = pd.concat([df, new_df], axis=0)
        
    return new_df

if __name__ == "__main__":
    new_df = process_table()
    # csvに書き出し
    new_df.to_csv('sampla_data.csv')