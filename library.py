import sys

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def remove(self, target_name):
        curr = self.head
        prev = None
        while curr:
            if curr.data.name == target_name:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return True
            prev = curr
            curr = curr.next
        return False

class Book:
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price

    def __str__(self):
        return f"Book: {self.name} | Author: {self.author} | Price: {self.price}"

class Category:
    def __init__(self, name):
        self.name = name
        self.sub_categories = LinkedList()
        self.books = LinkedList()

class BookStoreSystem:
    def __init__(self, root_name):
        self.root = Category(root_name)

    def _find_category(self, current_node, target_name):
        if current_node.name == target_name:
            return current_node
        curr = current_node.sub_categories.head
        while curr:
            found = self._find_category(curr.data, target_name)
            if found: return found
            curr = curr.next
        return None

    def _is_name_exists(self, current_node, name, search_type="both"):
        if (search_type == "cat" or search_type == "both") and current_node.name == name:
            return True
        if search_type == "book" or search_type == "both":
            curr_book = current_node.books.head
            while curr_book:
                if curr_book.data.name == name:
                    return True
                curr_book = curr_book.next
        curr_sub = current_node.sub_categories.head
        while curr_sub:
            if self._is_name_exists(curr_sub.data, name, search_type):
                return True
            curr_sub = curr_sub.next
        return False

    def add_category(self, parent_name, new_cat_name):
        if self._is_name_exists(self.root, new_cat_name, "cat"):
            print(f"Error: Category '{new_cat_name}' already exists.")
            return
        parent = self._find_category(self.root, parent_name)
        if parent:
            parent.sub_categories.append(Category(new_cat_name))
            print(f"Category '{new_cat_name}' added to '{parent_name}'.")
        else:
            print("Error: Parent category not found.")

    def delete_category(self, cat_name):
        if cat_name == self.root.name:
            print("Error: Cannot delete the root category.")
            return
        parent = self._find_parent_of_category(self.root, cat_name)
        if parent:
            parent.sub_categories.remove(cat_name)
            print(f"Category '{cat_name}' and its content deleted.")
        else:
            print("Error: Category not found.")

    def _find_parent_of_category(self, current_node, target_name):
        curr = current_node.sub_categories.head
        while curr:
            if curr.data.name == target_name:
                return current_node
            found = self._find_parent_of_category(curr.data, target_name)
            if found: return found
            curr = curr.next
        return None

    def add_book(self, cat_name, b_name, b_author, b_price):
        if self._is_name_exists(self.root, b_name, "book"):
            print(f"Error: Book name '{b_name}' must be unique.")
            return
        target_cat = self._find_category(self.root, cat_name)
        if target_cat:
            target_cat.books.append(Book(b_name, b_author, b_price))
            print(f"Book '{b_name}' added to '{cat_name}'.")
        else:
            print("Error: Category not found.")

    def delete_book(self, book_name):
        if self._delete_book_recursive(self.root, book_name):
            print(f"Book '{book_name}' deleted.")
        else:
            print("Error: Book not found.")

    def _delete_book_recursive(self, current_node, book_name):
        if current_node.books.remove(book_name):
            return True
        curr_sub = current_node.sub_categories.head
        while curr_sub:
            if self._delete_book_recursive(curr_sub.data, book_name):
                return True
            curr_sub = curr_sub.next
        return False

    def show_all_books(self, cat_name):
        target_cat = self._find_category(self.root, cat_name)
        if target_cat:
            print(f"--- Books in '{cat_name}' and its sub-categories ---")
            self._print_books_recursive(target_cat)
        else:
            print("Error: Category not found.")

    def _print_books_recursive(self, node):
        curr_book = node.books.head
        while curr_book:
            print(curr_book.data)
            curr_book = curr_book.next
        curr_sub = node.sub_categories.head
        while curr_sub:
            self._print_books_recursive(curr_sub.data)
            curr_sub = curr_sub.next

    def search_book(self, book_name):
        book = self._search_book_recursive(self.root, book_name)
        if book:
            print("Book Found:")
            print(book)
        else:
            print("Result: Book not found.")

    def _search_book_recursive(self, node, book_name):
        curr_book = node.books.head
        while curr_book:
            if curr_book.data.name == book_name:
                return curr_book.data
            curr_book = curr_book.next
        curr_sub = node.sub_categories.head
        while curr_sub:
            found = self._search_book_recursive(curr_sub.data, book_name)
            if found: return found
            curr_sub = curr_sub.next
        return None

def main():
    system = BookStoreSystem("Root")
    while True:
        print("\n=== BOOKSTORE MANAGEMENT SYSTEM ===")
        print("1. Add Category")
        print("2. Delete Category")
        print("3. Add Book")
        print("4. Delete Book")
        print("5. Display Category Books")
        print("6. Search Book")
        print("0. Exit")
        
        choice = input("Select Option: ")
        
        if choice == '1':
            parent = input("Enter Parent Category: ")
            name = input("Enter New Category Name: ")
            system.add_category(parent, name)
        elif choice == '2':
            name = input("Enter Category Name to Delete: ")
            system.delete_category(name)
        elif choice == '3':
            cat = input("Enter Target Category: ")
            name = input("Book Name: ")
            author = input("Author: ")
            try:
                price = float(input("Price: "))
                system.add_book(cat, name, author, price)
            except ValueError:
                print("Invalid price format.")
        elif choice == '4':
            name = input("Enter Book Name to Delete: ")
            system.delete_book(name)
        elif choice == '5':
            name = input("Enter Category Name: ")
            system.show_all_books(name)
        elif choice == '6':
            name = input("Enter Book Name: ")
            system.search_book(name)
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid input!")

if __name__ == "__main__":
    main()