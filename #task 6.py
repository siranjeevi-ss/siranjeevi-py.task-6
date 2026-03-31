#task 1

class User:
    def __init__(self):
        self.__user_name = None   # private variable
        self.__pwd = None         # private variable

    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name   # password hidden

    def register(self):
        print(f"Registering user: {self.__user_name}")

    def login(self):
        print(f"Logging in: {self.__user_name}")


# Usage
u1 = User()
u1.set_user("john", "1234")
u1.register()
u1.login()

#task 2

class User:
    def register(self):
        print("User Registered")

    def login(self):
        print("User Logged in")


class Student(User):
    def student_greet(self):
        print("Hello Student")


class Faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")


class TempFaculty(Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")


# Usage
s = Student()
s.register()          # parent method
s.login()             # parent method
s.student_greet()     # child method

f = Faculty()
f.register()
f.faculty_greet()

t = TempFaculty()
t.register()
t.faculty_greet()
t.tempFaculty_greet()

#task 3

class User:
    def greet(self):
        print("Welcome User")


class Student(User):
    def greet(self):
        print("Welcome Student")


class Faculty(User):
    def greet(self):
        print("Welcome Faculty")


# Usage
s = Student()
f = Faculty()

s.greet()
f.greet()

#task 4

class User:
    def login(self):
        print("logined")
        return self

    def greet(self):
        print("enjoy everyone")
        return self

    def register(self):
        print("registered")
        return self


# Usage
user = User()
user.login().greet().register()

#task 5

class User:
    users_count = 0   # class variable

    def __init__(self, name, pwd):
        self.__name = name
        self.__pwd = pwd
        User.users_count += 1

    def get_name(self):
        return self.__name

    def login(self):
        print(f"{self.__name} logged in")
        return self

    def register(self):
        print(f"{self.__name} registered")
        return self

    def greet(self):
        print("Welcome User")
        return self


class Student(User):
    def greet(self):
        print("Welcome Student")
        return self


class Faculty(User):
    def greet(self):
        print("Welcome Faculty")
        return self


# Usage
u1 = Student("John", "123")
u1.login().greet().register()

u2 = Faculty("David", "456")
u2.login().greet().register()

print("Total Users:", User.users_count)