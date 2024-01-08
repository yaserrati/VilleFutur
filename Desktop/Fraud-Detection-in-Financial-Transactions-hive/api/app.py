from flask import Flask,jsonify
import pandas as pd
import json



app = Flask(__name__)


# "get all transactions. (transactions endpoint)"

@app.route("/api/transactions/",methods=['GET'])
def get_all_transactions():
    df = pd.read_json("../data/transactions.json",orient='records')
    try:
        # Convert DataFrame to dictionary and get the item by ID
        item = df.to_json(orient='records')
        if item:
            return json.loads(item)
            # return jsonify(item)
        else:
            return jsonify({'error': 'transactions not found'}), 404

    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

# "get all customers. (customers endpoint)"

@app.route("/api/customers/",methods=['GET'])
def get_all_customers():
    df = pd.read_json("../data/customers.json",orient='records')
    try:
        # Convert DataFrame to dictionary and get the item by ID
        item = df.to_json(orient='records')
        if item:
            return json.loads(item)
        else:
            return jsonify({'error': 'customers not found'}), 404

    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    


# "get all external_data. (external_data endpoint)"

@app.route("/api/external_data/",methods=['GET'])
def get_all_external_data():
    try:
        with open('../data/external_data.json','r') as file:
            if file:
                return json.load(file)
            else:
                return jsonify({'error': 'external data not found'}), 404

    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500