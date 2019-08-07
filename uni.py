import datetime
from datetime import timedelta



class Day:
    def __init__(self, day_name, class_time):
        self.day_name = day_name
        self.class_time = timedelta(hours = float(class_time))

    def bed_time(self):
        hrs = input(f"""
You have class on {self.day_name} at {self.class_time}, how many hours of sleep would you like?
        """)
        hrs_sleep = timedelta(hours = float(hrs))
        leway = timedelta(minutes = 15)
        bed_time = self.class_time - hrs_sleep - leway
        print(f"You should be in bed by: {bed_time}")


monday = Day("Monday", 9.5)
tuesday = Day("Tuesday", 6)
wednesday = Day("Wednesday", 7)
thursday = Day("Thursday", 8)
friday = Day("Friday", 6.5)

monday.bed_time()
tuesday.bed_time()
wednesday.bed_time()
thursday.bed_time()
friday.bed_time()
