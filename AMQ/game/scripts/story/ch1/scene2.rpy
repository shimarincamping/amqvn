label ch1sc2:
    scene bg bedroom with fade

    j "Another great day farming tickets..."
    
    play sound "audio/knock.mp3"
    $ renpy.pause(2.5, hard=True)

    j "Mm...?"
    show kom base with moveinright
    
    play music "audio/bgm01.mp3" fadeout 1.0 fadein 1.0 volume 0.2
    $ renpy.notify('♪ Tobidase! Machine Hiryuu')

    kom "Greetings AMQ booli. 'Tis I, the great shrine maiden Komugi!"
    j "Whoa!!!"
    j "Wait, shouldn't you be at like, y'know a shrine?"
    kom "That's..."

    show kom pout
    kom "Why don't you ask Mizuki that instead?! Hmph..."
    kom "A~ ny~ way~!!"

    show kom think:
        xalign 0.5 yalign 0.99
        linear 0.3 xalign 0.99
    kom "The world of AMQ needs your help!"
    kom "{i}And I swear this isn't the beginning of a trashy isekai plot{/i}"
    kom "Based on how many hours you've spent mindlessly typing words into a box on a fucking browser game, {i}and I mean look at those hours...{/i}"
    
    show hib cursed at truecenter
    kom "We've decided you'd be perfect to help the world of AMQ defeat the illusive {b}SOLID GOLD HIBIKI{/b}"
    kom "You won't go unrewarded though - if successful, we'll pay you in glorious tickets! {i}More tickets than our game mods get in a whole year!{/i}"
    hide hib cursed
    
    j "So like... 3?"
    kom "Hey, don't get greedy now."

    show kom base at right
    kom "... So, to help you train for your big fight, I've enlisted the help of my good friend Noel to beat ya into shape"
    
    show noe appears at left with moveinleft
    noe "Yahallo! One wrong Gintama season is gonna be one Jashin-sized dropkick outa you!"
    j ":fearful:"

    show noe sparkle 
    noe "Our training begins at dawn, get ready soldier!"
    hide noe sparkle

    show kom cursed:
        xalign 0.99 yalign 0.99
        linear 0.3 xalign 0.5
    kom "May Ege's spirit have mercy on you."
    kom "Noel's training makes 4x 5s No DD Quick Draw Start Sample feel easy in comparison."
    kom "Hurry along and get some sleep now"

    menu:
        "Sleep":
            stop music fadeout 3.0
            $ renpy.pause(3.0, hard=True)
            scene black with fade
            narrator "..."
            narrator "......"
            narrator ".........?"