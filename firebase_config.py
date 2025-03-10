import firebase_admin
from firebase_admin import credentials, firestore
import os

# Load Firebase credentials securely
firebase_cred_path = os.getenv("FIREBASE_CREDENTIALS")

if not firebase_cred_path:
    raise ValueError("❌ FIREBASE_CREDENTIALS environment variable not set!")

# Initialize Firebase
cred = credentials.Certificate(firebase_cred_path)
firebase_admin.initialize_app(cred)

# Get Firestore Database
db = firestore.client()

print("✅ Firebase connection successful!")
