label ritsubattle:
    scene bg arcade with fade

    menu:
        "Please choose your difficulty"
        "Litterbox (5 lives, long sample)":
            $ lives = 5
            $ sample = 1.5
            $ total_sample = 5
            $ multiplier = 0.5
        "Easy (3 lives, long sample)":
            $ lives = 3
            $ sample = 1.5
            $ total_sample = 5
            $ multiplier = 1.0
        "Medium (3 lives, normal sample)":
            $ lives = 3
            $ sample = 1
            $ total_sample = 4
            $ multiplier = 1.5
        "Hard (2 lives, normal sample)":
            $ lives = 2
            $ sample = 1
            $ total_sample = 4
            $ multiplier = 1.75
        "Impossible (2 lives, short sample)":
            $ lives = 2
            $ sample = 0.5
            $ total_sample = 3
            $ multiplier = 2.25
        "Inazuma Eleven (1 life, short sample)":
            $ lives = 1
            $ sample = 0.5
            $ total_sample = 3
            $ multiplier = 2.5
    
    $ dial = [
        "Faster~",
        "",
        "",
        "*insert gamer girl dialogue here, idk does it look like i have a discord gf or smth",
        "",
        "This is... definitely one of the moments of all time",
        "um ackshualy its op 42 of meitantei conan :nerd_emoji:",
        "",
        "",
        "imagine getting a gaming setup and using it to play amq all day, just sell that gpu already",
        "youre welcome for all that shitty audio compression btw",
        "",
        "komugi asked me to leave her discordhere go add her Komugi#9780",
        "",
        "my favorite ranked meme is when catbox fucking dies",
        "",
        "you look like the kind of person to always, without fail, submit alfa-x for evangelion",
        "yearly reminder to clean your room",
        "...",
        "",
    ]

    $ guess_time = total_sample - sample
    
    narrator "--- Boss information ---\nName: Ritsu"
    narrator "Rules: [sample]s sample, [guess_time]s guessing time"
    narrator "Specialty: ?????"
    
    show rit smug at right with moveinright
    rit "Let's see how long you last Buni"

    $ game_points = 0
    $ curr_song = 1
    $ song_count = 20
    $ song_list = game_settings["ch3"]["ritsu"]
    $ renpy.random.shuffle(song_list)

    while curr_song <= song_count and lives > 0:
        $ song = song_list[curr_song-1]
        $ answer = ""

        narrator "Song [curr_song] of [song_count]"
        
        $ renpy.sound.play("audio/" + song["audio"] + ".mp3")
        $ dropdown = song["dropdown"]
        $ renpy.random.shuffle(dropdown)

        $ renpy.pause(sample, hard=True)
        $ renpy.music.set_pause(True, channel="sound")

        call countdown(guess_time, "outoftime_ritsu")
        
        menu:
            "[dropdown[0]]":
                $ answer = dropdown[0]
            "[dropdown[1]]":
                $ answer = dropdown[1]
            "[dropdown[2]]":
                $ answer = dropdown[2]
            "[dropdown[3]]":
                $ answer = dropdown[3]

        hide screen countdown
        
        $ renpy.music.set_pause(False, channel="sound")
        
        label outoftime_ritsu:
            if not answer: 
                $ lives -= 1
                rit "Heh... Too bad. Get better ears kid"
                narrator "Current score: [game_points]\nLives: [lives]"
            elif answer == song["answer"]:
                $ game_points += 15
                narrator "Correct! Current score: [game_points]\nLives: [lives]"
            else:
                $ lives -= 1
                narrator "Nope... Current score: [game_points]\nLives: [lives]"
        
        $ current_dial = dial[curr_song-1]
        if current_dial:
            rit "[current_dial]"

        $ curr_song += 1

    stop sound fadeout 1.0
    
    if lives == 0:
        label death_ritsu:
            stop sound fadeout 1.0

            rit "Well, well, well..."
            rit "Time to banish you from the arcade after all."
            rit "/kill JinAxel"

            $ MainMenu(confirm=False)()
    else:
        show rit dead at right
        rit "..."
        rit "......"
        rit "..............."
        rit "I hope you didn't think that's all I had in me."
        
        play music "audio/bgm08.mp3" fadeout 1.0 fadein 1.0 volume 0.2
        $ renpy.notify('♪ Boku no Hero Academia (OST)')
        
        rit "*friendship speech*"

        show rit revive at right
        rit "It's not over yet."
        
        show noe arcade sparkle at left with moveinleft
        noe "Quick! Take this!"
        
        show muscle at truecenter with moveinleft
        hide noe arcade sparkle with moveoutleft
        "Item {b}:muscle:{/b} acquired!"
        "Effect: +1 life"
        
        $ lives += 1
        
        hide muscle with dissolve
        rit "It's time for round 2 baby."
        
        narrator "--- Boss information ---\nName: Ritsu"
        narrator "Specialty: Second-Form"
        
        stop music fadeout 1.0
        
        $ song_count = 25
        $ song_list = game_settings["ch3"]["ritsu2"]
        $ renpy.random.shuffle(song_list)

        while curr_song <= song_count and lives > 0:
            $ song = song_list[curr_song-21]

            narrator "Song [curr_song] of [song_count]"
            
            $ renpy.sound.play("audio/" + song["audio"] + ".mp3")
            $ renpy.pause(sample, hard=True)
            $ renpy.music.set_pause(True, channel="sound")

            window hide
            call screen noddinput
            
            $ renpy.music.set_pause(False, channel="sound")
            $ answer = _return.lower().strip()
            
            if answer in song["answer"]:
                $ game_points += 20
                
                narrator "Correct! Current score: [game_points]\nLives: [lives]"
            else:
                $ lives -= 1
                $ answers = " / ".join(song["answer"])
                
                narrator "Nope... Current score: [game_points]\nLives: [lives]"
                narrator "Correct answer(s):\n{size=-8}[answers]{/size}"
            
            $ curr_song += 1
        
        stop sound fadeout 1.0
        
        if lives == 0:
            jump death_ritsu

        else:
            $ global_points += int(round(game_points * multiplier, 0))

            show rit dead2 at right
            rit "Wait, what?"
            
            scene black with fade
            return