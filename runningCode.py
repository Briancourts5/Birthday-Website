from flask import Flask, render_template
import mysql.connector
from datetime import date
import mysql.connector

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def loadInformation():
    startDate = date(2023, 6, 29)
    currentDate = date.today()
    position = (currentDate - startDate).days + 1
    # position = position % 100

    mydb = mysql.connector.connect(
        host="localhost",
        user="holly",
        password="Hollyisthebest!",
        database="ElephantFacts"
    )

    cursor = mydb.cursor()

    cursor.execute("SELECT COUNT(ID) FROM facts")
    numberOfElephantFacts = int(cursor.fetchone()[0])
    
    cursor.execute("SELECT COUNT(ID) FROM jokes")
    numberOfJokes = int(cursor.fetchone()[0])

    cursor.execute("SELECT COUNT(ID) FROM pickupLines")
    numberOfPickupLines = int(cursor.fetchone()[0])

    cursor.execute("SELECT COUNT(ID) FROM science")
    numberOfScienceFacts = int(cursor.fetchone()[0])

    cursor.execute("SELECT COUNT(ID) FROM general")
    numberOfGeneralFacts = int(cursor.fetchone()[0])

    cursor.execute("SELECT COUNT(ID) FROM love")
    numberOfLoveTranslations = int(cursor.fetchone()[0])


    elephantIndex = position % numberOfElephantFacts
    if elephantIndex == 0:
        elephantIndex = numberOfElephantFacts
    cursor.execute("SELECT fact FROM facts WHERE id = " + str(elephantIndex))
    elephantFact = cursor.fetchone()
    elephantFact = ["Elephant Fact: ", elephantFact[0]]

    badJokeIndex = position % numberOfJokes
    if badJokeIndex == 0:
        badJokeIndex = numberOfJokes
    cursor.execute("SELECT joke FROM jokes WHERE id = " + str(badJokeIndex))
    badJoke = cursor.fetchone()
    badJoke = ["Joke: ", badJoke[0]]

    pickupLineIndex = position % numberOfPickupLines
    if pickupLineIndex == 0:
        pickupLineIndex = numberOfPickupLines
    cursor.execute("SELECT line FROM pickupLines WHERE id = " + str(pickupLineIndex))
    pickupLine = cursor.fetchone()
    pickupLine = ["Pickup Line: ", pickupLine[0]]

    scienceFactIndex = position % numberOfScienceFacts
    if scienceFactIndex == 0:
        scienceFactIndex = numberOfScienceFacts
    cursor.execute("SELECT fact FROM science WHERE id = " + str(scienceFactIndex))
    scienceFact = cursor.fetchone()
    scienceFact = ["Science Fact: ", scienceFact[0]]

    generalFactIndex = position % numberOfGeneralFacts
    if generalFactIndex == 0:
        generalFactIndex = numberOfGeneralFacts
    cursor.execute("SELECT fact FROM general WHERE id = " + str(generalFactIndex))
    generalFact = cursor.fetchone()
    generalFact = ["General Fact: ", generalFact[0]]

    loveIndex = position % numberOfLoveTranslations
    if loveIndex == 0:
        loveIndex = numberOfLoveTranslations
    cursor.execute("SELECT translation FROM love WHERE id = " + str(loveIndex))
    loveTranslation = cursor.fetchone()
    loveTranslation = ["I Love You: ", loveTranslation[0]]

    elephantPath = "static/elephant" + str(position) + ".jpg"

    return render_template('mainPage.html', elephantFact=elephantFact, badJoke=badJoke, pickupLine=pickupLine, scienceFact=scienceFact, generalFact=generalFact, loveTranslation=loveTranslation, elephantPath=elephantPath)
