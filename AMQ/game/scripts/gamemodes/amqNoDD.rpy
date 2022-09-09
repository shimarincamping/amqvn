label initgamenodd(song_list, game_bg="bg ingame.jpg"):
    image game_bg = "[game_bg]"
    scene game_bg

    $ game_points = 0
    $ curr_song = 1
    $ song_count = len(song_list)

    while curr_song <= song_count:
        $ song = song_list[curr_song-1]

        narrator "Song [curr_song] of [song_count]"

        $ renpy.music.play("audio/" + song["audio"] + ".mp3")
        
        call screen noddinput
        $ answer = _return.lower().strip()
        $ print(answer)
        $ print("returned")

        if answer in song["answer"]:
            $ game_points += 15
            narrator "Correct! Current score: [game_points]"
        else:
            narrator "Nope... Current score: [game_points]"
            $ answers = " / ".join(song["answer"])
            narrator "Correct answer(s):\n[answers]"
        
        $ curr_song += 1

    $ global_points += game_points

    stop music fadeout 1.0
    scene black with fade
    return