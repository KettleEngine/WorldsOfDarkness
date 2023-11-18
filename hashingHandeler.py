import hashlib

class Hash():
    
    def __init__(self):
        pass
    
    #to hash data like passwords to protect them incase of a data leak
    def hash(self, data):
        sha256_hash = hashlib.sha256()
        sha256_hash.update(data.encode())
        return sha256_hash.hexdigest()
    
    #data is what will be salted (so stuff like passwords) and salt is what will be used to salt it
    def salt(self, data, salt):
        #hash the salt so that it looks all the same for the next step
        saltedData = data+hash(salt)
        return saltedData
    
    #this is a concept that i have been engineering in my head for a while and bassically it takes the hashed string
    #and divides it into many small little peices like how a cheff would dice an onion. then it takes all the small
    #segments and puts them in a different order this makes it so that a rainbow bridge should not work as even if it
    #cold figure out the salt it would not matter as it would look like random noise
    def dicing(self, data):
        #first get the length of the hashed string, this allos me to devide the string up roughly evenly
        #all of them should be 64 characters long but just incase it is best for it to be dynamic
        length = len(data)
        print(length)
        
        #next part is to just try and devide the length as much as possible to get an amount of groups ofcharacters
        #this will be done based on the length of the string so for a 64 length there may be 16 groups of 4 but 32 may have 8 groups of 4
        dices = length // 4 #4 is how big i am going to make each diced segment
        print(dices)
        
        #note to self: i can't wait to get this working only to find out a system like this is already been made and better than my one
        
        #next part is to split up each part of the string into groups of 4
        dicesList = []
        
        #to start with we need a for loop to dice each segment
        for i in range(0, dices):

            #first, the first 4 characters are appended to the dicesList array
            dicesList.append(data[:4])

            #removes the first 4 characters from the string so that for the next iteration new character are able to be appended
            data = data[4:]
        
        #next step is to shuffle the diced segments around in a pattern that is consistant
        print(dicesList)
        #the best way i have thought of to do this is to convert each character in each segment into their 
        #dinary representation. then sort the array, thenconvert it back into a string and concatinate the strings together
        
        
            
            