from methods import *
from hashingHandeler import *

meth = methods()

hash = Hash()
email = "csutton893@gmail.com"
pw = "test"

#meth.generateUID()
#meth.addUser("chrles", "csutton893@gmail.com", "test")
#print(meth.hash("test"))

#print(meth.checkEmail("csutton893@gmail.com"))
#print(meth.checkEmail("cs"))

#print(meth.login(email, pw))
#print(ord("1"))



def checkHashes(hash1, hash2):
    if hash1 == hash2:
        return True
    else:
        return False

hashed1 = "470621b10a08d015a5041c43d081822c6c152d18a955d548b9827d65884c9f86b0a02b0b11cbb0f0b22e4f1bc55ad15d7a2df53a38ac9a2feaa0a3bf8fcafe6e"
hashed2 = "5117470621b1a5041c432d189c13953ac547a95584c6d548b982b497b0a011cb1c6ab22eaa835c4b7a2df53a38ac4f4c59ae5eb8fb57b7e88fcafe6ef7eeeecb"

testString1 = "test"
testString2 = "test"
    
print(checkHashes(hash.hash(testString1), hash.hash(testString2)))

print(hash.hash(testString1))

print(hash.hash(testString2))