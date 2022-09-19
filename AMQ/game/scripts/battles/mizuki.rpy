label mizukibattle:
    scene bg shrineblur with fade

    narrator "--- Boss information ---\nName: Mizuki"
    narrator "Rules: 10 second time limit; 3 lives"
    narrator "Specialty: Quick-Time"

    show miz shrine at right with moveinright
    miz "Hope you're ready! I know I am~"

    $ song_list = game_settings["ch1"]["mizuki"]
    $ game_points = 0
    $ curr_song = 1
    $ song_count = len(song_list)

    $ dial = [
        "Not bad, but can you do 9 more?",
        "","Be sure to take your time\nJust not too much time~",
        "",
        "You're doing better than I thought\nThe last guy didn't make it this far",
        "",
        "Looks like I'll have to get serious with you",
        "Only hard songs from here on out",
        "I've saved my special attack for last...",
        "a"]
    $ lives = 3

    while curr_song <= song_count and lives > 0:
        $ song = song_list[curr_song-1]
        $ answer = ""

        narrator "Song [curr_song] of [song_count]"

        $ renpy.music.play("audio/" + song["audio"] + ".mp3")
        $ dropdown = song["dropdown"]

        call countdown(10.0, "outoftime_mizuki")

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

        label outoftime_mizuki:
            if not answer:
                $ lives -= 1
                narrator "Too slow... Current score: [game_points]\nLives: [lives]"
            elif answer == song["answer"]:
                $ game_points += 10
                narrator "Correct! Current score: [game_points]\nLives: [lives]"
            else:
                $ lives -= 1
                narrator "Nope... Current score: [game_points]\nLives: [lives]"

        $ currentdial = dial[curr_song-1]
        if currentdial:
            if curr_song >= 7:
                show miz shrine attack at right 
            miz "[currentdial]"

        $ curr_song += 1

    if lives > 0:
        $ global_points += int(round(game_points * (0.5 + (0.5 * lives)), 0))
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