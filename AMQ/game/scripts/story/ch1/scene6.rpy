label ch1sc6:    
    scene bg shrine with fade

    show kom shrine
    if game_points >= 30:
        kom "Hey! That wasn't so bad now was it..."
    else:
        kom "Well, today was your first day after all, don't sweat it!"

    kom "Just make sure to keep practicing and sooner or la-"

    show noe shrine at right with moveinright:
    noe "ME ME ME! My turn! My turn!"
    noe "Unlike Komugi, I won't be going so easy on you!"
    noe "Hope you remember your titles well~"

    call initgamenodd(game_settings["ch1"]["sc6"], "bg shrineblur.jpg") from _call_initgamenodd_1
