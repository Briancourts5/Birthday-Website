import mysql.connector

listOfFacts = [[1, "Neptune's moon, Triton, orbits the planet backwards. It's the only large moon in our solar system that does this."],
               [2, "10 percent of all human beings ever born are alive at this very moment."],
               [3, "The Earth spins at 1,000 mph but it travels through space at an incredible 67,000 mph."],
               [4, "Every year over one million earthquakes shake the Earth."],
               [5, "When Krakatoa erupted in 1883, its force was so great it could be heard 4,800 kilometres away in Australia."],
               [6, "Every second around 100 lightning bolts strike the Earth."],
               [7, "In October 1999 an Iceberg the size of London broke free from the Antarctic ice shelf ."],
               [8, "If you could drive your car straight up you would arrive in space in just over an hour."],
               [9, "The dinosaurs became extinct before the Rockies or the Alps were formed."],
               [10, "When a flea jumps, the rate of acceleration is 20 times that of the space shuttle during launch."],
               [11, "If our Sun were just inch in diameter, the nearest star would be 445 miles away."],
               [12, "The Australian billygoat plum contains 100 times more vitamin C than an orange."],
               [13, "Astronauts cannot belch – there is no gravity to separate liquid from gas in their stomachs."],
               [14, "The air at the summit of Mount Everest, 29,029 feet is only a third as thick as the air at sea level."],
               [15, "One million, million, million, million, millionth of a second after the Big Bang the Universe was the size of a …pea."],
               [16, "DNA was first discovered in 1869 by Swiss Friedrich Mieschler."],
               [17, "The first synthetic human chromosome was constructed by US scientists in 1997."],
               [18, "The thermometer was invented in 1607 by Galileo."],
               [19, "Englishman Roger Bacon invented the magnifying glass in 1250."],
               [20, "Alfred Nobel (whom the Nobel Prizes are named for) invented dynamite in 1866."],
               [21, "Wilhelm Rontgen won the first Nobel Prize for physics for discovering X-rays in 1895."],
               [22, "The tallest tree ever was an Australian eucalyptus – In 1872 it was measured at 435 feet tall."],
               [23, "Christian Barnard performed the first heart transplant in 1967 – the patient lived for 18 days."],
               [24, "The wingspan of a Boeing 747 is longer than the Wright brother’s first flight."],
               [25, "An electric eel can produce a shock of up to 650 volts."],
               [26, "The earliest wine makers lived in Egypt around 2300 BC."],
               [27, "Giraffes often sleep for only 20 minutes in any 24 hours. They may sleep up to 2 hours (in spurts – not all at once), but this is rare. They never lie down."],
               [28, "Without its lining of mucus your stomach would digest itself."],
               [29, "Humans have 46 chromosomes, peas have 14 and crayfish have 200."],
               [30, "There are 60,000 miles of blood vessels in the human body."],
               [31, "An individual blood cell takes about 60 seconds to make a complete circuit of the body."],
               [32, "On the day that Alexander Graham Bell was buried the entire US telephone system was shut down for 1 minute in tribute."],
               [33, "The low frequency call of the humpback whale is the loudest noise made by a living creature."],
               [34, "A quarter of the world’s plants are threatened with extinction by the year 2010."],
               [35, "Each person sheds 40lbs of skin in his or her lifetime."],
               [36, "At 15 inches the eyes of giant squids are the largest on the planet."],
               [37, "More germs are transferred shaking hands than kissing."],
               [38, "The longest glacier in Antarctica, the Almbert glacier, is 250 miles long and 40 miles wide."],
               [39, "The fastest speed a falling raindrop can hit you is 18mph."],
               [40, "A healthy person has 6,000 million, million, million haemoglobin molecules."],
               [41, "The world’s smallest winged insect, the Tanzanian parasitic wasp, is smaller than the eye of a housefly."],
               [42, "If the Sun were the size of a beach ball then Jupiter would be the size of a golf ball and the Earth would be as small as a pea."],
               [43, "It would take over an hour for a heavy object to sink 6.7 miles down to the deepest part of the ocean."],
               [44, "There are more living organisms on the skin of each human than there are humans on the surface of the earth."],
               [45, "The grey whale migrates 12,500 miles from the Artic to Mexico and back every year."],
               [46, "Each rubber molecule is made of 65,000 individual atoms."],
               [47, "Around a million, billion neutrinos from the Sun will pass through your body while you read this sentence."],
               [48, "Quasars emit more energy than 100 giant galaxies."],
               [49, "The saturn V rocket which carried man to the Moon develops power equivalent to fifty 747 jumbo jets."],
               [50, "Koalas sleep an average of 22 hours a day, two hours more than the sloth."],
               [51, "Neutron stars are so dense that a teaspoonful would weigh more than all the people on Earth."],
               [52, "Every hour the Universe expands by a billion miles in all directions."],
               [53, "Somewhere in the flicker of a badly tuned TV set is the background radiation from the Big Bang."],
               [54, "At over 2000 kilometres long The Great Barrier Reef is the largest living structure on Earth."],
               [55, "A thimbleful of a neutron star would weigh over 100 million tons."],
               [56, "The risk of being struck by a falling meteorite for a human is one occurence every 9,300 years."],
               [57, "The driest inhabited place in the world is Aswan, Egypt where the annual average rainfall is .02 inches."],
               [58, "The deepest part of any ocean in the world is the Mariana trench in the Pacific with a depth of 35,797 feet."],
               [59, "he largest meteorite craters in the world are in Sudbury, Ontario, canada and in Vredefort, South Africa."],
               [60, "The largest desert in the world, the Sahara, is 3,500,000 square miles."],
               [61, "The largest dinosaur ever discovered was Seismosaurus who was over 100 feet long and weighed up to 80 tonnes."],
               [62, "A typical hurricane produces the nergy equivalent to 8,000 one megaton bombs."],
               [63, "To escape the Earth’s gravity a rocket need to travel at 7 miles a second."],
               [64, "If every star in the Milky Way was a grain of salt they would fill an Olympic sized swimming pool."],
               [65, "Microbial life can survive on the cooling rods of a nuclear reactor."],
               [66, "Our oldest radio broadcasts of the 1930s have already travelled past 100,000 stars."],
               [67, "The human eye has a 576-megapixel resolution."],
               [68, "Feldspar is the most common mineral on Earth."],
               [69, "Hot water freezes more quickly than cold water."],
               [70, "It takes 6 minutes for brain cells to react to alcohol."],
               [71, "Most dinosaurs are known from just a single tooth or bone."],
               [72, "Nuclear power plants are safer work environments compared to offices."],
               [73, "50% of museum items are mislabeled."],
               [74, "The biggest tsunami reached over 1000 feet."],
               [75, "Oxygen isn’t colorless, rather solid and liquid oxygen have a pale blue color."],
               [76, "The hottest planet in our solar system is Venus."],
               [77, "The DNA in a person’s body, when uncoiled, can stretch from Pluto to the Sun and back."],
               [78, "There are more trees on the planet than stars in the solar system."],
               [79, "Hawaii moves closer to Alaska every year."],
               [80, "The average human body carries ten times more bacterial cells than human cells."],
               [81, "It takes a photon up to 40,000 years to travel from the core of the sun to its surface."],
               [82, "There are 8 times as many atoms in a teaspoonful of water as the."],
               [83, "In an entire lifetime, the average person walks the equivalent of five times around the world."],
               [84, "There are actually over two dozen states of matter!"],
               [85, "Killer whales are actually dolphins."],
               [86, "Grasshoppers have ears in their bellies."],
               [87, "You can't taste food without saliva."],
               [88, "Octopuses have three hearts, nine brains, and blue blood."],
               [89, "About 1% of our genes come from plants, fungi, and other germs."],
               [90, "The human brain can store as much information as the entire Internet."],
               [91, "The tallest mountain in the solar system is Olympus Mons on Mars."],
               [92, "Our planet is home to around 8.7 million different species."],
               [93, "Every second, the sun emits more energy than humanity has used since the dawn of civilization."],
               [94, "The longest-living cells in the body are neurons, which can live as long as your lifespan."],
               [95, "There are ice caves in Iceland that have hot springs."],
               [96, "A bolt of lightning is five times hotter than the sun."],
               [97, "Ham the Astrochimp was the first hominid in space, launched on Jan. 31, 1961."],
               [98, "Earwax is a type of sweat."],
               [99, "Your nose and ears never stop growing."],
               [100, "The average brain weighs about three pounds. A newborn brain weighs about 3/4 of a pound."]]

mydb = mysql.connector.connect(
  host="localhost",
  user="holly",
  password="Hollyisthebest!",
  database="ElephantFacts"
)

print(mydb)

cursor = mydb.cursor()

for i in range(len(listOfFacts)):
    sql = "DELETE FROM science WHERE ID = '" + str(i + 1) + "'"

    cursor.execute(sql)

    mydb.commit()

print(cursor.rowcount, "record deleted.")

cursor.execute("SELECT * FROM science")

result = cursor.fetchall()

for row in result:
    print(row)

sql = "INSERT INTO science (ID, fact) VALUES (%s, %s)"
for val in listOfFacts:
    # val = ("1", "Elephants are the world’s largest land mammal")
    cursor.execute(sql, val)

    mydb.commit()

print(cursor.rowcount, "record inserted.")

cursor.execute("SELECT * FROM science")

result = cursor.fetchall()

for row in result:
    print(row)
