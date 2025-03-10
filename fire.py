import os

firebase_cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
print(f"Firebase Credentials Path: {firebase_cred_path}")

if not firebase_cred_path or not os.path.exists(firebase_cred_path):
    print("❌ Firebase Key Missing or Incorrect!")
else:
    print("✅ Firebase Key Found!")
