label thirddream:
    $ is_dead = False

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
            $ is_dead = True
    
    if is_dead:
        "--- Death Match Begin Again ---"
    else:
        "--- Death Match Begin ---"

    $ game_points = 0
    $ curr_song = 1
    $ song_count = 12
    
    $ song_list = game_settings["ch4"]["third_Dream"]
    $ renpy.random.shuffle(song_list)

    if curr_song == 1 and not is_dead:
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
    
    while curr_song <= song_count:
        $ song = song_list[curr_song-1]
        $ answer = ""

        narrator "Song [curr_song] of [song_count]"

        $ renpy.music.play("audio/" + song["audio"] + ".mp3")

        show screen cp_button
        $ cpbutton_beforegame = False
        
        call screen noddinput

        $ answer = _return.lower().strip()

        hide screen cp_button
        
        if answer in song["answer"]:
            $ game_points += 10
            narrator "Correct! Current score: [game_points]"
        else:
            narrator "Nope... That ain't right..."
            $ allans = " / ".join(song["answer"])
            
            if song["audio"] == "game1608":
                narrator "Correct answer(s):\n{size=-12}[allans]{/size}"
            else:
                narrator "Correct answer(s):\n{size=-8}[allans]{/size}"

            jump dream_death
        
        $ curr_song += 1
    
    stop music fadeout 1.0
    hide screen cp_button
    
    $ global_points += game_points
    
    scene black with fade
    return
