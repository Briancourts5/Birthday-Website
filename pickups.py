import mysql.connector

listOfLines = [[1, "When I text you goodnight later, what phone number should I use?"],
               [2, "I seem to have lost my phone number. Can I have yours?"],
               [3, "Roses are red, violets are violet, can I have your number so I can dial it?"],
               [4, "I think there’s something wrong with my phone. Could you try calling it to see if it works?"],
               [5, "I was blinded by your beauty… I’m going to need your name and number for insurance purposes"],
               [6, "On a scale of 1 to America, how free are you tonight?"],
               [7, "I’m learning about important dates in history. Want to be one of them?"],
               [8, "Are you my Appendix? Because I have a funny feeling in my stomach that makes me feel like I should take you out"],
               [9, "Do you like raisins? What about dates?"],
               [10, "B1. Oh, sorry, I thought this was a vending machine because you’re a snack."],
               [11, "If you let me borrow a kiss, I promise I’ll give it right back."],
               [12, "Do you know what my shirt is made of? Girlfriend/boyfriend material."],
               [13, "I’d like to take you to the movies, but they don’t let you bring in your own snacks."],
               [14, "You know what you would look really good in? My arms."],
               [15, "I’ve always thought happiness started with an “H”. Why does mine start with “U”?"],
               [16, "If you were a vegetable, you’d be a “cute-cumber”"],
               [17, "If you were a fruit, you’d be a “fine-apple”"],
               [18, "Let me tie your shoes because I don’t want you falling for anyone else"],
               [19, "If you were a triangle, you’d be acute one!"],
               [20, "Even in zero gravity, I would still fall for you."],
               [21, "Are you a banana? Because I find you a-peeling."],
               [22, "Are there 21 letters in the alphabet? No? Oh, my bad! I forgot URAQT"],
               [23, "My parents have a son that’s interested in you."],
               [24, "If I had a nickel every time I saw someone as good-looking as you, I’d only have five cents"],
               [25, "Are you a campfire? Because you’re hot and I want s’more"],
               [26, "I’m not currently an organ donor, but I’d be happy to give you my heart"],
               [27, "I think you’re suffering from a lack of vitamin me"],
               [28, "I’m not a photographer, but I can definitely picture us together"],
               [29, "You must be tired because you’ve been running through my mind all day"],
               [30, "There’s only one thing I want to change about you and that’s your last name"],
               [31, "I’m really glad I just bought life insurance because when I saw you, my heart stopped"],
               [32, "Do you believe in love at first sight or should I try walking by again?"],
               [33, "Your hand looks heavy. Can I hold it for you?"],
               [34, "Kiss me if I’m wrong but dinosaurs still exist, right?"],
               [35, "You must be made of cheese because you’re looking Gouda tonight!"],
               [36, "You must be a great thief because you stole my heart from across the room!"],
               [37, "Anyone who says Disneyland is the happiest place on earth has clearly never stood next to you!"],
               [38, "Are you a parking ticket? ‘Cause you’ve got “fine” written all over you"],
               [39, "Is Summer over? Because I’m about to “fall” for you!"],
               [40, "Do you know CPR? Because you are taking my breath away!"],
               [41, "Life without you is like a broken pencil – pointless"],
               [42, "Something’s wrong with my eyes because I can’t take them off you"],
               [43, "Do you like buying your clothes on sale? At my place, they’re 100% off!"],
               [44, "Did you know that kissing burns 6.4 calories per minute? Wanna work out with me?"],
               [45, "Normally I press A to pick up an item, but what button do I press to pick you up?"],
               [46, "Is your name Coca-Cola? Because you're soda-licious!"],
               [47, "Do you work at Starbucks? Because I like you a latte!"],
               [48, "Hey, tie your shoes! I don’t want you falling for anyone else."],
               [49, "Are you a camera? Because every time I look at you, I smile."],
               [50, "Your lips look so lonely. Would they like to meet mine?"],
               [51, "Are you a tower? Because Eiffel for you!"],
               [52, "Let’s play a game! The winner gets to date the loser."],
               [53, "Do you like science? Because I've got my ion you."],
               [54, "Do you have a name, or can I call you mine?"],
               [55, "I'll make you dinner if you make me breakfast"],
               [56, "I’ve been wondering, do your lips taste as good as they look?"],
               [57, "If looks could kill, you'd be a weapon of mass destruction."],
               [58, "You know what you would really look beautiful in? My arms."],
               [59, "Hey girl, are you made of beryllium, Gold, and Titanium? Because you look so Be-Au-Ti-Ful to me"],
               [60, "Hey baby, do you happen to be an old carbon sample? Because something tells me that I should date you"],
               [61, "Assuming that Newton’s law of universal gravitation is valid, you should be attracted to me because I am attracted to you"],
               [62, "Are you currently vaporizing from a solid state? I find you very sublime"],
               [63, "Hey girl, I am sure you can travel at speed greater than light. Why else would time stop every time I see you around?"],
               [64, "Theoretically, the multiverse theory states that we would be dating each other in at least one universe. Do you want this to be that specific universe?"],
               [65, "Your refractive index must be greater than 2.42 because your beauty sparkles more than any diamond that I’ve ever seen"],
               [66, "Are you centripetal force? Because you make my world go round"],
               [67, "Copernicus was wrong, you are the center of my universe"],
               [68, "Are you the north magnet? Because I am on the south side and I feel myself being pulled to you."],
               [69, "I wish I were Adenine because then I could get paired with U"],
               [70, "Your name must be Andromeda, ’cause we are destined to collide"],
               [71, "That dress would look even better sweetheart accelerating towards my bedroom floor at 9.8 m/s^2"],
               [72, "We must be subatomic particles, because I feel strong force between us"],
               [73, "Whether you’re measured in Celsius, Fahrenheit, Kelvin, etc., you’ll always be smoking hot to me"],
               [74, "Your presence in my life is like gravitational microlensing, and I can see things I didn’t know existed before"],
               [75, "My love for you is like entropy, it never decreases"],
               [76, "You must be made of uranium and iodine because all I can see is U and I together"],
               [77, "Your body must be made of oxygen and neon because you are the ONe"],
               [78, "Are you a compound of beryllium and barium? Because you’re a total BaBe"],
               [79, "You’re so hot you denature my proteins"],
               [80, "If I had a choice between DNA and RNA, I’d choose RNA because it has U in it"],
               [81, "Do you live on Mars? ‘Cause you look out of this world"],
               [82, "To me, you’re hydrogen because you are my number 1"],
               [83, "You must be a 90-degree angle because to me you look just right"],
               [84, "I know hundreds of Pi digits, but what I really want to know is the 10 digits of your phone number"],
               [85, "Just like the digits of Pi, my love for you has no end"],
               [86, "Are you an earthquake, because you rock my world"],
               [87, "When I'm near you I undergo anaerobic respiration. 'Cause baby, you take my breath away."],
               [88, "We fit together like the sticky ends of recombinant DNA"],
               [89, "You must be the acid to my litmus paper, because every time I meet you I turn bright red"],
               [90, "You must be a magnetic monopole, because all I get from you is attraction"],
               [91, "Let’s flip a coin. Head’s you’re mine, tails I’m yours"],
               [92, "Do you play soccer? Because you look like a keeper"],
               [93, "I must be in a museum, because you truly are a work of art"],
               [94, "I’m not good at holding conversations. Can I hold your hand instead?"],
               [95, "If you were a flower you’d be a damnnnnnn-delion"],
               [96, "Do you work at NASA? Because your beauty is out of this world"],
               [97, "My new favorite numbers are 1 and 4 because I’m the 1 4 you"],
               [98, "Are you a taser? Cause you’re stunning"],
               [99, "I bet you dinner that you won’t give me your number"],
               [100, "I’m no mathematician, but I’m pretty good with numbers. Tell you what, give me yours and watch what I can do with it"]]

mydb = mysql.connector.connect(
  host="localhost",
  user="holly",
  password="Hollyisthebest!",
  database="ElephantFacts"
)

print(mydb)

cursor = mydb.cursor()

# for i in range(len(listOfLines)):
#     sql = "DELETE FROM pickupLines WHERE ID = '" + str(i + 1) + "'"

#     cursor.execute(sql)

#     mydb.commit()

# cursor.execute("SELECT * FROM pickupLines")

# result = cursor.fetchall()

# for row in result:
#     print(row)

cursor.execute("DELETE FROM pickupLines")

sql = "INSERT INTO pickupLines (ID, line) VALUES (%s, %s)"
for val in listOfLines:
    cursor.execute(sql, val)

    mydb.commit()

cursor.execute("SELECT * FROM pickupLines")

result = cursor.fetchall()

for row in result:
    print(row)
