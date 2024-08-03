# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from prettytable import PrettyTable

class algorithm():
    def __init__(self, file_path):
    # %%
        file_path = file_path

        # %%
        df = pd.read_json(file_path)
        column_name = ["is_hh_head", "is_fam_head", "title", "sex", "surname", "fa_surname", "mo_surname", "birthyear"]
        print(df.head(10))

        # %%
        # for i in range(len(df)):
        #     if pd.isna(df["fam_id"].iloc[i]):
        #         print(df.iloc[i])
        #         print("----------------------------")


        # %%
        df['NewColumn'] = [[] for _ in range(len(df))]
        df.rename(columns={'NewColumn': 'Column_filled'}, inplace=True)
        # print(df)

        # %%
        # print("Column Names:", column_name)

        # %%
        # df.describe()

        # %%
        missing_attributes = df.isnull().sum()
        # print(missing_attributes)

        # %% [markdown]
        # Fill Gender

        # %%
        sex_row_changed = []
        for i in range(len(df)):
            if pd.isna(df["sex"].iloc[i]):
                if df["title"].iloc[i] in ["นาย", "เด็กชาย"]:
                    df.at[i, "sex"] = "ชาย"
                    sex_row_changed.append(i)
                    df["Column_filled"].iloc[i].append("sex")
                else:
                    df.at[i, "sex"] = "หญิง"
                    sex_row_changed.append(i)
                    df["Column_filled"].iloc[i].append("sex")

        # %%
        # missing_attributes = df.isnull().sum()
        # print(missing_attributes)

        # %%
        # missing_percentage = (df.isnull().mean()*100).round(2)
        # print(missing_percentage)

        # %% [markdown]
        # Fill fa_id and mo_id

        # %%
        # for i in range(len(df)):
        #     if pd.isna(df["fa_name"].iloc[i]):
        #         print(df.iloc[i])
        #         print("-----------------------------")


        # %%
        # print(len(df))

        # %%
        # for i in range(len(df)):
        #     for j in range(len(df)):
        #         if df["nid"].iloc[i] == df["mo_nid"].iloc[j]:
        #             print("|", df["nid"].iloc[i],"|", df["mo_nid"].iloc[j])
        df = self.fill_fa_id(df)
        df = self.fill_mo_id(df)
        df = self.add_mo_row(df)
        df = self.add_fa_row(df)
        df[['is_hh_head', 'is_fam_head']] = df[['is_hh_head', 'is_fam_head']].fillna(0)
        df['isEdit'] = np.nan
        return df

    # %%
    def fill_fa_id(self, df):
        # Create a new column to store the updated values
        for i, row_i in df.iterrows():
            if pd.isna(row_i['fa_nid']):
                for j, row_j in df.iterrows():
                    if row_i['fa_name'] == row_j['name'] and row_i['hh_id'] == row_j['hh_id']:
                        if pd.notna(row_j['nid']):
                            df.at[i, 'fa_nid'] = row_j['nid']
                            df["Column_filled"].iloc[i].append("fa_id")
                            # print(df.at[i, 'fa_nid'])
        return(df)

    # %%

    # %%
    # print(df)

    # %%
    def fill_mo_id(self, df):
        # Create a new column to store the updated values
        for i, row_i in df.iterrows():
            if pd.isna(row_i['mo_nid']):
                for j, row_j in df.iterrows():
                    if row_i['mo_name'] == row_j['name'] and row_i['hh_id'] == row_j['hh_id']:
                        if pd.notna(row_j['nid']):
                            df.at[i, 'mo_nid'] = row_j['nid']
                            df["Column_filled"].iloc[i].append("mo_id")
                            # print(df.at[i, 'mo_nid'])
    

        return df

    # %%
    # df = fill_mo_id(df)

    # %%
    # missing_attributes = df.isnull().sum()
    # print(missing_attributes)

    # %%
    # print(df[['mo_nid']].head(10))

    # %% [markdown]
    # Add row for mo_name that not in name

    # %%
    def add_mo_row(self, df):
        count = 0
        for i, row_i in df.iterrows():
                existed = False
                if pd.notna(row_i['mo_name']):
                    for j, row_j in df.iterrows():
                        if row_i['mo_name'] == row_j['name'] and row_i['hh_id'] == row_j['hh_id']:
                            existed = True
                    if existed == False:
                        # print("pass")
                        if pd.notna(row_i['mo_nid']):
                            df = pd.concat([df, pd.DataFrame([{'title':'นาง', 'sex':'หญิง', 'hh_id':row_i['hh_id'], 'fam_id':row_i['fam_id'], 'name':row_i['mo_name'], 'surname':row_i['mo_surname'], 'nid':row_i['mo_nid'], 'Column_filled':[]}])], ignore_index=True)
                        else:
                            df.at[i, 'mo_nid'] = "gen_mo_nid#"+str(count)
                            df = pd.concat([df, pd.DataFrame([{'title':'นาง', 'sex':'หญิง', 'hh_id':row_i['hh_id'], 'fam_id':row_i['fam_id'], 'name':row_i['mo_name'], 'surname':row_i['mo_surname'], 'nid':"gen_mo_nid#"+str(count), 'Column_filled':[]}])], ignore_index=True)
                            count+=1
                            # print(count)             
        return df

    # %%
    # df = add_mo_row(df)

    # %%
    def add_fa_row(self, df):
        count = 0
        for i, row_i in df.iterrows():
                existed = False
                if pd.notna(row_i['fa_name']):
                    for j, row_j in df.iterrows():
                        if row_i['fa_name'] == row_j['name'] and row_i['hh_id'] == row_j['hh_id']:
                            existed = True
                    if existed == False:
                        if pd.notna(row_i['fa_nid']):
                            df = pd.concat([df, pd.DataFrame([{'title':'นาย', 'sex':'ชาย', 'hh_id':row_i['hh_id'], 'fam_id':row_i['fam_id'], 'name':row_i['fa_name'], 'surname':row_i['fa_surname'], 'nid':row_i['fa_nid'], 'Column_filled':[]}])], ignore_index=True)
                            # print("pass")
                        else:
                            df.at[i, 'fa_nid'] = "gen_fa_nid#"+str(count)
                            df = pd.concat([df, pd.DataFrame([{'title':'นาย', 'sex':'ชาย', 'hh_id':row_i['hh_id'], 'fam_id':row_i['fam_id'], 'name':row_i['fa_name'], 'surname':row_i['fa_surname'], 'nid':"gen_fa_nid#"+str(count), 'Column_filled':[]}])], ignore_index=True)
                            count+=1
                            # print(count)                 
        return df

    # %%
    # df = add_fa_row(df)

    # %%
    # df[['is_hh_head', 'is_fam_head']] = df[['is_hh_head', 'is_fam_head']].fillna(0)

    # %%
    # print(df)

    # %%
    # missing_attributes = df.isnull().sum()
    # print(missing_attributes)

    # %%
    # df['isEdit'] = np.nan

    # %%

    # Convert DataFrame to PrettyTable
    # table = PrettyTable()
    # table.field_names = df.columns

    # for row in df.itertuples(index=False):
    #     table.add_row(row)
        
    # print(table)

    # %%
    # df.to_json('cleanned_data.json', orient='records', lines=True)

    # %%
    # print(df['fa_nid'].head(10)) 

    # %%
    # df_test = df[df['fam_id'] == 'fam_id#0000']

    # %%
    # print(df_test)

    # %%
    # df_no_r = df[df[['nid']].isna().all(axis=1)]
    # print(df_no_r)


