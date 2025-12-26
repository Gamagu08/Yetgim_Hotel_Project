# Pendik YETGİM – Python Graduation Project
## Hotel Management System 🏨

This project was developed as the **Python Graduation Project** within the **Pendik YETGİM Software Training Program**.

It is a **console-based Hotel Management System** built with Python, designed to demonstrate core programming skills such as **Object-Oriented Programming (OOP)**, **Clean Architecture**, **error handling**, and **database operations**.

---

## 📌 Project Purpose

The main goal of this project is to apply Python fundamentals in a real-world scenario by building a modular and maintainable hotel management application.

This project focuses on:
- Clean code structure & Layered Architecture
- Separation of concerns (SoC)
- Readable and maintainable codebase
- Practical use of OOP concepts (Inheritance, Encapsulation, Polymorphism)

---

## ⚙️ Technologies Used

- **Python 3.x**
- **SQLite** (Persistent Database Storage)
- **Object-Oriented Programming (OOP)**
- **Git & GitHub** for Version Control
- **Modular Architecture**

---

## 🧱 Project Architecture

The project follows a **layered and modular structure**:

```text
Yetgim_Hotel_Project/
│
├── main.py          # Application entry point (Orchestrator)
├── ui.py            # User interface and menu operations
├── services.py      # Business logic layer (Rules & Calculations)
├── models.py        # Data models and entities
├── database.py      # Database access layer (SQLite)
├── exceptions.py    # Custom exception classes
├── utils.py         # Helper functions (Input Validation)
├── README.md        # Project documentation
└── .gitignore       # Git configuration

✨ Features
- Role-Based Access: Secure Admin and Guest login flows.

- Reservation Management: Add, view, and cancel reservations.

- Smart Booking Logic: Prevents double booking for overlapping dates.

- Financial Reporting: View total revenue (Admin only).

- Data Persistence: Automatically saves data to a local database.

- Robust Error Handling: Validates user inputs (dates, IDs, names).

▶️ How to Run the Project
Requirements
  - Python 3.8 or higher

  Steps
1. Clone the repository:
git clone https://github.com/Gamagu08/Yetgim_Hotel_Project.git

2. Navigate to the project directory:
   cd Yetgim_Hotel_Project

3. Run the application:
   python main.py

🧪 Error Handling
The project uses custom exceptions (HotelError, RoomOccupiedError, etc.) to handle invalid user input and unexpected situations gracefully, ensuring a smooth user experience without crashing.

🎓 Educational Context
This project was completed as part of the Pendik YETGİM Python Training Program and serves as a final graduation project. It is intended for educational purposes to demonstrate the developer’s understanding of Python programming concepts.

🚀 Potential Enhancements (Scope for Expansion)
*Note: This project is a finalized graduation assignment. However, in a real-world production scenario, the following features would be considered for implementation:*

- **Database Migration:** Switching from SQLite to **PostgreSQL** for better concurrency and scalability.
- **GUI Implementation:** Developing a desktop interface using **PyQt** or a web dashboard using **Django/Flask**.
- **Unit Testing:** Adding comprehensive test coverage using **PyTest**.
- **API Integration:** Creating RESTful API endpoints for mobile application support.

👤 Developer
Kadir Kırmızıyüz Python Developer GitHub: Gamagu08

📄 License This project is created for educational purposes.
















