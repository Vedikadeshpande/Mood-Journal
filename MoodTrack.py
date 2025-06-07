import csv
mood_scale = int(input("Enter your mood on a scale of 1 to 10: "))
date = input("Date in DD-MM-YYYY: ")
note = input("Any notes? ")
with open ('moodtrack.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=" ")
    csv_writer.writerow([date, mood_scale, note])
print("Your mood has been logged!")
if (mood_scale<=4):
    print("I am so sorry you had a bad day. The next day will be better!!")
elif(mood_scale<=6):
    print("Nothing too special? It's okay every new day comes with its own adventures!")
elif(mood_scale<=10):
    print("I am glad you had an amazing day!! The next will be even more better")
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

