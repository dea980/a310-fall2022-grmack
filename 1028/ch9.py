# Please uncomment code if you use it

# Writing to a document
from pathlib import Path
from re import A

from numpy import str_ 
p = Path("spam.txt")
# p.write_text("Hello world!")
# print(p.read_text())


# Opening with open()
# With absolute path:
# Windows:      helloFile = open('C:\\Users\\your_home_folder\\hello.txt')
# macOS / Linux: helloFile = open('/Users/your_home_folder/hello.txt')
# Relative path:
# doc = open("spam.txt")

# Read a document using doc.read()
# print(doc.read())

# doc.write("Test")
# Traceback (most recent call last):
#   File "/Users/gabrielmack/Desktop/lab/ch9.py", line 18, in <module>
#     doc.write("Test")
# io.UnsupportedOperation: not writable

# ^ This happens because we didn't open with w

doc = open("spam.txt", "w")
# doc.write("\nTest\n")


# Saving variables with shelve
import shelve 
# Saving data to mydata.db 

# shelfFile = shelve.open('mydata')
# my_favorite_animals = ["cats", "dogs"]
# shelfFile["fav_animals"] = my_favorite_animals
# shelfFile.close()

# Reading data from mydata.db
shelfFile = shelve.open('mydata')
favorite_animals = shelfFile["fav_animals"]

# for animal in favorite_animals:
#     print(animal)


# Pretty printing
import pprint 
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]

print(pprint.pformat(cats))

# [
# {'desc': 'chubby', 'name': 'Zophie'}, 
# {'desc': 'fluffy', 'name': 'Pooka'}
# ]

doc.write('cats = ' + pprint.pformat(cats) + '\n')



# Generating random quiz files
import random 

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
capitalsItems = list(capitals.items())

for quizNum in range(35):
    quizPath = "quizzes/capitalquiz" + str(quizNum + 1) + ".txt"
    quizFile = open(quizPath, "w")
    answerKeyFile = open("keys/" + str(quizNum + 1) + ".txt", "w")

    quizFile.write("Name:\n\nDate:\n\nPeriod:\n\n")
    quizFile.write("States Capital Quiz #" + str(quizNum + 1) + "\n\n")

    states = list(capitals.keys())
    random.shuffle(states)
    # States in random order

    for questionNumber in range(50):
        correctAnswer = capitals[states[questionNumber]]
        wrongAnswers = list(capitals.values()) # list of capitals
        del wrongAnswers[wrongAnswers.index(correctAnswer)] # delete correct capital from wrong answers list
        wrongAnswers = random.sample(wrongAnswers, 3) # random sample of 3 (wrong) capitals

        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        quizFile.write(f"{questionNumber + 1}What is the capital of {states[questionNumber]}?\n")
        # Print our potential answers:
        for i in range(4):
            quizFile.write('   %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        
        quizFile.write('\n\n')

        answerKeyFile.write(f"{questionNumber + 1}: {'ABCD'[answerOptions.index(correctAnswer)]}\n")
    quizFile.close()
    answerKeyFile.close()
