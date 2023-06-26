import mysql.connector

listOfFacts = [[1, "The world’s oldest wooden wheel has been around for more than 5,000 years"],
               [2, "Sudan has more pyramids than any country in the world"],
               [3, "There are parts of Africa in all four hemispheres"],
               [4, "The world’s first animated feature film was made in Argentina"],
               [5, "German chocolate cake was invented in Texas"],
               [6, "The Philippines consists of 7,641 islands"],
               [7, "A one-way trip on the Trans-Siberian Railway involves crossing 3,901 bridges"],
               [8, "There’s enough gold inside Earth to coat the planet"],
               [9, "Cleveland was once the country’s fifth-largest city"],
               [10, "It takes a drop of water 90 days to travel the entire Mississippi River"],
               [11, "People once ate arsenic to improve their skin"],
               [12, "The first person processed at Ellis Island was a 15-year-old girl from Ireland"],
               [13, "Japan has one vending machine for every 40 people"],
               [14, "Lemons float, but limes sink"],
               [15, "McDonald’s once made bubblegum-flavored broccoli"],
               [16, "The first oranges weren’t orange"],
               [17, "A cow-bison hybrid is called a beefalo"],
               [18, "Scotland has 421 words for snow"],
               [19, "Samsung tests phone durability with a butt-shaped robot"],
               [20, "Peanuts aren’t technically nuts"],
               [21, "Armadillo shells are bulletproof"],
               [22, "Firefighters use wetting agents to make water wetter"],
               [23, "The longest English word is 189,819 letters long"],
               [24, "Kleenex tissues were originally intended for gas masks"],
               [25, "Blue whales eat half a million calories in one mouthful"],
               [26, "Most Disney characters wear gloves to keep animation simple"],
               [27, "The man with the world’s deepest voice can make sounds humans can’t hear"],
               [28, "Cows don’t have upper front teeth"],
               [29, "Bananas grow upside down"],
               [30, "There were active volcanoes on the moon when dinosaurs were alive"],
               [31, "Theodore Roosevelt had a pet hyena"],
               [32, "The CIA headquarters has its own Starbucks, but baristas don’t write names on the cups"],
               [33, "Giraffe tongues can be 20 inches long"],
               [34, "The inventor of the microwave appliance received only $2 for his discovery"],
               [35, "The Eiffel Tower can grow more than six inches during the summer"],
               [36, "Frankenstein’s Creature is a vegetarian"],
               [37, "Sloths have more neck bones than giraffes"],
               [38, "Bees can fly higher than Mount Everest"],
               [39, "Cap’n Crunch’s full name is Horatio Magellan Crunch"],
               [40, "Humans have jumped farther than horses in the Olympics"],
               [41, "The Terminator script was sold for $1"],
               [42, "Abraham Lincoln was a bartender"],
               [43, "Beethoven never knew how to multiply or divide"],
               [44, "The word “aquarium” means “watering place for cattle” in Latin"],
               [45, "An employee at Pixar accidentally deleted a sequence of Toy Story 2 during production"],
               [46, "Steve Jobs, Steve Wozniak, and Ron Wayne started Apple Inc. on April Fools’ Day"],
               [47, "The inventor of the tricycle personally delivered two to Queen Victoria"],
               [48, "Your brain synapses shrink while you sleep"],
               [49, "A waffle iron inspired one of the first pairs of Nikes"],
               [50, "Baseball umpires used to sit in rocking chairs"],
               [51, "The first commercial passenger flight lasted only 23 minutes"],
               [52, "The world’s first novel ends mid-sentence"],
               [53, "The French-language Scrabble World Champion doesn’t speak French"],
               [54, "The British Empire was the largest empire in world history"],
               [55, "Penicillin was first called “mold juice”"],
               [56, "The first stroller was engineered to be pulled by a goat (or animal of similar size)"],
               [57, "Neil Armstrong’s hair was sold in 2004 for $3,000"],
               [58, "Pregnancy tests date back to 1350 B.C.E."],
               [59, "Martin Luther King Jr. got a C in public speaking"],
               [60, "Bees can make colored honey"],
               [61, "Bananas glow blue under black lights"],
               [62, "The Pope can’t be an organ donor"],
               [63, "Red is the first color a baby sees"],
               [64, "Disneyland serves 2.8 million churros a year"],
               [65, "A lit candle creates 1 million tiny diamonds per second"],
               [66, "Flowers grow faster with music"],
               [67, "Mr. Potato Head was the first toy to be advertised on TV"],
               [68, "Camels have three eyelids"],
               [69, "Mosquitoes are attracted to people who just ate bananas"],
               [70, "Sonic the Hedgehog’s full name is Ogilvie Maurice Hedgehog"],
               [71, "The world’s termites outweigh the world’s humans about 10 to 1"],
               [72, "Most toilet paper solid in France is pink"],
               [73, "The human nose can remember 50,000 different scents"],
               [74, "Sliced bread was invented a year after the invention of TV"],
               [75, "If you keep a goldfish in a dark room, it will eventually turn white"],
               [76, "Bullfrogs do not sleep"],
               [77, "It took the creator of the Rubik’s Cube one month to solve the cube after he created it"],
               [78, "An ant’s sense of smell is stronger than a dog’s"],
               [79, "Alligators will give manatees the right of way if they are swimming near each other"],
               [80, "Sunsets on Mars are blue"],
               [81, "A one-day weather forecast requires about 10 billion math calculations"],
               [82, "People don’t sneeze in their sleep due to their brain shutting down the reflex"],
               [83, "The average American will eat 35,000 cookies in their lifetime"],
               [84, "Smelling apples or bananas can help you lose weight"],
               [85, "The hummingbird is the only bird that can fly backward"],
               [86, "Beavers were once the size of bears"],
               [87, "A pigeon’s feathers weigh more than their bones"],
               [88, "The spiked dog collar was invented by the ancient Greeks to protect their dogs from wolf attacks"],
               [89, "During World War II, Germany planned to collapse the British economy by dropping millions of counterfeit bills over London"],
               [90, "The youngest pope in history was Pope Benedict IX. He is also the only person to have been the pope more than once"],
               [91, "There is a town in Nebraska called Monowi with a population of one. The only resident is a woman who serves as mayor, bartender, and librarian."],
               [92, "The unique smell of rain actually comes from plant oils, bacteria, and ozone"],
               [93, "In 2016, Domino’s tested pizza delivery via reindeer in Japan"],
               [94, "Helen Keller is related to Robert E. Lee—her paternal grandfather was his second cousin"],
               [95, "Starfish don’t have blood. They circulate nutrients by using seawater in their vascular system"],
               [96, "Bubble wrap was originally invented to be a kind of plastic wallpaper"],
               [97, "Gummy bears were originally called 'dancing bears'"],
               [98, "Laughter synchronizes the brains of both speaker and listener so that they become emotionally attuned"],
               [99, "An oak tree produces about 10 million acorns during its lifetime"],
               [100, "There's enough concrete in the Hoover Dam to build a two-lane highway from San Francisco to New York City"]]

mydb = mysql.connector.connect(
  host="localhost",
  user="holly",
  password="Hollyisthebest!",
  database="ElephantFacts"
)

print(mydb)

cursor = mydb.cursor()

for i in range(len(listOfFacts)):
    sql = "DELETE FROM general WHERE ID = '" + str(i + 1) + "'"

    cursor.execute(sql)

    mydb.commit()

cursor.execute("SELECT * FROM general")

result = cursor.fetchall()

for row in result:
    print(row)

sql = "INSERT INTO general (ID, fact) VALUES (%s, %s)"
for val in listOfFacts:
    cursor.execute(sql, val)

    mydb.commit()

cursor.execute("SELECT * FROM general")

result = cursor.fetchall()

for row in result:
    print(row)
