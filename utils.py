from datetime import datetime

class InputValidator:
    @staticmethod
    def get_valid_string(prompt, error_msg="Invalid input! Letters only."):
        while True:
            value = input(prompt).strip()
            if value.replace(" ", "").isalpha():
                return value
            print(f"❌ {error_msg}")

    @staticmethod
    def get_valid_int(prompt, error_msg="Invalid input! Numbers only."):
        while True:
            value = input(prompt).strip()
            if value.isdigit():
                return int(value)
            print(f"❌ {error_msg}")

    @staticmethod
    def get_valid_id(prompt):
        while True:
            value = input(prompt).strip()
            if value.isdigit() and len(value) == 11:
                return value
            print("❌ Error: ID must be exactly 11 digits.")

    @staticmethod
    def get_valid_date(prompt):
        while True:
            value = input(prompt).strip()
            try:
                datetime.strptime(value, "%d.%m.%Y")
                return value
            except ValueError:
                print("❌ Error: Invalid Date! Format: DD.MM.YYYY")