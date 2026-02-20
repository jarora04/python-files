class employee:
    def __init__(self,name,id,income):
        self.name=name
        self.id=id
        self.income=income
    def display(self):
        print(f"the employee name is {self.name} and id is {self.id} and income is {self.income}")
        
        
class manager(employee):
    def __init__(self,name,id,income,bonus):
        super().__init__(name,id,income)#supoer() is used to called parent function into child one
        self.bonus=bonus
    def display(self):
        super().display()
        print(f"the bonus is {self.bonus}")
        

e= manager("jatin",123,10000,2000)
print(e.display())

# _ to amke protected access modifier
#__ to make private access modifier and  a_class_name__attribute_name to acces that attribute
# class employee:
#     def __init__(self,name,id,income):
#         self.__name=name
#         self.__id=id
#         self.__income=income
#     def display(self):
#         print(f"the employee name is {self.__name} and id is {self.__id} and income is {self.__income}")
        
        
# class manager(employee):
#     def __init__(self,name,id,income,bonus):
#         super().__init__(name,id,income)
#         self.__bonus=bonus
#     def display(self):
#         super().display()
#         print(f"the bonus is {self.__bonus}")
        

# e= manager("jatin",123,10000,2000)
# print(e._manager__bonus)