class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email # intended for internal use should not be used outside the class
        self.password = password

    def get_email(self):
        return self._email


    '''def say_hi_to_user(self, user):
        print(f'Sending message to {user.username}, its me {self.username}')'''


user1 = User('sahil', 'sfsdf@gmail.com', '12345')
#user2 = User('john', 'asdsf@gmail.com', '12345')

print(user1._email) # just a convention not a true private variable
# to tell python developers that it shouldnt be accessed outside the class
user1.email = 'dan@gmail.com'

print(user1.email)

'''accessing and modifying data - 
1. the traditional way : make the data private and use getter and setters
To protect prefixing an underscore to the data  (not mandatory, just a convention)
this cannot be used outside of the class'''
