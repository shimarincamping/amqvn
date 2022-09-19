label ch4:
    scene bg dinner with Fade(2.0, 0.0, 2.0)

    show noe arcade sparkle with moveinleft
    noe "Uwaa~ I'm starving, what're you gonna order?"

    menu:
        noe "I think I'm having the Tropical-Rouge PanCake Tower!"
        "Cheese Gyuudon":
            noe "Oooh that looks yummy, do you get this often?"
        "Tuna Tataki":
            noe "Look at the price! Where'd you get the money for that...{w}{s}i thought u were a neet{/s}"
        "AMQ Player Salad":
            "{i}Garlic sautéed premium-grade Cheeto Puffs in an aromatic salted caramel Mountain Dew vinaigrette{/i}{w}\nLimited time only: Comes with free tendies!"

            show noe arcade think
            noe "W-well I was gonna ask to try some of your food but, you can have all of that one..."
            hide noe arcade think
    show noe arcade appears 
    noe "Fufu... of course, we didn't just come here to have fun... let's get some practice in while the waiter gets us more breadsticks!"
    noe "We'll be doing anime that have the {b}Food{/b} tag! Good luck~"
    scene black with fade
    call initgame({
        "game1201":["Sugar Sugar Rune","Dagashi Kashi 2","Yumeiro Pâtissière SP Professional","Pan de Peace!"],
        "game1202":["Nya-men","Onigiri","Bananya","Neko Ramen"],
        "game1203":["Takunomi.","Wakako-zake","Bartender","Osake wa Fuufu ni Natte kara"],
        "game1204":["Emiya-san Chi no Kyou no Gohan","Bonjour Sweet Love Patisserie","Kakuriyo no Yadomeshi","Yakitate!! Japan"],
        "game1205":["Valkyrie no Shokutaku II", "Isekai Shokudou 2","Koufuku Graffiti","Shokugeki no Souma: Shin no Sara"]
    },[
        "Dagashi Kashi 2", "Neko Ramen", "Bartender", "Emiya-san Chi no Kyou no Gohan", "Isekai Shokudou 2"
    ], gamebg="bg dinner.jpg") from _call_initgame_3
    scene bg dinner with fade
    show noe arcade appears
    noe "And just in time too... Our food's here! Itadakimasu~"
    scene bg movies with Fade(3.0, 0.0, 3.0)
    $ renpy.pause(3.0, hard=True)
    show noe arcade think at right
    noe "This is taking forever...."
    noe "{size=-3}Can't believe we pay $20 and still have to sit though a trailer for a B-list superhero movie, a commercial for a phone that barely improved over last year's model, and a random sob story that {i}somehow{/i} always turns out to be a car insurance ad...{/size}"
    hide noe arcade think
    show noe arcade appears at right
    noe "How's about we take this chance to try out some {s}boomer{/s} {b}classic movies{/b}!"
    noe "Anything after Y2K is NG!"
    scene black with fade
    call initgamenodd({
        "game1301":["mimi o sumaseba","whisper of the heart"],
        "game1302":["majo no takkyuubin","kiki's delivery service"],
        "game1303":["perfect blue"],
        "game1304":["hadashi no gen","barefoot gen","hiroshima"],
        "game1305":["little nemo","little nemo: adventures in slumberland"]
    }, gamebg="bg movies.jpg") from _call_initgamenodd_5
    scene bg movies with fade
    show noe arcade appears at right
    noe "Aaaaand the movie still hasn't started..."
    j "What even are we watching anyway?"
    noe "Mm... Well it's..."
    "???" "Shhhh!! Could ya pipe it down for just a sec back there..."
    show kur attack with moveinleft
    kur "Been waitin' for this movie since the day it was announced, wouldn't wanna miss a single moment~"
    kur "Are yall fans of the Rail the Blood: Index Fortress in Space of the Dead franchise too?"
    j "That's a... pretty elaborate getup just to see a movie"
    noe "Well it is an anime movie, I guess it isn't surprising to run into a few cosplayers"
    kur "Cosp- I'll have you know I'm a bona fide Royal Witch for the Imperial Magical Nation Army! {size=-10}{w}(At least in my headcanon fanfiction for what happens after Chapter 16.5){/size}"
    show miy base with moveinleft:
        xalign 0.1
        yalign 0.8
    miy "Ahhh... don't mind my friend here, we're from the convention down the street..."
    j "Oh, it's starting, it's starting"
    miy "Let's head back then shall we~"
    hide kur attack
    show kur tehe behind miy:
        xalign 0.5 yalign 0.85
    kur "Okie!"
    hide miy base with moveoutleft
    hide kur tehe with moveoutleft
    scene black with Fade(3.0, 0.0, 3.0)
    $ renpy.pause(3.0, hard=True)
    centered "After the movie..."
    scene bg bedroom with fade
    show noe appears at right with moveinright 
    noe "Hope you learned something at least from today's training~ and also had fun along the way!"
    noe "Looks like you're getting used to the booli lifestyle already; eating, sleeping, and breathing AMQ all day"
    noe "Soon you'll be humming Aikatsu inserts on the bus and referring to anime only by their flex names in no time!"
    noe "Good night now~ Komugi's got plans for us tomorrow so make sure to wake up refreshed!"
    menu:
        "Sleep":
            scene black with Fade(3.0, 0.0, 3.0)