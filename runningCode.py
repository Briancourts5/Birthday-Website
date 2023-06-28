from flask import Flask, render_template
import mysql.connector
import random
from datetime import date

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def loadInformation():
    # position = random.randint(1, 100)

    startDate = date(2023, 6, 27)
    currentDate = date.today()
    position = (currentDate - startDate).days + 1
    position = position % 100

    mydb = mysql.connector.connect(
        host="localhost",
        user="holly",
        password="Hollyisthebest!",
        database="ElephantFacts"
    )

    cursor = mydb.cursor()

    cursor.execute("SELECT fact FROM facts WHERE id = " + str(position))
    elephantFact = cursor.fetchone()
    elephantFact = ["Elephant Fact:", elephantFact[0]]

    cursor.execute("SELECT joke FROM jokes WHERE id = " + str(position))
    badJoke = cursor.fetchone()
    badJoke = ["Joke:", badJoke[0]]

    cursor.execute("SELECT line FROM pickupLines WHERE id = " + str(position))
    pickupLine = cursor.fetchone()
    pickupLine = ["Pickup Line:", pickupLine[0]]

    cursor.execute("SELECT fact FROM science WHERE id = " + str(position))
    scienceFact = cursor.fetchone()
    scienceFact = ["Science Fact:", scienceFact[0]]

    cursor.execute("SELECT fact FROM general WHERE id = " + str(position))
    generalFact = cursor.fetchone()
    generalFact = ["General Fact:", generalFact[0]]

    cursor.execute("SELECT translation FROM love WHERE id = " + str(position))
    loveTranslation = cursor.fetchone()
    loveTranslation = ["I Love You:", loveTranslation[0]]

    elephantPath = "static/elephant" + str(position) + ".jpg"

    return render_template('mainPage.html', elephantFact=elephantFact, badJoke=badJoke, pickupLine=pickupLine, scienceFact=scienceFact, generalFact=generalFact, loveTranslation=loveTranslation, elephantPath=elephantPath)
