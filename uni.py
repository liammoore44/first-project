import datetime
from datetime import timedelta

#for first draft assume class begins at 9am every day

class_time = timedelta(hours = 9 )

amount_of_sleep = timedelta(hours = 7, minutes = 30)

bed_time = class_time - amount_of_sleep

print(bed_time)
