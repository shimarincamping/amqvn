label ch1sc1:
    scene bg bedroom

    j "God... what even was that nightmare..."
    j "Time to set up the stream I guess"
    
    scene black

    narrator "You are about to play as an AMQ bully!"
    narrator "Guess the anime opening correctly and earn points, rise above the rest, emerge triumphant..."
    narrator "...and get called out for having not touched grass in weeks"
    narrator "Good luck!"

    call initgame(game_settings["ch1"]["sc1"]) from _call_initgame
    
    if game_points > 0:
        narrator "Not bad, %(game_points)d points... That'll show those default Hibikis"
    else:
        j "Haha sorry guys, my Catbox wasn't working"
        narrator "Kitty will remember that."