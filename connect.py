import pandas as pd
from pymongo import MongoClient

file_path = 'creditcard_with_feedback.csv'  
df = pd.read_csv(file_path)

data_dict = df.to_dict(orient='records')

client = MongoClient('mongodb://localhost:27017/')  
db = client['fraud_detection']  
collection = db['transactions']  

collection.insert_many(data_dict)

print("Data inserted successfully into MongoDB")

print(collection.find_one())

# ------------------- CRUD Operations -------------------

# 1. Create: Insert a new transaction manually
new_transaction = {
    "Time": 172792.0,
    "V1": -1.359807,
    "V2": -0.072781,
    "V3": 2.536346,
    "Amount": 149.62,
    "Class": 0,  # Legitimate transaction
    "Feedback": "Valid Transaction"
}
collection.insert_one(new_transaction)
print("New transaction inserted.")

# 2. Read: Fetch and print the first transaction document
print("First transaction in the collection:")
print(collection.find_one())  # Fetch the first document

# 2.1 Read: Fetch all fraudulent transactions (Class = 1)
print("\nAll fraudulent transactions (Class = 1):")
fraud_transactions = collection.find({"Class": 1})
for transaction in fraud_transactions:
    print(transaction)

# 2.2 Read: Count the total number of transactions in the collection
transaction_count = collection.count_documents({})
print(f"\nTotal number of transactions: {transaction_count}")

# 3. Update: Update a specific transaction (manually chosen or fetched by _id)
transaction_id = collection.find_one({"Amount": 149.62})["_id"]  # Get _id for update
collection.update_one(
    {"_id": transaction_id},
    {"$set": {"Amount": 200.0, "Feedback": "Updated Transaction"}}
)
print(f"\nTransaction with _id: {transaction_id} updated successfully.")

# 3.1 Update: Update multiple transactions (e.g., all transactions where Amount > 1000)
collection.update_many(
    {"Amount": {"$gt": 1000}},
    {"$set": {"high_value_flag": True}}
)
print("All transactions with Amount > 1000 have been flagged as high value.")

# 4. Delete: Delete one transaction (using the _id fetched earlier)
collection.delete_one({"_id": transaction_id})
print(f"\nTransaction with _id: {transaction_id} deleted successfully.")

# 4.1 Delete: Delete all transactions where Class = 1 (fraudulent transactions)
delete_result = collection.delete_many({"Class": 1})
print(f"Deleted {delete_result.deleted_count} fraudulent transactions.")

# ------------------- Additional Operations -------------------

# 5. Aggregation: Find the average 'Amount' for legitimate transactions (Class = 0)
pipeline = [
    {"$match": {"Class": 0}},  # Match legitimate transactions
    {"$group": {"_id": None, "avg_amount": {"$avg": "$Amount"}}}
]
result = collection.aggregate(pipeline)
for item in result:
    print(f"\nAverage Amount for legitimate transactions: {item['avg_amount']}")

# 6. Sorting: Fetch all transactions and sort by 'Amount' in descending order
print("\nTransactions sorted by Amount (descending):")
sorted_transactions = collection.find().sort("Amount", -1)
for transaction in sorted_transactions:
    print(transaction)

# 7. Count: Count how many legitimate (Class = 0) vs fraudulent (Class = 1) transactions are there
legit_count = collection.count_documents({"Class": 0})
fraud_count = collection.count_documents({"Class": 1})
print(f"\nLegitimate transactions: {legit_count}, Fraudulent transactions: {fraud_count}")
