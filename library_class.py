class Library:
    
    def __init__(self):
        self.books = []
        self.noBooks=0
        
    def addBook(self,book):
        self.books.append(book)
        self.noBooks+=1
        
    def showInfo(self):
        print(f"Total books in the library are {self.noBooks}")
        for book in self.books:
            print(book)
            
            

li=Library()
li.addBook("Python")
li.addBook("C++")
li.showInfo()