
def military_time(date):
    if "PM" in date:
        date_section = date[2:8]
        number = int(date[0:2])
        new_number = number + 12
        new_number = str(new_number)
        military = new_number + date_section
        print(military)
    else:
        if "12:00:00AM" in date:          # falta el caso  para el rango entre 12:00 am a 1:00am
            print("00:00:00")
        else:
            new_date = date.replace("AM", "")
            print(new_date)

        
military_time("05:00:12PM")
military_time("07:00:12AM")
military_time("12:00:00AM")
