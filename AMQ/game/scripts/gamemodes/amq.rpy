label initgame(song_list, game_bg="bg ingame.jpg", special_mode="None"):
    image game_bg = "[game_bg]"
    scene game_bg

    $ game_points = 0
    $ curr_song = 1
    $ song_count = len(song_list)

    while curr_song <= song_count:
        $ song = song_list[curr_song-1]

        narrator "Song [curr_song] of [song_count]"

        $ renpy.music.play("audio/" + song["audio"] + ".mp3")
        $ dropdown = song["dropdown"]

        menu:
            "[dropdown[0]]":
                $ answer = dropdown[0]
            "[dropdown[1]]":
                $ answer = dropdown[1]
            "[dropdown[2]]":
                $ answer = dropdown[2]
            "[dropdown[3]]":
                $ answer = dropdown[3]

        if answer == song["answer"]:
            $ game_points += 10
            narrator "Correct! Current score: [game_points]"
        else:
            narrator "Nope... Current score: [game_points]"

        $ curr_song += 1

    $ global_points += game_points

    stop music fadeout 1.0
    scene black with fade
    return