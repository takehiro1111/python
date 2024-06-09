scores = [10, 20, 30, 20, 40]
tokyo = ("JPY", 36, 140)

name = "Takehiro" "Tanaka"

replaced_string = name.replace("Takehiro", "雄大").replace('Tanaka','田中')
upper_string = name.upper()
print(replaced_string)
print(upper_string)


# birthday = "2011-11-27"
# print(birthday.split('-'))

# birthday = ['2011', '11', '27']
# print('-'.join(birthday))

birthday = [2011, 11, 27]
print('-'.join([str(x) for x in birthday]))
