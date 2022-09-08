label daytbattle:
    scene bg karaokedark with fade
    menu:
        "Please choose your difficulty"
        "Free (20 pts)":
            $ pointgoal = 20
            $ multiplier = 0.5
        "Easy (30 pts)":
            $ pointgoal = 30
            $ multiplier = 1.0
        "Medium (40 pts)":
            $ pointgoal = 40
            $ multiplier = 1.33
        "Hard (50 pts)":
            $ pointgoal = 50
            $ multiplier = 1.67
        "Expert (65 pts)":
            $ pointgoal = 65
            $ multiplier = 2.25
        "Lunatic (80 pts)":
            $ pointgoal = 80
            $ multiplier = 2.83
    narrator "--- Boss information ---\nName: Daytona"
    narrator "Rules: 20 second time limit; Quick-Draw Style"
    narrator "{size=-8}The faster you answer the more points you receive:{/size}{w}{size=-13}\nWithin 7 seconds - 7 pts\nWithin 10 seconds - 5 pts\nWithin 15 seconds - 3 pts\nWithin 20 seconds - 1 pt{/size}{w}\nRequired points: {b}[pointgoal] pts{/b}"
    narrator "Flex bonus: +2 pts for using the longest valid name\nStreak bonus: +1 pt per song in longest streak\nShortcut penalty: -5 pts for each deleted answer"
    narrator "Specialty: Title-Deletion\n{i}{size=-8}Shortened titles such as 'LasDan', 'EnStars', 'Genkoku', 'Yu-sibu', 'Haifuri', 'TsureKano' etc. are {b}not{/b} valid answers for this battle.{/size}{/i}"
    show dayt at left with moveinleft
    $ gamepoints = 0
    $ currentsong = 1
    $ numofsongs = 12
    $ currentstreak = 0
    $ streaks = [0]
    $ songdict = {
        "game601":["tensei shitara slime datta ken", "that time i got reincarnated as a slime"],
        "game602":["shigatsu wa kimi no uso", "your lie in april", "shigatsu wa kimi no uso: moments", "your lie in april: moments"],
        "game603":["sora yori mo tooi basho", "a place further than the universe"],
        "game604":["dungeon ni deai o motomeru no wa machigatteiru darou ka","is it wrong to try to pick up girls in a dungeon?"],
        "game605":["ore no imouto ga konnani kawaii wake ga nai","my little sister can't be this cute!"],
        "game606":["boku wa tomodachi ga sukunai"],
        "game607":["my teen romantic comedy snafu","yahari ore no seishun love come wa machigatteiru.","my teen romantic comedy snafu too!","yahari ore no seishun love come wa machigatteiru. zoku", "my teen romantic comedy snafu climax!","yahari ore no seishun love come wa machigatteiru. kan"],
        "game608":["my next life as a villainess: all routes lead to doom!","otome game no hametsu flag shika nai akuyaku reijou ni tensei shiteshimatta...","my next life as a villainess: all routes lead to doom! x","otome game no hametsu flag shika nai akuyaku reijou ni tensei shiteshimatta... x"],
        "game609":["ore no kanojo to osananajimi ga shuraba sugiru"],
        "game610":["shuumatsu nani shitemasu ka? isogashii desu ka? sukutte moratte ii desu ka?","worldend: what are you doing at the end of the world? are you busy? will you save us?"],
        "game611":["shimoneta to iu gainen ga sonzai shinai taikutsu na sekai","shimoneta: a boring world where the concept of dirty jokes doesn't exist"],
        "game612":["isekai wa smartphone to tomo ni.","in another world with my smartphone"],
        "game613":["watashi ga motenai no wa dou kangaete mo omaera ga warui!","no matter how i look at it, it's you guys' fault i'm not popular!"],
        "game614":["rikei ga koi ni ochita no de shoumei shitemita.","science fell in love, so i tried to prove it"],
        "game615":["watashi, nouryoku wa heikinchi de tte itta yo ne!","didn't i say to make my abilities average in the next life?!"],
        "game616":["uchi no ko no tame naraba, ore wa moshikashitara maou mo taoseru kamo shirenai.","if it's for my daughter, i'd even defeat a demon lord"],
        "game617":["saikin, imouto no yousu ga chotto okashiin da ga.","recently, my sister is unusual."],
        "game618":["uchi no maid ga uzasugiru!"],
        "game619":["ore no nounai sentakushi ga, gakuen love come o zenryoku de jama shiteiru","my mental choices are completely interfering with my school romantic comedy"],
        "game620":["jinrui wa suitai shimashita","humanity has declined"],
        "game621":["onii-chan dakedo ai sae areba kankei nai yo ne"],
        "game622":["rokudenashi majutsu koushi to akashic records","akashic records of bastard magical instructor"],
        "game623":["koi to yobu ni wa kimochi warui"],
        "game624":["tada-kun wa koi o shinai","tada never falls in love"],
        "game625":["ore ga suki nano wa imouto dakedo imouto ja nai", "my sister, my writer"]
    }
    # God my spaghetti code makes Ege's look pristine in comparison lul
    $ illegalans = {"game601":["tensura"],"game602":["kimiuso", "kimiuso: moments"],"game603":["yorimoi"],"game604":["danmachi"],"game605":["oreimo"],"game606":["haganai"],"game607":["oregairu", "oregairu zoku", "oregairu kan"],"game608":["hamefura", "hamefura x"],"game609":["oreshura"],"game610":["sukasuka"],"game611":["shimoseka"],"game612":["isesuma"],"game613":["watamote"],"game614":["rikekoi"],"game615":["noukin"],"game616":["uchinoko"],"game617":["imocho."],"game618":["uzamaid!"],"game619":["noucome"],"game620":["jintai"],"game621":["oniai"],"game622":["rokuaka"],"game623":["koikimo"],"game624":["tadakoi"],"game625":["imoimo"]}
    $ dial = ["I've got a toothbrush with your name on it","I deleted it (yaoi!!! on ice) and ege made me readd it","the last time i played amq was in january i think", "(real Dayt quote) did you know that Hitler was an animal lover and was actually a huge advocate for more laws protecting animals", "wtf a furry that looks decent", "Yes the idol jihen fan base is so trash", "thats why i back catbox adn not amq amq is trash catbox is god","time to ban jax for playing osu","if youre getting anythign right in 5 sec youre cheating anyway jsut not with shazam", "saro wtf", "oh my god these titles are giving me cancer","the reason quickdraw is so unplayed is because it legimitaly is a typing test"]
    while len(songdict) > numofsongs:
        $ popped = renpy.random.randint(1, len(songdict))
        $ poppedkey = list(songdict.keys())[popped-1]
        $ songdict.pop(poppedkey)
        $ songtup = list(songdict.items())
        $ renpy.random.shuffle(songtup)
        $ songdict = dict(songtup)
    while currentsong <= numofsongs:
        $ i = 0
        $ flexans = []
        $ longestlen = 0
        $ currentques = (list(songdict.items()))[currentsong-1][0]
        $ currentans = (list(songdict.items()))[currentsong-1][1]
        $ currentillegal = illegalans[currentques]
        while i < len(currentans):
            if len(currentans[i]) > longestlen:
                $ flexans = [currentans[i]]
                $ longestlen = len(currentans[i])
            elif len(currentans[i]) == longestlen:
                $ flexans.append(currentans[i])
            $ i += 1
        narrator "Song [currentsong] of [numofsongs]"
        $ timeleft = 20
        $ timer_range = 20
        show screen countdown2
        $ starttime = gettime.time()
        $ renpy.music.play("audio/" + currentques + ".mp3")
        call screen noddinput
        $ ans = _return.lower().strip()
        $ endtime = gettime.time()
        hide screen countdown2
        $ timedif = endtime - starttime
        $ timedifrnd = round(timedif, 2)
        $ timepoints = 7 if timedif <= 7 else 5 if timedif <= 10 else 3 if timedif <= 15 else 1 if timedif <= 20 else 0
        if currentques == "game606" and _return.strip() == "hagAnaI":
            dayt "heh nice, still wrong tho"
        if ans in currentillegal:
            $ gamepoints -= 5
            $ streaks.append(currentstreak)
            $ currentstreak = 0
            dayt "Looks like you entered in an answer I Thanos snapped, better luck next time"
            narrator "{size=-5}Answer score: 0 ([timedifrnd]s)\nFlex bonus: 0\nPenalty: -5{b}\nCurrent score: [gamepoints] points{/b} (Streak: 0){/size}"
        elif ans in currentans:
            $ currentstreak += 1
            narrator "Correct answer!"
            $ gamepoints += timepoints
            if ans in flexans:
                $ gamepoints += 2
                narrator "{size=-5}Answer score: [timepoints] ([timedifrnd]s)\nFlex bonus: 2\nPenalty: 0{b}\nCurrent score: [gamepoints] points{/b} (Streak: [currentstreak]){/size}"
            else:
                narrator "{size=-5}Answer score: [timepoints] ([timedifrnd]s)\nFlex bonus: 0\nPenalty: 0{b}\nCurrent score: [gamepoints] points{/b} (Streak: [currentstreak]){/size}"
        else:
            narrator "Nope... That ain't right..."
            $ streaks.append(currentstreak)
            $ currentstreak = 0
            $ allans = " / ".join(currentans)
            narrator "Correct answer(s):\n{size=-8}[allans]{/size}"
            narrator "{size=-5}Answer score: 0 ([timedifrnd]s)\nFlex bonus: 0\nPenalty: 0{b}\nCurrent score: [gamepoints] points{/b} (Streak: 0){/size}"
        if dial[currentsong-1]:
            $ currentdial = dial[currentsong-1]
            dayt "[currentdial]"
        $ currentsong += 1
    stop music fadeout 1.0
    $ streaks.append(currentstreak)
    $ highstreak = max(streaks)
    $ totalpoints = gamepoints + highstreak
    narrator "Game points: [gamepoints]\nHighest streak: [highstreak]\n{b}Total points: [totalpoints] points{/b}"
    if totalpoints >= pointgoal:
        $ weightedpoints = totalpoints * multiplier
        $ xpgain = int(round(weightedpoints,0))
        $ globalpoints += xpgain
        narrator "You win!"
        dayt "wtf bet you copy pasted half of those anyway"
        hide dayt with moveoutleft
        show shi2 with moveinright
        shi "Yayy~ Now I'll never have to read the pins ever again thanks to you!!"
    else:
        dayt "Well, well, well, looks like you couldn't handle it after all"
        dayt "Say goodbye to Shiina, and yourself."
        $ MainMenu(confirm=False)()
    scene black with fade
    return