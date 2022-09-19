label ch5:
    "..."
    "......"
    "............."
    ".....................................!"
    ""
    "Welcome to your worst nightmare"
    show actualnightmare
    $ renpy.pause(11.5, hard=True)
    scene black
    ""
    "???" "...So ye finally decided to rear ye ugly head on me ship ay?"
    scene bg pirate with fade
    show mar pirate think with moveinright:
        yalign 0.4
        xalign 0.5
    play music "audio/bgm09.mp3" fadein 1.0 fadeout 1.0 volume 0.2
    $ renpy.notify('♪ Mouretsu Pirates')
    mar "Who do you think ye are... steeping foot in MY WATERS?"
    hide mar pirate think
    show mar pirate sparkle:
        yalign 0.4
        xalign 0.5
    mar "Best ye speak up before I splice ye into smithereens"
    j "W-who are you?"
    hide mar pirate sparkle
    show mar pirate angry:
        yalign 0.4
        xalign 0.5
    mar "THE LEVEL OF DISRESPECT COMING FROM YER TRAP"
    mar "I'm the feared Nightmare Lancer of the Tyrant's Eye - Deus Highest Death Impact of the Seventh Resilience Crest Master of Spinjitsu Houshou Fitzgerald Lalatina Marine the Swashbuckler"
    hide mar pirate angry
    show mar pirate sparkle:
        yalign 0.4
        xalign 0.5
    mar "Now remember that ok?"
    mar "Repeat after me!"
    mar "Night-"
    j "N-night..."
    scene bg playground
    stop music fadeout 1.0
    show mar excite
    mar "-mare Lancer"
    j "Who is this... sassy lost child?"
    hide mar excite
    show mar angry
    mar "H-hey!!{w} {size=-7}At least play along for the name bit... I spent all day coming up with that...{/size}"
    mar "And!! I'll have you know I'm 4000 years old! (so you can go ahead and use that argument online i suppose but ymmv)"
    j "We are literally at a playground"
    mar "Humph. Mom said it was play time ok... Just follow 'long or I'll have you walk the plank!!"
    j "It's not nice to steal y'know...? Now give that piece of plywood back to whoever you sto-"
    mar "I've had enough!!!! Face me in a challenge this instant or off with your head!!"
    $ currentmonth = gettime.localtime(gettime.time())
    $ monthstr = gettime.strftime("%B", currentmonth)
    $ halloweendial = "Little early for Halloween don't cha think... It's only {}...".format(monthstr) if currentmonth.tm_mon < 10 else "Little late for Halloween don't cha think... It's already {}...".format(monthstr) if currentmonth.tm_mon > 10 else "Oh I guess it is October... Must be some Halloween thing..."
    j "[halloweendial]"
    show fortniteloli:
        xalign 0.1
        yalign 0.1
        xzoom 1.3
        yzoom 1.3
    mar "Just join my room already!!"
    scene black with fade
    call initgame({
        "game1401":["Youkai Watch", "Deltora Quest", "Future Card Buddyfight", "Ben 10: Omniverse"],
        "game1402":["Kira Kira Happy Hirake! Cocotama","Kamisama Minarai: Himitsu no Cocotama", "Mono no Kami-sama Cocotama", "Wonder Pets!"],
        "game1403":["Ojamajo Doremi Na-i-sho","Ojamajo Doremi Dokkaan","Motto! Ojamajo Doremi","Winx Club"],
        "game1404":["Barbapapa","BuBu ChaCha","Bonobono","Big Time Rush"],
        "game1405":["Kaiju Girls Season 2","Kaiju Step Wandabada","Wandaba Style","The Fairly OddParents"],
        "game1406":["Stitch! Itazura Alien no Daibouken","himitsukesshatakanotsume.jp","Hakata Mentai! Pirikarako-chan","Wow! Wow! Wubbzy!"],
        "game1407":["Ichigo Mashimaro", "Ichigo 100%", "Gal-gaku. II: Lucky Stars", "Strawberry Shortcake's Berry Bitty Adventures"],
        "game1408":["Totally Spies","Star vs. the Forces of Evil","Steven Universe","Phineas and Ferb"],
        "game1409":["Kim Possible", "The Legend of Korra", "Dexter's Laboratory", "Numb Chucks"],
        "game1410":["Pickle and Peanut", "Planet Sheen", "Fanboy & Chum Chum", "My Little Pony: A New Generation"]
    },[
        "Youkai Watch", "Mono no Kami-sama Cocotama", "Ojamajo Doremi Na-i-sho", "Bonobono", "Kaiju Step Wandabada", "Hakata Mentai! Pirikarako-chan", "Gal-gaku. II: Lucky Stars", "Jewelpet: Magical Change", "Beyblade Burst Sparking", "Eiga Precure Dream Stars!"
    ], gamebg="bg playground.jpg", randsong = True,fortniteloli=True) from _call_initgame_4
    ""
    "..."
    "......."
    "...................!"
    play sound "audio/alarm.mp3" 
    $ renpy.pause(3.0, hard=True)
    "So... bright..."
    scene bg bedroom2 with fade
    play music "audio/bgm11.mp3" volume 0.2 fadein 1.0 fadeout 1.0
    $ renpy.notify('♪ Comic Girls')
    "Just as the early morning sunlight filled the room through the windows beside me, I opened my eyes..."
    "Carried by a gentle breeze, a cherry blossom petal made its way onto the palm of my hand..."
    "Spring..."
    "Despite having lived here my entire life, never before had I seen the small town of Toyosato blanketed in a fluttering ocean of pink"
    "Like a scene from a movie... the Tokyo from 5 Centimeters per Second comes to mind..."
    "And in that sort of cliché sense, starting today, I would finally become a high school student."
    "With that, I closed the door behind me, and made my way to the entrance ceremony."
    play sound "audio/door.mp3"
    stop music fadeout 1.0
    $ renpy.pause(0.6, hard=True)
    scene black with fade
    $ renpy.movie_cutscene("newbeginning.webm")
    play sound "audio/bell.mp3"
    scene bg musicroom with Fade(3.0, 0.0, 3.0)
    "It was on that day, however, that I met them..."
    "Looking for a club to join, I climbed the stairs up to the music room..."
    scene bg musicroom2 with fade
    show kon_ritsu with moveinright:
        xalign 0.9
        yalign 1.0
    rit "Ah! You're the freshman aren't ya? I see you brought your guitar, do you play?"
    show kon_mio with moveinleft
    "Mio" "We're just about to practice too, why don't you stay for a bit"
    show kon_mugi with moveinleft:
        xalign 0.1
        yalign 1.15
    "Mugi" "And perhaps stay for some tea as well~"
    "You" "Ehhhh.... I don't know that many songs though, compared to you guys I'm a total beginner!"
    rit "Relax~ We mostly play anime openings around here, so there's gotta be at least some you recognise..."
    rit "How's about you sit through our practice today, then you can decide if you wanna join us"
    "Mugi" "Oh~ Tea's ready!"
    rit "Well, we'll get started {i}eventually...{/i}"
    scene bg perform with fade
    rit "Well then, after 12 entire cakes and the entire Asian continent's worth of tea gone, let's get started!"
    call initgamenodd({
        "game1501":["rakudai kishi no cavalry","chivalry of a failed knight","yrlavac on ihsik iadukar","thgink deliaf a fo yrlavihc"],
        "game1502":["baka to test to shoukanjuu","baka & test: summon the beasts","uujnakuohs ot tset ot akab","stsaeb eht nommus :tset & akab"],
        "game1503":["nanbaka", "the numbers","akabnan","srebmun eht"],
        "game1504":["amagami ss+","+ss imagama"],
        "game1505":["2.43: seiin koukou danshi volley-bu","2.43: seiin high school boys volleyball team","ub-yellov ihsnad uokuok niies :34.2","maet llabyellov syob loohcs hgih niies :34.2"]
    },gamebg="bg perform.jpg", keion=True) from _call_initgamenodd_6
    centered "You begin to feel lightheaded..."
    play sound "audio/drop.mp3"
    ""
    "..."
    "........."
    "..................?!"
    call thirddream from _call_thirddream
    scene bg ruins with fade
    show hik scholar at right with moveinright
    hik "Congrats! For getting every song right you've managed to finish 7th in today's Ranked Death Match!"
    hik "{s}Though half of those songs were namedrops anyway{/s}"
    j "So that means I've done it? I've beat everyone? I've saved my clan?"
    hik "lol no that was just todays game you have to come back here every day without fail for the next month and pray your connection never dies"
    hik "also only the top 3 get rewarded anyway soo"
    hik "but hey at least you're not dead"
    j "I'm starting to wish I... {cps=*0.5}was{/cps}{cps=*0.25}...{/cps}"
    scene black 
    $ renpy.pause(0.3, hard=True)
    scene bg ruins
    $ renpy.pause(0.3, hard=True)
    scene black with fade
    scene black 
    $ renpy.pause(0.3, hard=True)
    scene bg ruins
    $ renpy.pause(0.3, hard=True)
    scene black with fade
    scene black 
    $ renpy.pause(0.3, hard=True)
    scene bg ruins
    $ renpy.pause(0.3, hard=True)
    scene black
    play sound "audio/drop.mp3"
    ""
    centered "The ringing grows louder..."
    "..."
    "......."
    "..............?"
    scene bg movies with Fade(2.0, 0.0, 2.0)
    "Club Leader" "Alright minna-san, welcome to the biweekly Ouran High School Anime Society groupwatch!"
    "Club Leader" "Today we'll be watching, by popular demand, the latest episode (#1122) of Crayon Shin-chan!"
    play sound "audio/legalanime.mp3" volume 0.5
    "Club Member #1" "I've got my popcorn ready"
    "Club Member #2" "You gonna join us, Jin?"
    "Club Member #3" "We better start soon... Jin looks so bored he might just actually start watching Love Live unironically"
    j "You know of all the nightmares so far this is probably the scariest..."
    scene black
    centered "Oi...."
    centered "He's really out cold huh..."
    centered "I guess it can't be helped then..."
    scene bg bedroom 
    show noe think at right
    show kom think at left
    "..."
    noe "Oh, there you are!"
    kom "We thought you were a goner..."
    noe "I know I said to get some good rest but I didn't mean to sleep in till noon..."
    kom "And you were sweating and mumbling to yourself the whole time too... What happened?"
    "..."
    noe "Eh...?! Another nightmare?"
    kom "The spirit of the {b}SOLID GOLD HIBIKI{/b} must be getting stronger..."
    noe "This is bad... If this gets any worse... it's gonna... *gasp*"
    kom "No... it can't be..."
    noe "We have to save him..."
    noe "Before..."
    noe "{cps=*0.3}Before he becomes... an Inserts only player{/cps}"
    scene black with fade