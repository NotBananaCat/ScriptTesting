import os
import csv
import firebase_admin
from firebase_admin import credentials, firestore

# Set up Firebase Admin SDK
cred = credentials.Certificate("/Users/danielwu/Desktop/Rolodex Scripts/juniorkids-x-rolodex-firebase-adminsdk-jadrm-87274b3e78.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore DB
db = firestore.client()

def add_or_update_user(user_id, user_info):
    """
    Adds a user to the Firestore database or updates the user if the user_id already exists.
    
    Parameters:
    user_id (str): The unique identifier for the user.
    user_info (dict): A dictionary containing user information.
    """
    try:
        # Check if the user already exists
        user_ref = db.collection('users').document(user_id)
        if user_ref.get().exists:
            # Update the existing user
            user_ref.update(user_info)
            print(f'User {user_id} updated successfully.')
        else:
            # Add a new user
            user_ref.set(user_info)
            print(f'User {user_id} added successfully.')
    except Exception as e:
        print(f'An error occurred: {e}')

def create_test_profiles_from_csv(file_path):
    """
    Creates test profiles from the data in the CSV file.
    
    Parameters:
    file_path (str): The path to the CSV file containing user data.
    """
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user_id = row['user_id']
                user_info = {
                    "name": row['fullName'],
                    "email": row['email'],
                    "age": int(row['age']),
                    "uid": user_id,
                    "displayName": row['displayName'],
                    "fullName": row['fullName'],
                    "firstName": row['firstName'],
                    "lastName": row['lastName'],
                    "contactList": [],  # Assuming contactList is empty in the CSV
                    "instagramUsername": row['instagramUsername'],
                    "tiktokUsername": row['tiktokUsername'] if 'tiktokUsername' in row else "",
                }
                add_or_update_user(user_id, user_info)
    except Exception as e:
        print(f'An error occurred while reading the CSV file: {e}')

# Example usage
if __name__ == "__main__":
    # Grab from file
    user_id = "example_user_id"
    displayName = "example_display_name"
    fullName = "example_full_name"
    ###############
    user_info = {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "age": 30,
        "uid": user_id,
        "displayName": displayName,
        "fullName": fullName,
        "firstName": "",
        "lastName": "",
        "contactList": [],
        "instagramUsername": "",
        "tiktokUsername": "",
    }
    
    add_or_update_user(user_id, user_info)
    
    # Create test profiles from CSV
    create_test_profiles_from_csv('users.csv')
