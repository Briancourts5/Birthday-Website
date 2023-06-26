import mysql.connector

listOfJokes = [[1, "Why don't oysters donate to charity? Because they're shellfish"],
               [2, "What does a baby computer call its father? Data"],
               [3, "What did the custodian say when he jumped out of the closet? \"Supplies!\""],
               [4, "Why are colds bad criminals? Because they're easy to catch"],
               [5, "How does a penguin build its house? Igloos it together"],
               [6, "Which knight invented King Arthur's Round Table? Sir Cumference"],
               [7, "What do sprinters eat before a race? Nothing. They fast"],
               [8, "What do you call a fly without wings? A walk!"],
               [9, "What happens when you witness a ship wreck? You let it sink in"],
               [10, "What does a clock do when it's hungry? It goes back four seconds"],
               [11, "What do you call a belt made of watches? A waist of time!"],
               [12, "What's the best way to carve wood? Whittle by whittle"],
               [13, "What did the teacher do with the student's report on cheese? She grated it"],
               [14, "What's the difference between a piano and a fish? You can tune a piano, but you can't tuna fish"],
               [15, "What did the pirate say on his 80th birthday? \"Aye, matey!\""],
               [16, "How do you organize an astronomer's party? You planet"],
               [17, "What's the action like at a circus? In-tents"],
               [18, "Why did the scarecrow get promoted? Because he was outstanding in his field"],
               [19, "What do you call a pony with a sore throat? A little hoarse"],
               [20, "What do you call a fish with no eye? Fsh"],
               [21, "What kind of car does an egg drive? A Yolkswagen"],
               [22, "What do you call a factory that sells generally decent goods? A satisfactory"],
               [23, "Why should you never eat a clock? Because it's too time-consuming"],
               [24, "What should a sick bird do? Get tweetment"],
               [25, "I want a job cleaning mirrors. It's something I can really see myself doing"],
               [26, "What grades did the pirate get on his report card? Seven Cs"],
               [27, "How do you make a tissue dance? Put a little boogie in it"],
               [28, "Did you hear about the mediocre restaurant on the moon? It has great food but no atmosphere"],
               [29, "What kinds of pictures do hermit crabs take? Shellfies"],
               [30, "What do you call a person with a briefcase in a tree? A branch manager"],
               [31, "Why did the baby cookie cry? Because its mother was a wafer so long"],
               [32, "When is a door not really a door? When it's really ajar"],
               [33, "Did you hear about the claustrophobic astronaut? Poor guy really needed some space"],
               [34, "Why did the coffee call the police? It got mugged!"],
               [35, "Why did Cyclops close his school? He only had one pupil"],
               [36, "Where do skunks pray? In pews"],
               [37, "If you're American when you come out of the bathroom, what are you when you're in the bathroom? European."],
               [38, "Why do birds fly south for the winter? Because it's too far to walk"],
               [39, "What was the mummy's favorite type of music? Wrap"],
               [40, "I'm only familiar with 25 letters of the alphabet. I don't know why"],
               [41, "Did you hear about the beautiful wedding? Even the cake was in tiers"],
               [42, "Why are there fences are cemeteries? Because everyone's always dying to get in"],
               [43, "What did one wall say to the other? \"Meet me at the corner!\""],
               [44, "What do you call a large African mammal with long hair and sandals? A hippie-potamus"],
               [45, "What's the award for being the best dentist? A plaque"],
               [46, "Why can't you hear a pterodactyl go to the bathroom? Because the P is silent"],
               [47, "I bought sneakers from a drug dealer. I don't know what he laced them with but I've been tripping all day!"],
               [48, "Why did Mozart hate chickens? Because when he asked them for their favorite composer, they said, \"Bach! Bach! Bach!\""],
               [49, "Why did the toilet paper roll downhill? To get to the bottom"],
               [50, "What's the best name for a man who can't stand? Neil"],
               [51, "Why are groups of fish so smart? Because they travel in schools"],
               [52, "How much does the heaviest skeleton weigh? A skele-TON"],
               [53, "What did the drummer name her twin daughters? Anna One, Anna Two"],
               [54, "What's big, gray and doesn't matter? An irrelephant"],
               [55, "Why did the snowman pick through a bag of carrots? Because he was picking his nose"],
               [56, "Why does Waldo only wear stripes? Because he doesn't want to be spotted"],
               [57, "I witnessed an attempted murder earlier—fortunately only one crow showed up!"],
               [58, "How do you catch a bra? With a booby trap"],
               [59, "What do clouds wear under their shorts? Thunderpants"],
               [60, "Did you hear about the guy who won the award for best knock knock joke? He won the no bell prize"],
               [61, "Why did Cinderella get kicked off of the soccer team? Because she kept running from the ball!"],
               [62, "Did you hear the one about the three watering holes in the ground? Well, well, well..."],
               [63, "What did the socks say to the pants? \"Sup britches?!\""],
               [64, "What shivers at the bottom of the ocean? A nervous wreck"],
               [65, "What's a ninja's favorite type of shoes? Sneakers!"],
               [66, "I have the world's worst thesaurus. Not only is it terrible, it's also terrible"],
               [67, "Why did the invisible man turn down a job offer? He couldn't see himself doing it"],
               [68, "What kind of music do windmills like? They're metal fans"],
               [69, "I'd tell you the joke about perforated paper, but it's tear-able"],
               [70, "What do you call a canine magician? A labracadabrador"],
               [71, "Why do seagulls fly over the sea? Because if they flew over the bay, they'd be called bagels"],
               [72, "What do you call Samsung's security team? The Guardians of the Galaxy!"],
               [73, "I sold my vacuum yesterday. It was just collecting dust"],
               [74, "Why did the golfer need new pants? Because he got a hole in one"],
               [75, "Why did the man get fired from the calendar factory? Because he took a few days off"],
               [76, "What do you call an alligator wearing a vest? An investigator"],
               [77, "How do snails fight? They slug it out"],
               [78, "What did the left butt cheek say to the right butt cheek? \"You crack me up!\""],
               [79, "What sound does a nut make when it sneezes? Cashew!"],
               [80, "Did you hear about the satellites' wedding? The ceremony was OK, but the reception was terrific"],
               [81, "What did the Atlantic Ocean say to the Pacific Ocean? Nothing, it just waved"],
               [82, "What did the fish say when it swam into the wall? \"Dam!\""],
               [83, "Which school supply is king? The ruler"],
               [84, "What do you get when you cross a vampire with a snowman? Frostbite"],
               [85, "What's green and sings? Elvis Parsley"],
               [86, "How do you make holy water? You boil the hell out of it"],
               [87, "A jumper cable walks into a bar. The bartender says, \"I'll serve you, but don't start anything.\""],
               [88, "Why can't a hand be 12 inches long? Because then it'd be a foot"],
               [89, "What's the difference between a dapper man on a bicycle and a poorly dressed man on a unicycle? Attire!"],
               [90, "The past, the present and the future walked into a bar. It was tense"],
               [91, "What does a nosy pepper do? It gets jalapeno business!"],
               [92, "Why do ghosts love elevators? Because they lift their spirits"],
               [93, "What do you call a snobby criminal going downstairs? A condescending con descending"],
               [94, "How do prisoners communicate with one another? Cell phones"],
               [95, "How many bugs do you need to rent out an apartment? Ten-ants"],
               [96, "You know why they called it \"the dark ages?\" There were too many knights"],
               [97, "What's the loudest kind of pet you can get? A trumpet"],
               [98, "Why shouldn't you make a dad joke if you're not a dad? Because it's a faux pa"],
               [99, "What's the derivative of Amazon? Amazon Prime"],
               [100, "Why couldn't the pirate sit down? His booty got stolen!"]]

mydb = mysql.connector.connect(
  host="localhost",
  user="holly",
  password="Hollyisthebest!",
  database="ElephantFacts"
)

print(mydb)

cursor = mydb.cursor()

for i in range(len(listOfJokes)):
    sql = "DELETE FROM jokes WHERE ID = '" + str(i + 1) + "'"

    cursor.execute(sql)

    mydb.commit()

cursor.execute("SELECT * FROM jokes")

result = cursor.fetchall()

for row in result:
    print(row)

sql = "INSERT INTO jokes (ID, joke) VALUES (%s, %s)"
for val in listOfJokes:
    cursor.execute(sql, val)

    mydb.commit()

cursor.execute("SELECT * FROM jokes")

result = cursor.fetchall()

for row in result:
    print(row)
