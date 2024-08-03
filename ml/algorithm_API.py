from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from algorithm import algorithm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'
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

def save_to_database(cleaned_data):
    dynamic_model = create_dynamic_model(cleaned_data)

    # Create a new entry with the dynamic model
    new_entry = dynamic_model(**cleaned_data)

    # Save the dynamic model and entry to the database
    db.create_all()
    db.session.add(new_entry)
    db.session.commit()

@app.route('/algorithm_data', methods=['POST'])
def algorithm_data():
    try:
        # Assuming the uploaded file is named 'data' in the request
        uploaded_file = request.files['data']
        
        # Process the file or perform data cleaning using your model
        file_path = 'upload/'+uploaded_file.filename
        algorithm_data = algorithm(file_path)

        # Save cleaned data to the PostgreSQL database
        save_to_database(algorithm_data)

        # Example: Return a cleaned response
        response = {'result': 'Data cleaned and saved successfully'}
        return jsonify(response)

    except Exception as e:
        # Handle errors
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)