import datetime
def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date}")

number_of_days = int(input("Enter number of days to add to the current date: "))
def calculate_future_date():
    future_date = timedelta(days=number_of_days) + datetime.now()
    print(f"Future date: {future_date}")

display_current_datetime()
calculate_future_date()
