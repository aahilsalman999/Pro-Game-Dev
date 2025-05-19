class Student:
    print("*Welcome to Year 7!*")
    name = ""
    age = 12
    s_class = "7H1"
    teacher = "Mr Heale"
    house = "Newton"
    country = ""
    
    def __init__(self):
        print(" New student!")
        self.name = input("What is your name?")
        self.age = int(input("What is your age?"))
        self.country = input("Where do you live?")
        self.s_class = "7H1"
        self.teacher = "Mr Heale"
        self.house = "Newton"

    def show_details(self):
        print("Hello "+ self.name)
        print(f"Your age is {self.age}")
        print(f"Aahil lives in {self.country}")
        print("Your class is "+ self.s_class)
        print("Your teacher is "+ self.teacher)
        print("Your house is "+ self.house)
        print("*Have Fun!")
    
student1 = Student()
student1.show_details()


        
