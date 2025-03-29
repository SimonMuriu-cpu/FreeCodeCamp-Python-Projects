def add_time(start, duration, starting_day=None):
    # Convert 12-hour time to 24-hour time
    def convert_to_24_hour(time):
        hours, minutes = map(int, time[:-2].split(':'))
        period = time[-2:]
        if period == "PM" and hours != 12:
            hours += 12
        elif period == "AM" and hours == 12:
            hours = 0
        return hours, minutes

    # Convert 24-hour time to 12-hour time
    def convert_to_12_hour(hours, minutes):
        period = "AM"
        if hours >= 12:
            period = "PM"
        if hours == 0:
            hours = 12
        elif hours > 12:
            hours -= 12
        return f"{hours}:{str(minutes).zfill(2)} {period}"

    # Get the day of the week
    def get_day_of_week(current_day, days_later):
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        current_day = current_day.capitalize()
        current_index = days_of_week.index(current_day)
        new_index = (current_index + days_later) % 7
        return days_of_week[new_index]

    # Parse start time
    start_hours, start_minutes = convert_to_24_hour(start)

    # Parse duration time
    duration_hours, duration_minutes = map(int, duration.split(':'))

    # Calculate new time
    new_minutes = start_minutes + duration_minutes
    new_hours = start_hours + duration_hours + (new_minutes // 60)
    new_minutes %= 60
    new_days = new_hours // 24
    new_hours %= 24

    # Convert new time to 12-hour format
    new_time = convert_to_12_hour(new_hours, new_minutes)

    # Prepare the result string
    result = new_time

    if starting_day:
        new_day = get_day_of_week(starting_day, new_days)
        result += f", {new_day}"

    if new_days == 1:
        result += " (next day)"
    elif new_days > 1:
        result += f" ({new_days} days later)"

    return result
print(add_time('3:30 PM', '2:12'))