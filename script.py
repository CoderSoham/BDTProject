import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, RobustScaler
from sklearn.metrics import classification_report

# Load the structured dataset
file_path = 'creditcard.csv' 

df = pd.read_csv(file_path)

# Check for class imbalance
print('No Frauds', round(df['Class'].value_counts()[0] / len(df) * 100, 2), '% of the dataset')
print('Frauds', round(df['Class'].value_counts()[1] / len(df) * 100, 2), '% of the dataset')

# Scale the 'Amount' and 'Time' columns
rob_scaler = RobustScaler()
df['scaled_amount'] = rob_scaler.fit_transform(df['Amount'].values.reshape(-1, 1))
df['scaled_time'] = rob_scaler.fit_transform(df['Time'].values.reshape(-1, 1))
df.drop(['Time', 'Amount'], axis=1, inplace=True)

# Shuffle and balance the dataset
df = df.sample(frac=1)
fraud_df = df.loc[df['Class'] == 1]
non_fraud_df = df.loc[df['Class'] == 0][:492]  # Balance with fraud samples
balanced_df = pd.concat([fraud_df, non_fraud_df]).sample(frac=1, random_state=42)

# Prepare the data for model training
X = balanced_df.drop('Class', axis=1)
y = balanced_df['Class']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestClassifier
rf_classifier = RandomForestClassifier(random_state=42)
rf_classifier.fit(X_train, y_train)

# Make predictions
y_pred = rf_classifier.predict(X_test)

# Evaluate the model
print(classification_report(y_test, y_pred))

# Add unstructured comments based on predictions
def add_customer_feedback(row):
    fraud_comments = [
        "I didn't authorize this payment!",
        "Transaction looks suspicious, please check.",
        "Please block my card, this is fraud!",
        "I am not sure if this is my purchase.",
        "This charge is unknown to me."
    ]
    
    non_fraud_comments = [
        "No issues with this transaction.",
        "Transaction verified.",
        "This was a legitimate purchase.",
        "Authorized transaction.",
        "Known transaction by family."
    ]
    
    if row['Class'] == 1:  # Fraud
        return random.choice(fraud_comments)
    else:  # Non-fraud
        return random.choice(non_fraud_comments)

# Apply the function to add unstructured comments
balanced_df['CustomerFeedback'] = balanced_df.apply(add_customer_feedback, axis=1)

# Save the modified dataset with unstructured data
output_file_path = 'creditcard_with_feedback.csv'
balanced_df.to_csv(output_file_path, index=False)

print(f"Modified dataset with customer feedback saved at {output_file_path}")
