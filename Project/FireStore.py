from firebase import firebase

class User():

    url = 'https://fresh-base-246509.firebaseio.com/'
    db = firebase.FirebaseApplication(url)

    def __init__(self,name,_id):
        self.name = name
        self._id = _id
    
    def __CreateUserData(self):
        return {
            'id' : self._id,
            'name' : self.name
        }
    
    def sendData(self):
        User.db.put('/user',self.name,self.__CreateUserData())


        




# engineer = {'id':1001,'name':'Uncle Engineer'}
# engineer2 = {'id':1002,'name':'Lung Tu'}

# result = messenger.put('/Project/user','Book',engineer)
# result2 = messenger.put('/Project/user','book2',engineer2)

# print("Engineer 1", result)
# print("Engineer 2", result2)
