from pyhive import hive 
import requests as req

# Get data from the API
transactions = req.get("http://127.0.0.1:5000/api/customers/")


if transactions.status_code == 200:
    result = transactions.json()
    counter = 0
    while True:
        data = transactions.json()[counter]
        # Establish a connection
        connection = hive.connect(host='localhost', database='testdb')
        cursor = connection.cursor()
        
        # Create the table
        table_creation_query = """
        CREATE TABLE IF NOT EXISTS testdb.customers (
            account_history STRING,
            avg_transaction_value DOUBLE,
            customer_id STRING,
            age INT,
            location STRING
        )
        """
        cursor.execute(table_creation_query)

        account_history_string = ",".join(data["account_history"])

        # Insert data into the table
        insert_query = '''
        INSERT INTO testdb.customers
        VALUES ('{a}',
        '{b}',
        '{c}',
        {d},
        '{e}')
        '''.format(
            a = account_history_string,
            b = data['behavioral_patterns']['avg_transaction_value'],
            c = data['customer_id'],
            d = data['demographics']['age'],
            e = data['demographics']['location']
        )
        # print(insert_query)
        cursor.execute(insert_query)
        # Commit the transaction
        connection.commit()

        # Fetch and print the inserted data
        cursor.execute('SELECT * FROM testdb.customers')
        print(cursor.fetchall())

        # Close the cursor and connection
        cursor.close()
        connection.close()
        counter += 1
        print(counter)
        if counter == len(result) :
            break
else:
    print("Failed to fetch data from the API.")
