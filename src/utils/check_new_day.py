import datetime
from utils.constants import current_date,start_date
# Function to check if the day has changed
def check_new_day():
    current_date = datetime.now().date()  # Get the current date
    return current_date != start_date  # Compare with the start date
