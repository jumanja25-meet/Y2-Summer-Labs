import random

temperatures = [random.randint(26, 40) for _ in range(7)]
days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

good_days_count = 0
even_days = []

for i in range(len(temperatures)):
    if temperatures[i] % 2 == 0:
        good_days_count += 1
        even_days.append(days_of_the_week[i])

highest_temp = max(temperatures)
lowest_temp = min(temperatures)
highest_temp_day = days_of_the_week[temperatures.index(highest_temp)]
lowest_temp_day = days_of_the_week[temperatures.index(lowest_temp)]

average_temp = sum(temperatures) / len(temperatures)
above_avg = [temp for temp in temperatures if temp > average_temp]

print("Temperatures for the week:", temperatures)
print("Good days for Shelly:", even_days)
print(f"Highest temperature: {highest_temp} on {highest_temp_day}")
print(f"Lowest temperature: {lowest_temp} on {lowest_temp_day}")
print(f"Average temperature: {average_temp:.2f}")
print("Temperatures above average:", above_avg)
