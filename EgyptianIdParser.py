import datetime

class EgyptianIdParserBase:
    
    # Mapping of governorate codes
    governorate_map = {
        '01': 'Cairo',
        '02': 'Alexandria',
        '03': 'Port Said',
        '04': 'Suez',
        '11': 'Damietta',
        '12': 'Dakahlia',
        '13': 'Sharqia',
        '14': 'Qalyubia',
        '15': 'Kafr El Sheikh',
        '16': 'Gharbia',
        '17': 'Monufia',
        '18': 'Beheira',
        '19': 'Ismailia',
        '21': 'Giza',
        '22': 'Beni Suef',
        '23': 'Faiyum',
        '24': 'Minya',
        '25': 'Asyut',
        '26': 'Sohag',
        '27': 'Qena',
        '28': 'Aswan',
        '29': 'Luxor',
        '31': 'Red Sea',
        '32': 'New Valley',
        '33': 'Matrouh',
        '34': 'North Sinai',
        '35': 'South Sinai',
    }

    @staticmethod
    def validate_id(id_number):
        if not id_number.isdigit() or len(id_number) != 14:
            raise ValueError("ID Number Must Be 14 Digits Long.")
    
    @staticmethod
    def extract_birth_date(id_number):
        century_code = id_number[0]
        year = id_number[1:3]
        month = id_number[3:5]
        day = id_number[5:7]

        if century_code == '2':
            birth_year = '19' + year
        elif century_code == '3':
            birth_year = '20' + year
        else:
            raise ValueError("Invalid century code in ID")

        try:
            birth_date = datetime.datetime.strptime(f"{birth_year}-{month}-{day}", "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Invalid date in ID.")
        
        return birth_date

    @staticmethod
    def extract_governorate(id_number):
        governorate_code = id_number[7:9]
        return EgyptianIdParserBase.governorate_map.get(governorate_code, "Unknown Governorate")

    @staticmethod
    def extract_gender(id_number):
        serial_number = int(id_number[9:13])
        return 'Male' if serial_number % 2 != 0 else 'Female'

    @staticmethod
    def calculate_age_components(birth_date):
        today = datetime.date.today()
        years = today.year - birth_date.year
        months = today.month - birth_date.month
        days = today.day - birth_date.day

        if days < 0:
            months -= 1
            days += (birth_date + datetime.timedelta(days=30)).day
        if months < 0:
            months += 12
            years -= 1

        return years, months, days


def main():
    id_number = input("Enter Your ID Number: ")
    
    try:
        #Validate the ID first
        EgyptianIdParserBase.validate_id(id_number)
        
        #Extract data
        birth_date = EgyptianIdParserBase.extract_birth_date(id_number)
        governorate = EgyptianIdParserBase.extract_governorate(id_number)
        gender = EgyptianIdParserBase.extract_gender(id_number)
        years, months, days = EgyptianIdParserBase.calculate_age_components(birth_date)

        #Output the results
        print(f"Birth Date: {birth_date}")
        print(f"Governorate: {governorate}")
        print(f"Gender: {gender}")
        print(f"Age: {years} years, {months} months, {days} days")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
