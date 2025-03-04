import firebase_admin
from firebase_admin import db

# Initialize Firebase Admin SDK
cred = firebase_admin.credentials.Certificate('service.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://test-1ef0d-default-rtdb.asia-southeast1.firebasedatabase.app'
})

# Reference to the root
ref = db.reference('/users')

def create_user(user_id,email,password):
   ref.child(user_id).set({
      'email': email,
      'password': password
   })
   print (f"the {email} added Successfully")
   
# create_user("21CSR002", "test@nediveil.in","123456")


def get_all_users():
   users=ref.get()
   print(users)
   
# get_all_users()

def get_user(user_id):
   user = ref.child(user_id).get()
   print(user)
   
# get_user("21CSR001")

def update_data(user_id,email=None, password=None):
   updates={}
   if email:
      updates['email'] = email
   if password:
      updates['password'] = password
   
   ref.child(user_id).update(updates)
   print("User Updated Successfully")
   
# update_data('21CSR002',password="987654")

def delete_user(user_id):
   ref.child(user_id).delete()
   print("user deleted successfully")
   
def delete_user(user_id):
   ref.child(user_id).delete()
   print("user deleted successfully")
   
   
delete_user('21CSR002')