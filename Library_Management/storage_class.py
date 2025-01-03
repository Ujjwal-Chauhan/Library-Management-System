from books_storage import books 

books_data = []

class Storage:
    def __init__(self,title,autor):
        self.title = title
        self.author = autor

    
for i in books:
    title = i["title"]   
    author = i["author"]
    book = Storage(title,author)
    books_data.append(book)



