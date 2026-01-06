from datetime import datetime, timedelta
import random
from config import SIMULATION_START_DATE, SIMULATION_END_DATE

def get_random_date(start_date_str=SIMULATION_START_DATE, end_date_str=SIMULATION_END_DATE):
    """Generates a random date between start and end."""
    start = datetime.strptime(start_date_str, "%Y-%m-%d")
    end = datetime.strptime(end_date_str, "%Y-%m-%d")
    
    delta = end - start
    random_days = random.randrange(delta.days)
    return (start + timedelta(days=random_days)).date()

def get_timestamp_in_range(start_date, end_date):
    """Generates a random timestamp between two dates."""
    delta = end_date - start_date
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start_date + timedelta(seconds=random_second)

def is_business_day(date_obj):
    """Returns True if date is Mon-Fri."""
    return date_obj.weekday() < 5