# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from sklearn.metrics import mean_absolute_error, r2_score
from prettytable import PrettyTable
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import hashlib
import xgboost as xgb
# %matplotlib inline

# %%
class model():
    def __init__(self, df):
        self.df = df

        df_later = df
        # %%
        print(df.head(10))
        # %%
        # Convert DataFrame to PrettyTable
        table = PrettyTable()
        table.field_names = df.columns

        for row in df.itertuples(index=False):
            table.add_row(row)
            
        # print(table)

        # %%
        columns_to_drop = ['Column_filled', 'isEdit']
        # df_use = df.drop(columns=columns_to_drop)

        # %%
        # table = PrettyTable()
        # table.field_names = df_use.columns

        # for row in df_use.itertuples(index=False):
        #     table.add_row(row)
            
        # print(table)

        # %%
        # fa_nid_nan = df[df['fa_nid'].isna()]
        # print(len(fa_nid_nan))

        # %%
        # non_nan_rows_count = df_use.notna().all(axis=1).sum()

        # Display the count
        # print("Number of rows with no missing values:", non_nan_rows_count)

        # %%
        # df_no_missing_values = df_use[df_use.notna().all(axis=1)]

        # %%
        # table = PrettyTable()
        # table.field_names = df_no_missing_values.columns

        # for row in df_no_missing_values.itertuples(index=False):
        #     table.add_row(row)
            
        # print(table)

        # %%
        # column_to_move = 'Age'
        # df_no_missing_values = df_no_missing_values[[col for col in df_no_missing_values.columns if col != column_to_move] + [column_to_move]]

        # %%
        # X = df_no_missing_values.iloc[:, :-1].values
        # y = df_no_missing_values.iloc[:, -1].values

        # %%
        # from sklearn.compose import ColumnTransformer
        # from sklearn.preprocessing import OneHotEncoder
        # ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [2])], remainder='passthrough')
        # X = np.array(ct.fit_transform(X))

        # %%
        # print(X[0])

        # %%
        # print(y[0:10])

        # %%
        # Define the columns to be hashed
        columns_to_hash = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

        desired_digits = 8

        # Define a hash function
        hash_function = np.vectorize(self.sha256_hash)

        # Apply the hash function to the specified columns along the axis 1 (row-wise)
        # hashed_columns = np.apply_along_axis(hash_function, axis=1, arr=X[:, columns_to_hash])

        # Convert the hashed values to int64
        # hashed_columns = hashed_columns % (10 ** desired_digits)

        # Replace the original columns with the hashed values
        # X[:, columns_to_hash] = hashed_columns


        # %%
        # print(X[0])

        # %%
        # le = LabelEncoder()
        # X[:,2] = le.fit_transform(X[:, 2])

        # %%
        # X[:,3] = le.fit_transform(X[:, 3])

        # %%
        # print(X[10])

        # %%

        # %%
        # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)

        # %%
        # print(X_train)

        # %%
        # print(y_train)

        # %%
        # sc = StandardScaler()
        # X_train[:, 8:] = sc.fit_transform(X_train[:, 8:])
        # X_test[:, 8:] = sc.transform(X_test[:, 8:])

        # %%
        # model = XGBRegressor()

        # model.fit(X_train, y_train)
        # Assuming you have already trained the model (model) and split the data (X_test, y_test)
        # mse, mae, r_squared = self.evaluate_model(model, X_test, y_test)
        # Create a new model instance
        pretrained_model = xgb.XGBRegressor()
        import os
        os.chdir('C:/Users/User/Desktop/CS400/Gemogram_data1l')
        absolute_path = os.path.abspath('new_model.pth')

        # Load the pre-trained model
        pretrained_model.load_model(absolute_path)

        print(df.columns)
        if 'birthyear' in df.columns:
        # Access the 'birthyear' column
            df['birthyear']
        else:
            print("'birthyear' column does not exist.")
        # %%
        df_without_by = df[df['birthyear'].isna()]

        # %%
        # print(df_without_by)

        # %%
        columns_to_drop = ['birthyear', 'Column_filled', 'isEdit']
        d_by = df_without_by.drop(columns=columns_to_drop)
        d_by = d_by.iloc[:,:].values

        df = d_by

        columns_to_drop = ['Column_filled', 'isEdit']
        self.df = self.df.drop(columns=columns_to_drop, errors='ignore')

        columns_to_replace = ['fa_name', 'fa_surname', 'mo_name', 'mo_surname']
        # Replace empty values with 'undefined'
        self.df[columns_to_replace] = self.df[columns_to_replace].replace('', 'undefined')
        # %%
        # print(d_by)

        # %%
        # print(d_by[0])

        # %%
        # Apply the hash function only if there are elements in the specified columns
        # Check if the NumPy array is not empty
        # if d_by.size > 0 and d_by[:, columns_to_hash].size > 0:
        #     hashed_columns = np.apply_along_axis(hash_function, axis=1, arr=d_by[:, columns_to_hash])
        #     hashed_columns = hashed_columns % (10 ** desired_digits)
        #     d_by[:, columns_to_hash] = hashed_columns
        # else:
        #     print("No elements in the specified columns to hash.")
        # # %%
        # le = LabelEncoder()
        # d_by[:,2] = le.fit_transform(d_by[:, 2])
        # d_by[:,3] = le.fit_transform(d_by[:, 3])

        # %%
        # print(d_by[0])
        class MyModel:
            def __init__(self, model_path='path_to_my_model.json'):
                # Initialize your model (XGBRegressor in this case)
                self.model = xgb.XGBRegressor()
                # Load the pretrained model
                self.model.load_model(model_path)

            def predict(self, X):
                # Use the pretrained model to make predictions
                return self.model.predict(X)    
        # %%
        model_path = 'C:/Users/User/Desktop/CS400/Gemogram_data1l/new_model.pth'
        my_model = MyModel(model_path)  
        by_prediction = my_model.predict(d_by)

        # %%
        # print(by_prediction)

        # %%
        # print(len(by_prediction))
        # print(len(df_without_by['birthyear']))
    
        # %%
        # print(by_prediction)
        # print(df_without_by['birthyear'])
        # df_without_by['birthyear'] = np.array(by_prediction)
        # df_without_by['birthyear'] = df_without_by['birthyear'].astype(int)
        # print(df_without_by.head(10))
        # %%
        # print(df_without_by)

        # %%
        for i, row_i in df_without_by.iterrows():
            for j, row_j in df.iterrows():
                if row_j['nid'] == row_i['nid']:
                    df.loc[j, 'birthyear'] = row_i['birthyear']

        # %%
        # print(df)

        # %
    def get_dataframe(self):
        return self.df        
    
    def sha256_hash(self, value):
            return int(hashlib.sha256(str(value).encode('utf-8')).hexdigest(), 16)

    def evaluate_model(self, my_model, X_test, y_test):
        # Make predictions on the testing data
        y_pred = my_model.predict(X_test)

        # Calculate Mean Squared Error
        mse = mean_squared_error(y_test, y_pred)
        print(f"Mean Squared Error: {mse}")

        # Calculate Mean Absolute Error
        mae = mean_absolute_error(y_test, y_pred)
        print(f"Mean Absolute Error: {mae}")

        # Calculate R-squared
        r_squared = r2_score(y_test, y_pred)
        print(f"R-squared: {r_squared}")

        return mse, mae, r_squared
    


    
        