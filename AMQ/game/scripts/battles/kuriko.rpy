label kurikobattle:
    $ game_points = 0

    menu:
        "Please choose your difficulty"
        "Forgiving (100 points)":
            $ point_goal = 100
            $ multiplier = 0.33
        "Comfy (160 points)":
            $ point_goal = 160
            $ multiplier = 0.67
        "Normal (220 points)":
            $ point_goal = 220
            $ multiplier = 1.0
        "Challenge (280 points)":
            $ point_goal = 280
            $ multiplier = 1.5
        "Veteran (350 points)":
            $ point_goal = 350
            $ multiplier = 2.0
        "Perfect (420 points)":
            $ point_goal = 420
            $ multiplier = 3.0
    
    narrator "--- Boss information ---\nName: Valkyrie Miyu"
    narrator "Specialty: Brain-Damage"
    
    scene bg quiz1 with fade
    
    show vmiy2 at right with moveinright
    miy "Ohayou minna~ Kitekurete arigatou~"
    miy "It's me, sonicyellow, back with another positively subarashii~ anime openings quiz for you guys!!"
    j "Oh nyo..."
    miy "In any case, let's get right to it shall we~! Hope everyone's ready!"
    
    show screen sectionheader(1, "Difficulty: 45-100%\nModifiers: none\n\n6 songs / +5 points each\n10 second time limit")
    ">>> Begin Stage 1 <<<"
    hide screen sectionheader
    
    $ curr_song = 1
    $ song_count = 6
    $ guess_time = 10

    $ total_song = curr_song
    $ total_song_count = song_count
    
    $ song_list = game_settings["ch5"]["kuriko"]["battle1"]
    $ renpy.random.shuffle(song_list)
    
    while curr_song <= song_count:
        $ song = song_list[curr_song-1]
        $ answer = ""
        
        show screen songnumbertext(total_song, total_song_count)

        $ renpy.sound.play("audio/" + song["audio"] + ".mp3")
        
        call countdown(guess_time, "stage1_outoftime", None, True)
        call screen noddinput
        
        $ answer = _return.lower().strip()

        hide screen countdown3
        hide screen songnumbertext

        if answer in song["answer"]:
            $ game_points += 5
            show screen correctscreen(_return)
            ">>> Click to continue <<<"
            hide screen correctscreen

        else:
            $ answers = " / ".join(song["answer"])
            show screen wrongscreen(_return, answers)
            ">>> Click to continue <<<"
            hide screen wrongscreen
        
        if False:
            label stage1_outoftime:
                hide screen countdown3
                hide screen songnumbertext
                hide screen countdown3
                show screen notime
                ">>> Click to continue <<<"
                hide screen notime
        
        $ curr_song += 1
        $ total_song += 1
    
    stop music fadeout 1.0
    scene bg quiz2 with fade
    
    show vmiy2 at right with moveinright
    miy "Hai~~ hope everyone had a good warm up! Now it's time to get this quiz {i}really{/i} started!"
    
    show screen sectionheader(2, "Difficulty: 32-45%\nModifiers: 4x speed, 6s sample\n\n7 songs / +10 points each\n15 second time limit")
    ">>> Begin Stage 2 <<<"
    hide screen sectionheader
    
    $ curr_song = 1
    $ song_count = 7
    $ guess_time = 15

    $ total_song_count += song_count

    $ song_list = game_settings["ch5"]["kuriko"]["battle2"]
    $ renpy.random.shuffle(song_list)

    while curr_song <= song_count:
        $ song = song_list[curr_song-1]
        $ answer = ""
        
        show screen songnumbertext(total_song, total_song_count)

        $ renpy.sound.play("audio/" + song["audio"] + ".mp3")
        
        call countdown(guess_time, "stage2_outoftime", None, True)
        call screen noddinput
        
        $ answer = _return.lower().strip()

        hide screen countdown3
        hide screen songnumbertext

        if answer in song["answer"]:
            $ game_points += 10
            show screen correctscreen(_return)
            ">>> Click to continue <<<"
            hide screen correctscreen

        else:
            $ answers = " / ".join(song["answer"])
            show screen wrongscreen(_return, answers)
            ">>> Click to continue <<<"
            hide screen wrongscreen
        
        if False:
            label stage2_outoftime:
                hide screen countdown3
                hide screen songnumbertext
                hide screen countdown3
                show screen notime
                ">>> Click to continue <<<"
                hide screen notime
        
        $ curr_song += 1
        $ total_song += 1
    
    stop sound fadeout 1.0
    scene bg quiz3 with fade
    
    show vmiy2 at right with moveinright
    miy "Hmmm... maybe that was too easy for you after all... Let's change things up a little!"
    
    show screen sectionheader(3, "Difficulty: 20-32%\nModifiers: double-layered gamemode (guess two songs at once)\n\n6 pairs of songs / +10 points for each correct answer\n15 second time limit")
    ">>> Begin Stage 3 <<<"
    hide screen sectionheader
    
    $ curr_song = 1
    $ song_count = 6
    $ guess_time = 15

    $ total_song_count += song_count

    $ song_list = game_settings["ch5"]["kuriko"]["battle3"]
    $ renpy.random.shuffle(song_list)

    while curr_song <= song_count:
        $ song = song_list[curr_song-1]
        $ answer = ""
        
        show screen songnumbertext(total_song, total_song_count)

        $ renpy.sound.play("audio/" + song["audio"] + ".mp3")
        
        call countdown(guess_time, "stage3_outoftime", None, True)
        
        call screen noddinput("Enter your first answer:")
        $ raw_answer1 =_return.strip()
        $ answer1 = raw_answer1.lower()
        
        call screen noddinput("Enter your first answer:")
        $ raw_answer2 =_return.strip()
        $ answer2 = raw_answer2.lower()

        hide screen countdown3
        hide screen songnumbertext
        
        if (answer1 in song["answer"][0] and answer2 in song["answer"][1]) or (answer1 in song["answer"][1] and answer2 in song["answer"][0]):
            # Both correct
            $ game_points += 20

            show screen answerlabel("FIRST ANSWER")
            show screen correctscreen(rawans1)
            ">>> Click to continue <<<"

            hide screen answerlabel
            hide screen correctscreen
            show screen answerlabel("SECOND ANSWER")
            show screen correctscreen(rawans2)
            ">>> Click to continue <<<"

            hide screen answerlabel
            hide screen correctscreen

        elif (answer1 in song["answer"][0] and answer2 in song["answer"][1]) or (answer1 in song["answer"][1] and answer2 in song["answer"][0])
            # First correct, second wrong
            $ answers = ["(Song 1) " + i for i in song["answer"][0]] + ["(Song 2) " + i for i in song["answer"][1]]
            $ answers = "\n".join(answers)
            
            $ game_points += 10

            if (answer1 in song["answer"][0] and answer2 in song["answer"][1]):
                $ correct_answer = answer1
                $ wrong_answer = answer2
            else:
                $ correct_answer = answer2
                $ wrong_answer = answer1
            
            show screen answerlabel("CORRECT ANSWER")
            show screen correctscreen(correct_answer)
            ">>> Click to continue <<<"

            hide screen answerlabel
            hide screen correctscreen
            show screen answerlabel("WRONG ANSWER")
            show screen wrongscreen(wrong_answer, answers)
            ">>> Click to continue <<<"

            hide screen answerlabel
            hide screen wrongscreen

        else:
            $ answers = ["(Song 1) " + i for i in song["answer"][0]] + ["(Song 2) " + i for i in song["answer"][1]]
            $ answers = "\n".join(answers)

            # Both wrong
            show screen answerlabel("FIRST ANSWER")
            show screen wrongscreen(rawans1, answers)
            ">>> Click to continue <<<"

            hide screen answerlabel
            hide screen wrongscreen
            show screen answerlabel("SECOND ANSWER")
            show screen wrongscreen(rawans2, answers)
            ">>> Click to continue <<<"

            hide screen answerlabel
            hide screen wrongscreen

        if False:
            label stage3_outoftime:
                hide screen countdown3
                hide screen songnumbertext
                hide screen countdown3
                show screen notime
                ">>> Click to continue <<<"
                hide screen notime
    
        $ curr_song += 1
        $ total_song += 1

    stop music fadeout 1.0

    scene bg quiz4 with fade

    show vmiy2 at right with moveinright
    miy "This video already has 23 copyright strikes, that's a new record!"
    
    show screen sectionheader(4, "Difficulty: 0-20%\nModifiers: reverse audio\n\n7 songs / +20 points each\n15 second time limit")
    ">>> Begin Stage 4 <<<"
    hide screen sectionheader
    
    $ curr_song = 1
    $ song_count = 7
    $ guess_time = 15

    $ total_song_count += song_count

    $ song_list = game_settings["ch5"]["kuriko"]["battle4"]
    $ renpy.random.shuffle(song_list)
    
    while curr_song <= song_count:
        $ song = song_list[curr_song-1]
        $ answer = ""
        
        show screen songnumbertext(total_song, total_song_count)

        $ renpy.sound.play("audio/" + song["audio"] + ".mp3")
        
        call countdown(guess_time, "stage4_outoftime", None, True)
        call screen noddinput
        
        $ answer = _return.lower().strip()

        hide screen countdown3
        hide screen songnumbertext

        if answer in song["answer"]:
            $ game_points += 20

            show screen correctscreen(_return)
            ">>> Click to continue <<<"

            hide screen correctscreen

        else:
            $ answers = " / ".join(song["answer"])
            show screen wrongscreen(_return, answers)
            ">>> Click to continue <<<"

            hide screen wrongscreen

        if False:
            label stage4_outoftime:
                hide screen countdown3
                hide screen songnumbertext
                hide screen countdown3
                show screen notime
                ">>> Click to continue <<<"
                hide screen notime

        $ curr_song += 1
        $ total_song += 1
    
    stop music fadeout 1.0
    
    scene bg quiz5 with fade
    
    show vmiy2 at right with moveinright
    miy "Well, we're almost done~ For our last segment, we have songs that our lovely viewers submitted in for us!"
    miy "Let's see what kind of wonderful music our talented AMQ players love listening to~"
    
    show screen sectionheader(5, "Difficulty: 0-25%\nModifiers: none (fan-requested songs)\n\n4 songs / +15 points each\n15 second time limit")
    ">>> Begin Stage 5 <<<"
    hide screen sectionheader
    
    $ curr_song = 1
    $ song_count = 4
    $ guess_time = 15

    $ total_song_count += song_count

    $ song_list = game_settings["ch5"]["kuriko"]["battle4"]
    $ renpy.random.shuffle(song_list)

    while curr_song <= song_count:
        $ song = song_list[curr_song-1]
        $ answer = ""
        
        show screen songnumbertext(total_song, total_song_count)

        $ renpy.sound.play("audio/" + song["audio"] + ".mp3")
        
        call countdown(guess_time, "stage5_outoftime", None, True)
        call screen noddinput
        
        $ answer = _return.lower().strip()

        hide screen countdown3
        hide screen songnumbertext

        if answer in song["answer"]:
            $ game_points += 25

            show screen correctscreen(_return)
            ">>> Click to continue <<<"

            hide screen correctscreen

        else:
            $ answers = " / ".join(song["answer"])
            show screen wrongscreen(_return, answers)
            ">>> Click to continue <<<"

            hide screen wrongscreen

        if False:
            label stage5_outoftime:
                hide screen countdown3
                hide screen songnumbertext
                hide screen countdown3
                show screen notime
                ">>> Click to continue <<<"
                hide screen notime

        $ curr_song += 1
        $ total_song += 1

    if game_points >= point_goal:
        $ points_percentage = 100
        
        show screen gameend("You win!","#bcff7d")
        miy "Eeeeeh... Looks like you won! Don't forget to subscribe~"
        
        $ weighted = game_points * multiplier
        $ global_points += int(round(weighted))
    
    else: 
        $ points_percentage = round(game_points / point_goal * 100, 2)
        show screen gameend("You lost...", "#ff7070")
        miy "Looks like you made a mistake coming to my channel today~ See you next time, ok?"
        $ MainMenu(confirm=False)()
    
    hide screen gameend
    stop music fadeout 1.0
    
    scene black with fade
    return