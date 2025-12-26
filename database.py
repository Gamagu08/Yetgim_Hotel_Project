import sqlite3

class DatabaseManager:
    def __init__(self, db_name="hotel_management.db"):
        self.db_name = db_name
        self._create_tables()

    def get_connection(self):
        return sqlite3.connect(self.db_name)

    def _create_tables(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS rooms (
                    room_no INTEGER PRIMARY KEY,
                    type TEXT,
                    price REAL
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS reservations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_name TEXT,
                    customer_id TEXT,
                    room_no INTEGER,
                    check_in TEXT,
                    check_out TEXT,
                    total_fee REAL,
                    FOREIGN KEY(room_no) REFERENCES rooms(room_no)
                )
            """)
            conn.commit()

    def add_room(self, room_no, room_type, price):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO rooms (room_no, type, price) VALUES (?, ?, ?)", 
                               (room_no, room_type, price))
                conn.commit()
                return True
            except sqlite3.IntegrityError:
                return False 

    def delete_room(self, room_no):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE FROM rooms WHERE room_no = ?", (room_no,))
                conn.commit()
                return cursor.rowcount > 0 
            except sqlite3.Error:
                return False

    def save_reservation(self, name, id_no, room_no, check_in, check_out, fee):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO reservations (customer_name, customer_id, room_no, check_in, check_out, total_fee)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (name, id_no, room_no, check_in, check_out, fee))
            conn.commit()

    def get_reservation_by_id(self, res_id):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM reservations WHERE id = ?", (res_id,))
            return cursor.fetchone()

    def delete_reservation(self, res_id):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE FROM reservations WHERE id = ?", (res_id,))
                conn.commit()
                return cursor.rowcount > 0
            except sqlite3.Error:
                return False

    def get_total_revenue(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT SUM(total_fee) FROM reservations")
            result = cursor.fetchone()[0]
            return result if result else 0.0

    def get_all_rooms(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM rooms")
            return cursor.fetchall()

    def get_all_reservations(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM reservations")
            return cursor.fetchall()