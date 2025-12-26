from datetime import datetime
from models import StandardRoom, SuiteRoom
from exceptions import RoomNotFoundError, InvalidDateError, HotelError

class HotelService:
    def __init__(self, db_manager):
        self.db = db_manager
        self._rooms = [] 
        self._load_rooms_from_db()
        self._seed_initial_data() 

    def _load_rooms_from_db(self):
        records = self.db.get_all_rooms()
        self._rooms = [] 
        for record in records:
            room_no, r_type, price = record
            if r_type == "StandardRoom":
                self._rooms.append(StandardRoom(room_no, price))
            elif r_type == "SuiteRoom":
                self._rooms.append(SuiteRoom(room_no, price))

    def _seed_initial_data(self):
        if not self._rooms:
            self.add_room(1, 101, 100.0) 
            self.add_room(1, 102, 100.0) 
            self.add_room(2, 201, 250.0) 

    def add_room(self, room_type, room_no, price):
        type_str = "StandardRoom" if room_type == 1 else "SuiteRoom"
        success = self.db.add_room(room_no, type_str, price)
        if success:
            self._load_rooms_from_db()
            return True
        return False

    def remove_room(self, room_no):
        success = self.db.delete_room(room_no)
        if success:
            self._load_rooms_from_db() 
            return True
        else:
            return False

    def check_availability(self, room_no, new_check_in, new_check_out):
        all_reservations = self.db.get_all_reservations()
        for res in all_reservations:
            db_room_no = res[3]
            if db_room_no == room_no:
                existing_in = datetime.strptime(res[4], "%d.%m.%Y")
                existing_out = datetime.strptime(res[5], "%d.%m.%Y")
                
                if new_check_in < existing_out and new_check_out > existing_in:
                    return False
        return True

    def make_reservation(self, first_name, last_name, id_no, room_no, check_in_str, check_out_str):
        try:
            target_room = next((r for r in self._rooms if r.room_number == room_no), None)
            if not target_room:
                raise RoomNotFoundError("Specified room not found.")

            check_in = datetime.strptime(check_in_str, "%d.%m.%Y")
            check_out = datetime.strptime(check_out_str, "%d.%m.%Y")
            duration = (check_out - check_in).days

            if duration <= 0:
                raise InvalidDateError("Check-out date must be after check-in date.")
            
            if not self.check_availability(room_no, check_in, check_out):
                print(f"❌ Error: Room {room_no} is ALREADY BOOKED for these dates!")
                return
            
            fee = target_room.calculate_price(duration)
            full_name = f"{first_name} {last_name}"
            
            self.db.save_reservation(full_name, id_no, room_no, check_in_str, check_out_str, fee)
            
            print(f"\n✅ Reservation Confirmed!")
            print(f"Customer: {full_name}")
            print(f"Room: {target_room.room_number} ({type(target_room).__name__})")
            print(f"Duration: {duration} Nights")
            print(f"Total Fee: ${fee:.2f}")

        except ValueError:
            print("❌ Error: Invalid date format! (Use DD.MM.YYYY)")
        except HotelError as e:
            print(f"❌ Operation Failed: {e}")

    def cancel_reservation(self, res_id):
        reservation = self.db.get_reservation_by_id(res_id)
        if not reservation:
            return "❌ Error: Reservation ID not found."
        
        check_in_str = reservation[4]
        check_in_date = datetime.strptime(check_in_str, "%d.%m.%Y")
        today = datetime.now()
        
        days_left = (check_in_date - today).days

        if days_left < 2:
            return f"❌ Cancellation Failed: Only {days_left} days left (Minimum 2 days required)."
        
        if self.db.delete_reservation(res_id):
            return "✅ Reservation cancelled successfully."
        return "❌ Error: Database error."

    def get_revenue(self):
        return self.db.get_total_revenue()

    def get_rooms(self):
        return self._rooms

    def get_reservations(self):
        return self.db.get_all_reservations()