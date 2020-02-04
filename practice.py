import pyrebase

config = {
    "apiKey": "AIzaSyCxnFqPQ4Rv3wxK8ajGWzDE_kIOtCaN2Bs",
    "authDomain": "test-f8bf5.firebaseapp.com",
    "databaseURL": "https://test-f8bf5.firebaseio.com",
    "projectId": "test-f8bf5",
    "storageBucket": "test-f8bf5.appspot.com",
    "messagingSenderId": "138404693159",
    "appId": "1:138404693159:web:c6f4edd5a809158560c782"
}


firebase = pyrebase.initialize_app(config)

db = firebase.database()

# db.child("names").push({"name" : "shivay"})
# db.child("names").child("name").update({"name" : "lamba"}) 

# users = db.child("names").child("name").get()
# print(users.key())
# db.child("names").remove()