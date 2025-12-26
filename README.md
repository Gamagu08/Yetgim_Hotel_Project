# Hotel Management System 🏨
### Pendik YETGİM Nesneye Dayalı Programlama - Python Geliştirme ve Uyum Eğitimi Bitirme Projesi
*(Pendik YETGİM Object-Oriented Programming - Python Development and Compliance Training Capstone Project)*

This project is a professional, terminal-based Hotel Management System developed as the **Capstone Project** for the YETGİM Bootcamp. It demonstrates advanced Python concepts including **Object-Oriented Programming (OOP)**, **Layered Architecture**, **SOLID Principles**, and **Database Management**.

## 🚀 Features
- **Role-Based Access Control:** Secure Admin and Guest login systems.
- **Reservation Management:** Create, view, and cancel reservations.
- **Smart Booking System:** Prevents double booking with overlap logic.
- **Financial Reporting:** Admins can view real-time total revenue.
- **Data Persistence:** Uses SQLite for reliable and permanent data storage.
- **Input Validation:** Robust error handling for user inputs using a dedicated Utils class.

## 📂 Project Architecture
The project follows a modular **Clean Architecture**:
- `main.py`: Entry point (Orchestrator).
- `ui.py`: User Interface handling (Console Menus).
- `services.py`: Business Logic Layer (Calculations & Rules).
- `models.py`: Data Structures (Encapsulated Classes).
- `database.py`: Data Access Layer (SQLite Operations).
- `utils.py`: Static Helper Methods (Validation).
- `exceptions.py`: Custom Error Handling.

## 🛠️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/yetgim-hotel-project.git](https://github.com/YOUR_USERNAME/yetgim-hotel-project.git)

2. **Navigate to the project directory:**

     cd yetgim-hotel-project

3. **Run the application:**

    python main.py