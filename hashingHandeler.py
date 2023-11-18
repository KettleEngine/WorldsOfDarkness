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
        pass