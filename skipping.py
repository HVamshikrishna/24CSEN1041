raw_data = ["100", "200", "vamshi", "300", "krishna", "400", "1000", "2000"]
clean_sum = 0

for entry in raw_data:
    if not entry.isdigit():
        print(f"Skipping invalid data: '{entry}'")
        continue  
    number = int(entry)
    clean_sum += number

print(f"{clean_sum}")
##output
Skipping invalid data: 'vamshi'
Skipping invalid data: 'krishna'
4000
