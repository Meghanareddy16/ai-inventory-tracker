import firebase_admin
from firebase_admin import credentials, firestore

# Load Firebase credentials (Update with your actual path)
cred = credentials.Certificate("/Users/meghanareddymacha/Downloads/dataset/ai-inventory-tracker-12678-45d0b8791e7f.json")

# Initialize Firebase
firebase_admin.initialize_app(cred)

# Get Firestore Database
db = firestore.client()

print("Firebase connection successful!")
