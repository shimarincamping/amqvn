label blindbr:
    # Category 1 - Time Period (1990s, 2000s, 2010s)
    # Category 2 - Genre (Ecchi, Sports, Mecha)
    # Category 3 - Type (Movies, Special, OVA)
    
    scene bg main with fade
    
    gm "Welcome to Blind Battle Royale! Sponsored by ggius amq tours"
    gm "Ever thought to yourself 'Gee this BR mode really sucks ass why is it even a daily quest its literally bs amq cant get any worse than this'?"
    gm "Well good! We have too, which is why we came up with an even worse version of BR! Where you don't even know what you're looting!"
    gm "You have to blindly loot a theme from each category, and 2 songs from each theme will play during the game for you to guess!"
    gm "At the end of the game, your job is to figure out what you looted at the beginning of the game~"
    gm "I'd rewrite this explanation more concisely but it'd make more sense just to get started! Let's play~"
    
    show bbr_loot with fade:
        xalign 0.5
        yalign 0.4
    ""
    
    hide bbr_loot

    $ cat_selected = []
    $ cat_guessed = []
    $ loot = game_settings["ch3"]["blind_br"]
    
    $ song_list = []
    $ category1 = loot["category1"]
    $ category2 = loot["category2"]
    $ category3 = loot["category3"]

    menu:
        "Category 1 - Vintage\nPossible choices: 1990s, 2000s, 2010s"
        "?????":
            $ songlist += category1["option1"]["songs"]
            $ desc1 = category1["option1"]["desc"]
        "?????":
            $ songlist += category1["option2"]["songs"]
            $ desc1 += category1["option2"]["desc"]
        "?????":
            $ songlist += category1["option3"]["songs"]
            $ desc1 += category1["option3"]["desc"]
    
    $ cat_selected.append(desc1)
    
    "Got it!\nTwo songs will play from the {b}?????{/b} category"
    
    menu:
        "Category 2 - Genre\nPossible choices: Ecchi, Sports, Mecha"
        "?????":
            $ songlist += category2["option1"]["songs"]
            $ desc2 = category2["option1"]["desc"]
        "?????":
            $ songlist += category2["option2"]["songs"]
            $ desc2 += category2["option2"]["desc"]
        "?????":
            $ songlist += category2["option3"]["songs"]
            $ desc2 += category2["option3"]["desc"]

    $ cat_selected.append(desc2)

    "Great choice!\nTwo songs will play from the {b}???????{/b} category"
    
    menu:
        "Category 3 - Type\nPossible choices: Movie, OVA, Rebroadcast"
        "?????????":
            $ songlist += category3["option1"]["songs"]
            $ desc3 = category3["option1"]["desc"]
        "?????????":
            $ songlist += category3["option2"]["songs"]
            $ desc3 += category3["option2"]["desc"]
        "?????????":
            $ songlist += category3["option3"]["songs"]
            $ desc3 += category3["option3"]["desc"]

    $ cat_selected.append(desc3)
    
    "Yikes, good luck on that one...\nTwo songs will play from the {b}?????????{/b} category"
    
    $ renpy.random.shuffle(song_list)
    
    "Let's begin, hope you're ready!"
    
    show bbr_guess with fade:
        xalign 0.5
        yalign 0.4
    ""
    
    hide bbr_guess
    window hide
    
    call initgamenodd(song_list) from _call_initgamenodd_3
    
    scene bg ingame with fade
    
    gm "Hope you managed to get at least some of those right! Time to solve the mystery of what you picked~"
    
    window hide
    
    show bbr_answer with fade:
        xalign 0.5
        yalign 0.4
    ""
    
    hide bbr_answer
    
    menu:
        "First category - Vintage\n{i}{size=-5}   What do you think you looted earlier?\n   Two songs from this category played{/size}{/i}"
        "1990s":
            $ guess1 = "1990s"
        "2000s":
            $ guess1 = "2000s"
        "2010s":
            $ guess1 = "2010s"
    
    $ cat_guessed.append(guess1)
    
    gm "Interesting choice..."

    menu:
        "Second category - Genre\n{i}{size=-5}   What do you think you looted earlier?\n   Two songs from this category played{/size}{/i}"
        "Ecchi":
            $ guess2 = "Ecchi"
        "Sports":
            $ guess2 = "Sports"
        "Mecha":
            $ guess2 = "Mecha"

    $ cat_guessed.append(guess2)

    gm "Perhaps that could be the one..."

    menu:
        "Third category - Type\n{i}{size=-5}   What do you think you looted earlier?\n   Two songs from this category played{/size}{/i}"
        "Movie":
            $ guess3 = "Movie"
        "OVA":
            $ guess3 = "OVA"
        "Rebroadcast":
            $ guess3 = "Rebroadcast"

    $ cat_guessed.append(guess3)

    gm "Hmm... let's see if you're right on this..."
    gm "So, you guessed {b}[guess1]{/b}, {b}[guess2]{/b}, and {b}[guess3]{/b}..."
    gm "... And the three that you picked were{w} {b}[desc1]{/b}{w}, {b}[desc2]{/b}{w}, and {b}[desc3]{/b}!"
    
    if cat_selected == cat_guessed:
        gm "Congratulations! Looks like you're pretty good at this guessing thing after all!"
        $ globalpoints += 25
    
    else:
        gm "Darn... Better luck next time... Thanks for playing!"
    
    scene black with fade
    return