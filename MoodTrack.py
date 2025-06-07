import csv
mood_scale = int(input("Enter your mood on a scale of 1 to 10: "))
date = input("Date in DD-MM-YYYY: ")
note = input("Any notes? ")
with open ('moodtrack.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=" ")
    csv_writer.writerow([date, mood_scale, note])
print("YOur mood has been logged!")
if (mood_scale<=4):
    print("Im so sorry you had a bad day. The next day will be better!! <3")
elif(mood_scale<=7):
    print("Nothing too special? Its okay every new day comes with its own advetures!")
elif(mood_scale<=10):
    print("Im glad you had an amazing day!! The next will be even better")
else:
    print("Invalid Input")
pulltherecords = input("Do you want to pull the records? (Y or N)")
match pulltherecords:
    case "Y":
        with open('moodtrack.csv', mode='r') as records:
            csv_reader = csv.reader(records)
            for row in records:
                print(row)
    case "N":
        print("Okay! Have a good day!")

