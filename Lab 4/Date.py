from datetime import datetime, timedelta

# Get the current date
current_date = datetime.now()

# Subtract five days
new_date = current_date - timedelta(days=5)

# Print the new date
print("Current Date:", current_date.strftime('%Y-%m-%d'))
print("New Date:", new_date.strftime('%Y-%m-%d'))


# 2 = Write a Python program to print yesterday, today, tomorrow.
#Today date
today = datetime.now()

#yesterdays and tomorrows dates
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

#Print the dates
print("Yesterday:", yesterday.strftime('%Y-%m-%d'))
print("Today:", today.strftime('%Y-%m-%d'))
print("Tomorrow:", tomorrow.strftime('%Y-%m-%d'))


# 3 = Write a Python program to drop microseconds from datetime.
#Get the current date
current_datetime = datetime.now()

#Remove microseconds by setting them to 0
new_datetime = current_datetime.replace(microsecond=0)

#Print the original and the new datetime
print("Original datetime:", current_datetime)
print("Datetime without microseconds:", new_datetime)

#4 = Write a Python program to calculate two date difference in seconds
#Define two date strings
date1_str = '2024-06-28 14:30:00'
date2_str = '2024-06-27 12:15:00'

#Convert date strings to datetime objects
date1 = datetime.strptime(date1_str, '%Y-%m-%d %H:%M:%S')
date2 = datetime.strptime(date2_str, '%Y-%m-%d %H:%M:%S')

# Calculate the difference between the two dates
difference = date1 - date2

# Get the difference in seconds
difference_in_seconds = difference.total_seconds()

# Print the difference in seconds
print("Difference in seconds:", difference_in_seconds)
