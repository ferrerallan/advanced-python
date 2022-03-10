import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyDMXhq4JmSW79L7AIOOuRBMhUJkTx3-KH8",
  "authDomain": "testing-python-7820d.firebaseapp.com",
  "projectId": "testing-python-7820d",
  "storageBucket": "testing-python-7820d.appspot.com",
  "messagingSenderId": "340447020494",
  "appId": "1:340447020494:web:0977f676d0a03af33f179f",
  "measurementId": "G-CPMRDTNGNS",
  "databaseURL": "https://testing-python-7820d-default-rtdb.firebaseio.com/",
}

firebase = pyrebase.initialize_app(firebaseConfig)

database = firebase.database()
database.child().update({"guitar":"ibanez"})