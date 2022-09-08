label thirddream:
    $ isdead = False
    centered "Year: 24XX"
    centered "Amidst the chaos and calamity of the Great Warring Epoch, warriors clash in the centre of what once was the Advanced Technological State"
    centered "Someone please help me I'm running out of AMQ lore to plagiarise"
    scene bg ruins with fade
    play music "audio/bgm12.mp3" volume 0.15 fadein 1.0 fadeout 1.0
    $ renpy.notify('♪ Hataage! Kemono Michi')
    "???" "And now... our next contender in the arena!!"
    show shik1 at right with moveinright
    hik "You're new to this whole thing right? Lemme tell you how everything works..."
    j "Have I been... isekai'd...?"
    hik "No, worse..."
    j "SO YOU'RE TELLING ME EVERYONE HERE'S A NANA MIZUKI FAN?!"
    hik "Ok maybe not {i}that{/i} bad... You're just in a fight to the death battle to save your clan from being wiped out entirely"
    j "Oh, so just another Tuesday, got it"
    hik "You only have one life though... Make a single mistake and it's game over for you, you got that?"
    j "Sure sure, I got this, how hard can it be?"
    hik "Looks like we're all good here then, lemme get your opponents in"
    hik "Shuuka! watashiii! Rukawa!!"
    stop music fadeout 1.0
    hide shik1 with moveoutright
    if False:
        label dream_death:
            stop music fadeout 1.0
            hide screen cp_button
            scene bg ruins with fade
            show shik1 at right with moveinright
            hik "Welp... Looks like you didn't have what it takes after all..."
            hik "You missed a free and now you're out of Box 1"
            hik "No amount of Shazamming can help you now... Goodbye."
            scene dreamdeathscreen with Fade(2.0, 0.0, 2.0)
            ""
            "...."
            "I have seen the other side... It can wait."
            scene bg ruins with fade
            $ isdead = True
    if isdead:
        "--- Death Match Begin Again ---"
    else:
        "--- Death Match Begin ---"
    $ gamepoints = 0
    $ currentsong = 1
    $ numofsongs = 12
    $ songdict = {
        "game1601":["animal 1"],
        "game1602":["space runaway ideon","densetsu kyojin ideon"],
        "game1603":["big x"],
        "game1604":["jetter mars"],
        "game1605":["aggretsuko: we wish you a metal christmas","aggressive retsuko: we wish you a metal christmas"],
        "game1606":["oh! super milk-chan", "the super milk chan show"],
        "game1607":["thermae romae novae"],
        "game1608":["uchuu senkan yamato","star blazers","uchuu senkan yamato 2","star blazers: the bolar wars","uchuu senkan yamato 3","star blazers: space battleship yamato 2199","uchuu senkan yamato 2199","space battleship yamato 2199: voyage of remembrance","uchuu senkan yamato 2199: tsuioku no koukai","space battleship yamato","space cruiser: guardian of the galaxy","star blazers: the quest for iscandar","uchuu senkan yamato 2205: aratanaru tabidachi"],
        "game1609":["wish"],
        "game1610":["winter sonata","fuyu no sonata"],
        "game1611":["iron man"],
        "game1612":["47 todoufuken r"],
        "game1613":["knights of sidonia: battle for planet nine", "sidonia no kishi: dai-kyuu wakusei seneki"],
        "game1614":["super dimension century orguss", "choujikuu seiki orguss"],
        "game1615":["skyers 5"],
        "game1616":["tetsujin 28-go", "gigantor"],
        "game1617":["soccer fever"],
        "game1618":["kenzen robo daimidaler","daimidaler the sound robot","daimidaler: prince vs. penguin empire"],
        "game1619":["chirin no suzu","ringing bell"],
        "game1620":["keroro"],
        "game1621":["the story of young hanada","hanada shounen-shi"],
        "game1622":["himitsu no akko-chan"],
        "game1623":["kemono to chat"]
    }
    while len(songdict) > numofsongs:
        $ popped = renpy.random.randint(1, len(songdict))
        $ poppedkey = list(songdict.keys())[popped-1]
        $ songdict.pop(poppedkey)
    $ songtup = list(songdict.items())
    $ renpy.random.shuffle(songtup)
    $ songdict = dict(songtup)
    while currentsong <= numofsongs:
        if currentsong == 1 and not isdead:
            show bnoe1 with moveinleft
            noe "Psst!! Hey! Hey!"
            j "Wha!! Noel!! I can't believe you're here! I must be dreaming :')"
            noe "Well, you kinda are..."
            noe "Anyway, I took a sneaky peek at what songs they were gonna play here, and I literally have no clue who even watches this shit"
            noe "So~~~ How's about we bend a rules a little?"
            noe "If you ever need help I'll DM you the answers, just don't let Steph find out"
            noe "Here's your handy dandy Co-Op Button, now good luck out there!"
            $ cpbutton_beforegame = True
            show screen cp_button
            hide bnoe1 with moveoutleft
        narrator "Song [currentsong] of [numofsongs]"
        $ currentques = (list(songdict.items()))[currentsong-1][0]
        $ currentans = (list(songdict.items()))[currentsong-1][1]
        $ renpy.music.play("audio/" + currentques + ".mp3")
        show screen cp_button
        $ cpbutton_beforegame = False
        $ ans = None
        while ans is None:
            call screen noddinput
            $ ans = _return
        $ ans = _return.lower().strip()
        hide screen cp_button
        if ans in currentans:
            $ gamepoints += 10
            narrator "Correct! Current score: [gamepoints]"
        else:
            narrator "Nope... That ain't right..."
            $ allans = " / ".join(currentans)
            if currentques == "game1608":
                narrator "Correct answer(s):\n{size=-12}[allans]{/size}"
            else:
                narrator "Correct answer(s):\n{size=-8}[allans]{/size}"
            jump dream_death
        $ currentsong += 1
    stop music fadeout 1.0
    hide screen cp_button
    $ globalpoints += gamepoints
    scene black with fade
    return
