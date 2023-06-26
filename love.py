import mysql.connector

listOfTranslations = [[1, "English: I love you"],
                      [2, "Mandarin: Wǒ ài nǐ"],
                      [3, "Spanish: te amo, te quiero"],
                      [4, "Hindi: main tumse pyar karta hoon"],
                      [5, "Arabic: ahabak"],
                      [6, "Portuguese: eu te amo"],
                      [7, "Bengali: Āmi tōmāẏa bhālōbāsi"],
                      [8, "Russian: ya lyublyu tebya"],
                      [9, "Japanese: watashi wa, anata o aishiteimasu"],
                      [10, "Punjabi: maiṁ tuhānū pi’āra karadā hāṁ"],
                      [11, "German: ich liebe dich"],
                      [12, "Javanese: Aku tresna sampeyan"],
                      [13, "Wu (Shanghainese): (ngu eh nóng) Ngu long hushin long lah"],
                      [14, "Malay/Indonesian: saya sayang awak"],
                      [15, "Korean: salanghae"],
                      [16, "Telugu: nēnu ninnu prēmistunnānu"],
                      [17, "Vietnamese: anh yêu em"],
                      [18, "French: je t’aime"],
                      [19, "Marathi: mī tujhyāvara prēma karatō"],
                      [20, "Tamil: nāṉ uṉṉai kātalikkiṟēṉ"],
                      [21, "Urdu: m – (mein ap say muhabat karta hoon) & f – (mein ap say muhabat karti hoon)"],
                      [22, "Persian/Farsi: (asheghetam) used in poetry and songs – (dūset dāram)"],
                      [23, "Turkish: seni seviyorum"],
                      [24, "Cantonese: ngóh oi néih"],
                      [25, "Italian: ti amo"],
                      [26, "Thai: P̄hm rạk khuṇ"],
                      [27, "Gujarati: Huṁ tanē prēma karuṁ chu"],
                      [28, "Basque: maite zaitut"],
                      [29, "Minnan hua: wǒ ài rǔ"],
                      [30, "Polish: kocham Cię"],
                      [31, "Pashto: (za la ta sara meena kawom)"],
                      [32, "Kannada: Nānu ninnannu prītisuttēne"],
                      [33, "Malayalam: ñān ninne snēhikkunnu"],
                      [34, "Sundanese: abdi bogoh ka anjeun"],
                      [35, "Chamorro: Hu guiaya hao"],
                      [36, "Hausa: Ina son ka"],
                      [37, "Burmese: mainnkohkyittaal"],
                      [38, "Oriya: mu tumoku bhala paye"],
                      [39, "Armenian: Yes sirum yem k’yez"],
                      [40, "Ukrainian: ya tebe lyublyu"],
                      [41, "Bhojpuri: hum tohse pyaar kareni"],
                      [42, "Tagalog: Iniibig kita"],
                      [43, "Yoruba: mo nifẹ rẹ"],
                      [44, "Maithili: hawm ahāṃ se prem karechi"],
                      [45, "Sindhi: Man tokhe prem karyan ti or Man tokhe prem karyan to"],
                      [46, "Swahili: nakupenda"],
                      [47, "Uzbek: Men seni Sevaman"],
                      [48, "Amharic: ewedihalehu"],
                      [49, "Fula: mi yidi ma"],
                      [50, "Igbo: a hụrụ m gị n’anya"],
                      [51, "Oromo: Sin jaalladha’"],
                      [52, "Romanian: te iubesc"],
                      [53, "Azerbaijani: Mən səni sevirəm"],
                      [54, "Manipuri/Meitei: əi-nə nəng-bu nung-shi"],
                      [55, "Chichewa: Ndimakukonda Ndimakukondani"],
                      [56, "Cebuano: gihigugma TIKA"],
                      [57, "Dutch: ik hou van je"],
                      [58, "Kurdish: Ez hej te dikim"],
                      [59, "Serbo-Croatian: Volim te"],
                      [60, "Malagasy: tiako ianao"],
                      [61, "Nepali: Ma timīlā’ī māyā garchu"],
                      [62, "Saraiki: mẽ tenū̃ piār kardā hā̃"],
                      [63, "Santali: ing aming sibilama"],
                      [64, "Khmer: khnhom sralanh anak"],
                      [65, "Sinhalese: mama oyāṭa ādareyi"],
                      [66, "Bambara: M’bi fe"],
                      [67, "Assamese: môi apunak bhal paû"],
                      [68, "Madurese: Kula tresna / panjengan"],
                      [69, "Somali: Waan ku jeclahay"],
                      [70, "Magahi: həm t̪oːraː seː pjaːr kərə hɪjoː/"],
                      [71, "Dogri: Minjo tere naal pyar hega"],
                      [72, "Marwari: main tanne pyaar karoon"],
                      [73, "Hungarian: Szeretlek"],
                      [74, "Chewa: ndimakukondani"],
                      [75, "Kinyarwanda: Ndagukunda"],
                      [76, "Greek: Se agapó"],
                      [77, "Akan/Twi: Me dor wo"],
                      [78, "Khasi: Nga ieid ia phi"],
                      [79, "Kazakh: men seni jaqsı köremin"],
                      [80, "Tswana: Ke a go rata"],
                      [81, "Hebrew: (man to a woman) – “Ani Ohev Otach”, (woman to a man) –“Ani Ohevet Otcha”, (woman to a woman) –“Ani Ohevet Otach”, (man to a man) –“Ani Ohev Otcha”"],
                      [82, "Zulu: Ngiyakuthanda"],
                      [83, "Czech: Miluji tě"],
                      [84, "Kinyarwanda: ndagukunda"],
                      [85, "Kokani: hav tujo mog korta"],
                      [86, "Haitian Creole: Mwen renmen ou"],
                      [87, "Afrikaans: Ek het jou lief"],
                      [88, "Ilokano: Ayayatenka, (ay-aya-ten kaw)"],
                      [89, "Quechua: Kuyayki"],
                      [90, "Kirundi: Ndagukunda"],
                      [91, "Swedish: jag älskar dig"],
                      [92, "Hmong: Kuv hlub koj"],
                      [93, "Shona: Ndinokuda"],
                      [94, "Hiligaynon: Palangga ko ikaw Guina higugma ko ikaw"],
                      [95, "Uyghur: Män sızni söyümän"],
                      [96, "Balochi: Tu mana doost biyeh"],
                      [97, "Belarusian: ja ciabie kachaju"],
                      [98, "Maori: Kei te aroha au ki a koe"],
                      [99, "Xhosa: ndiyakuthanda"],
                      [100, "Konkani: Hav tukka Mog Karta"]]

mydb = mysql.connector.connect(
  host="localhost",
  user="holly",
  password="Hollyisthebest!",
  database="ElephantFacts"
)

print(mydb)

cursor = mydb.cursor()

for i in range(len(listOfTranslations)):
    sql = "DELETE FROM love WHERE ID = '" + str(i + 1) + "'"

    cursor.execute(sql)

    mydb.commit()

print(cursor.rowcount, "record deleted.")

cursor.execute("SELECT * FROM love")

result = cursor.fetchall()

for row in result:
    print(row)

sql = "INSERT INTO love (ID, translation) VALUES (%s, %s)"
for val in listOfTranslations:
    # val = ("1", "Elephants are the world’s largest land mammal")
    cursor.execute(sql, val)

    mydb.commit()

print(cursor.rowcount, "record inserted.")

cursor.execute("SELECT * FROM love")

result = cursor.fetchall()

for row in result:
    print(row)
