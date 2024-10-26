# Fraud Detection with MongoDB, PyMongo, and Spark

This project demonstrates how to detect fraudulent transactions using a dataset of credit card transactions. It involves using MongoDB for CRUD operations, PyMongo to connect and interact with MongoDB, and Apache Spark for advanced data processing and analysis.

## Project Overview

The main purpose of this project is to upload and manage a credit card transaction dataset in MongoDB, perform CRUD operations using PyMongo, and leverage Apache Spark for data processing. This dataset includes anonymized transaction features (`V1` to `V28`), as well as feedback and classifications for transaction fraud detection.

## Features

- **MongoDB Integration**: The `pymongo_connect.py` script enables CRUD operations on MongoDB.
- **Data Processing with Spark**: The `sparkconnect.py` script connects to Apache Spark for scalable data analysis.
- **Credit Card Fraud Detection Dataset**: Sample data to experiment with fraud detection methods.

---

## Project Setup

### Prerequisites

1. **Python 3.8+**: Make sure Python is installed.
2. **MongoDB**: Install and run MongoDB locally.
3. **Apache Spark**: Install Apache Spark on your system.
4. **PyMongo & pyspark Libraries**: Install these libraries using pip.

### Installation Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/CoderSoham/BDTProject.git
   cd BDTProject

2. **Install Dependencies**

```bash
pip install pymongo pyspark pandas
```
3. **Set Up MongoDB Database**

Ensure MongoDB is running locally on the default port 27017.
Import the CSV dataset into MongoDB by running the pymongo_connect.py script.
Data Import with PyMongo

Run the pymongo_connect.py script to insert data into MongoDB:
```bash
python pymongo_connect.py
```
The script will insert the data into a collection named transactions in a database named fraud_detection.

4. **Spark Setup**

Start the sparkconnect.py script to connect to Spark and perform data processing:
```bash
python sparkconnect.py
```
This script connects to Spark, processes the transactions, and outputs key insights.

5. **MongoDB CRUD Operations:**

After running pymongo_connect.py, MongoDB should have a transactions collection populated with credit card transaction data.
A sample document will be printed to the console after successful insertion.
Spark Data Processing:

Running sparkconnect.py will connect to Spark, read the dataset, and output the following:
Data summaries (e.g., fraud vs. non-fraud transactions)
Basic analytics on transaction features
Common Debugging Tips
MongoDB Connection Errors
Error: pymongo.errors.ServerSelectionTimeoutError
Solution: Ensure MongoDB is running on your machine. Start it with mongod if needed, and verify that it’s listening on localhost:27017.
Large File Not Uploading to GitHub
Error: File creditcard.csv is 143.84 MB; this exceeds GitHub's file size limit of 100.00 MB
Solution: This project uses Git LFS for managing large files. Make sure Git LFS is installed (git lfs install) and configured to track creditcard.csv.
Spark Connection Issues
Error: pyspark.sql.utils.AnalysisException
Solution: Make sure Spark is properly installed and configured. Check your environment variables (SPARK_HOME and PATH) to ensure Spark is accessible.
License
This project is open-source and available for modification. Feel free to contribute or adjust the code to suit your specific use case.