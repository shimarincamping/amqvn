label ch1sc7:    
    scene bg shrine with fade
    
    show noe shrine
    if game_points >= 45:
        noe "Woaah!! I'm getting pumped~ Good job back there!"
    else:
        noe "Hey, we've still got tons of days together ahead of us to get better~"
        noe "And I'll be supporting you all the way~"
    
    show miz shrine at right with moveinright:
    
    play music "audio/bgm02.mp3" fadeout 1.0 fadein 1.0 volume 0.2
    $ renpy.notify('♪ Zombie Land Saga')
    
    miz "Move outa here!"
    
    hide noe shrine
    show miz shrine
    miz "I didn't come all the way out here so that those two could baby you with their {b}FREE SONGS{/b}"
    miz "Tell you what, I'll give you a real challenge, stuff that'll make everyone :place_of_worship: when you join a pub room"
    miz "You'll be a legend!"
    miz "But it won't be easy... Fail my training and you die."

    show miz shrine attack
    miz "Quite literally."
    miz "So just tell me when you're ready"

    $ proceed = False
    while not proceed:
        menu:
            "Ege's Spirit" "It's recommended you save your game before fighting bosses; dying means you lose your current save data"
            "Begin fight":
                $ proceed = True
            "Maybe later...":
                miz "I'll be waiting..."

    call mizukibattle from _call_mizukibattle
