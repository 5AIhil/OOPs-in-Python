# getter and setter method

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email 
        self.password = password

    def get_email(self):
        print(f'email accessed') # this method gives us full contol aon everthing , what needs to be added and what not
        return self._email

    def set_email(self, new_email): # can add validation logic 
        if '@' in new_email:
            self._email = new_email
        else:
            raise ValueError('Invalid email')

user1 = User('sahil', 'sfsdf@gmail.com', '12345')
print(user1.get_email())

#user1._email = 'sasf'. this should not be done 
user1.set_email('scac')
print(user1.get_email())

# mantains the integrity of the data 
# helps to access and modify the data in an controlled way