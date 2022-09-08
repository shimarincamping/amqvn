label ch1sc3:
    scene bg main with fade

    show hib wait at right
    hib "{cps=10}...Oooooi{/cps}"
    hib "Just how long do you plan on dozing off like that!"
    hib "Even Yukari's gotten impatient y'know"
    
    show yuk pumped at left with moveinleft
    yuk "Finally awake are nya?"
    hib "It's finally time for us to learn every {b}ALI PROJECT{/b} song!"
    
    show hib yay
    hib "There won't ever be another Rozen Maiden or Avenger song that'll get us!!"
    hib "Ready when you are! Let's disable dropdown too while we're at it!"
    
    call initgamenodd(game_settings["ch1"]["sc3"]) from _call_initgamenodd
    
    scene bg main with fade

    if game_points == 15:
        show hib think at right with moveinright
        hib "I'm glad you got that at least, only 1921 left to go!"
        hib "{cps=10}... to {cps=*0.5}... go {cps=*0.25}...{/cps}"
    else:
        show yuk fire at left with moveinleft
        yuk "God, you're bad at this game aren't nya..."
        yuk "Let's keep going though~ Only 1921 songs left!"
        yuk "{cps=10}... songs {cps=*0.5}... left {cps=*0.25}...{/cps}"
    
    stop music fadeout 2.5
    $ renpy.pause(2.5, hard=True)
    scene black with Fade(2.0, 0.0, 2.0)