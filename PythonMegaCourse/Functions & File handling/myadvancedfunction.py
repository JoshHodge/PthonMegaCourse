def minutes_to_hours(minutes, seconds):
    hours = minutes / 60 + seconds / 3600
    return hours

print(minutes_to_hours(70,7200))
