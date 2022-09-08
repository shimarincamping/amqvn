label mizukibattle:
    scene bg shrineblur with fade
    narrator "--- Boss information ---\nName: Mizuki"
    narrator "Rules: 10 second time limit; 3 lives"
    narrator "Specialty: Quick-Time"
    show miz shrine at right with moveinright
    miz "Hope you're ready! I know I am~"
    $ gamepoints = 0
    $ currentsong = 1
    $ numofsongs = 10
    $ songdict = {
        "game501" : ["Flip Flappers", "Shokugeki no Souma: San no Sara", "Chuunibyou demo Koi ga Shitai! Ren", "Trinity Seven"],
        "game502" : ["Toaru Kagaku no Railgun S", "Owari no Seraph: Nagoya Kessen-hen", "Black Bullet", "Toaru Kagaku no Railgun T"],
        "game503" : ["Kekkaishi", "Kokkoku", "Kekkai Sensen", "Kakkou no Iinazuke"],
        "game504" : ["Magia Record: Mahou Shoujo Madoka☆Magica Gaiden", "Classroom☆Crisis", "Demi-chan wa Kataritai", "Denpa Kyoushi"],
        "game505" : ["Mahouka Koukou no Rettousei", "Back Arrow", "Genei wo Kakeru Taiyou", "Qualidea Code"],
        "game506" : ["Mewkledreamy", "Waccha PriMagi!", "Idol Time PriPara", "Kiratto Pri☆chan"],
        "game507" : ["Hanasaku Iroha", "Non Non Biyori Nonstop", "Bakuman.", "Sankarea"],
        "game508" : ["Senki Zesshou Symphogear G", "Senki Zesshou Symphogear GX", "Senki Zesshou Symphogear XV", "Senki Zesshou Symphogear AXZ"],
        "game509" : ["Yuusha-Oh GaoGaiGar", "Yuusha-Oh GaoGaiGar Final", "Yuusha-Oh GaoGaiGar Final Grand Glorious Gathering", "Gintama'"],
        "game510" : ["Tottoko Hamtarou", "Tottoko Hamtarou: Ham-Ham Paradi-chu! Hamtarou to Fushigi no Oni no Ehonto", "Tottoko Hamtarou: Ham-Ham Land Daibouken", "Tottoko Hamtarou Anime Dechu!"]
    }
    $ anslist = ["Chuunibyou demo Koi ga Shitai! Ren","Toaru Kagaku no Railgun T","Kokkoku","Magia Record: Mahou Shoujo Madoka☆Magica Gaiden","Qualidea Code","Waccha PriMagi!","Bakuman.","Senki Zesshou Symphogear GX","Yuusha-Oh GaoGaiGar","Tottoko Hamtarou Anime Dechu!"]
    $ dial = ["Not bad, but can you do 9 more?","","Be sure to take your time\nJust not too much time~","","You're doing better than I thought\nThe last guy didn't make it this far","","Looks like I'll have to get serious with you","Only hard songs from here on out","I've saved my special attack for last...","a"]
    $ lives = 3
    while currentsong <= numofsongs and lives > 0:
        $ ontime = True
        $ savedans = ""
        narrator "Song [currentsong] of [numofsongs]"
        $ songaudio = (list(songdict.items()))[currentsong-1][0]
        $ renpy.music.play("audio/" + songaudio + ".mp3")
        $ option1 = (list(songdict.items()))[currentsong-1][1][0]
        $ option2 = (list(songdict.items()))[currentsong-1][1][1]
        $ option3 = (list(songdict.items()))[currentsong-1][1][2]
        $ option4 = (list(songdict.items()))[currentsong-1][1][3]
        $ timeleft = 10
        $ timer_range = 10
        $ timer_jump = "outoftime"
        show screen countdown
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
        if not savedans:
            label outoftime:
                $ ontime = False
                $ lives -= 1
                narrator "Too slow... Current score: [gamepoints]\nLives: [lives]"
        if savedans == anslist[currentsong-1] and ontime:
            $ gamepoints += 10
            narrator "Correct! Current score: [gamepoints]\nLives: [lives]"
        elif ontime:
            $ lives -= 1
            narrator "Nope... Current score: [gamepoints]\nLives: [lives]"
        if dial[currentsong-1]:
            if currentsong >= 7:
                hide miz shrine
                show miz shrine attack at right 
            $ currentdial = dial[currentsong-1]
            miz "[currentdial]"
        $ currentsong += 1
    if lives > 0:
        $ xpgain = int(round(gamepoints * (0.5+(0.5 * lives)),0))
        $ globalpoints += xpgain
        stop music fadeout 1.0
        scene black with fade
        return
    else:
        stop music fadeout 1.0
        miz "Oh! I almost didn't notice"
        miz "Looks like it's my win! Not like I had any doubts though~"
        miz "Now then..."
        scene bg dead with Fade(2.0, 0.0, 2.0)
        show miz shrine attack at right
        $ renpy.pause(1.8, hard=True)
        miz "{cps=5}Goodbye{/cps}"
        $ MainMenu(confirm=False)()