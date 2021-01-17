import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyBcAcwWpcQPsGUzKfhtgeF0Io7lfWJ2n0U",
    "authDomain": "webtest-ba543.firebaseapp.com",
    "databaseURL": "https://webtest-ba543-default-rtdb.firebaseio.com",
    "projectId": "webtest-ba543",
    "storageBucket": "webtest-ba543.appspot.com",
    "messagingSenderId": "117806514902",
    "appId": "1:117806514902:web:fa40ed51bb3f5b4f297f77",
    "measurementId": "G-DETW1MTKNP"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db=firebase.database()

'''
#Change Data
#create own key (will only be one per child) prefered method
choice = int(input("Select an Option  |  (1)Business  |  (2)Human  "))
if choice == 1:

  company = int(input ("Select Company to Report: (1)Dominos, (2)Starbucks, (3)Panda Express "))
  occupants = int(input("What is the current occupancy? "))

  
  if company == 1:
    data = {"Current Occupency": occupants}
    db.child("Dominos").set(data)
  elif company == 2:
    data1 = {"Current Occupency": occupants}
    db.child("Starbucks").set(data1)
  elif company == 3:
    data2 = {"Current Occupency": occupants}
    db.child("Panda Express").set(data2)

'''


#GOAL: PYTHON VARIABLES TO FIREBASE
company = str(input("What Business are you recording? "))
occupants = int(input("What is the current occupancy? "))

data = {"Current Occupency": occupants}
db.child(company).set(data)

'''
#Retrieve data
#Need to type in name like this (Dominos, Panda Express, Starbucks)
place = str(input("Enteter a business to check current occupency: "))
data = db.child(place).child("Current Occupency").get()
#data = db.child("Business").get()
print("Current Occupency " + str(data.val()))
'''