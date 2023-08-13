#this file is for handeling anything to do with emails such as email verifcations and notifcations

class Email():
    def __init__(self):
        pass
    
    #checks for the presence of an email
    def checkEmail(self, email):
        #searches the database for the email in question
        check = self.db.queryDB("SELECT email FROM users WHERE email = '{}';".format(email))
        #if it is none then it means that the email is not in use
        if check is None:
            return True
        else:
            return False