import sys
from services import HotelService
from database import DatabaseManager
from utils import InputValidator

class UIManager:
    def __init__(self):
        db_manager = DatabaseManager()
        self.service = HotelService(db_manager)

    def start_app(self):
        while True:
            print("\n" + "="*40)
            print("   PYTHON PALACE - WELCOME")
            print("="*40)
            print("--- INFO: Manager Password is 'admin123' ---")
            print("1. Admin Login")
            print("2. Guest Login")
            print("3. Exit")
            
            choice = input("Select User Type (1-3): ")
            
            if choice == '1':
                self._admin_login_flow()
            elif choice == '2':
                self._guest_flow()
            elif choice == '3':
                print("Goodbye!")
                sys.exit()
            else:
                print("Invalid selection.")

    def _admin_login_flow(self):
        password = input("Enter Admin Password: ")
        if password == "admin123":
            print("\n✅ Login Successful! Welcome Admin.")
            self._admin_menu()
        else:
            print("\n❌ Access Denied.")

    def _admin_menu(self):
        while True:
            print("\n--- ADMIN PANEL ---")
            print("1. Add New Room")
            print("2. View All Reservations")
            print("3. List All Rooms")
            print("4. Delete Room")
            print("5. Cancel Reservation")
            print("6. View Total Revenue")
            print("7. Logout")
            
            choice = input("Admin Choice: ")
            
            if choice == '1':
                print("\n--- Add New Room ---")
                r_type = InputValidator.get_valid_int("Type (1.Standard / 2.Suite): ")
                no = InputValidator.get_valid_int("Room No: ")
                price = float(input("Price: ")) 
                
                if self.service.add_room(r_type, no, price):
                    print(f"✅ Room {no} added.")
                else:
                    print(f"❌ Error: Room {no} exists.")

            elif choice == '2':
                self._display_reservations()

            elif choice == '3':
                self._display_rooms()

            elif choice == '4':
                self._display_rooms()
                try:
                    no = InputValidator.get_valid_int("Room No to DELETE: ")
                    if input(f"Are you sure to delete Room {no}? (y/n): ").lower() == 'y':
                        if self.service.remove_room(no):
                            print(f"✅ Room {no} deleted.")
                        else:
                            print(f"❌ Error: Could not delete Room {no}.")
                except Exception:
                    print("Error during deletion.")
            
            elif choice == '5':
                self._display_reservations()
                res_id = InputValidator.get_valid_int("Enter Reservation ID to Cancel: ")
                result = self.service.cancel_reservation(res_id)
                print(result)

            elif choice == '6':
                total = self.service.get_revenue()
                print(f"\n💰 Total Hotel Revenue: ${total:,.2f}")
            
            elif choice == '7':
                break

    def _guest_flow(self):
        print("\n👋 Welcome Dear Guest!")
        while True:
            print("\n--- GUEST MENU ---")
            print("1. View Available Rooms")
            print("2. Make a Reservation")
            print("3. Cancel My Reservation")
            print("4. Main Menu")
            
            choice = input("Choice: ")
            
            if choice == '1':
                self._display_rooms()
            
            elif choice == '2':
                print("\n--- New Reservation ---")
                fn = InputValidator.get_valid_string("First Name: ")
                ln = InputValidator.get_valid_string("Last Name: ")
                id_no = InputValidator.get_valid_id("ID Number: ")
                
                room = InputValidator.get_valid_int("Room No to Book: ")
                cin = InputValidator.get_valid_date("Check-in (DD.MM.YYYY): ")
                cout = InputValidator.get_valid_date("Check-out (DD.MM.YYYY): ")

                self.service.make_reservation(fn, ln, id_no, room, cin, cout)
            
            elif choice == '3':
                res_id = InputValidator.get_valid_int("Enter Reservation ID to Cancel: ")
                result = self.service.cancel_reservation(res_id)
                print(result)

            elif choice == '4':
                break

    def _display_rooms(self):
        rooms = self.service.get_rooms()
        print("\n--- ROOM LIST ---")
        if not rooms:
            print("No rooms found.")
        for r in rooms:
            print(r)

    def _display_reservations(self):
        res = self.service.get_reservations()
        print("\n--- RESERVATIONS ---")
        if not res:
            print("No reservations found.")
        for r in res:
             print(f"ID: {r[0]} | Name: {r[1]} | Room: {r[3]} | Dates: {r[4]}-{r[5]} | Fee: ${r[6]}")