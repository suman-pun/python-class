class User:
    def __init__(self, _id, username, password):
        self._id = _id
        self.username = username
        self.password = password

    def login(self, username, password):
        #Implement this function
        # Student and Teacher object should be able to log in
        # pass#
        
        # s=Student("1", "Shyam", "shyam123")
        self.username=username
        self.password=password
        if username==userName and password==passWord:
            print(f"Welcome {self.username}")
        else:
            print("Incorrect username or password")
            enteruser=input("Enter username: ")
            enterpass=input("Enter password: ")
            if username==enteruser and password==enterpass:
                print(f"Welcome {self.username}")
            else:
                print("error")
        
        

class Person(User):
    def __init__(self, _id, username, password, name, contact, address):
        super().__init__(_id, username, password)
        self.name = name
        self.contact = contact
        self.address = address

    def display_profile(self):
        # Implement this function
        # _id, username, contact, address, name
        # course if person is Student
        # designation if person is Teacher
        pass

class Student(Person):
    def __init__(self, _id, username, password, name, contact, address, course):
        super().__init__(_id, username, password, name, contact, address)
        self.course = course


class Teacher(Person):
    def __init__(self, _id, username, password, name, contact, address, designation):
        super().__init__(_id, username, password, name, contact, address)
        self.designation = designation

p=Person("1", "Ramdon", "ram123", "Ram", "234234", "KTM")
userName=input("Enter username: ")
passWord=input("Enter password: ")

u=User("2", "shyam", "shyam123")
u.login( "hari", "hari123")