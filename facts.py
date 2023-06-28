import mysql.connector

elephantFacts = [[1, "Elephants are the world's largest land mammal"],
                 [2, "On average, adult males weigh 18000 pounds. Female elephants are smaller, weighing up to 8000 pounds"],
                 [3, "On average, African elephants are about 10 feel tall at the shoulder"],
                 [4, "Asian elephants are slightly smaller than African elephants reaching 9 feet tall and weighing 13000 pounds"],
                 [5, "The largest elephant ever recorded was 13 feet tall and weighted 24000 pounds"],
                 [6, "Male elephants only reach their full size at 35-40 years"],
                 [7, "Elephants can live for up to 60-70 years!"],
                 [8, "The oldest elephant is Vatsala of Panna, who lives in India and is over 100 years old!"],
                 [9, "Adult elephants eat about 220 pounds of food (70000 calories) every day"],
                 [10, "Adult elephants consume 50 gallons of water per day"],
                 [11, "Elephants spend up to 75% of their day, or 12-18 hours, eating"],
                 [12, "Elephants eat grasses, leaves, shrubs, fruits, roots, twigs, branches, and tree bark, depending on the season and their habitat"],
                 [13, "Up to half of the food they eat leaves their body undigested"],
                 [14, "An elephant creates one ton of poop per week"],
                 [15, "Elephant poop is great for the environment. It keeps the soil fertile and helps disperse tree seeds"],
                 [16, "Adult females are pregnant for 22 months"],
                 [17, "Elephants have the longest gestation period of any land animals"],
                 [18, "A baby elephant is called a calf"],
                 [19, "A baby elephant can weigh over 250 pounds"],
                 [20, "A baby elephant can stand within 20 minutes of being born"],
                 [21, "A baby elephant can walk within one hour of being born"],
                 [22, "After two days, young elephants can keep up with the heard. This is a survival technique that allows the elephant to keep moving around to find food and water."],
                 [23, "There are three different species of elephants: The African Savanna Elephant (Bush), the African Forest Elephant, and the Asian Elephant"],
                 [24, "Until recently, African Forest elephants were thought to be a subspecies of the African elephant, but new research discovered that they are actually a separate species entirely"],
                 [25, "African Forest elephants live in the tropical forests on the continent of Africa. They have straighter tusks and more rounded ears than Savannah elephants"],
                 [26, "You can tell the three species of elephants apart by their large ears"],
                 [27, "African elephants have larger ears than the others. Their big ears are shaped like the African continent!"],
                 [28, "Asian elephants have smaller ears that are shaped like the Indian subcontinent"],
                 [29, "Elephants can use their ears as big fans to radiate excess heat away from the body"],
                 [30, "Elephants are the only living animals with long trunks"],
                 [31, "Elephants use their long trunks to suck up water to drink, smell their food, lift food to their mouth to eat, bathe, pick up or touch objects, trumpet warnings, and greet one another"],
                 [32, "Elephants have around 150000 muscles in their trunk. By comparison, a human has just over 600 muscles in the entire body"],
                 [33, "An elephant's trunk is actually a fusion of their nose and upper lip"],
                 [34, "An elephant's trunk is one of the most sensitive organs found in any mammal"],
                 [35, "An elephant's trunk can weigh nearly 300 pounds"],
                 [36, "An elephant's trunk can lift objects nearly twice its size"],
                 [37, "An elephant can use its trunk to pick up a peanut, shell it, blow the shell out, and then eat the nut"],
                 [38, "Elephant trunks can suck up for gallons of water at once then spray it back out again"],
                 [39, "Elephants use their trunks to greet one another, reassure one another, and show affection"],
                 [40, "African elephants have two 'fingers' at the end of their trunks, whereas Asian elephants only have one"],
                 [41, "Elephant tusks are actual giant teeth"],
                 [42, "Their tusks first appear when an elephant is two years old"],
                 [43, "Young elephants get a first set of teeth and tusks that fall out and are replaced with adult tusks"],
                 [44, "Elephant tusks never stop growing! They continue to grow throughout their entire lives"],
                 [45, "Giant tusks are a sign of a very old elephant"],
                 [46, "Elephant tusks can grow up to six feet long and weigh 50 pounds each"],
                 [47, "Elephants have a dominant tusk. THey are either left- or right-tusked, just like you are either right or left-handed"],
                 [48, "The dominant tusk is generally smaller because of wear and tear from frequent use"],
                 [49, "Both male and female African elephants grow tusks, but only male Asian elephants grow them. Female Asian elephants do not have tusks."],
                 [50, "Elephant tusks help them get bark off trees, dig up roots, and defend themselves when fighting"],
                 [51, "Elephant tusks are made of ivory"],
                 [52, "Elephant tusks cannot grow back. Once it is broken, damaged, or removed, it stays that way. Just like human teeth in this way"],
                 [53, "Elephant skin is 2.5 centimeters thick. That's almost one inch!"],
                 [54, "The folds and wrinkles in their skin an retain lots of water, which helps cool them down"],
                 [55, "Elephants take regular dust and mud baths to keep their skin clean"],
                 [56, "Elephants use mud as their very own sunscreen. They throw mud on themselves to protect their skin from the hot, burning sun"],
                 [57, "Elephants can walk very long distances, up to 80 miles in a day"],
                 [58, "Elephants can swim and float in deep water for many hours without stopping"],
                 [59, "When swimming, they use their trunks as a snorkel"],
                 [60, "Elephants are one of the only mammals that can't jump because their legs are too slender to propel their weight upward"],
                 [61, "Elephants can change the landscape around them by digging waterholes and creating footpaths"],
                 [62, "An elephant footprint can also enable a micro-ecosystem that, when filled with water, can provide a home for tadpoles and other organisms"],
                 [63, "Elephants communicate with trumpet calls, some of witch are too low for people to even hear"],
                 [64, "Elephants can 'talk' with their feet. They communicate through vibrations in the ground that travel faster than sound through air. These deep-pitched sounds and vibrations in the ground travel through their feet, up the leg and shoulder bones, and into the middle ear. The elephants use the timing and strength of these signals to determine the sound's direction and threat potential."],
                 [65, "Elephants also use body language, touch, and scent to communicate with each other"],
                 [66, "Female elephants generally stay with their herds for life"],
                 [67, "Males leave the elephant herd between the ages of 12-15"],
                 [68, "Male elephants tend to live in isolation or in small bachelor groups"],
                 [69, "The basic family group has anywhere between 6 and 20 members, including the female matriarch and her calves and grand calves"],
                 [70, "The family group forms a hierarchy based on age and knowledge of safe spaces for food and water"],
                 [71, "Clans with older matriarchs have higher survival rates because they can use their memory of previous dangers and threats to avoid them now"],
                 [72, "Elephants have the largest brain of any land mammal"],
                 [73, "Elephants have an incredible memory. Their temporal lobe (the part of the brain associated with memory) is actually larger and denser than human beings. As they say, 'an elephant never forgets!'"],
                 [74, "Elephants can remember distant watering holes that they visited many years before along their migration route"],
                 [75, "Elephants know every member of their herd and are able to recognize up to 30 companions by sight or smell"],
                 [76, "Elephants can remember other elephant and humans who they met decades earlier"],
                 [77, "Elephants are the only non-human animals to mourn their dead. They perform burial rituals and return to visit graves."],
                 [78, "Elephants also mourn other unfamiliar elephants who have died by stroking carcasses that they pass in the wild"],
                 [79, "It's possible that elephants cry"],
                 [80, "Elephant attacks on human villages often occur after significant poaching events, suggesting deliberate revenge as motive"],
                 [81, "Elephants can recognize 12 distinct tones of music and recreate melodies"],
                 [82, "Elephants show empathy. One elephant refused to set a log down into a hole where a dog was sleeping, and other elephants have consoled injured humans."],
                 [83, "Elephants are one of the few non-human mammals to suffer from post traumatic stress disorder"],
                 [84, "Elephants can create art by carefully choosing and combining different colors and elements"],
                 [85, "Elephants have grasped basic arithmetic, like how much fruit is in a basket after multiple changes"],
                 [86, "Elephants have demonstrated an understanding of syntax and likely have their own language and grammar"],
                 [87, "Elephants can distinguish between human languages. When elephants hear voices of a group they fear, they act defensively."],
                 [88, "Elephants are one of the only mammals that can recognize their reflection in a mirror or water"],
                 [89, "Elephants can use and make tools, such as using plants to scratch places on their bodies that they can't reach"],
                 [90, "In Mount Elgon National Park in Kenya, a group of elephants use their tusks to mine for salt in underground caves. They feel their way around with their trunks and eat the salt by breaking them off with their tusks."],
                 [91, "The Asian elephant has lived alongside humans for over 4000 years"],
                 [92, "In Thailand, the elephant is a national icon. It has a national holiday designated in its honor and elephants can receive a Royal title from the King."],
                 [93, "Elephants hate ants! They avoid them entirely because ants can easily get into their trunk and irritate their sensitive nerve endings."],
                 [94, "Contrary to popular belief, elephants don't actually like peanuts very much!"],
                 [95, "Elephants are endangered because they are being killed by humans for their ivory tusks"],
                 [96, "An estimated 100 African elephants are killed each day by poachers seeking ivory, meat, and body parts"],
                 [97, "Around 90% of African Elephants have been wiped out in the past century"],
                 [98, "There are around 415000 wild African Elephants alive today, and around 45000 Asian Elephants"],
                 [99, "Asian elephants have also declined by about half in the last three generations"],
                 [100, "You can help elephants by not buying items containing ivory, buying elephant-friendly fair tree coffee, making donation to an organization that helps elephants, and adopting an elephant through the World Wildlife Foundation"]]

mydb = mysql.connector.connect(
  host="localhost",
  user="holly",
  password="Hollyisthebest!",
  database="ElephantFacts"
)

print(mydb)

cursor = mydb.cursor()

# for i in range(len(elephantFacts)):
#     sql = "DELETE FROM facts WHERE ID = '" + str(i + 1) + "'"

#     cursor.execute(sql)

#     mydb.commit()

# cursor.execute("SELECT * FROM facts")

# result = cursor.fetchall()

# for row in result:
#     print(row)

cursor.execute("DELETE FROM facts")

sql = "INSERT INTO facts (ID, fact) VALUES (%s, %s)"
for val in elephantFacts:
    cursor.execute(sql, val)

    mydb.commit()

cursor.execute("SELECT * FROM facts")

result = cursor.fetchall()

for row in result:
    print(row)
