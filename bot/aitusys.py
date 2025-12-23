from minline import MinlineApp, Menu, Button
import json


x = '{"football_club_instagram": "https://www.instagram.com/football_club/","table_tennis_club_instagram": "https://www.instagram.com/table_tennis_club/","basketball_club_instagram": "https://www.instagram.com/basketball_club/"}'
data = json.loads(x)

app = MinlineApp("8490071348:AAEVnHAcT6pR1WBshEHfN9wyaxQ101uIBk4")

###Main Menu
@app.route("/")
def main():
    return Menu(
        menu_id="Список клубов АИТУ",
        controls=[
            [Button("Settings", "#route:/settings")],
            [Button("Категории клубов", "#route:/categories")]
        ]
    )
###Settings Menu
@app.route("/settings")
def settings():
    return Menu(
        menu_id="settings",
        controls=[[]]
    )



###Categories
@app.route("/categories")
def categories():
    return Menu(
        menu_id="Категории клубов",
        controls=[[Button("Спорт", "#route:/categories/sport")],[Button("Культурно-массовые", "#route:/categories/cultural")],[Button("Интеллектуальные", "#route:/categories/intellectual")]]
    )
    
    
###Sport path
@app.route("/categories/sport")
def sport():
    return Menu(
        menu_id="Спорт клубы",
        controls=[[Button("Futsal", "#route:/categories/sport/football")],[Button("Table Tennis", "#route:/categories/sport/tennis")],[Button("Basketball", "#route:/categories/sport/basketball")],[Button("Volleyball", "#route:/categories/sport/volleyball")],[Button("Next", "#route:/categories/sport2")]]
    )
    
    
@app.route("/categories/sport2")
def sport2():
    return Menu(
        menu_id="Спорт клубы",
        controls=[[Button("Cycling","#route:/categories/sport2/cycling")],[Button("Running","#route:/categories/sport2/running")],[Button("Calestenics","#route:/categories/sport2/calestenics")],[Button("Arm-Wrestling","#route:/categories/sport2/armwrestling")]]
    )  
    
    

 
###Sport Category 
@app.route("/categories/sport/football")
def football():
    return Menu(
        menu_id="Futsal Club\nстуденческий клуб, посвященный развитию футзала в университете",
        controls=[[Button("Instagram",url = data["football_club_instagram"])],[Button("Telegram Channel",url = "https://t.me/aitu_futsal")]]
    )
    
    
@app.route("/categories/sport/tennis")
def tennis():
    return Menu(
        menu_id="Table Tennis Club",
        controls=[[Button("Instagram",url = data["table_tennis_club_instagram"])],[Button("Telegram Channel",url = "https://t.me/+ZVRFUhmGTz9jYTAy")]]
    )
    
    
@app.route("/categories/sport/basketball")
def basketball():
    return Menu(
        menu_id="Basketball Club",
        controls=[[Button("Instagram",url = data["basketball_club_instagram"])]]
    )


@app.route("/categories/sport/volleyball")
def volleyball():
    return Menu(
        menu_id="Volleyball Club",
        controls=[[Button("Instagram",url = "https://www.instagram.com/vc_aitu/")]]
    )
    
    

@app.route("/categories/sport2/cycling")
def cycling():
    return Menu(
        menu_id="Cycling Club",
        controls=[[Button("Instagram",url = "https://www.instagram.com/aitucyclingclub?igsh=Y3FoMzZha25sNXNl&utm_source=qr")]]
    )
    
    
    
@app.route("/categories/sport2/running")
def running():
    return Menu(
        menu_id="Running Club",
        controls=[[Button("Instagram",url = "https://www.instagram.com/aitu_running?igsh=ejlkdXd4dHh2Y3lw&utm_source=qr")]]
    )
    
    
@app.route("/categories/sport2/calestenics")
def calestenics():
    return Menu(
        menu_id="Calestenics Club",
        controls=[[Button("Instagram",url = "https://www.instagram.com/aitu_calisthenics?igsh=Y2NtcTkzdWZtM256")]]
    )
@app.route("/categories/sport2/armwrestling")
def armwrestling():
    return Menu(
        menu_id="Arm-Wrestling Club",
        controls=[[Button("Instagram",url = "https://www.instagram.com/aitu_armwrestling?igsh=MWpwZGpiNWVxZWhzZg==")]]
    )
   
      
###Cultural path
@app.route("/categories/cultural")
def musical():
    return Menu(
        menu_id="Культурно-массовые клубы",
        controls=[[Button("AITU KCA","#route:/categories/cultural/kca")],[Button("AITU JCA","#route:/categories/cultural/jca")],[Button("AITU Orchestra","#route:/categories/cultural/orchestra")],[Button("Anime Club","#route:/categories/cultural/anime")],[Button("Next","#route:/categories/cultural/next")]]
    )

