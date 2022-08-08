
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os

Normal = []
Special = []
Assist = []
Super = []

Site = requests.get("https://www.dustloop.com/w/DBFZ/Kefla/Frame_Data", headers={
    'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
SiteSoup = Site.content

SiteParser = BeautifulSoup(SiteSoup, "html.parser")

Table = SiteParser.find_all('table', attrs={'class': 'cargoDynamicTable'})

Table_body = Table[0].find('tbody')  # Normal Attacks
Rows = Table_body.find_all('tr')
for row in Rows:
    Cols = row.find_all('td')
    Cols = [element.text for element in Cols]
    Normal.append(element for element in Cols)  # Get rid of empty values

Table_body2 = Table[1].find('tbody')  # Special Attacks
Rows2 = Table_body2.find_all('tr')
for row2 in Rows2:
    Cols = row2.find_all('td')
    Cols = [element.text for element in Cols]
    Special.append(element for element in Cols)  # Get rid of empty values
    # Special.append([element for element in Cols if element]) # Get rid of empty values

Table_body3 = Table[2].find('tbody')  # Assist
Rows3 = Table_body3.find_all('tr')
for row3 in Rows3:
    Cols = row3.find_all('td')
    Cols = [element.text for element in Cols]
    Assist.append(element for element in Cols)  # Get rid of empty values
    # Special.append([element for element in Cols if element]) # Get rid of empty values

Table_body4 = Table[3].find('tbody')  # Supers
Rows4 = Table_body4.find_all('tr')
for row4 in Rows4:
    Cols = row4.find_all('td')
    Cols = [element.text for element in Cols]
    Super.append(element for element in Cols)  # Get rid of empty values
    # Special.append([element for element in Cols if element]) # Get rid of empty values

import pandas

NormalDF = pandas.DataFrame(Normal)
NormalDF.columns = ["index", "input", "damage", "smash", "prorate", "guard", "startup", "active", "recovery", "onBlock",
                    "invuln", "level", "blockstun", "groundHit", "airHit"]
# NormalDF.columns = ["index","input","damage","guard","startup","active","recovery","onBlock","onHit","riscGain","level","counter","invulnerability","prorate"]
# NormalDF.columns = ["index","input","damage","guard","startup","active","recovery","onBlock","onHit","riscGain","level","counter","invulnerability","prorate", "haha"]
# NormalDF.columns = ["index","input","damage","guard","startup","active","recovery","onBlock","onHit","riscGain","level","invulnerability","prorate"]
SpecialDF = pandas.DataFrame(Special)
SpecialDF.columns = ["index", "input", "name", "damage", "smash", "prorate", "guard", "startup", "active", "recovery",
                     "onBlock", "invuln", "level", "blockstun", "groundHit", "airHit"]
# SpecialDF.columns = ["index","input","name","damage","guard","startup","active","recovery","onBlock","onHit","riscGain","level","counter","invulnerability","prorate"]
# SpecialDF.columns = ["index","input","name","damage","guard","startup","active","recovery","onBlock","onHit","riscGain","level","invulnerability","prorate"]
AssistDF = pandas.DataFrame(Assist)
AssistDF.columns = ["index", "input", "name", "damage", "smash", "prorate", "guard", "startup", "active", "recovery",
                    "onBlock", "invuln", "level", "blockstun", "groundHit", "airHit"]
# AssistDF.columns = ["index","name","damage","guard","startup","active","recovery","onBlock","onHit","riscGain","level","invulnerability","prorate"]
# AssistDF.columns = ["index","name","damage","guard","startup","active","recovery","onBlock","onHit","riscGain","level","invulnerability"] #nago #Gold
# AssistDF.columns = ["index","input","name","damage","guard","startup","active","recovery","onBlock","onHit","riscGain","level","invulnerability","prorate"] #Leo
SuperDF = pandas.DataFrame(Super)
SuperDF.columns = ["index", "input", "name", "damage", "smash", "prorate", "guard", "startup", "active", "recovery",
                   "onBlock", "invuln", "level", "blockstun", "groundHit", "airHit"]

test = []  # Rennlar gever (Rows command)
for item in NormalDF.iterrows():
    test.append("None")

test2 = []  # Rennlar gever (Rows command)
for item in AssistDF.iterrows():
    test2.append("None")

NormalDF.insert(2, "name", test, True)  # Need to make an array that sets value automatically.
# AssistDF.insert(1,"input",test2,True) # Need to make an array that sets value automatically.

Merge = pandas.concat([NormalDF, SpecialDF])

MergeHarder = pandas.concat([Merge, AssistDF])

GoEvenFurtherBeyond = pandas.concat([MergeHarder, SuperDF])

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())  # Lezyes image snatch (FrameDataFull)
driver.get("https://www.dustloop.com/w/DBFZ/Kefla/Frame_Data")

for c in driver.find_elements_by_class_name("details-control"):
    try:
        c.click()
    except:
        pass

imgs = []
for img in driver.find_elements_by_tag_name("img"):
    src = img.get_attribute("src")
    if ('https://www.dustloop.com/wiki/images/' in src) and (
            "DBFZ" in src) and ("Icon" not in src):
        imgs.append("/".join("/".join(src.split("/")[:-1]).split("/thumb/")))

# find how to download files


# img_data = requests.get(image_url).content - Download images #Lezyes make it work later (selenium)
# with open(img_path, 'wb') as handler:
#    handler.write(img_data)

# soup_result = BeautifulSoup(driver.page_source, 'lxml') (soup)
# images_in_page = soup_result.find_all('img')
# for i in images_in_page:
#    src = "https://www.dustloop.com"+i.get("src")
#    if ("GGST" in src) and ("Icon" not in src):
#        img = "/".join("/".join(src.split("/")[:-1]).split("/thumb/"))
#        print(img)

GoEvenFurtherBeyond.to_csv("kefla.csv")

counter = 0
for item in imgs:
    if not os.path.exists(imgs[counter][42:]):
        response = requests.get(imgs[counter])
        file = open(imgs[counter][42:], "wb")  # Get substring of image name
        file.write(response.content)
        file.close()
        print("file", imgs[counter][42:], "copied successfully")
        counter = counter + 1
    else:
        counter = counter + 1

print("All Framedata + images have been printed successfully")