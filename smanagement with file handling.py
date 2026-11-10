class student:
    def __init__(self,id,name,age,place):
        self.id=id
        self.name=name
        self.age=age
        self.place=place
    def display_details(self):
        print("ID:",self.id)    
        print("Name:",self.name)
        print("Age:",self.age)
        print("Place:",self.place)
class studentmanagement:
    def __init__(self):
        self.students=[]
        with open("student.txt","a"):
            pass

    def add_student(self):
        id=input("Enter Id")
        name=input("Enter your Name")
        age=input("Enter Age")
        place=input("Enter Place")
        s=student(id,name,age,place)
        self.students.append(s)
        self.save_details()
        print("STUDENT ADDED SUCCESSFULLY!!!!")
    def view_all_students(self):
        if not self.students:
            print("No Students Available")
        else:
            for i in self.students:
                i.display_details()
    def serach_student(self):
        search_id=input("Enter Student ID to search")
        for i in self.students:
            if i.id==search_id:
                i.display_details()
                print("Student Found")
                break
        else:
            print("Student not Found")
    def update_student(self):
        id=input("Enter student ID")
        for i in self.students:
            if i.id==id:
                new_name=input("Enter new name")
                new_age=input("Enter new age") 
                new_place=input("Enter new place")
                i.name=new_name
                i.age=new_age
                i.place=new_place
                self.save_details()
                print("Student Updated Successfully!")
                i.display_details()
                break
        else:
            print("Student Not Found")
    def delete_student(self):
        id=input("Enter student id to remove")
        for i in self.students:
            if i.id==id:
                self.students.remove(i)
                self.save_details()
                print("Student Deleted Successfully!")
                break
        else:
            print("Student Not Found!")
    def save_details(self):
        with open("student.txt","w") as file:
            for i in self.students:
                data=i.id+","+i.name+","+i.age+","+i.place+"\n"
                file.write(data)

    def run(self):
        while True:
            print("===== STUDENT MANAGEMENT SYSTEM =====")
            print("1. Add Student")
            print("2. View All Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Exit")
            choice=input("Enter your Choice")
            if choice=="1":
                self.add_student()
            elif choice=="2":
                self.view_all_students()
            elif choice=="3":
                self.serach_student()
            elif choice=="4":
                self.update_student()
            elif choice=="5":
                self.delete_student() 
            elif choice=="6":
                print("Thank You") 
                break
            else:
                print("Invalid choice ,Select 1 to 6")                  


if __name__ == "__main__":
    sm =studentmanagement ()
    sm.run()





                   
