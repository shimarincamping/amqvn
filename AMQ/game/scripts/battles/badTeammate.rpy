label badteammate:    
    $ correctdial = [
        "how tf did you know that",
        "bro quit sweating so hard",
        "how much anime have you seen tf",
        "go touch grass"
    ]
    $ wrongdial = [
        "even i knew that",
        "tf my teammates trolling",
        "*starts reciting the entire wikipedia list of ethnic slurs*",
        "can we kick this guy wtf who even are they"
    ]
    
    $ renpy.random.shuffle(song_list)
    
    scene bg main with fade
    
    gm "Welcome to Bad Teammate! Powered by Shinomiya Group"
    gm "Once upon a time, you accidentally joined a team lobby full of single-digit level Hibiks!"
    gm "Ignoring the shocking fact they didn't kick you out and call you racial slurs within a nanosecond of you clicking Ready..."
    gm "They don't know anything!"
    gm "Help determine if your teammate's answer is correct in the short short time you have to think..."
    gm "Be quick! You need to act fast to let it slide or invalidate their answers to save you from complete embarrassment!"
    gm "{size=-8}(Becuase you've already tied up an unhealthy chunk of your self-worth into this meaningless memory and typing game){/size}"
    gm "Good luck out there! Let's play~"
    "Game settings: Song plays for 5 seconds, you have 5 seconds after that to respond with Yes or No"
    
    scene bg ingame with Fade(2.0, 0.0, 2.0)

    $ guess_time = 5.0
    $ game_points = 0
    $ curr_song = 1
    $ song_count = 10
    $ song_list = game_settings["ch3"]["bad_teammate"]
    
    while curr_song <= song_count:
        $ song = song_list[curr_song-1]
        $ answer = ""
        
        narrator "Song [curr_song] of [song_count]"
        
        window hide
        
        call countdown(guess_time, "btans")

        $ renpy.music.play("audio/" + song["audio"] + ".mp3")
        $ renpy.pause(5.0, hard=True)

        label btans:
            call countdown(guess_time, "btoutoftime")

            $ team_answer = song["image"]
            image team_answer = "[team_answer]"
            
            show team_answer:
                xalign 0.5
                yalign 0.6
                xzoom 2.0 
                yzoom 2.0
            
            menu:
                "Accept your teammate's answer?"
                "Yes":
                    hide screen countdown
                    hide team_answer
                    $ accepted = "Y"
                "No":
                    hide screen countdown
                    hide team_answer
                    $ accepted = "N"
            
            if accepted == song["answer"]:
                $ random_dial = renpy.random.choice(correctdial)
                $ game_points += 10
                "Good job! Current score: {b}[game_points] points{/b} (+10)"
                "Guest-56941" "[random_dial]"
            
            else:
                $ random_dial = renpy.random.choice(wrongdial)
                $ game_points -= 10
                "Mmmm no... Current score: {b}[game_points] points{/b} (-10)"
                "Guest-56941" "[random_dial]"
            hide team_answer
        
        if False:
            label btoutoftime:
                hide team_answer
                $ game_points -= 5
                "Rip too slow... Current score: {b}[game_points] points{/b} (-5)"
        
        $ curr_song += 1
    
    stop music fadeout 1.0
    
    scene bg main with fade
    
    gm "Game complete! Total score: {b}[game_points] points{/b}"
    
    show bt_kick at truecenter with zoomin
    
    gm "Thank you for playing Bad Teammate!"
    
    $ global_points += game_points
    
    scene black with fade
    return