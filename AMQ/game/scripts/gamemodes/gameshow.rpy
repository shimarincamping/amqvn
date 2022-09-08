label gameshow:
    $ prizes = [0, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]
    $ prizelevel = 0
    $ currentquestion = 1
    $ numofquestions = 10
    $ questions = {
        "How many song segments were played?":["12", "14", "16", "18"],
        "Which anime's opening was played as a start sample?":["Usagi Drop", "Amagi Brilliant Park", "Little Witch Academia", "Stella no Mahou"],
        "What anime's opening was the 5th song that was played?":["Umineko no Naku Koro ni", "91 Days", "pet", "Scan2Go"],
        "Which of the following anime did NOT have its opening play?":["Shadows House", "Fate/kaleid liner Prisma☆Illya 2wei!", "Ano Hi Mita Hana no Namae o Boku-tachi wa Mada Shiranai.", "Hakata Tonkotsu Ramens"],
        "Which anime's opening had the longest played sample?":["Amagi Brilliant Park", "Little Busters!", "Macross Dynamite 7", "Little Busters! EX"],
        "Which artist performed more than one song that was played?":["Minami Kuribayashi", "TRUE", "Kishida Kyoudan &THE Akeboshi Rockets", "TK from Ling Tosite Sigure"],
        "In which position did the non-Japanese song play?":["6th","8th","9th","11th"],
        "In which position did the instrumental song play?":["12th", "13th", "14th", "15th"],
        "How many anime played have a number in the title?":["1", "2", "3", "4"],
        "The opening to which anime played twice?":["Hakata Tonkotsu Ramens","Kikou Shoujo wa Kizutsukanai","Ghost Hunt","The World of GOLDEN EGGS"],
    }
    $ answers = ["C","B","A","A","D","C","C","C","D","B"]
    narrator "..."
    narrator "......"
    narrator ".........?"
    play music "audio/bgm04.mp3" fadein 1.0 fadeout 1.0 volume 0.2
    $ renpy.notify('♪ Buzzer Beater')
    scene bg gameshow with fade
    show gsyuk at left with moveinleft
    gsyuk "And here we have our next contestant on... {b}Who Wants to Be An AMQ Booli?{/b}"
    j "W-where am I...?"
    gsyuk "The rules are simple! You listen to the copyrighted music, you answer some lazily-written questions! Get them all right and the million's yours!"
    gsyuk "That's before taxes of course, tehe~"
    gsyuk "Our special guest here has clocked in over 6300 hours on AMQ since December of 2017, and has a promising guess rate of 31.52\%"
    gsyuk "Let's see if they've got what it takes to become the world's next certified AMQ booli!"
    j "Ayo that's a lotta money I could win... That's like 2 whole ten-pulls in Genshin..."
    gsyuk "Now... shush, shush."
    stop music
    gsyuk "You're about to hear a 96-second audio clip full of bits and pieces of AMQ songs! Now pay attention, cus it's not gonna play a second time!"
    gsyuk "Take down some notes, cram it all in your head, do whatever! Just be prepared for the 11 questions afterwards~"
    gsyuk "Good luck!!"
    hide gsyuk with moveoutleft
    window hide
    play sound "audio/gameshow.mp3" fadein 1.0 fadeout 1.0
    $ timeleft = 96
    $ timer_range = 96
    show screen countdown2
    $ renpy.pause(96, hard=True)
    hide screen countdown2
    stop sound fadeout 1.0
    show gsyuk at right with moveinright
    gsyuk "Ready? Let's get this cursed show on the road~"
    play music "audio/bgm05.mp3" fadein 1.0 fadeout 1.0 volume 0.2
    $ renpy.notify('♪ Nana Maru San Batsu')
    while currentquestion <= numofquestions:
        $ questiontext = list(questions.keys())[currentquestion-1]
        $ option1 = list(questions.values())[currentquestion-1][0]
        $ option2 = list(questions.values())[currentquestion-1][1]
        $ option3 = list(questions.values())[currentquestion-1][2]
        $ option4 = list(questions.values())[currentquestion-1][3]
        $ correctanswer = answers[currentquestion-1]
        narrator "Question [currentquestion] of 11"
        menu:
            "[questiontext]"
            "[option1]":
                $ selectedans = "A"
            "[option2]":
                $ selectedans = "B"
            "[option3]":
                $ selectedans = "C"
            "[option4]":
                $ selectedans = "D"
        if selectedans == correctanswer:
            gsyuk "Your answer is{cps=*0.5}.....{/cps} CORRECT!"
            $ prizelevel += 1
        else:
            gsyuk "Your answer is{cps=*0.5}.....{/cps} incorrect..."
            gsyuk "Let's keep going though~ You've still got big money to win!"
        $ currentprize = prizes[prizelevel]
        gsyuk "Current earnings: {b}[currentprize] notes{/b}"
        $ currentquestion += 1
    gsyuk "...And now for the final question"
    stop music fadeout 1.0
    gsyuk "Get ready, this is the biggest one yet!"
    menu:
        "What do you think of Yukari?"
        "I love Yukari!!!!":
            gsyuk "Wha-!!"
        "I only ever use Yukari skins, the rest are trash":
            gsyuk "Now that I can agree with"
        "Every day I wake up and bow down to my shrine of Yukari merch consisting of 30 copies of the same silhouette shirt made from pre-shrunk 100\% Cotton and available for only $28.12 before shipping":
            gsyuk "Ok this is... mildly concerning... but..."
        "Ew furry avatar":
            gsyuk "..."
            scene black
            gsyuk "Get out of my game show"
            centered "DrNyanpasu Ending"
            show drnyanpasu at truecenter with fade
            ""
            $ MainMenu(confirm=False)()
    $ prizelevel += 1
    $ currentprize = prizes[prizelevel]
    $ xpgain = prizelevel * 10
    $ globalpoints += xpgain
    gsyuk "I-I'm glad you think so, of course I was just asking this for a friend nya-"
    gsyuk "Ahem"
    gsyuk "Your answer is{cps=*0.5}.....{/cps} CORRECT!"
    gsyuk "Congratulations! You are now officially the world's next certified AMQ BOOLI and {b}[currentprize] notes{/b} richer!!"
    gsyuk "{cps=*0.5}Richer!! ... {/cps}{cps=*0.25} richer ...{/cps}{cps=*0.125} r i c h e r . . . . .{/cps}"
    scene black with Fade(2.0, 0.0, 2.0)
    return