@app.route("/categories/cultural/next")
def musical_next():
    return Menu(
        menu_id = "Культурно-массовые клубы",
        controls = [[Button("Cinephiles Club","#route:/categories/cultural/cinephiles")],[Button("Тұңғиық","#route:/categories/cultural/tungiyk")],[Button("AITU QazaQ-POP CULTURE","#route:/categories/cultural/qazaqpopculture")],[Button("AITU CHOIR","#route:/categories/cultural/choir")],[Button("Next","#route:/categories/cultural/next2")]]
    )
@app.route("/categories/cultural/next2")
def musical_next2():
    return Menu(
        menu_id = "Культурно-массовые клубы",
        controls = [[Button("Music Club","#route:/categories/cultural/musicclub")],[Button("Dance Club","#route:/categories/cultural/danceclub")],[Button("Devine Club","#route:/categories/cultural/devineclub")]]
    )    
    
    
     
###Cultural Category  
@app.route("/categories/cultural/kca")
def kca():
    return Menu(
        menu_id="AITU KCA\nКлуб корейской культуры",
        controls=[[Button("Instagram",url = "https://www.instagram.com/aitu_kca?igsh=MWZ1Z2ZtbW1iZ2Zz")]]
    )
@app.route("/categories/cultural/jca")
def jca():
    return Menu(
        menu_id="AITU JCA\nКлуб японской культуры",
        controls=[[Button("Instagram",url = "https://www.instagram.com/aitu_jca?igsh=MWZ1Z2ZtbW1iZ2Zz")]]
    )
@app.route("/categories/cultural/orchestra")
def orchestra():
    return Menu(
        menu_id="AITU Orchestra",
        controls=[[Button("Instagram",url = "https://www.instagram.com/aitu_orchestra?igsh=MWZ1Z2ZtbW1iZ2Zz")]]
    )
@app.route("/categories/cultural/anime")
def anime():
    return Menu(
        menu_id="Anime Club",
        controls=[[Button("Instagram",url = "https://www.instagram.com/aitu_anime?igsh=MWZ1Z2ZtbW1iZ2Zz")]]
    )
@app.route("/categories/cultural/cinephiles")
def cinephiles():
    return Menu(
        menu_id="Cinephiles Club",
        controls=[[Button("Instagram",url = "https://www.instagram.com/aitu_cinephiles?igsh=MWZ1Z2ZtbW1iZ2Zz")]]
    )
@app.route("/categories/cultural/tungiyk")
def tungiyk():
    return Menu(
        menu_id="Тұңғиық",
        controls=[[Button("Instagram",url = "https://www.instagram.com/tungiyq.aitu?igsh=Z2U5ZjRzdWVzbXFz")]]
    )
@app.route("/categories/cultural/qazaqpopculture")
def qazaqpopculture():
    return Menu(
        menu_id="AITU QazaQ-POP CULTURE",
        controls=[[Button("Instagram",url = "https://www.instagram.com/qpop_aitu/")]]
    )
@app.route("/categories/cultural/choir")
def choir():
    return Menu(
        menu_id="AITU CHOIR",
        controls=[[Button("Instagram",url ="https://www.instagram.com/aitu_choir?igsh=eW0xZXZhdWR4OTYx")]]
    )
@app.route("/categories/cultural/musicclub")
def musicclub():
    return Menu(
        menu_id="Music Club",
        controls=[[Button("Instagram",url = "https://www.instagram.com/aitu_music?igsh=MTc5bDhlOWNmNGMy")]]
    )
@app.route("/categories/cultural/danceclub")
def danceclub():
    return Menu(
        menu_id="Dance Club",
        controls=[[Button("Instagram",url = "https://www.instagram.com/aitu_dance?igsh=Ymt5OHJheHk0cm9q&utm_source=qr")]]
    )
@app.route("/categories/cultural/devineclub")
def devineclub():
    return Menu(
        menu_id="Devine Club",
        controls=[[Button("Instagram",url = "https://www.instagram.com/devine_aitu?igsh=MW8yeGIybnBqbWVpbg==")]]
    )
    
###Intellectual path
@app.route("/categories/intellectual")
def intellectual():
    return Menu(
        menu_id="Интеллектуальные клубы",
        controls = [[Button("Chess Club","#route:/categories/intellectual/chess")],[Button("Coffee-Philo","#route:/categories/intellectual/coffeephilo")],[Button("GDCS","#route:/categories/intellectual/gdcs")],[Button("Linux Klub","#route:/categories/intellectual/linuxklub")],[Button("Next","#route:/categories/intellectual/next")]]
    )
