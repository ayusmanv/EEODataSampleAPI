import pandas as pd
import openpyxl

def data_read():
    toc = pd.read_excel('data/FY 2020 Annual Report Workforce Tables.xlsx', sheet_name='Table of Contents', skiprows=4, nrows= 17)
    eeo1_2020_merged_dataset = pd.DataFrame(columns = ['Table','Table Name','Agency Name','Agency Code', 'Demographic Slice',	'Data'])

    for index, row in toc.iterrows():
        df = pd.read_excel('data/FY 2020 Annual Report Workforce Tables.xlsx', sheet_name=row["Table"], skiprows=1)
        df.columns = df.columns.str.replace('\n', '').str.replace('\r', '').str.strip()
        df = df.dropna(subset=['Agency Name'])
        #print(df.head())
        df_melt = pd.melt(df, id_vars=['Agency Name', 'Agency Code'], var_name='Demographic Slice', value_name='Data')
        df_melt['Table Name'] = row['Table Name']
        df_melt['Table'] = row['Table']
        #filename = row["Table"]+".csv"
        #df_melt.to_csv(f'data/{filename}', index=False)
        eeo1_2020_merged_dataset = pd.concat([eeo1_2020_merged_dataset, df_melt])

    #eeo1_2020_merged_dataset.to_csv('data/eeo1_2020_merged_dataset.csv', index=False)
    return eeo1_2020_merged_dataset
