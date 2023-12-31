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
               [100, "Why couldn't the pirate sit down? His booty got stolen!"],
               [101, 'How many telemarketers does it take to change a light bulb? Only one, but he has to do it while you are eating dinner.'],
               [102, 'Today, my son asked, “Can I have a bookmark?” I burst into tears—11 years old and he still doesn’t know my name is Brian.'],
               [103, 'I don’t trust stairs. They are always up to something.'],
               [104, 'Why didn’t Han Solo enjoy his steak dinner? It was Chewie.'],
               [105, 'Why don’t pirates take a bath before they walk the plank? They just wash up on shore.'],
               [106, 'Did you hear about the racing snail who got rid of his shell? He thought it would make him faster, but it just made him sluggish.'],
               [107, 'A turtle is crossing the road when he’s mugged by two snails. When the police ask him what happened, the shaken turtle replies, “I don’t know. It all happened so fast.”'],
               [108, 'Did you hear about the guy who froze to death at the drive-in? He went to see Closed for the Winter.'],
               [109, 'When does a joke become a “dad joke”? When it becomes apparent.'],
               [110, 'What invention allows us to see through walls? Windows.'],
               [111, 'I know a bunch of good jokes about umbrellas, but they usually go over people’s heads.'],
               [112, 'How many narcissists does it take to screw in a light bulb? One. The narcissist holds the light bulb while the rest of the world revolves around him.'],
               [113, 'The bank keeps calling me to give me compliments. They say I have an “outstanding balance.”'],
               [114, 'What is the most popular fish in the ocean? A starfish.'],
               [115, 'What did one plate say to another plate? Tonight, dinner’s on me.'],
               [116, 'Did you hear about the surgeon who enjoyed performing quick surgeries on insects? He did one on the fly.'],
               [117, 'What’s a vampire’s favorite ship? A blood vessel.'],
               [118, 'There’s only one thing I can’t deal with, and that’s a deck of cards glued together.'],
               [119, 'The past, the present, and the future walked into a bar. It was tense.'],
               [120, 'What’s the least-spoken language in the world? Sign language.'],
               [121, 'What do you call a hippie’s wife? Mississippi.'],
               [122, 'Why did the people stop supporting the crab running for mayor? Turns out he was just promoting his own shelffish interests.'],
               [123, 'Did you hear about the bankrupt poet? He ode everyone'],
               [124, 'What did the evil chicken lay? Deviled eggs.'],
               [125, 'Did you hear they arrested the devil? Yeah, they got him on possession.'],
               [126, 'A friend of mine didn’t pay his exorcist. He got repossessed.'],
               [127, 'Did you hear about the sheperd who drove his sheep through town? He was given a ticked for making a ewe turn'],
               [128, 'How do you make holy water? You boil the hell out of it.'],
               [129, 'What sound does a witch’s car make? Broom broom!'],
               [130, 'I want to go on record that I support farming. As a matter of fact, you could call me protractor.'],
               [131, 'Did you hear about the cat who ate the ball of yarn? She had mittens'],
               [132, 'What’s the best way to watch a fly-fishing tournament? Live stream.'],
               [133, 'How do you tell the difference between an alligator and a crocodile? You will see one later and one in a while.'],
               [134, 'Why did the man name his dogs Rolex and Timex? Because they were watchdogs.'],
               [135, 'What do you call a dog that can do magic? A Labracabrador.'],
               [136, 'Did you hear about the clausterphobic astronaut? He just wanted a little more space'],
               [137, 'Why do dogs float in water? Because they are good buoys.'],
               [138, 'Why do cows wear bells? Because their horns don’t work.'],
               [139, 'What do you call a fish with no eye? A fsh.'],
               [140, 'Police arrested a bottle of water because it was wanted in three different states: solid, liquid, and gas.'],
               [141, 'What do you call a lazy kangaroo? Pouch potato.'],
               [142, 'Why is grass so dangerous? Because it’s full of blades.'],
               [143, 'What is the Easter bunny’s favorite type of music? Hip-hop.'],
               [144, 'A friend of mine is known for sweeping girls off their feet. He’s an extremely aggressive janitor.'],
               [145, 'I’m an expert at picking leaves and heating them in water. It’s my special tea.'],
               [146, 'My son’s fourth birthday was today. When he came to see me, I didn’t recognize him at first. I had never seen him be four.'],
               [147, 'I recently went to the “World’s Tiniest Wind Turbine” exhibit. Honestly, not a big fan.'],
               [148, 'I was out on a walk when I saw a sign that said, “Man wanted for robbery.” So I went in and applied for the job.'],
               [149, 'How long should socks be? Twelve inches, so you can fit in one foot.'],
               [150, 'A bartender broke up with her boyfriend, but he kept asking her for another shot.'],
               [151, 'My doctor told me I’ve really grown as a person. Well, her exact words were that I “gained excess weight.”'],
               [152, 'Scientists have discovered what is believed to be the world’s largest bedsheet. More on this story as it unfolds.'],
               [153, '3.14 percent of sailors are pi-rates.'],
               [154, 'You can’t plant flowers if you haven’t botany.'],
               [155, 'What did the French chef give his wife for Valentine’s Day? A hug and a quiche.'],
               [156, 'Why did Beethoven get rid of his chickens? All they said was, “Bach, Bach, Bach…”'],
               [157, 'What did one DNA say to the other DNA? “Do these genes make me look fat?”'],
               [158, 'What do you need to make a small fortune on Wall Street? A large fortune.'],
               [159, 'How does the man in the moon get his hair cut? Eclipse it.'],
               [160, 'Did you hear about the restaurant on the moon? Great food, no atmosphere.'],
               [161, 'Did you hear the one about the kid who started a business tying shoelaces on the playground? It was a knot-for-profit.'],
               [162, 'My kid wants to invent a pencil with an eraser on each end, but I just don’t see the point.'],
               [163, 'Why should you never mention the number 288? It’s two gross.'],
               [164, 'I spent a lot of time, money, and effort childproofing my house, but the kids still get in.'],
               [165, 'A cheese factory exploded in France. Da brie is everywhere!'],
               [166, 'Did you hear the rumor about butter? Well, I’m not going to spread it!'],
               [167, 'Why do melons have weddings? Because they cantaloupe.'],
               [168, 'What do Bostonians call a fake noodle? An impasta.'],
               [169, 'What does a mobster buried in cement soon become? A hardened criminal.'],
               [170, 'What does “idk” stand for? Everyone I ask says, “I don’t know.”'],
               [171, 'Why was the pig covered in ink? Because it lived in a pen.'],
               [172, 'Did you hear about the guy who stole 50 cartons of hand sanitizer? They couldn’t prosecute—his hands were clean.'],
               [173, 'What do you call a snitching scientist? A lab rat.'],
               [174, 'What’s the difference between a man wearing pajamas on a bicycle and a guy wearing a tuxedo on a unicycle? Attire.'],
               [175, 'It’s a shame that the Beatles didn’t make the submarine in that song green. That would’ve been sublime.'],
               [176, 'Did you hear about the aquatic sea mammals that escaped from the zoo? It was otter chaos.'],
               [177, 'Why do nurses like red crayons? Sometimes they have to draw blood.'],
               [178, 'How much do I love crunchy tacos? From my head tomatoes.'],
               [179, 'What kind of spells do leprechauns use? Lucky Charms.'],
               [180, 'What do you call a bear with no teeth? A gummy bear.'],
               [181, 'My IQ test results came back. They were negative.'],
               [182, 'My wife asked me to sync her phone, so I threw it into the ocean.'],
               [183, 'My wife is really mad that I have no sense of direction. I packed up my stuff and right.'],
               [184, 'What did one cannibal say to the other while they were eating a clown? Does this taste funny to you?'],
               [185, 'Do I enjoy making courthouse puns? Guilty.'],
               [186, 'What do you call someone with no body and no nose? Nobody knows.'],
               [187, 'You know, people say they pick their nose, but I feel like I was just born with mine.'],
               [188, 'In a freak accident today, a photographer was killed when a huge lump of cheddar landed on him. To be fair, the people who were being photographed did try to warn him.'],
               [189, 'If you see a robbery at an Apple store, does that make you an iWitness?'],
               [190, 'What did the drummer call his twin daughters? Anna one, Anna two…'],
               [191, 'What’s a bad wizard’s favorite computer program? Spell check.'],
               [192, 'I was just reminiscing about the beautiful herb garden I had when I was growing up. Good thymes.'],
               [193, 'I began to read a horror novel in braille. Something bad is about to happen—I can feel it.'],
               [194, 'My friend wants to become an archaeologist, but I’m trying to put him off. I’m convinced his life will be in ruins.'],
               [195, 'I got hit in the head with a can of Coke today. Don’t worry, I’m not hurt. It was a soft drink.'],
               [196, 'Cooking out this weekend? Don’t forget the pickle. It’s kind of a big dill.'],
               [197, 'Justice is a dish best served cold. If it were served warm, it would be justwater.'],
               [198, 'What’s orange and sounds like a parrot? A carrot.'],
               [199, 'Why did the raisin go out with the prune? Because he couldn’t find a date.'],
               [200, 'What’s brown and sticky? A stick.'],
               [201, 'My dog accidentally swallowed a bunch of Scrabble tiles. I think this could spell disaster.'],
               [202, 'I wondered why the ball was getting bigger. Then it hit me.'],
               [203, 'I had a date last night. It was perfect. Tomorrow, I’ll try a grape.'],
               [204, 'Armed robbers—some say they’re a drain on society, but you’ve got to give it to them.'],
               [205, 'It hurts me to say this, but I have a sore throat.'],
               [206, 'I know a surgeon who puts organs back in upside down. I told him that’s not funny, but he said it was an inside joke.'],
               [207, 'My girlfriend says it’s either her or my career as a news reporter. I have some breaking news for her.'],
               [208, 'Inflation is really getting out of hand, but that’s just my five cents.'],
               [209, 'I can guess what people do for a living just by looking at their hands. I mean, I’m usually wrong, but I can guess.'],
               [210, 'I’ve been breeding racing deer. Just trying to make a quick buck.'],
               [211, 'How many mystery writers does it take to change a light bulb? Two: One to screw it in most of the way and another to give it a surprise twist at the end.'],
               [212, 'My dentist offered me dentures for only a dollar. It sounded like a good deal at the time, but now I have buck teeth.'],
               [213, 'What’s the smartest insect? A spelling bee!'],
               [214, 'How does the ocean say hi? It waves!'],
               [215, 'Name the kind of tree you can hold in your hand? A palm tree!'],
               [216, 'Where did the music teacher leave her keys? In the piano!'],
               [217, 'Why do birds fly south in the winter? It’s faster than walking!'],
               [218, 'Which superhero hits home runs? Batman!'],
               [219, 'Why is a football stadium always cold? It has lots of fans!'],
               [220, 'Why did the chicken cross the playground? To get to the other slide?'],
               [221, 'What kind of math do birds love? Owl-gebra!'],
               [222, 'How does a barber drive to work? He takes shortcuts!'],
               [223, 'What kind of shoes do frogs love? Open-toad!'],
               [224, 'Why do ducks always pay with cash? Because they always have bills!'],
               [225, 'Where do most horses live? In neigh-borhoods!'],
               [226, 'Which planet loves to sing? Nep-tune!'],
               [227, 'Why are basketball courts always wet? Because the players dribble!'],
               [228, 'What kind of keys are sweet? Cookies!'],
               [229, 'Why did the peanut get into a rocket? He wanted to be an astro-nut!'],
               [230, 'What fruit do twins love? Pears!'],
               [231, 'How do bees brush their hair? With honeycombs!'],
               [232, 'Why won’t peanut butter tell you a secret? He’s afraid you’ll spread it!'],
               [233, 'Who eats snails? People who don’t like fast food!'],
               [234, 'Why did the banana visit the doctor? He wasn’t peeling well!'],
               [235, 'Why did the computer get sick? It caught a virus!'],
               [236, 'Why did the teacher have birdseed? For her parrot-teacher conference!'],
               [237, 'Why are elephants to wrinkly? Have you ever tried to iron one?'],
               [238, 'Why was the broom late to school? It over-swept!'],
               [239, 'What is the strongest animal in the sea? Mussels!'],
               [240, 'What kind of chicken is the funniest? A comedi-hen!'],
               [241, 'What do you call a seagull that lives by the bay? A bagel!'],
               [242, 'What color do cats prefer? Purr-ple'],
               [243, 'What does a triceratops sit on? Its tricera-bottom!'],
               [244, 'What is a sleeping dinosaur? A dino-snore!'],
               [245, 'What kind of pizza do dogs eat? Pup-eroni pizza!'],
               [246, 'What do cats wear to bed? Paw-jamas!'],
               [247, 'What kind of pictures do turtles take? Shell-fies!'],
               [248, 'What do you call a famous turtle? A shell-ebrity!'],
               [249, 'What makes a sick lemon feel better? Lemon-aid!'],
               [250, 'How does Spiderman do research? On the World Wide Web!'],
               [251, 'What’s the largest gem on earth? A baseball diamond!'],
               [252, 'What do you get if you dip a cat in chocolate? A Kitty-Kat Bar!'],
               [253, 'What food is never on time? Choco-late!'],
               [254, 'What cookie flavor do monkeys love? Chocolate Chimp!'],
               [255, 'Why do hurricanes wear a monocle to see? Because they have one eye!'],
               [256, 'What did the clock ask the watch? Hour you doing?'],
               [257, 'Why don’t oysters share? They’re shell-fish!'],
               [258, 'Why are fish so intelligent? Because they live in schools!'],
               [259, 'What kind of fish loves going to battle? A swordfish!'],
               [260, 'Where do birds invest their money? The stork-market!'],
               [261, 'What nut has the most money? A cashew!'],
               [262, 'What do you call a cow who plays the trumpet? A moo-sician!'],
               [263, 'What’s a pirate’s favorite county? Arrrrgh-entina!'],
               [264, 'Why can’t Dalmatians win at hide and seek? Because they’re always spotted!'],
               [265, 'What do newborn kittens wear? Dia-purrs!'],
               [266, 'What did the little tree say to the big tree? Leaf me alone!'],
               [267, 'What’s in the recipe for gold soup? Fourteen carrots!'],
               [268, 'Name Spiderman’s favorite month? Web-ruary!'],
               [269, 'What’s an astronaut’s favorite meal? Launch!'],
               [270, 'Why can’t noses be 12 inches long? They’d be a foot!'],
               [271, 'What does it sound like when a nut sneezes? Ca-shew!'],
               [272, 'Where do smart burgers sit? On honor rolls!'],
               [273, 'Which holiday do cows enjoy most? Moo-Year’s Day!'],
               [274, 'Why can’t bicycles stand on on their own? They’re two-tired!'],
               [275, 'Where do you go to school to learn how to greet people? Hi school!'],
               [276, 'What do cheerleaders eat for breakfast? Cheerios!'],
               [277, 'What’s the hardest part about learning to skydive? The ground!'],
               [278, 'Why did the piano teacher need a ladder? To reach the high notes!'],
               [279, 'What kind of fishing bait do librarians use? Book-worms!'],
               [280, 'Which state is the smartest? Alabama—it has four As and one B!'],
               [281, 'What state does the most writing? Pennsylvania!'],
               [282, 'Which country is fastest? Russia!'],
               [283, 'Why was the math book crying? It had lots of problems!'],
               [284, 'What’s a math teacher’s favorite season? Sum-mer!'],
               [285, 'What starts with P and ends with E and has thousands of letters? Post office!'],
               [286, 'What breaks when you speak? Silence!'],
               [287, 'What do attorneys wear to court? Law-suits!'],
               [288, 'Why did the doctor get mad? He ran out of patients!'],
               [289, 'What notes do pirates love to sing? The high Cs!'],
               [290, 'How are dogs like cell phones? They both have collar id.'],
               [291, 'Which month do trees dislike? Sep-timber!'],
               [292, 'Why are ducks good at basketball? They make fowl shots!'],
               [293, 'How do snowmen travel around? By icicle!'],
               [294, 'What always sits in the corner but can move all round the world? A stamp.'],
               [295, 'What did one oar say to the other? “Can I interest you in a little row-mance?”'],
               [296, 'What do you call a hippie’s wife? Mississippi.'],
               [297, 'What happens to an illegally parked frog? It gets toad away.'],
               [298, 'Why aren’t dogs good dancers? Because they have two left feet.'],
               [299, 'What’s a dog’s favorite homework assignment? A lab report.'],
               [300, 'Why did the parents not like their son’s biology teacher? He had skeletons in his closet.'],
               [301, 'Their first daughter was born with a silver spoon in her mouth. Now they’re hoping for triplets so they can have a whole set.'],
               [302, 'What do fish say when they hit a concrete wall? Dam!'],
               [303, 'Did you hear about the salamander who went to Hollywood? He wanted to make newt movies'],
               [304, 'How much did Santa pay for his sleigh? Nothing, it was on the house.'],
               [305, 'What do you call a steak that’s been knighted by the queen? Sir Loin.'],
               [306, 'What did the shark say to the marlin at prom? Lookin’ Sharp.'],
               [307, 'here are sharks from? Finland.'],
               [308, 'Why didn’t the elephant buy a suitcase for his summer vacation? Because he already had a trunk!'],
               [309, 'Where does a fish go to borrow money? The loan shark!'],
               [310, 'Why does an elephant use its trunk as a bookmark? So it nose where it stopped reading.'],
               [311, 'What do physicists enjoy doing the most at sporting events? The Wave'],
               [312, 'What do you get from a pampered cow? Spoiled milk.'],
               [313, 'What do you call an elephant that doesn’t matter? Irrelephant.'],
               [314, 'Why did the police arrest the turkey? They suspected foul play.'],
               [315, 'I used to own a taser. It was stunning.'],
               [316, 'Why did elephants form a union They work for peanuts.'],
               [317, 'I don\'t like facial hair, but it\'s starting to grow on me.'],
               [318, 'Once I ate a fancy Italian restaurant. It cost a pretty penne.'],
               [319, 'Why did the elephants go on strike? They worked for peanuts.'],
               [320, 'What happens when doctors get mad? They lose their patients.'],
               [321, 'Why was the broom late to work? It over-swept.'],
               [322, 'How do elephants talk to each other? On the ele-phone!'],
               [323, 'What do you call a medieval lamp? A knight light.'],
               [324, 'What did the horse say after he tripped? I\'ve fallen and I can\'t giddy up.'],
               [325, 'How do elephants stay cool during a heat wave? Ear Conditioning!'],
               [326, 'Why can’t you borrow money from elves? They’re always short.'],
               [327, 'What do you call a hat for your leg? Kneecap.'],
               [328, 'What did the momma elephant say to her kid when he was misbehaving? “Tusk, tusk!”'],
               [329, 'Why do ghosts ride elevators? It lifts their spirits.'],
               [330, 'What did the envelope say to the stamp? Stick with me and you’ll go places.'],
               [331, 'How do you prevent an elephant from charging? Take away it’s credit card.'],
               [332, 'Why don’t ants get sick? They have anty-bodies.'],
               [333, 'What do you need to cook an alligator? A croc-pot.'],
               [334, 'What’s the only way an elephant flies? By dumbo jet!'],
               [335, 'Where does Wonder Woman go shopping? At the supermarket.'],
               [336, 'What kind of shoes do breadsticks wear? Loafers.'],
               [337, 'What do sea monsters eat for dinner? Fish and ships.'],
               [338, 'Why did the elephants get kicked out of the pool? Because their trunks kept falling down!'],
               [339, 'Did you hear about the emotional wedding? Even the cake was in tiers.'],
               [340, 'Did you hear about the homicidal oatmeal? It’s a cereal killer.'],
               [341, 'Did you hear about the guy who drank invisible ink? He’s in the ER waiting to be seen.'],
               [342, '1. Did you know elephants can grow up to 11 feet? Most only have four.'],
               [343, 'What kind of award do you give dentist of the year? A little plaque.'],
               [344, 'Did you hear about the coffee robbery? It got mugged.'],
               [345, 'What kind of shoes do bananas wear? Slippers.'],
               [346, 'Did you hear the sausage joke? It’s the wurst.'],
               [347, 'What do you call an indecisive bug? A may-bee.'],
               [348, 'What do you call a rude cow? Beef jerky.'],
               [349, 'What does a house wear? Address.'],
               [350, 'Why should you avoid trees? They can be shady.'],
               [351, 'What type of underwear do lawyers wear? Briefs.'],
               [352, 'What do you call a well-balanced horse? Stable.'],
               [353, 'What do you call an angry carrot? A steamed veggie.'],
               [354, 'Where do polar bears keep their money? Snow banks.'],
               [355, 'What do lawyers wear to court? Lawsuits.'],
               [356, 'What do elves learn in school? The elf-abet'],
               [357, 'what do sprinters eat before they race? Nothing, they fast.'],
               [358, 'What has more lives than a cat? A frog, because it croaks every day.'],
               [359, 'Why was the fish\'s grades so bad? They were below sea level.'],
               [360, 'What do you call a pig that practices karate? A pork chop.'],
               [361, 'What does a spy do when he is gold? He goes undercover.'],
               [362, 'Where does the general put his armies? In his sleevies'],
               [363, 'How do rabbits travel? By hareplanes'],
               [364, 'Why don\'t astronomers like Orion\'s Belt? It\'s a big waist of space.'],
               [365, 'What do you get when you cross a fish and an elephant? Swimming trunks']
]

mydb = mysql.connector.connect(
  host="localhost",
  user="holly",
  password="Hollyisthebest!",
  database="ElephantFacts"
)

print(mydb)

cursor = mydb.cursor()

# for i in range(len(listOfJokes)):
#     sql = "DELETE FROM jokes WHERE ID = '" + str(i + 1) + "'"

#     cursor.execute(sql)

#     mydb.commit()

# cursor.execute("SELECT * FROM jokes")

# result = cursor.fetchall()

# for row in result:
#     print(row)

cursor.execute("DELETE FROM jokes")

sql = "INSERT INTO jokes (ID, joke) VALUES (%s, %s)"
for val in listOfJokes:
    cursor.execute(sql, val)

    mydb.commit()

cursor.execute("SELECT * FROM jokes")

result = cursor.fetchall()

for row in result:
    print(row)
