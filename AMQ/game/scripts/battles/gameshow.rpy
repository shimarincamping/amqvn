label gameshow:
    $ prizes = [0, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]
    $ prize_level = 0
    $ curr_question = 1
    
    $ question_list = game_settings["ch3"]["gameshow"]
    $ question_count = len(question_list) + 1
    
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
    
    call countdown(96.0, None, {"xalign":0.5, "yalign":0.1, "xmaximum":1350})
    
    $ renpy.pause(96, hard=True)
    hide screen countdown
    stop sound fadeout 1.0

    show gsyuk at right with moveinright
    gsyuk "Ready? Let's get this cursed show on the road~"
    
    play music "audio/bgm05.mp3" fadein 1.0 fadeout 1.0 volume 0.2
    $ renpy.notify('♪ Nana Maru San Batsu')
    
    while curr_question <= question_count-1:
        $ question = question_list[curr_question-1]

        $ questiontext = question["question"]
        $ options = question["option"]

        narrator "Question [curr_question] of [question_count]"
        
        menu:
            "[questiontext]"
            "[options[0]]":
                $ answer = "A"
            "[options[1]]":
                $ answer = "B"
            "[options[2]]":
                $ answer = "C"
            "[options[3]]":
                $ answer = "D"
        
        if answer == question["answer"]:
            gsyuk "Your answer is{cps=*0.5}.....{/cps} CORRECT!"
            $ prize_level += 1
        
        else:
            gsyuk "Your answer is{cps=*0.5}.....{/cps} incorrect..."
            gsyuk "Let's keep going though~ You've still got big money to win!"

        $ curr_prize = prizes[prize_level]
        
        gsyuk "Current earnings: {b}[curr_prize] notes{/b}"
        
        $ curr_question += 1
    
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
    
    $ prize_level += 1
    $ curr_prize = prizes[prize_level]
    $ global_points += prize_level * 10

    gsyuk "I-I'm glad you think so, of course I was just asking this for a friend nya-"
    gsyuk "Ahem"
    gsyuk "Your answer is{cps=*0.5}.....{/cps} CORRECT!"
    gsyuk "Congratulations! You are now officially the world's next certified AMQ BOOLI and {b}[curr_prize] notes{/b} richer!!"
    gsyuk "{cps=*0.5}Richer!! ... {/cps}{cps=*0.25} richer ...{/cps}{cps=*0.125} r i c h e r . . . . .{/cps}"
    
    scene black with Fade(2.0, 0.0, 2.0)
    return