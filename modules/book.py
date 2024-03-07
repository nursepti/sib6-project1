from modules.library_item import LibraryItem #panggil parent class


class Book(LibraryItem):
    def __init__(self, title, upc, subject, issbn, authors, dds_number): #constructor
        super().__init__(title, upc, subject) #super class untuk mewarisi dari parent class
        self.issbn = issbn
        self.authors = authors
        self.dds_number = dds_number
