import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("/Users/danielwu/Desktop/Rolodex Scripts/juniorkids-x-rolodex-firebase-adminsdk-jadrm-87274b3e78.json")  # Replace with the path to your Firebase Admin SDK JSON file
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://juniorkids-x-rolodex-default-rtdb.firebaseio.com/'
})


contacts_ref = db.reference('contacts')
contacts = contacts_ref.get()

if contacts:
    for name, details in contacts.items():

        if 'email' in details:
            print(f"{name}: {details['email']}")
else:
    print("No contacts found.")

