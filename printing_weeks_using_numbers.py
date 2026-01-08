def get_day_name(day_num):
    
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    
   
    return days.get(day_num, "Invalid Input! Please enter 1-7.")


try:
    num = int(input("Enter day number (1-7): "))
    print("Day:", get_day_name(num))
except ValueError:
    print("Please enter a valid number.")
  ##output
  Enter day number (1-7): 5
  Day: Friday
