''' static attribute
sometimes called a class attribute is an attribute that belongs to the class itself not to any particular object
'''

class user:
    user_count = 0  #this is a static attribute
    # remains on the class not on the object created in the class 

    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password
        user.user_count += 1 # incrementing the static variable every time the object is created

    def display_user(self):
        print(f'User: {self.username}, Email: {self._email}')

user1 = user('sahil', 'sfsdf@gmail.com', '12345')
user2 = user('john', 'asdsf@gmail.com', '12345')
user3 = user('jane', 'ajdksf@gmail.com', '12345')

user1.display_user()
user2.display_user()
user3.display_user()

print(f'Total users: {user.user_count}') # accessing the static variable using the class name   

print(user2._user__count) # accessing the static variable using the object  