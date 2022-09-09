label op:
    narrator "Welcome to your worst nightmare"

    scene bg main
    play music "audio/amqtheme.mp3" fadeout 1.0 fadein 1.0
    $ renpy.notify('♪ No Game No Life')
    
    show hib wait at right
    hib "God you're bad at this game"
    
    show hib think
    hib "Still, I'm surprised you managed to sit through all 30 Precure openings..."
    hib "... You even rolled All Stars DX2 right that one time!"
    
    show hib yay
    hib "I'd consider that a victory, if anything"
    hib "Lemme know if you're still down to learn the Pokémon movies next week!"
    
    menu:
        "S-sure... Ahaha...":
            show hib base
            hib "Great! Here's to more mental deterioriation!"

        "M-maybe not...":
            show hib pout
            hib "Fine... But if you don't we're not going to ever hit our goal of 5 points in Eastern Ranked"
            hib "Spamming Conan isn't going to get us to the top!"

    scene black
    narrator "Your vision begins to blur..."
    stop music