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
        self.name = input("What is your name? ")
        self.age = int(input("What is your age? "))
        self.country = input("Where do you live? ")

    def show_details(self):
        print("\nHello "+ self.name)
        print(f"Your age is {self.age}")
        print(f"{self.name} lives in {self.country}")
        print("Your class is "+ self.s_class)
        print("Your teacher is "+ self.teacher)
        print("Your house is "+ self.house)
        print("*Have Fun!\n")

    
    def change_details(self):
        print("Change details:")
        self.name = input("What is your name? ")
        student1.show_details()

    
    
student1 = Student()
student1.show_details()
#student2 = Student()
#student2.show_details()
student1.change_details()



        
