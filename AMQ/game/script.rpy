define config.rollback_enabled = False
define config.has_autosave = False

init python:
    import time as gettime
    rhythm_game_songs = [
        Song('Seishun wa Non-stop!', 'audio/sb69.mp3', 'audio/sb69.beatmap.txt'),
        Song('Tokimeki Experience!', 'audio/bandori.mp3', 'audio/bandori.beatmap.txt'),
        Song('Colorful Dreams! Colorful Smiles!', 'audio/lovelive.mp3', 'audio/lovelive.beatmap.txt'),
        Song('Onegai! Cinderella', 'audio/imas.mp3', 'audio/imas.beatmap.txt'), 
        Song('Make debut!', 'audio/umamusume.mp3', 'audio/umamusume.beatmap.txt')
    ]
    
    #config.has_quicksave = False
    #config.has_autosave = False
init:
    $ timer_range = 0
    $ timer_jump = 0

default persistent.rhythm_game_high_scores = {
    song.name: (0, 0) for song in rhythm_game_songs
}
default selected_song = None

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

screen countdown3:
    fixed:
        text "{color=#d9f5ff}{b}Time left:{/b}{/color}":
            xpos 230 ypos 420
    timer 1 repeat True action If(timeleft > 0, true=SetVariable('timeleft', timeleft - 1), false=[Hide('countdown'), Jump(timer_jump)])
    if timeleft <= 3:
        text str(timeleft) xpos .25 ypos .35 color "#FF0000" size 200 at alpha_dissolve 
    else:
        text str(timeleft) xpos .25 ypos .35 size 200 at alpha_dissolve

label start:
    $ global_points = 0

    call op
    call ch1
    call ch2
    call ch3
    call ch4
    call ch5
    call ch6

    python:
        rhythm_game_scores_list = []
        for i in persistent.rhythm_game_high_scores.values():
            rhythm_game_scores_list.append(i[0])
        avg_rhythm_game_score = int(round((sum(rhythm_game_scores_list) / len(rhythm_game_scores_list) / 1000),0))
        game_points += avg_rhythm_game_score * 2
    ""
    scene black with fade
    centered "~ to be continued ~"
    centered "Thanks for playing till the end!"
    centered "Total XP: {b}[global_points]{/b}"
    return