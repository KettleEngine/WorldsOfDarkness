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

hash.dicing(hash.hash(pw))