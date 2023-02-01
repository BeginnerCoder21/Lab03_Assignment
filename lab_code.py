import pandas as pd

data=[]
class Employee:
    def __init__(self,id,name,age,salary):
       self.id=id
       self.name=name
       self.age=age
       self.salary=salary

    def disp(self):
        print(self.id)
        print(self.name)
        print(self.age)
        print(self.salary)

    def to_dict(self):
        headers = ['Employee ID', 'Name', 'Age', 'Salary (PM)']
        for i in range(0,len(headers)):
            return[self.id,self.name,self.age,self.salary]
            
    def sort_age(self):
        self.data = self.data.sort_values("Age")
        return data

e1=Employee("161E90","Raman",41,56000)
e2=Employee("161F91","Himadri",38,67500)
e3=Employee("161F99","Jaya",51,82100)
e4=Employee("171E20","Tejas",30,55000)
e5=Employee("171G30","Ajay",45,44000)

res1=e1.to_dict()
res2=e2.to_dict()
res3=e3.to_dict()
res4=e4.to_dict()

data.append(res1)
data.append(res2)
data.append(res3)
data.append(res4)

df = pd.DataFrame(data, columns=['Employee ID', 'Name', 'Age', 'Salary (PM)'])
print(df)
print("------MENU------")
print("1. Sort by AGE")
print("2. Sort by NAME")
print("3. Sort by SALARY")
print("4. Exit")
print()
val=1
while val:
    val=int(input("\nEnter your choice: "))
    if val==1:
        df=df.sort_values("Age")
        print(df)
    elif val==2:
        df=df.sort_values("Name")
        print(df)
    elif val==3:
        df=df.sort_values("Salary (PM)")
        print(df)
    elif val==4:
        exit()
    else:
        exit()