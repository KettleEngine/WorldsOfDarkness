from databaseHandler import *
from emailHandeler import *
import random
import hashlib
from hashingHandeler import *

class methods():
    
    def __init__(self):
        #database handler
        self.db = DB()
        
        #email handler
        self.email = Email()
        
        #hash function
        self.hash = Hash()
    
    def addUser(self, username, email, password):
        #gets a unique user ID
        userID = self.generateUID()
        
        #hashes password
        password = self.hash.hash(password)
        
        if self.email.checkEmail(email) == True:
        
            self.db.commitDB("INSERT INTO users (userID, username, email) VALUES ({}, '{}', '{}')".format(userID, username, email))
            self.db.commitDB("INSERT INTO passwords (userID, password) VALUES ({}, '{}')".format(userID, password))
            
            #returns true to tell the server that this function has executed succesfully
            return True

        else:
            #return fasle means that it failed the email check and the server can then tell the user
            return False
        
    #generates a uneque user id for creating a new user
    def generateUID(self):
        loop = True
        while loop == True:
            num = random.randint(100_000, 9_223_372_036_854_775_800)
            check = self.db.queryDB("SELECT userID FROM users WHERE userID = '{}';".format(num))
            #if check is not the same as num that means that nothing was found so that user ID is available for use
            if check != num:
                loop = False
        #once the loop is broken we know that num is uneque so it can be returned
        return num
    
    #returns the userID if all the inputs match up and flase if they dont match up
    def login(self, email, password):
        #hash the password
        password = self.hash.hash(password)
        
        check = self.db.queryDB("SELECT userID FROM users WHERE email = '{}';".format(email))
        
        if check is not None:
            check2 = self.db.queryDB("SELECT userID FROM passwords WHERE password = '{}';".format(password))

            #if they are the same then the use inputed the correct email and password
            if check2 == check:
                return True
            else:
                return False
        #email was not registered so there is no point continuing and wasting time
        else:
            return False
    
    # this function handles saving all the data of a character sheet into the database
    # general data is the information like name, player, chronicle, nature, etc
    # attributes is a list of all the attribute values
    # abilities is like attributes but for abilities instead
    # advantages is the same as abilities and attributes but with the difference of an extra dimention to the lists becasue of the text required for diciplins and advantages
    # other is just all the other data of the sheet
    def saveSheet(self, userID, generalData, attributes, abilities, advantages, other):
        pass