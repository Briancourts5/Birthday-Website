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

    cursor.execute("SELECT fact FROM facts WHERE id = " + str(position % numberOfElephantFacts))
    elephantFact = cursor.fetchone()
    elephantFact = ["Elephant Fact: ", elephantFact[0]]

    cursor.execute("SELECT joke FROM jokes WHERE id = " + str(position % numberOfJokes))
    badJoke = cursor.fetchone()
    badJoke = ["Joke: ", badJoke[0]]

    cursor.execute("SELECT line FROM pickupLines WHERE id = " + str(position % numberOfPickupLines))
    pickupLine = cursor.fetchone()
    pickupLine = ["Pickup Line: ", pickupLine[0]]

    cursor.execute("SELECT fact FROM science WHERE id = " + str(position % numberOfScienceFacts))
    scienceFact = cursor.fetchone()
    scienceFact = ["Science Fact: ", scienceFact[0]]

    cursor.execute("SELECT fact FROM general WHERE id = " + str(position % numberOfGeneralFacts))
    generalFact = cursor.fetchone()
    generalFact = ["General Fact: ", generalFact[0]]

    cursor.execute("SELECT translation FROM love WHERE id = " + str(position % numberOfLoveTranslations))
    loveTranslation = cursor.fetchone()
    loveTranslation = ["I Love You: ", loveTranslation[0]]

    elephantPath = "static/elephant" + str(position) + ".jpg"

    return render_template('mainPage.html', elephantFact=elephantFact, badJoke=badJoke, pickupLine=pickupLine, scienceFact=scienceFact, generalFact=generalFact, loveTranslation=loveTranslation, elephantPath=elephantPath)