@app.route("/categories/intellectual/next")
def intellectual_next():
    return Menu(
        menu_id="Интеллектуальные клубы",
        controls = [[Button("SEDS AITU","#route:/categories/intellectual/next/seds")],[Button("SIAM AITU SC","#route:/categories/intellectual/next/siam")],[Button("Intellectum Games","#route:/categories/intellectual/next/intellectum")],[Button("AITU Electronics","#route:/categories/intellectual/next/electronics")],[Button("Next","#route:/categories/intellectual/next2")]]
    )
@app.route("/categories/intellectual/next2")
def intellectual_next2():
    return Menu(
        menu_id="Интеллектуальные клубы",
        controls=[[Button("AITU AWS 3C","#route:/categories/intellectual/next2/aws3c")],[Button("AITU Singularity","route:/categories/intellectual/next2/singularity")],[Button("PsyClub","route:/categories/intellectualnext2/psy")],[Button("Board Games","#route:/categories/intellectual/next2/board")],[Button("AI club","#route:/categories/intellectual/next2/aiclub")]]                                                                                                                                                                                                                                                 
    )
###Intellectual Category
@app.route("/categories/intellectual/chess")
def chess_club():
    return Menu(
        menu_id="Chess Club",
        controls=[[Button("Instagram",url= "https://www.instagram.com/chess.aitu?igsh=MTk1ZDZhdzd0NmxiZQ==")]]
    )
@app.route("/categories/intellectual/coffeephilo")
def chess_club():
    return Menu(
        menu_id="Coffee-Philo",
        controls=[[Button("Instagram",url= "https://www.instagram.com/coffeephilos?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==")]]
    )
@app.route("/categories/intellectual/gdcs")
def chess_club():
    return Menu(
        menu_id="Google Developer Student Club",
        controls=[[Button("Instagram",url= "https://www.instagram.com/gdsc_aitu/")]]
    )
@app.route("/categories/intellectual/linuxklub")
def chess_club():
    return Menu(
        menu_id="Linux Klub",
        controls=[[Button("Instagram",url= "https://instagram.com/linux.klub.aitu?igshid=OTJlNzQ0NWM")]]
    )
@app.route("/categories/intellectual/next/seds")
def chess_club():
    return Menu(
        menu_id="SEDS AITU",
        controls=[[Button("Instagram",url= "https://www.instagram.com/seds.aitu?igsh=MXJ5Ym1yZTZ0cmJ2NA==")]]
    )
@app.route("/categories/intellectual/next/siam")
def chess_club():
    return Menu(
        menu_id="SIAM AITU SC",
        controls=[[Button("Instagram",url= "https://www.instagram.com/aitusiamsc?igsh=MWxyb3poa2RxeTdiYw%3D%3D&utm_source=qr")]]
    )
@app.route("/categories/intellectual/next/intellectum")
def chess_club():
    return Menu(
        menu_id="Intellectum Games",
        controls=[[Button("Instagram",url= "https://www.instagram.com/intellectumgames_kz")]]
    )
@app.route("/categories/intellectual/next/electronics")
def chess_club():
    return Menu(
        menu_id="AITU Electronics",
        controls=[[Button("Instagram",url= "https://www.instagram.com/aitu.electronicss?igsh=c2l0dGYxM2FyMW5v")]]
    )
@app.route("/categories/intellectual/next2/aws3c")
def chess_club():
    return Menu(
        menu_id="AITU AWS 3C",
        controls=[[Button("Instagram",url= "https://www.instagram.com/aitu_aws_3c?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==")]]
    )
@app.route("#/categories/intellectual/next2/singularity")
def chess_club():
    return Menu(
        menu_id="AITU Singularity",
        controls=[[Button("Instagram",url= "https://www.instagram.com/aitusingularity?igsh=MWxmZXd3cXdmaTYxdw==")]]
    )
@app.route("/categories/intellectual/next2/psy")
def chess_club():
    return Menu(
        menu_id="PsyClub",
        controls=[[Button("Instagram",url= "https://www.instagram.com/psy_club_aitu?igsh=YzJ3enN5NGlydDN2")]]
    )
@app.route("/categories/intellectual/next2/board")
def chess_club():
    return Menu(
        menu_id="Board Games",
        controls=[[Button("Instagram",url= "https://www.instagram.com/aitu_board_games/")]]
    )
@app.route("/categories/intellectual/next2/aiclub")
def chess_club():
    return Menu(
        menu_id="AI club",
        controls=[[Button("Instagram",url= "https://www.instagram.com/aitu_board_games/")]]
    )


app.run()
