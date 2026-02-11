# 📚 Bookstore Management System (Python)

This project is a console-based Bookstore Management System implemented in Python.  
It uses custom **Linked List** data structures and a **recursive tree-based category system** to manage books and hierarchical categories.

---

## 🚀 Features

- Add and delete categories (with hierarchical structure)
- Add and delete books
- Unique name validation for books and categories
- Recursive search for books
- Display all books inside a category (including sub-categories)
- Console-based interactive menu system

---

## 🏗️ Data Structure Design

- Custom `LinkedList` implementation (no built-in Python list used)
- `Category` nodes form a tree structure
- Each category contains:
  - A linked list of sub-categories
  - A linked list of books
- Recursive traversal for:
  - Searching
  - Deleting
  - Displaying content

---

## 🎯 Educational Purpose

This project is designed to demonstrate:

- Linked List implementation
- Tree structures
- Recursion
- Object-Oriented Programming (OOP) in Python
- Data structure design without relying on built-in containers

---

## ▶️ How to Run

```bash
python filename.py
