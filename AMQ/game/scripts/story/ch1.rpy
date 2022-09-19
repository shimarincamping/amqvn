label ch1:
    scene bg bedroom

    j "God... what even was that nightmare..."
    j "Time to set up the stream I guess"
    
    scene black

    narrator "You are about to play as an AMQ bully!"
    narrator "Guess the anime opening correctly and earn points, rise above the rest, emerge triumphant..."
    narrator "...and get called out for having not touched grass in weeks"
    narrator "Good luck!"

    call initgame(game_settings["ch1"]["game1"]) from _call_initgame
    
    if game_points > 0:
        narrator "Not bad, %(game_points)d points... That'll show those default Hibikis"
    else:
        j "Haha sorry guys, my Catbox wasn't working"
        narrator "Kitty will remember that."

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
    
    call initgamenodd(game_settings["ch1"]["game2"]) from _call_initgamenodd
    
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

    scene bg bedroom

    j "..."
    j "Masaka... yume?!"
    narrator "(Least cringe weeb)"

    show noe think at right with moveinright
    noe "You alright...? You look like you've seen a ghost..."
    noe "Or worse, {i}a Hibiki{/i}"

    menu:
        "It's nothing...":
            show noe sparkle at right
            noe "Then I suppose we should get started with our training today then!"
            noe "Let's go~ Komugi and Mizuki are waiting for us"
        
        "Just a nightmare":
            noe "Then I suppose you're in no shape to come train today then"
            
            show noe appears at right
            noe "Just leave it to the world's greatest detective Noel! I'll have you feeling better in no time!"
            noe "Hurry, lie down and relax your min-"
            
            play sound "audio/knock.mp3"
            $ renpy.pause(2.5, hard=True)
            
            show kom pout at left with moveinleft
            kom "Oi what's takin' so long! Mizuki and I have been waiting ages over there, {i}and you know how much I can't stand her...{/i}"
            
            show noe pout at right
            noe "F-fine... I'll get changed and we can go..."
        
        "OH MY SWEET ANGEL NOEL_#)@!THANK HEAVENS YOU'RE REAL":
            scene black
            centered "Bonked by Ege Ending"
            "Ege's Spirit" "Bad"
            $ renpy.set_return_stack([])
            return

    scene black with fade

    scene bg shrine with fade

    show kom shrine at right
    kom "Here we are!"

    show miz shrine
    miz "Hiya, looks like you made it~"

    show noe shrine at left
    noe "Now it's time to regret all your life decisions!"
    noe "Noel's super ultra intense bootcamp begins now!"

    scene bg shrine with fade

    show kom shrine
    kom "Let's start you off with an easy warm up round!"
    kom "Here we go!"

    call initgame(game_settings["ch1"]["game3"], "bg shrineblur.jpg") from _call_initgame_1

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

    call initgamenodd(game_settings["ch1"]["game4"], "bg shrineblur.jpg") from _call_initgamenodd_1

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

    scene bg shrine with fade
    
    show miz shrine
    miz "Well, looks like you beat me... Guess you're better at this than I thought"
    miz "And here I was taking you for some loser who does nothing other than bully streamers and play S/A lobbies"
    miz "You've earned my respect"
    narrator "Mizuki joins your party!"
    
    hide miz shrine
    show kom shrine at right with moveinright
    show noe shrine at left with moveinleft
    noe "Wooo~ You did it! Just like I knew you could, of course"
    kom "To commemorate this occassion, I reckon we should go celebrate!"
    noe "And what better way to celebrate than with..."
    kom "Karaoke!"
    noe "Karaoke!"
    miz "Smurfing ranked!"
    miz "Oh yeah, right, karaoke, force of habit my bad"
    noe "Hurry weeb-kun, that Japanese isn't gonna butcher itself"

    scene black with Fade(3.0, 0.0, 3.0)