class Book:
    def __init__(self, title, author, isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.checked_out=False

    def info(self):
        print(self.title, self.author)


    def check_out(self):
        if self.checked_out:
            print("Grāmata pie lasītāja")
        else:
            self.checked_out=True
            print("Grāmata tik izdota")
    
    def check_in(self):
        if not self.checked_out:
            print("Grāmata ir uz vieta")
        else:
            self.checked_out=False
            print("Pieņemam grāmatu")




book1=Book("Soli pa solim", "Ērglis Kage", "978-07432")
book1.info()
book1.check_out()
book1.check_out()
book1.check_in()
book1.check_in()