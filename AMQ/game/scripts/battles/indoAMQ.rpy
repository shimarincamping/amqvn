label indonesianamq:
    scene bg main with fade
    gm "Welcome to Indonesian AMQ Simulator!"
    gm "A brand-new state-of-the-art game that lets you experience what it's like to play AMQ in Indonesia!"
    gm "Heralded as absolutely accurate by many of our loyal players, we hope you'll enjoy it too!"
    gm "Let's begin shall we~"
    scene bg ingame with fade
    window hide
    call initgamenodd(game_settings["ch3"]["indonesian_amq"], indonesia=True) from _call_initgamenodd_4
    "Total points: {b}[game_points] pts{/b}"
    if game_points > 0:
        gm "So, how many playthroughs have you done? Two? Three? Seventeen?"
        gm "Maybe you should try the other minigames, they're actually playable somewhat..."
    else:
        gm "Wowww, look at all those solo points you missed, tough luck"
    gm "Thanks for playing Indonesian AMQ Simulator! We hope you enjoyed it~"
    scene black with fade
    return