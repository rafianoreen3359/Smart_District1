""" Task: 
● Library Management System: A library needs to manage books, members, and 
borrowing records. Books are borrowed and returned. Members have limits. Overdue 
books trigger fines. Different membership tiers have different rules and privileges. Use 
single and multilevel inheritance for tiers, method overriding for fine logic, and dunder 
methods for display."""
class Book:
    def __init__(self, title):
        self.title = title
        self.borrowed = False

    def __str__(self):
        return self.title

class Member:
    def __init__(self, name):
        self.name = name
        self.books = []

    def borrow_book(self, book):
        if len(self.books) >= self.limit():
            print("Borrowing limit reached!")
        elif book.borrowed:
            print("Book is already borrowed!")
        else:
            self.books.append(book)
            book.borrowed = True
            print(self.name, "borrowed", book.title)

    def limit(self):
        return 2

    def calculate_fine(self, days):
        return days * 10

    def __str__(self):
        return f"{self.name} borrowed {len(self.books)} book(s)"

class PremiumMember(Member):
    def limit(self):
        return 4

class GoldMember(PremiumMember):
    def calculate_fine(self, days):
        return days * 5

class PlatinumMember(GoldMember):
    def calculate_fine(self, days):
        return 0

book1 = Book("Python")
book2 = Book("HTML")
book3 = Book("CSS")

member1 = Member("Ali")
member2 = GoldMember("Sara")
member3 = PlatinumMember("Ahmed")

member1.borrow_book(book1)
member2.borrow_book(book2)
member3.borrow_book(book3)

print("\n--- Members ---")
print(member1)
print(member2)
print(member3)

print("\n--- Fines ---")
print("Normal member:", member1.calculate_fine(3))
print("Gold member:", member2.calculate_fine(3))
print("Platinum member:", member3.calculate_fine(3))


