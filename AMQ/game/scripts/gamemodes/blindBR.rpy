label blindbr:
    # Category 1 - Time Period (1990s, 2000s, 2010s)
    # Category 2 - Genre (Ecchi, Sports, Mecha)
    # Category 3 - Type (Movies, Special, OVA)
    python:
        cat1_opt1 = {
            "game801":["vampire knight"],
            "game802":["fruits basket"]
        }
        cat1_opt2 = {
            "game803":["chihayafuru 3"],
            "game804":["ramen daisuki koizumi-san","ms. koizumi loves ramen noodles"]
        }
        cat1_opt3 = {
            "game805":["magic knight rayearth"],
            "game806":["one piece"]
        }
        cat2_opt1 = {
            "game807":["azur lane"],
            "game808":["shinmai maou no testament burst","the testament of sister new devil burst","shinmai maou no testament departures","the testament of sister new devil departures"]
        }
        cat2_opt2 = {
            "game809":["aquarion evol","sousei no aquarion evol","aquarion logos"],
            "game810":["macross f","macross frontier"]
        }
        cat2_opt3 = {
            "game811":["slow loop"],
            "game812":["re-main"]
        }
        cat3_opt1 = {
            "game813":["soul eater"],
            "game814":["code geass: hangyaku no lelouch","code geass: lelouch of the rebellion"]
        }
        cat3_opt2 = {
            "game815":["bubble"],
            "game816":["josee to tora to sakana-tachi","josee, the tiger and the fish"]
        }
        cat3_opt3 = {
            "game817":["higurashi no naku koro ni kira","when they cry kira"],
            "game818":["nekopara ova"]
        }
        cat_selected = []
        cat_guessed = []
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
    menu:
        "Category 1 - Vintage\nPossible choices: 1990s, 2000s, 2010s"
        "?????":
            $ cat1 = cat1_opt1
            $ cat1_desc = "2000s"
        "?????":
            $ cat1 = cat1_opt2
            $ cat1_desc = "2010s"
        "?????":
            $ cat1 = cat1_opt3
            $ cat1_desc = "1990s"
    $ cat_selected.append(cat1_desc)
    "Got it!\nTwo songs will play from the {b}?????{/b} category"
    menu:
        "Category 2 - Genre\nPossible choices: Ecchi, Sports, Mecha"
        "???????":
            $ cat2 = cat2_opt1
            $ cat2_desc = "Ecchi"
        "???????":
            $ cat2 = cat2_opt2
            $ cat2_desc = "Mecha"
        "???????":
            $ cat2 = cat2_opt3
            $ cat2_desc = "Sports"
    $ cat_selected.append(cat2_desc)
    "Great choice!\nTwo songs will play from the {b}???????{/b} category"
    menu:
        "Category 3 - Type\nPossible choices: Movie, OVA, Rebroadcast"
        "?????????":
            $ cat3 = cat3_opt1
            $ cat3_desc = "Rebroadcast"
        "?????????":
            $ cat3 = cat3_opt2
            $ cat3_desc = "Movie"
        "?????????":
            $ cat3 = cat3_opt3
            $ cat3_desc = "OVA"
    $ cat_selected.append(cat3_desc)
    "Yikes, good luck on that one...\nTwo songs will play from the {b}?????????{/b} category"
    $ songdict = cat1 | cat2 | cat3
    $ songtup = list(songdict.items())
    $ renpy.random.shuffle(songtup)
    $ songdict = dict(songtup)
    "Let's begin, hope you're ready!"
    show bbr_guess with fade:
        xalign 0.5
        yalign 0.4
    ""
    hide bbr_guess
    window hide
    call initgamenodd(songdict) from _call_initgamenodd_3
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
            $ cat1_guess = "1990s"
        "2000s":
            $ cat1_guess = "2000s"
        "2010s":
            $ cat1_guess = "2010s"
    $ cat_guessed.append(cat1_guess)
    gm "Interesting choice..."
    menu:
        "Second category - Genre\n{i}{size=-5}   What do you think you looted earlier?\n   Two songs from this category played{/size}{/i}"
        "Ecchi":
            $ cat2_guess = "Ecchi"
        "Sports":
            $ cat2_guess = "Sports"
        "Mecha":
            $ cat2_guess = "Mecha"
    $ cat_guessed.append(cat2_guess)
    gm "Perhaps that could be the one..."
    menu:
        "Third category - Type\n{i}{size=-5}   What do you think you looted earlier?\n   Two songs from this category played{/size}{/i}"
        "Movie":
            $ cat3_guess = "Movie"
        "OVA":
            $ cat3_guess = "OVA"
        "Rebroadcast":
            $ cat3_guess = "Rebroadcast"
    $ cat_guessed.append(cat3_guess)
    gm "Hmm... let's see if you're right on this..."
    gm "So, you guessed {b}[cat1_guess]{/b}, {b}[cat2_guess]{/b}, and {b}[cat3_guess]{/b}..."
    gm "... And the three that you picked were{w} {b}[cat1_desc]{/b}{w}, {b}[cat2_desc]{/b}{w}, and {b}[cat3_desc]{/b}!"
    if cat_selected == cat_guessed:
        gm "Congratulations! Looks like you're pretty good at this guessing thing after all!"
        $ globalpoints += 25
    else:
        gm "Darn... Better luck next time... Thanks for playing!"
    scene black with fade
    return