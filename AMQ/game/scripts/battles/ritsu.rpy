label ritsubattle:
    scene bg arcade with fade
    menu:
        "Please choose your difficulty"
        "Litterbox (5 lives, long sample)":
            $ lives = 5
            $ sample = 1.5
            $ totalsample = 5
            $ multiplier = 0.5
        "Easy (3 lives, long sample)":
            $ lives = 3
            $ sample = 1.5
            $ totalsample = 5
            $ multiplier = 1.0
        "Medium (3 lives, normal sample)":
            $ lives = 3
            $ sample = 1
            $ totalsample = 4
            $ multiplier = 1.5
        "Hard (2 lives, normal sample)":
            $ lives = 2
            $ sample = 1
            $ totalsample = 4
            $ multiplier = 1.75
        "Impossible (2 lives, short sample)":
            $ lives = 2
            $ sample = 0.5
            $ totalsample = 3
            $ multiplier = 2.25
        "Inazuma Eleven (1 life, short sample)":
            $ lives = 1
            $ sample = 0.5
            $ totalsample = 3
            $ multiplier = 2.5
    $ guesstime = totalsample - sample
    narrator "--- Boss information ---\nName: Ritsu"
    narrator "Rules: [sample]s sample, [guesstime]s guessing time"
    narrator "Specialty: ?????"
    show rit2 at right with moveinright
    rit "Let's see how long you last Buni"
    $ gamepoints = 0
    $ currentsong = 1
    $ numofsongs = 20
    $ songdict = {
        "game1001":["Michiko to Hatchin","Great Pretender","Baccano!","Hakumei to Mikochi"],
        "game1002":["Maou-jou de Oyasumi","Gochuumon wa Usagi Desu ka?","Tsurezure Children","Genjitsu Shugi Yuusha no Oukoku Saikenki"],
        "game1003":["Sakura Trick","B Gata H Kei","Kiss × Sis","Amaama to Inazuma"],
        "game1004":["Momokuri","Acchi Kocchi","Last Period: Owarinaki Rasen no Monogatari","Mikakunin de Shinkoukei"],
        "game1005":["Deatte 5-byou de Battle","Jibaku Shounen Hanako-kun","Mahou Shoujo Tokushusen Asuka","Inou-Battle wa Nichijou-kei no Naka de"],
        "game1006":["Minami-ke: Tadaima","Mahou Sensei Negima!","Strike Witches","Love Lab"],
        "game1007":["Beastars","JoJo no Kimyou na Bouken","Megalobox","One Piece Film: Gold"],
        "game1008":["Itai no wa Iya nano de Bougyoryoku ni Kyokufuri Shitai to Omoimasu.","Kuma Kuma Kuma Bear","Mayo Chiki!","Ore, Twintail ni Narimasu."],
        "game1009":["Kingdom","3D Kanojo Real Girl","Black Clover","Fairy Tail: Final Season"],
        "game1010":["Peter Grill to Kenja no Jikan","Musaigen no Phantom World","Kaijin Kaihatsu-bu no Kuroitsu-san","Mairimashita! Iruma-kun"],
        "game1011":["Machikado Mazoku 2-choume","Tamako Market","Hibike! Euphonium","Girls und Panzer"],
        "game1012":["Hamatora","Hamtaro","Re:␣Hamatora","Devil Survivor 2 The Animation"],
        "game1013":[".hack//Intermezzo","xxxHOLiC","Koukaku Kidoutai","Aoi Bungaku Series"],
        "game1014":["Gangsta.","Dimension W","Gantz","Super Crooks"],
        "game1015":["Full Metal Panic? Fumoffu","Kino no Tabi: The Beautiful World","Ookami to Koushinryou II","Mushoku Tensei: Isekai Ittara Honki Dasu"],
        "game1016":["Fate/Grand Order: Zettai Majuu Sensen Babylonia","Kekkai Sensen & Beyond","Yozakura Quartet: Hana no Uta","Kaze ga Tsuyoku Fuiteiru"],
        "game1017":["Free!: Take Your Marks","A3! Season Spring & Summer","TsukiPro the Animation","The iDOLM@STER SideM"],
        "game1018":["Dororo","Durarara!!","Dorohedoro","Ninja Hattori-kun"],
        "game1019":["Boku-tachi no Remake","BanG Dream! 2nd Season","Bermuda Triangle: Colorful Pastrale","Cardfight!! Vanguard"],
        "game1020":["Osananajimi ga Zettai ni Makenai Love Come","Boku-tachi wa Benkyou ga Dekinai!","Midara na Ao-chan wa Benkyou ga Dekinai","Jaku-Chara Tomozaki-kun"],
        "game1021":["Ore dake Haireru Kakushi Dungeon: Kossori Kitaete Sekai Saikyou","Sono Bisque Doll wa Koi o Suru","Okaa-san Online","Gundam Build Divers Re:RISE"],
        "game1022":["Hanayamata","Ochikobore Fruit Tart","Futsuu no Joshikousei ga Locodol Yattemita OVA","Senryuu Shoujo"],
        "game1023":["Hidamari Sketch × Honeycomb","Kono Bijutsu-bu ni wa Mondai ga Aru!","GA: Geijutsuka Art Design Class","Sketchbook: Full Color's"],
        "game1024":["Koisuru Asteroid","Honzuki no Gekokujou: Shisho ni Naru Tame ni wa Shudan o Erandeiraremasen","Tsuki ga Kirei","Chain Chronicle: Haecceitas no Hikari"],
        "game1025":["Long Riders!","To LOVE-Ru Darkness 2nd","Wakaba*Girl","Ao no Kanata no Four Rhythm"],
        "game1026":["Saki Zenkoku-hen","Date A Live IV","Dakara Boku wa, H ga Dekinai.","Maken-Ki! Two"],
        "game1027":["To LOVE-Ru","Okusama ga Seitokaichou!+!","Seitokai Yakuindomo*","Choujigen Game Neptune The Animation"],
        "game1028":["Bishounen Tanteidan","Kimi no Suizou o Tabetai","Wotaku ni Koi wa Muzukashii","Mix: Meisei Story"],
        "game1029":["Hidan no Aria AA","Btooom!","Aoki Hagane no Arpeggio: Ars Nova","Conception"],
        "game1030":["Sentouin, Hakenshimasu!","Ueno-san wa Bukiyou","Plunderer","Busou Shoujo Machiavellism"],
        "game1031":["Masamune-kun no Revenge","Hajimete no Gal","Oshiete! Galko-chan","Boku no Kanojo ga Majime Sugiru Shobitch na Ken"],
        "game1032":["Ousama Game The Animation","Rainbow: Nisha Rokubou no Shichinin","Enen no Shouboutai","EVIL OR LIVE"],
        "game1033":["Daiya no Ace: Second Season","Prince of Stride: Alternative","Hand Shakers","Ple Ple Pleiades: Clementine Toubou-hen"],
        "game1034":["Hitorijime My Hero","Grand Blue Dreaming","Sasaki to Miyano","Udon no Kuni no Kin-iro Kemari"],
        "game1035":["Sakamichi no Apollon","Hachimitsu to Clover","3-gatsu no Lion","Dance Dance Danseur"],
        "game1036":["Senyoku no Sigrdrifa","Happy Sugar Life","Fuuka","Shichisei no Subaru"],
        "game1037":["Working'!!","Servant × Service","Ore o Suki nano wa Omae Dake ka yo","Sore ga Seiyuu!"],
        "game1038":["Peach Boy Riverside","Shinka no Mi: Shiranai Uchi ni Kachigumi Jinsei","Darker than Black: Ryuusei no Gemini","Vivy: Fluorite Eye's Song"],
        "game1039":["Shoujo☆Kageki Revue Starlight: Rondo Rondo Rondo","Lapis Re:LiGHTs","Princess Connect! Re:Dive Season 2","Oshi ga Budoukan Ittekuretara Shinu"],
        "game1040":["Choujin Koukousei-tachi wa Isekai demo Yoyuu de Ikinuku Youdesu!","Kenja no Mago","Tejina Senpai","Uzaki-chan wa Asobitai!"],
        "game1041":["Leadale no Daichi nite","Saihate no Paladin","Zero kara Hajimeru Mahou no Sho","Kenja no Deshi o Nanoru Kenja"],
        "game1042":["Yokohama Kaidashi Kikou","Shingetsutan Tsukihime","Tsukuyomi: Moon Phase","Abenobashi Mahou☆Shoutengai"],
        "game1043":["Date A Bullet","Hajime no Ippo","Zombie-Loan","The Big O"],
        "game1044":["Harukana Receive","Kami Nomi zo Shiru Sekai: 4-nin to Idol","Magical Star Kanon 100%","Kannagi"],
        "game1045":["Mashiro no Oto","Tsurune: Kazemai Koukou Kyuudou-bu","Dokyuu Hentai HxEros","Dr. Stone Special Episode: Ryusui"],
        "game1046":["Death March kara Hajimaru Isekai Kyousoukyoku","Arifureta Shokugyou de Sekai Saikyou","Assassins Pride","Girly Air Force"]
    }
    $ dial = ["Faster~","","","*insert gamer girl dialogue here, idk does it look like i have a discord gf or smth","","This is... definitely one of the moments of all time","um ackshualy its op 42 of meitantei conan :nerd_emoji:","","","imagine getting a gaming setup and using it to play amq all day, just sell that gpu already","youre welcome for all that shitty audio compression btw","","komugi asked me to leave her discordhere go add her Komugi#9780","","my favorite ranked meme is when catbox fucking dies","","you look like the kind of person to always, without fail, submit alfa-x for evangelion","yearly reminder to clean your room","...",""]
    while len(songdict) > numofsongs:
        $ popped = renpy.random.randint(1, len(songdict))
        $ poppedkey = list(songdict.keys())[popped-1]
        $ songdict.pop(poppedkey)
        $ songtup = list(songdict.items())
        $ renpy.random.shuffle(songtup)
        $ songdict = dict(songtup)
    while currentsong <= numofsongs and lives > 0:
        python:
            ontime = True
            savedans = ""
            optionslist = (list(songdict.items()))[currentsong-1][1]
            currentans = optionslist[0]
            renpy.random.shuffle(optionslist)
            option1 = optionslist[0]
            option2 = optionslist[1]
            option3 = optionslist[2]
            option4 = optionslist[3]
            songaudio = (list(songdict.items()))[currentsong-1][0]
            timeleft = totalsample
            timer_range = totalsample
            timer_jump = "outoftime_ritsu"
        narrator "Song [currentsong] of [numofsongs]"
        $ renpy.sound.play("audio/" + songaudio + ".mp3")
        show screen countdown
        $ renpy.pause(sample, hard=True)
        $ renpy.music.set_pause(True, channel="sound")
        menu:
            "[option1]":
                $ savedans = option1
            "[option2]":
                $ savedans = option2
            "[option3]":
                $ savedans = option3
            "[option4]":
                $ savedans = option4
        hide screen countdown
        $ renpy.music.set_pause(False, channel="sound")
        if not savedans:
            label outoftime_ritsu:
                $ renpy.music.set_pause(False, channel="sound")
                $ ontime = False    
                $ lives -= 1
                rit "Heh... Too bad. Get better ears kid"
                narrator "Current score: [gamepoints]\nLives: [lives]"
        if savedans == currentans and ontime:
            $ gamepoints += 15
            narrator "Correct! Current score: [gamepoints]\nLives: [lives]"
        elif ontime:
            $ lives -= 1
            narrator "Nope... Current score: [gamepoints]\nLives: [lives]"
        if dial[currentsong-1]:
            $ currentdial = dial[currentsong-1]
            rit "[currentdial]"
        $ currentsong += 1
    stop sound fadeout 1.0
    if lives == 0:
        label death_ritsu:
            stop sound fadeout 1.0
            rit "Well, well, well..."
            rit "Time to banish you from the arcade after all."
            rit "/kill JinAxel"
            $ MainMenu(confirm=False)()
    else:
        hide rit2
        show rit6 at right
        rit "..."
        rit "......"
        rit "..............."
        rit "I hope you didn't think that's all I had in me."
        play music "audio/bgm08.mp3" fadeout 1.0 fadein 1.0 volume 0.2
        $ renpy.notify('♪ Boku no Hero Academia (OST)')
        rit "*friendship speech*"
        hide rit6
        show rit7 at right
        rit "It's not over yet."
        show anoe1 at left with moveinleft
        noe "Quick! Take this!"
        show muscle at truecenter with moveinleft
        hide anoe1 with moveoutleft
        "Item {b}:muscle:{/b} acquired!"
        "Effect: +1 life"
        $ lives += 1
        hide muscle with dissolve
        rit "It's time for round 2 baby."
        narrator "--- Boss information ---\nName: Ritsu"
        narrator "Specialty: Second-Form"
        stop music fadeout 1.0
        $ numofsongs = 25
        $ songdict = {
            "game1101":["wonder egg priority"],
            "game1102":["made in abyss","made in abyss recaps"],
            "game1103":["guilty crown"],
            "game1104":["goblin slayer"],
            "game1105":["date a live ii"],
        }
        $ songtup = list(songdict.items())
        $ renpy.random.shuffle(songtup)
        $ songdict = dict(songtup)
        while currentsong <= numofsongs and lives > 0:
            narrator "Song [currentsong] of [numofsongs]"
            $ songaudio = (list(songdict.items()))[currentsong-21][0]
            $ currentans = (list(songdict.items()))[currentsong-21][1]
            $ renpy.sound.play("audio/" + songaudio + ".mp3")
            $ renpy.pause(sample, hard=True)
            $ renpy.music.set_pause(True, channel="sound")
            window hide
            call screen noddinput
            $ renpy.music.set_pause(False, channel="sound")
            $ ans = _return.lower().strip()
            if ans in currentans:
                $ gamepoints += 20
                narrator "Correct! Current score: [gamepoints]\nLives: [lives]"
            else:
                $ lives -= 1
                narrator "Nope... Current score: [gamepoints]\nLives: [lives]"
                $ allans = " / ".join(currentans)
                narrator "Correct answer(s):\n{size=-8}[allans]{/size}"
            $ currentsong += 1
        stop sound fadeout 1.0
        if lives == 0:
            jump death_ritsu
        else:
            hide rit7
            show rit8 at right
            rit "Wait, what?"
            $ weightedpoints = gamepoints * multiplier
            $ globalpoints += int(round(weightedpoints,0))
            scene black with fade
            return