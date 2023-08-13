from databaseHandler import *
from emailHandeler import *
import random
import hashlib

class methods():
    
    def __init__(self):
        #database handler
        self.db = DB()
        
        #email handler
        self.email = Email()
    
    def addUser(self, username, email, password):
        #gets a unique user ID
        userID = self.generateUID()
        
        #hashes password
        password = self.hash(password)
        
        if self.email.checkEmail(email) == True:
        
            self.db.commitDB("INSERT INTO users (userID, username, email) VALUES ({}, '{}', '{}')".format(userID, username, email))
            self.db.commitDB("INSERT INTO passwords (userID, password) VALUES ({}, '{}')".format(userID, password))

        else:
            #return fasle measne that it failed the email check and the server can then tell the user
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
    
    #to hash data like passwords to protect them incase of a data leak
    def hash(self, data):
        sha256_hash = hashlib.sha256()
        sha256_hash.update(data.encode())
        return sha256_hash.hexdigest()            
    
    #returns the userID if all the inputs match up and flase if they dont match up
    def login(self, email, password):
        #hash the password
        password = self.hash(password)
        
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