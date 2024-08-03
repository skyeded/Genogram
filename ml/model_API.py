from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from model import model
import os
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:129303@localhost/NewDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

def create_dynamic_model(cleaned_data):
    # Start with a base class
    base_class = db.Model

    # Dynamically add columns based on cleaned_data keys
    attributes = {'id': db.Column(db.Integer, primary_key=True)}
    attributes.update({key: db.Column(db.String(255)) for key in cleaned_data.keys()})

    # Create a new class with the added columns using type
    dynamic_model = type('DynamicTable', (base_class,), attributes)

    return dynamic_model

def save_to_database(cleaned_data_list):
    # Create a dynamic model based on the keys of the first dictionary in the list
    dynamic_model = create_dynamic_model(cleaned_data_list[0])

    # Create entries with the dynamic model for each dictionary in the list
    new_entries = [dynamic_model(**data) for data in cleaned_data_list]

    # Save the dynamic model and entries to the database
    db.create_all()
    db.session.add_all(new_entries)
    db.session.commit()

@app.route('/ML_data', methods=['POST'])
def ML_data():
    try:
        # Assuming the uploaded file is named 'data' in the request
        uploaded_file = request.files['data']

        # Read the content of the file
        file_content = uploaded_file.read()

        # Convert bytes to a string
        file_content_str = file_content.decode('utf-8')

        # Load the JSON content
        df_json = pd.io.json.loads(file_content_str)

        # Create a DataFrame from the JSON content
        df = pd.DataFrame(df_json)

        # Process the file or perform data cleaning using your model
        ML_data = model(df)

        get_data = ML_data.get_dataframe()

        # Convert the DataFrame to a list of dictionaries
        cleaned_data_list = get_data.to_dict(orient='records')

        # Save all rows to the database
        save_to_database(cleaned_data_list)

        # Example: Return a cleaned response
        response = {'result': 'Data cleaned and saved successfully'}
        return jsonify(response)

    except Exception as e:
        # Handle errors
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=3005)
