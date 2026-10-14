''' 2. Properties in python  - syntactic sugar 
 '''

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email 
        self.password = password

    @property   #decorator (turns method into property , so that we can access it directly without parentheses)
    def email(self):
        print('email fetching')
        return self._email 

    @email.setter  # this is an public email property while protecting the original email
    def email(self, new_email):
        if '@' in new_email:
            print('setting new email')
            self._email = new_email 
        else:
            print('Invalid email')

user1 = User('sahil', 'sfsdf@gmail.com', '12345')
#user1.email = 'this is not an email'
print(user1.email) # this code didnt need to be changed even if the property was not used this is called as syntactic sugar 
# no change in the calling code 

user1.email = 'sassad@sfsdf.com'
print(user1.email)