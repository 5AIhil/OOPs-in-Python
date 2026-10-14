# both protected and private variable can be accessed within a class

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.__email = email 

    def clean_email(self):
        return self.__email.lower().strip()

    
user1 = User('sahil', 'sfsdf@gmail.com', '12345')
print(user1.clean_email())

# the consenting adults philosophy 
# double underscore before the email will throw an error this is actually protected

# print(user1.__email) # this will actually not throw an error as 
# under the hood the name is changed to _classname__email by the python interpreter
# name mangled

# protected is usually used when we want to access the variable in the child class
