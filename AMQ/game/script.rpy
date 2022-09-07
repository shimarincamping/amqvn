define config.rollback_enabled = False
define config.has_autosave = False

define j = Character("JinAxel")
define hib = Character("Hibiki")
define kom = Character("Komugi")
define noe = Character("Noel")
define yuk = Character("Yukari")
define miz = Character("Mizuki")
define shi = Character("Shiina")
define rit = Character("Ritsu")
define hon = Character("Honoka")
define kur = Character("Kuriko")
define miy = Character("Miyu")
define mar = Character("Marine")
define hik = Character("Hikari")
define dayt = Character("Daytona")
define gsyuk = Character("Regis Philbin")
define gm = Character("Game Master")
image hib1 = im.Scale("hib wait.webp", 550, 800)
image hib2 = im.Scale("hib think.webp", 550, 800)
image hib3 = im.Scale("hib yay.webp", 550, 800)
image hib4 = im.Scale("hib base.webp", 550, 800)
image hib5 = im.Scale("hib pout.webp", 550, 800)
image kom1 = im.Scale("kom base.webp", 550, 800)
image kom2 = im.Scale("kom pout.webp", 550, 800)
image kom3 = im.Scale("kom think.webp", 550, 800)
image kom4 = im.Scale("kom cursed.png", 550, 800)
image skom = im.Scale("kom shrine.webp", 745, 950)
image ghib1 = im.Scale("cursed.png", 550, 550)
image noe1 = im.Scale("noe appears.webp", 550, 800)
image noe2 = im.Scale("noe sparkle.webp", 550, 800)
image noe3 = im.Scale("noe think.webp", 550, 800)
image noe4 = im.Scale("noe pout.webp", 550, 800)
image snoe = im.Scale("noe shrine.webp", 540, 800)
image anoe1 = im.Scale("noe appears arcade.webp", 550, 800)
image anoe2 = im.Scale("noe sparkle arcade.webp", 550, 800)
image anoe3 = im.Scale("noe think arcade.webp", 550, 800)
image bnoe1 = im.Scale("noe brawler.webp", 550, 800)
image yuk1 = im.Scale("yuk pumped.webp", 550, 800)
image yuk2 = im.Scale("yuk yahoi.webp", 550, 800)
image yuk3 = im.Scale("yuk fire.webp", 550, 800)
image gsyuk = im.Scale("yuk gameshow.png", 550, 800)
image miz1 = im.Scale("miz happy.webp", 550, 800)
image smiz = im.Scale("miz shrine.webp", 550, 800)
image smizangry = im.Scale("miz shrineattack.webp", 550, 800)
image shi1 = im.Scale("shi tehe.webp", 550, 800)
image shi2 = im.Scale("shi sing.webp", 550, 800)
image shi3 = im.Scale("shi shock.webp", 550, 800)
image rit1 = im.Scale("rit cheese.webp", 550, 800)
image rit2 = im.Scale("rit smug.webp", 550, 800)
image rit3 = im.Scale("rit sweat.webp", 550, 800)
image rit4 = im.Scale("rit smile.webp", 550, 800)
image rit5 = im.Scale("rit think.webp", 550, 800)
image rit6 = im.Scale("rit dead.webp", 550, 800)
image rit7 = im.Scale("rit revive.webp", 550, 800)
image rit8 = im.Scale("rit dead2.webp", 550, 800)
image hon1 = im.Scale("hon smile.webp", 640, 925)
image kur1 = im.Scale("kur attack.webp", 710, 913)
image kur2 = im.Scale("kur tehe.webp", 710, 913)
image miy1 = im.Scale("miy base.webp", 710, 937)
image mar1 = im.Scale("mar excite.webp", 540, 850)
image mar2 = im.Scale("mar angy.webp", 550, 850)
image mar3 = im.Scale("mar hmmm.webp", 550, 850)
image pmar1 = im.Scale("mar pirate think.webp", 900, 1150)
image pmar2 = im.Scale("mar pirate sparkle.webp", 900, 1150)
image pmar3 = im.Scale("mar pirate angy.webp", 900, 1150)
image shik1 = im.Scale("hik scholar.webp", 590, 800)
image dayt = im.Scale("dayt.png", 700, 700)
image bg dead = im.Scale("bg dead.jpg", 1920, 1080)
image mic1 = "mic.png"
image mic2 = "mic.png"
image senko = im.Scale("komStare.webp", 250, 250)
image cringe = im.Scale("mizCringe.webp", 250, 250)
image kommiz = im.Scale("mizKom.webp", 200, 200)
image muscle = im.Scale("muscle.png", 250, 250)
image badsub = Movie(play="hitorigoto.webm", loop=False)
image actualnightmare = Movie(play="cursed.webm", loop=False)

init python: 
    import time as gettime
    rhythm_game_songs = [
    Song('Seishun wa Non-stop!', 'audio/sb69.mp3', 'audio/sb69.beatmap.txt'),
    Song('Tokimeki Experience!', 'audio/bandori.mp3', 'audio/bandori.beatmap.txt'),
    Song('Colorful Dreams! Colorful Smiles!', 'audio/lovelive.mp3', 'audio/lovelive.beatmap.txt'),
    Song('Onegai! Cinderella', 'audio/imas.mp3', 'audio/imas.beatmap.txt'), 
    Song('Make debut!', 'audio/umamusume.mp3', 'audio/umamusume.beatmap.txt')
    ]
    config.has_quicksave = False
    config.has_autosave = False
init:
    $ timer_range = 0
    $ timer_jump = 0
default persistent.rhythm_game_high_scores = {
    song.name: (0, 0) for song in rhythm_game_songs
}
default selected_song = None
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
screen countdown:
    timer 0.01 repeat True action If(timeleft > 0, true=SetVariable('timeleft', timeleft - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value timeleft range timer_range xalign 0.5 yalign 0.93 xmaximum 1000 at alpha_dissolve 
    zorder 99
screen countdown2:
    timer 0.01 repeat True action If(timeleft > 0, true=SetVariable('timeleft', timeleft - 0.01), false=[Hide('countdown')])
    bar value timeleft range timer_range xalign 0.5 yalign 0.1 xmaximum 1350 at alpha_dissolve 

label start:
    $ globalpoints = 0
    narrator "Welcome to your worst nightmare"
    scene bg main
    play music "audio/amqtheme.mp3" fadeout 1.0 fadein 1.0
    $ renpy.notify('Now playing: No Game No Life')
    show hib1 at right
    hib "God you're bad at this game"
    hide hib1
    show hib2 at right
    hib "Still, I'm surprised you managed to sit through all 30 Precure openings..."
    hib "... You even rolled All Stars DX2 right that one time!"
    hide hib2
    show hib3 at right
    hib "I'd consider that a victory, if anything"
    hib "Lemme know if you're still down to learn the Pokémon movies next week!"
    menu:
        "S-sure... Ahaha...":
            hide hib3
            show hib4 at right
            hib "Great! Here's to more mental deterioriation!"
        "M-maybe not...":
            hide hib3
            show hib5 at right
            hib "Fine... But if you don't we're not going to ever hit our goal of 5 points in Eastern Ranked"
            hib "Spamming Conan isn't going to get us to the top!"
    scene black
    narrator "Your vision begins to blur..."
    stop music
    scene bg bedroom
    j "God... what even was that nightmare..."
    j "Time to set up the stream I guess"
    scene black
    narrator "You are about to play as an AMQ bully!"
    narrator "Guess the anime opening correctly and earn points, rise above the rest, emerge triumphant..."
    narrator "...and get called out for having not touched grass in weeks"
    narrator "Good luck!"
    call initgame({"game101":["Kuroko no Basuke", "Haikyuu!! Second Season", "SK8 the Infinity", "Pingu in the City"], "game102":["Initial D: First Stage", "Drifters", "Ikki Tousen", "Yaoi!!! on Ice"], "game103":["Marie & Gali ver. 2.0", "Sword Art Online: Extra Edition", "Naruto Shippuuden", "Hunter x Hunter"]}, ["Haikyuu!! Second Season","Ikki Tousen","Marie & Gali ver. 2.0"]) from _call_initgame
    if gamepoints > 0:
        narrator "Not bad, %(gamepoints)d points... That'll show those default Hibikis"
    else:
        j "Haha sorry guys, my Catbox wasn't working"
        narrator "Kitty will remember that."
    scene bg bedroom with fade
    j "Another great day farming tickets..."
    play sound "audio/knock.mp3"
    $ renpy.pause(2.5, hard=True)
    j "Mm...?"
    show kom1 with moveinright
    play music "audio/bgm01.mp3" fadeout 1.0 fadein 1.0 volume 0.2
    $ renpy.notify('Now playing: Tobidase! Machine Hiryuu')
    kom "Greetings AMQ booli. 'Tis I, the great shrine maiden Komugi!"
    j "Whoa!!!"
    j "Wait, shouldn't you be at like, y'know a shrine?"
    kom "That's..."
    hide kom1
    show kom2
    kom "Why don't you ask Mizuki that instead?! Hmph..."
    kom "A~ ny~ way~!!"
    hide kom2
    show kom3:
        xalign 0.5 yalign 0.99
        linear 0.3 xalign 0.99
    kom "The world of AMQ needs your help!"
    kom "{i}And I swear this isn't the beginning of a trashy isekai plot{/i}"
    kom "Based on how many hours you've spent mindlessly typing words into a box on a fucking browser game, {i}and I mean look at those hours...{/i}"
    show ghib1 at truecenter
    kom "We've decided you'd be perfect to help the world of AMQ defeat the illusive {b}SOLID GOLD HIBIKI{/b}"
    kom "You won't go unrewarded though - if successful, we'll pay you in glorious tickets! {i}More tickets than our game mods get in a whole year!{/i}"
    hide ghib1
    j "So like... 3?"
    kom "Hey, don't get greedy now."
    hide kom3
    show kom1 at right
    kom "... So, to help you train for your big fight, I've enlisted the help of my good friend Noel to beat ya into shape"
    show noe1 at left with moveinleft
    noe "Yahallo! One wrong Gintama season is gonna be one Jashin-sized dropkick outa you!"
    j ":fearful:"
    hide noe1
    show noe2 at left 
    noe "Our training begins at dawn, get ready soldier!"
    hide noe2
    hide kom1
    show kom4:
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
    show hib1 at right
    hib "{cps=10}...Oooooi{/cps}"
    hib "Just how long do you plan on dozing off like that!"
    hib "Even Yukari's gotten impatient y'know"
    show yuk1 at left with moveinleft
    yuk "Finally awake are nya?"
    hib "It's finally time for us to learn every {b}ALI PROJECT{/b} song!"
    hide hib1
    show hib3 at right
    hib "There won't ever be another Rozen Maiden or Avenger song that'll get us!!"
    hib "Ready when you are! Let's disable dropdown too while we're at it!"
    call initgamenodd({"game201":["tsuki to laika to nosferatu", "irina: the vampire cosmonaut"]}, randsong=True) from _call_initgamenodd
    scene bg main with fade
    if gamepoints == 15:
        show hib2 at right with moveinright
        hib "I'm glad you got that at least, only 1921 left to go!"
        hib "{cps=10}... to {cps=*0.5}... go {cps=*0.25}...{/cps}"
    else:
        show yuk3 at left with moveinleft
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
    show noe3 at right with moveinright
    noe "You alright...? You look like you've seen a ghost..."
    noe "Or worse, {i}a Hibiki{/i}"
    menu:
        "It's nothing...":
            hide noe3
            show noe2 at right
            noe "Then I suppose we should get started with our training today then!"
            noe "Let's go~ Komugi and Mizuki are waiting for us"
        "Just a nightmare":
            noe "Then I suppose you're in no shape to come train today then"
            hide noe3
            show noe1 at right
            noe "Just leave it to the world's greatest detective Noel! I'll have you feeling better in no time!"
            noe "Hurry, lie down and relax your min-"
            play sound "audio/knock.mp3"
            $ renpy.pause(2.5, hard=True)
            show kom2 at left with moveinleft
            kom "Oi what's takin' so long! Mizuki and I have been waiting ages over there, {i}and you know how much I can't stand her...{/i}"
            hide noe1
            show noe4 at right
            noe "F-fine... I'll get changed and we can go..."
        "OH MY SWEET ANGEL NOEL_#)@!THANK HEAVENS YOU'RE REAL":
            scene black
            centered "Bonked by Ege Ending"
            "Ege's Spirit" "Bad"
            return
    scene black with fade
    scene bg shrine with fade
    show skom at right
    kom "Here we are!"
    show smiz
    miz "Hiya, looks like you made it~"
    show snoe at left
    noe "Now it's time to regret all your life decisions!"
    noe "Noel's super ultra intense bootcamp begins now!"
    scene bg shrine with fade
    show skom
    kom "Let's start you off with an easy warm up round!"
    kom "Here we go!"
    call initgame({"game302":["Digimon Ghost Game","Pocket Monsters","Doraemon","Pico: Boku no Chiisana Natsu Monogatari"], "game304":["Noragami","Ao no Exorcist","Arslan Senki","gdgd Fairies"], "game305":["Enen no Shouboutai: Ni no Shou", "Kiseijuu: Sei no Kakuritsu", "Shingeki no Kyojin: The Final Season", "Love Live! Sunshine!!"], "game303":["Himouto! Umaru-chan", "New Game!", "Gamers!", "When They Cry Extra: Cat Killing Chapter"], "game301":["Kishibe Rohan wa Ugokanai", "Shadows House", "Ghost Hunt", "Gegege no Kitarou"]}, ["Doraemon", "Noragami", "Shingeki no Kyojin: The Final Season", "Himouto! Umaru-chan", "Gegege no Kitarou"], gamebg="bg shrineblur.jpg") from _call_initgame_1
    scene bg shrine with fade
    show skom
    if gamepoints >= 30:
        kom "Hey! That wasn't so bad now was it..."
    else:
        kom "Well, today was your first day after all, don't sweat it!"
    kom "Just make sure to keep practicing and sooner or la-"
    show snoe at right with moveinright:
    noe "ME ME ME! My turn! My turn!"
    noe "Unlike Komugi, I won't be going so easy on you!"
    noe "Hope you remember your titles well~"
    call initgamenodd({"game404":["clannad after story"], "game405":["komi can't communicate","komi-san wa comyushou desu."], "game402":["yuru yuri san☆hai!", "yuru yuri san hai!", "yuruyuri season 3"], "game401":["the familiar of zero", "the familiar of zero f", "zero no tsukaima", "zero no tsukaima f"], "game403":["brynhildr in the darkness", "gokukoku no brynhildr"]}, gamebg="bg shrineblur.jpg") from _call_initgamenodd_1
    scene bg shrine with fade
    show snoe
    if gamepoints >= 45:
        noe "Woaah!! I'm getting pumped~ Good job back there!"
    else:
        noe "Hey, we've still got tons of days together ahead of us to get better~"
        noe "And I'll be supporting you all the way~"
    show smiz at right with moveinright:
    play music "audio/bgm02.mp3" fadeout 1.0 fadein 1.0 volume 0.2
    $ renpy.notify('Now playing: Zombie Land Saga')
    miz "Move outa here!"
    hide snoe
    hide smiz
    show smiz
    miz "I didn't come all the way out here so that those two could baby you with their {b}FREE SONGS{/b}"
    miz "Tell you what, I'll give you a real challenge, stuff that'll make everyone :place_of_worship: when you join a pub room"
    miz "You'll be a legend!"
    miz "But it won't be easy... Fail my training and you die."
    hide smiz
    show smizangry
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
    show smiz
    miz "Well, looks like you beat me... Guess you're better at this than I thought"
    miz "And here I was taking you for some loser who does nothing other than bully streamers and play S/A lobbies"
    miz "You've earned my respect"
    narrator "Mizuki joins your party!"
    hide smiz
    show skom at right with moveinright
    show snoe at left with moveinleft
    noe "Wooo~ You did it! Just like I knew you could, of course"
    kom "To commemorate this occassion, I reckon we should go celebrate!"
    noe "And what better way to celebrate than with..."
    kom "Karaoke!"
    noe "Karaoke!"
    miz "Smurfing ranked!"
    miz "Oh yeah, right, karaoke, force of habit my bad"
    noe "Hurry weeb-kun, that Japanese isn't gonna butcher itself"
    scene bg karaoke with fade
    kom "Let's get this started then! I'll go first"
    scene bg karaokedark
    show kom1 at right with moveinright
    show mic1:
        xalign 0.8
        yalign 1.05
    kom "Here I go..."
    $ renpy.notify('Now playing: Kekkai Sensen & Beyond (Kamishiro)')
    play sound "audio/karaoke1.mp3" fadein 1.0 fadeout 1.0
    $ renpy.pause(5.0, hard=True)
    miz "{i}Oooh!{/i} I know this one!{p=5.0}{nw}"
    noe "You're killin it!{p=5.0}{nw}"
    miz "Letsgooooo{p=59.5}{nw}"
    stop sound fadeout 1.0
    hide kom1 with moveoutright
    show miz1 at right behind mic1 with moveinright
    miz "Step aside and I'll show you guys how it's {i}really{/i} done~"
    $ renpy.notify('Now playing: M3: Sono Kuroki Hagane (Daytona)')
    play sound "audio/karaoke2.mp3" fadein 1.0 fadeout 1.0
    "{p=5.0}{nw}"
    kom "I guess this isn't too bad... {w=3.0}\n{size=-8}{i}Though mine was better... obviously...{/i}{/size}{p=5.0}{nw}"
    noe "The voice of an angel... honSugoi {p=56.5}{nw}"
    stop sound fadeout 1.0
    hide miz1 with moveoutright
    miz "Thank you, thank you~ I knew you guys would love it"
    noe "Oh, my turn already?"
    show noe1 at right behind mic1 with moveinright
    noe "Well, I'm not really the best at singing but I'll give this my best shot~✰"
    hide noe1
    show noe2 at right behind mic1
    $ renpy.notify('Now playing: Yu-Gi-Oh! (Shuuka)')
    play sound "audio/karaoke3.mp3" fadein 1.0 fadeout 1.0
    "{p=8.0}{nw}"
    miz "Who told you you couldn't sing, Noel? You're already waaaay better than Komugi here {p=5.0}{nw}"
    kom "{size=+10}{b}Oi!{/b}{/size}{w=3.0}\n...But you are pretty good though...{p=5.0}{nw}"
    j "B-boku no kirakira pikapika kagayaku aidoru!!!!!!{p=6.0}{nw}"
    narrator "(Still least cringe weeb){p=50.0}{nw}"
    stop sound fadeout 1.0
    hide noe2 with moveoutright
    j "I understood nothing but that was beautiful :')"
    narrator "You applaud like the absolute simp you are"
    noe "Ehe~ thanks everyone~"
    miz "Oh? This next one's a duet"
    noe "Maybe you and Komugi should do it together then!"
    kom "Wha-"
    noe "C'mon... just this one time"
    kom "Fine..."
    show mic2:
        xalign 0.2
        yalign 1.05
        xzoom -1.0
    show miz1 at left behind mic2 with moveinleft:
        xzoom -1.0
    show kom1 at right behind mic1 with moveinright 
    $ renpy.notify('Now playing: Sewayaki Kitsune no Senko-san (ChriS)')
    play sound "audio/karaoke4.mp3" fadein 1.0 fadeout 1.0
    "{p=5.0}{nw}"
    noe "Time to get my glowsticks out cus this is :fire:{p=5.0}{nw}"
    show glowsticks with pixellate:
        xalign 0.5
        yalign 0.3
        xzoom 0.67
        yzoom 0.67
    show senko behind mic1:
        xalign 0.903
        yalign 0.54
    show cringe behind mic2:
        xalign 0.1
        yalign 0.54
    show kommiz:
        xalign 0.5
        yalign 0
    "{size=-12}One more ashubiduba mofu-mofu, yeei, Two more ashubiduba mofu-mofu, yeei, Forever ashubiduba mofu-mofu, chu! Kuragari no heya akari tomosu Kesshite (kesshite) Hitori ni nado sasenu zo Itsu datte koko ga yasurageru basho Anata (onushi) mo kitto sou omou deshou Konya wa sukoshi hierukara Kaze demo hiicha inai ka no? (shinpaisei nee) Atatakai ryouri o tsukutte matou Amayakasa rete agerukara (warawa mo mazeru no ja!) hayaku kaette kinasai yo Go houbi mo youi shite mattete agerukara Okaeri nanojya kyou mo otsukaresama Itoshisa ga heya-chuu dondon hirogatte iku Onushi no shiawase o negau Saa zonbun ni kokoroyukumade motto amaeru ga yoi Nanbyakkai, nanzenkai suki na dake amaeru nojya Kyou mo shippo futte mofu-mofu!{/size}{p=80.0}{nw}"
    stop sound fadeout 1.0
    scene bg karaokedark with Fade(2.0, 0.0, 2.0)
    show noe2 at right
    show mic1:
        xalign 0.8
        yalign 1.05
    $ renpy.notify('Now playing: Bakemonogatari (???)')
    play sound "audio/karaoke5.mp3" fadein 1.0 fadeout 1.0
    narrator "{i}...And the karaoke room continues...{/i}{p=88.0}{nw}"
    stop sound fadeout 1.0
    scene bg karaokedark with Fade(2.0, 0.0, 2.0)
    show miz1
    show kom1 at left with moveinleft
    show noe1 at right with moveinright
    noe "Hey, hey! It's your turn now~"
    miz "Sing something for us will ya?"
    kom "C'mon, can't be that bad amirite?"
    narrator "You take a deep breath{cps=3}......{/cps}"
    $ renpy.notify('Now playing: Eromanga Sensei (Jack Parkson)')
    play sound "audio/karaoke6.mp3" fadein 1.0 fadeout 1.0
    show badsub:
        yalign 0.00
    "{p=3.0}{nw}"
    hide noe1 
    show noe3 at right
    noe "...{p=5.0}{nw}"
    hide kom1
    show kom3 at left
    kom "...{p=5.0}{nw}"
    show cringe:
        xalign 0.5
        yalign 0.54
        xzoom -1.00
    miz "Maybe I should've killed you back at the shrine after all{p=8.0}{nw}"
    noe "Please... stop dancing...{p=73.0}{nw}"
    hide badsub
    stop sound fadeout 1.0
    scene bg karaoke 
    show miz1
    show kom3 at left
    show noe3 at right
    noe "{cps=3}.....{/cps} That was... really somethin alright... ahah"
    j "Never again..."
    play sound "audio/knock.mp3"
    $ renpy.pause(2.5, hard=True)
    kom "Mm? Who could that be..."
    hide miz1 with moveoutleft
    hide kom3 with moveoutleft
    hide noe3 with moveoutleft
    show shi1 with moveinleft
    shi "Hiiii~ I heard y'all were doing a karaoke room so I stopped by"
    shi "The name's Shiina, you can call me Shi or Ina"
    hide shi1
    show shi2
    shi "So, you're the guy who spends 10 hours a day in their room guessing anime songs?"
    shi "Why don't 'cha try guessing the stuff I'm gonna sing then!"
    shi "You'd be surprised at my immaculate vocal range, I tell ya"
    "Ege's Spirit" "Warning: This is not true and Shiina's voice is impossible to listen to"
    shi "Let's get started then shall we~ I promise it'll be easy breezy~"
    scene black
    narrator "The following songs' vocals have been generated with text-to-speech software. They sound horrible. Good luck."
    call initgamenodd({"shiina01":["lucky star"],"shiina02":["blend-s"], "shiina03":["boku no hero academia", "my hero academia"], "shiina04":["sword art online ii"], "shiina05":["gon"]}, gamebg="bg karaokedark.jpg") from _call_initgamenodd_2
    scene bg karaoke
    show shi2 with fade
    shi "That was so much fun!! Glad you guys let me join~"
    shi "Oh, that reminds me, I came here to ask you guys for help"
    show kom1 at right with moveinright
    kom "Sure, whadaya need?"
    hide shi2
    show shi1 
    shi "Well, it's no big deal really, there's just some dude who's been chasing me since morning"
    j "Chasing you?! That doesn't seem safe!"
    play sound "audio/knock.mp3"
    $ renpy.pause(2.5, hard=True)
    "???" "I FINALLY FOUND YOU SHIINA GET OVER HERE!"
    play music "audio/bgm03.mp3" fadein 1.0 fadeout 1.0 volume 0.25
    $ renpy.notify('Now playing: Gun X Sword')
    show dayt at left with moveinleft:
        yalign 0.9
    j "Hold up! Who are you? Why are you after her!"
    narrator "{i}The (possibly) only act of heroic bravery our protagonist will ever display{/i}"
    dayt "Well, she comitted the HEINOUS crime of requesting a SEASONAL INSERT in #database-fixes"
    shi "B-but it's already been out for 2 months-"
    dayt "WAS IT EVEN CREDITED?"
    hide shi1
    show shi3
    shi "N-no... "
    dayt "That's what I thought"
    dayt "Now then, time for your ban, see you next year~"
    j "STOP RIGHT THERE!"
    dayt "Oi kid, do you even know who I am?"
    noe "That's Daytona! The notorious AMQ mod who deletes short titles and compares everything to Hitler!"
    miz "You sure? Pretty rare to see an AMQ player outside their room dont'cha think?"
    dayt "That's cus I don't play that game"
    kom "But you still gladly delete beloved names like {i}A Tale of Worst One{/i}?!"
    dayt "Fun is not allowed."
    dayt "Look, I'll tell ya what, defeat me and I'll let 'er go{p}But be warned, I won't be going easy on ya."
    dayt "In fact, I've already REMOVED all those PRECIOUS NAMES people keep whining over."
    dayt "Come at me, what're you waiting for"
    $ proceed = False
    while not proceed:
        menu:
            "Ege's Spirit" "It's recommended you save your game before fighting bosses; dying means you lose your current save data"
            "Begin fight":
                $ proceed = True
            "Maybe later...":
                dayt "I don't have all day, I have a lot of Swift code to procrastinate writing"
    call daytbattle from _call_daytbattle
    centered "Back home..."
    scene bg bedroom with fade
    j "Sure's been a long day..."
    show noe2 at right with moveinright:
    noe "But you did great today!! {size=-1}A{/size}{size=-3}si{/size}{size=-4}de{/size} {size=-5}fr{/size}{size=-7}om {/size}{size=-8}th{/size}{size=-9}at {/size}{size=-10}sin{/size}{size=-12}gin{/size}{size=-13}g e{/size}{size=-15}arl{/size}{size=-16}ier{/size}{size=-18}...{/size}"
    noe "Be sure to get some rest now~ Tomorrow we'll be off to the arcade!"
    noe "... For training purposes of course"
    noe "Good night now~"
    hide noe2 with moveoutright
    menu:
        "Sleep":
            scene black with Fade(3.0, 0.0, 3.0)
    call gameshow from _call_gameshow
    scene bg bedroom
    j "... {w} I gotta stop watching all that Jewelpet, I swear it's driving me insane"
    "???" "Oh~ You're finally awake! Took you long enough..."
    show noe1 at right with moveinright
    j "Were... you just standing there all night?"
    noe "Well if I told you what happened we won't be able to sell Denpasoft patches of this game if it ever takes off"
    j "Wha-"
    noe "Don't mind that! It's time for your morning training!"
    noe "They say the best way to remember something is frequently recalling what you've learnt"
    noe "{size=-5}I mean, I personally prefer staring at my spreadsheet of poorly written notes and beating myself up for every song I miss for hours and hours and hours... {/size}BUT!"
    noe "I wouldn't put you through that, or anyone... So! Hope you're ready~ Here it comes!"
    scene black with fade
    call initgame({
        "game701":["Shouwa Genroku Rakugo Shinjuu: Sukeroku Futatabi-hen","Kabukichou Sherlock","Mawaru Penguindrum","Bem"],
        "game702":["Toaru Majutsu no Index", "Nogizaka Haruka no Himitsu", "Kannazuki no Miko", "Hayate no Gotoku!"],
        "game703":["Witch Craft Works","Maerchen Maedchen","Comet Lucifer", "Gingitsune"],
        "game704":["Tsukimonogatari","Monogatari Series Second Season", "Zoku Owarimonogatari", "Koyomimonogatari"],
        "game705":["Soutai Sekai","Build-Divide: #000000 (Code Black)","Build-Divide: #FFFFFF (Code White)","Fight League: Gear Gadget Generators"],
        "game706":["Bokurano","Seikon no Qwaser","Rail Wars!","Suzumiya Haruhi-chan no Yuuutsu"],
        "game707":["Aldnoah.Zero","Re:Creators","Kidou Senshi Gundam Unicorn RE:0096","Ginga Eiyuu Densetsu: Die Neue These - Kaikou"],
        "game708":["Itsudatte Bokura no Koi wa 10 cm Datta.","Kono Sekai no Tanoshimikata: Secret Story Film","Suki ni Naru Sono Shunkan o: Kokuhaku Jikkou Iinkai","Heroine Tarumono! Kiraware Heroine to Naisho no Oshigoto"]
    },[
        "Bem", "Nogizaka Haruka no Himitsu", "Comet Lucifer", "Koyomimonogatari", "Soutai Sekai", "Suzumiya Haruhi-chan no Yuuutsu", "Kidou Senshi Gundam Unicorn RE:0096", "Heroine Tarumono! Kiraware Heroine to Naisho no Oshigoto"
    ], gamebg="bg bedroom.jpg") from _call_initgame_2
    scene bg bedroom with fade
    show noe2 at right with moveinright
    noe "How was it? I threw in a few curveballs for ya in there!"
    noe "Well, now that that's out of the way, let's get going~☆"
    hide noe2 with moveoutright
    scene bg arcade with fade 
    show anoe1 at right with moveinright
    noe "Here we are!"
    play music "audio/bgm07.mp3" fadein 1.0 fadeout 1.0 volume 0.08
    $ renpy.notify('Now playing: Gamers!')
    noe "Isn't this great~? The fresh sweet smell of sweat, sweaty people, questionable pizza and a random kid's birthday party"
    noe "Of course {i}you've{/i} never been here though so let me show you around!"
    j "Eh- Shouldn't we wait for Komugi and Mizuki to arrive at least?"
    noe "Mm? Oh, well Mizuki's busy prepping for New Year's... something about stealing all the lucky fortunes for herself..."
    j "Oh so Komugi's probably doing the same thing then..."
    noe "lol no she failed math class so she's stuck with Hikari-sensei learning polynomials or something kekw"
    noe "So anyway, it's just the two of us today~"
    hide anoe1
    show anoe2 with fade:
        xalign 0.5
        yalign 1.00
    noe "And here's my favorite game~ Why don't 'cha give it a whirl, I'm sure it'll be fun{w}\n{size=-10}... (Unless you're allergic to idol songs){/size}"
    "♪ Welcome to Arse ♪{w}\n{i}{size=-7}♪ Tap your keyboard, to the beat ♪{/size}{/i}"
    window hide
    $ renpy.music.set_pause(True, channel="music")
    call rhythm_game_entry_label from _call_rhythm_game_entry_label
    $ renpy.music.set_pause(False, channel="music")
    noe "{size=-10}Bet all you osu!mania players are frothing right about now, all 7 of you{/size}{w}\nAhem-"
    "{i}{size=-7}♪ See ya next time ♪{/size}{/i}"
    noe "So how was it~ I think you did pretty good back there!"
    noe "While you were gone I found some more cool games in the arcade!"
    noe "Looks like they even have some AMQ themed ones, your forte~"
    menu:
        noe "Which one should we play?"
        "Blind Battle Royale":
            call blindbr from _call_blindbr
        "Bad Teammate":
            call badteammate from _call_badteammate
        "Indonesian AMQ Simulator":
            scene black with fade
            call indonesianamq from _call_indonesianamq
    scene bg arcade with fade
    show anoe1 at right with moveinright
    noe "See? Even someone like you can have fun outdoors, I knew you had it in ya mhm"
    "???" "So I heard there's a new god in town..."
    play music "audio/bgm06.mp3" fadein 1.0 fadeout 1.0 volume 0.2
    $ renpy.notify('Now playing: Hakaima Sadamitsu')
    show rit1 at left with moveinleft
    rit "Ah, I've heard of ye alright... You're that Yolowolf something kid aren't cha?"
    j "Uhhh"
    rit "Names Ritsu, but they call me Risu, cus I'm fast, like a squirrel."
    narrator "(Least cringe gamer)"
    rit "First time around these parts I reckon, mineas?"
    j "Uhhh..."
    hide rit1
    show rit2 at left
    rit "I'll have ya know I set the world reck'rd for all these here games... I'm, kind of what they call a big deal"
    j "Oh, I didn't see any scores earlier on Arse though"
    $ renpy.music.set_pause(True, channel="music")
    hide rit2
    show rit5 at left
    rit "No one plays that game, it's broken af"
    rit "{size=-10}... Keeps telling me I missed when I CLEARLY HIT THEM NOTES I TELL YA*@^!{/size}"
    narrator "(Least salty osu player)"
    rit "I asked the loser in charge to fix that thing like three months ago, but you know how it is... soon™ (just like Ege fiixing tpyos)"
    hide anoe1
    show anoe3 at right
    noe "Wait, so you're saying Ege didn't make this game?"
    rit "Please, that's just as believable as him saying 'people play AMQ for the avatars'"
    rit "Ahem- ANYWAY!"
    $ renpy.music.set_pause(False, channel="music")
    hide rit5
    show rit2 at left
    rit "I hereby challenge ye to defend my title as the strongest in all of Bumfuck, Missouri"
    rit "Prepare to meet your match Orfey!!"
    j "Uuuuuuuuuuuhhhhhhhh"
    rit "What."
    rit "I know, you think you're too good for me don't 'cha small fry?"
    rit "Show me your diamond badge then c:{w}\nOooooh wait~ You don't have any badges aha!"
    rit "You just don't have my top-tier gamer reflexes{w} {size=-5}(to google the lyrics in 15 seconds){/size}"
    rit "I'm not letting you go that easily."
    $ proceed = False
    while not proceed:
        menu:
            "Ege's Spirit" "It's recommended you save your game before fighting bosses; dying means you lose your current save data"
            "Begin fight":
                $ proceed = True
            "Maybe later...":
                rit "Quit bein' a coward already, krice"
    stop music fadeout 1.0
    call ritsubattle from _call_ritsubattle
    scene bg arcade with fade
    show rit3 at left with moveinleft
    rit "...I guess you *cough* really are sumthin... WinAxel..."
    rit "B..but mark my words Mael!! I'll get 'cha some day!!"
    j "(Man... and she almost got my name right there)"
    "???" "There you are~ finally found you-"
    show hon1 at right with moveinright
    hon "Ricchan~"
    hide rit3
    show rit4 at left
    rit "{size=-7}H-Honocchi!! I told you to call me Risu, remember!{/size}"
    hon "Ah~ my bad..."
    hon "Anyway... Kyouko's ready to pick us up, let's go~"
    rit "Ah"
    hide rit4
    show rit2 at left
    rit "Well I guess that can't be helped, see ya next time Anti"
    hide hon1 with moveoutright
    hide rit2 with moveoutright
    show anoe2 at left with moveinleft
    noe "Looks like Komugi and Mizuki aren't done yet... Let's go grab dinner then~ You did great back there!"
    scene bg dinner with Fade(2.0, 0.0, 2.0)
    show anoe2 with moveinleft
    noe "Uwaa~ I'm starving, what're you gonna order?"
    menu:
        noe "I think I'm having the Tropical-Rouge PanCake Tower!"
        "Cheese Gyuudon":
            noe "Oooh that looks yummy, do you get this often?"
            hide anoe2
        "Tuna Tataki":
            noe "Look at the price! Where'd you get the money for that...{w}{s}i thought u were a neet{/s}"
            hide anoe2
        "AMQ Player Salad":
            "{i}Garlic sautéed premium-grade Cheeto Puffs in an aromatic salted caramel Mountain Dew vinaigrette{/i}{w}\nLimited time only: Comes with free tendies!"
            hide anoe2
            show anoe3
            noe "W-well I was gonna ask to try some of your food but, you can have all of that one..."
            hide anoe3
    show anoe1 
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
    show anoe1
    noe "And just in time too... Our food's here! Itadakimasu~"
    scene bg movies with Fade(3.0, 0.0, 3.0)
    $ renpy.pause(3.0, hard=True)
    show anoe3 at right
    noe "This is taking forever...."
    noe "{size=-3}Can't believe we pay $20 and still have to sit though a trailer for a B-list superhero movie, a commercial for a phone that barely improved over last year's model, and a random sob story that {i}somehow{/i} always turns out to be a car insurance ad...{/size}"
    hide anoe3
    show anoe1 at right
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
    show anoe1 at right
    noe "Aaaaand the movie still hasn't started..."
    j "What even are we watching anyway?"
    noe "Mm... Well it's..."
    "???" "Shhhh!! Could ya pipe it down for just a sec back there..."
    show kur1 with moveinleft
    kur "Been waitin' for this movie since the day it was announced, wouldn't wanna miss a single moment~"
    kur "Are yall fans of the Rail the Blood: Index Fortress in Space of the Dead franchise too?"
    j "That's a... pretty elaborate getup just to see a movie"
    noe "Well it is an anime movie, I guess it isn't surprising to run into a few cosplayers"
    kur "Cosp- I'll have you know I'm a bona fide Royal Witch for the Imperial Magical Nation Army! {size=-10}{w}(At least in my headcanon fanfiction for what happens after Chapter 16.5){/size}"
    show miy1 with moveinleft:
        xalign 0.1
        yalign 0.8
    miy "Ahhh... don't mind my friend here, we're from the convention down the street..."
    j "Oh, it's starting, it's starting"
    miy "Let's head back then shall we~"
    hide kur1
    show kur2 behind miy1:
        xalign 0.5
        yalign 0.85
    kur "Okie!"
    hide miy1 with moveoutleft
    hide kur2 with moveoutleft
    scene black with Fade(3.0, 0.0, 3.0)
    $ renpy.pause(3.0, hard=True)
    centered "After the movie..."
    scene bg bedroom with fade
    show noe1 at right with moveinright 
    noe "Hope you learned something at least from today's training~ and also had fun along the way!"
    noe "Looks like you're getting used to the booli lifestyle already; eating, sleeping, and breathing AMQ all day"
    noe "Soon you'll be humming Aikatsu inserts on the bus and referring to anime only by their flex names in no time!"
    noe "Good night now~ Komugi's got plans for us tomorrow so make sure to wake up refreshed!"
    menu:
        "Sleep":
            scene black with Fade(3.0, 0.0, 3.0)
    "..."
    "......"
    "............."
    ".....................................!"
    ""
    "Welcome to your worst nightmare"
    show actualnightmare
    $ renpy.pause(11.5, hard=True)
    scene black
    ""
    "???" "...So ye finally decided to rear ye ugly head on me ship ay?"
    scene bg pirate with fade
    show pmar1 with moveinright:
        yalign 0.4
        xalign 0.5
    play music "audio/bgm09.mp3" fadein 1.0 fadeout 1.0 volume 0.2
    $ renpy.notify('Now playing: Mouretsu Pirates')
    mar "Who do you think ye are... steeping foot in MY WATERS?"
    hide pmar1
    show pmar2:
        yalign 0.4
        xalign 0.5
    mar "Best ye speak up before I splice ye into smithereens"
    j "W-who are you?"
    hide pmar2
    show pmar3:
        yalign 0.4
        xalign 0.5
    mar "THE LEVEL OF DISRESPECT COMING FROM YER TRAP"
    mar "I'm the feared Nightmare Lancer of the Tyrant's Eye - Deus Highest Death Impact of the Seventh Resilience Crest Master of Spinjitsu Houshou Fitzgerald Lalatina Marine the Swashbuckler"
    hide pmar3
    show pmar2:
        yalign 0.4
        xalign 0.5
    mar "Now remember that ok?"
    mar "Repeat after me!"
    mar "Night-"
    j "N-night..."
    scene bg playground
    stop music fadeout 1.0
    show mar1
    mar "-mare Lancer"
    j "Who is this... sassy lost child?"
    hide mar1
    show mar2
    mar "H-hey!!{w} {size=-7}At least play along for the name bit... I spent all day coming up with that...{/size}"
    mar "And!! I'll have you know I'm 4000 years old! (so you can go ahead and use that argument online i suppose but ymmv)"
    j "We are literally at a playground"
    mar "Humph. Mom said it was play time ok... Just follow 'long or I'll have you walk the plank!!"
    j "It's not nice to steal y'know...? Now give that piece of plywood back to whoever you sto-"
    mar "I've had enough!!!! Face me in a challenge this instant or off with your head!!"
    $ currentmonth = gettime.localtime(gettime.time())
    $ monthstr = gettime.strftime("%B", currentmonth)
    $ halloweendial = "Little early for Halloween don't cha think... It's only {}...".format(monthstr) if currentmonth.tm_mon < 10 else "Little late for Halloween don't cha think... It's already {}...".format(monthstr) if currentmonth.tm_mon > 10 else "Oh I guess it is October... Must be some Halloween thing..."
    j "[halloweendial]"
    show fortniteloli:
        xalign 0.1
        yalign 0.1
        xzoom 1.3
        yzoom 1.3
    mar "Just join my room already!!"
    scene black with fade
    call initgame({
        "game1401":["Youkai Watch", "Deltora Quest", "Future Card Buddyfight", "Ben 10: Omniverse"],
        "game1402":["Kira Kira Happy Hirake! Cocotama","Kamisama Minarai: Himitsu no Cocotama", "Mono no Kami-sama Cocotama", "Wonder Pets!"],
        "game1403":["Ojamajo Doremi Na-i-sho","Ojamajo Doremi Dokkaan","Motto! Ojamajo Doremi","Winx Club"],
        "game1404":["Barbapapa","BuBu ChaCha","Bonobono","Big Time Rush"],
        "game1405":["Kaiju Girls Season 2","Kaiju Step Wandabada","Wandaba Style","The Fairly OddParents"],
        "game1406":["Stitch! Itazura Alien no Daibouken","himitsukesshatakanotsume.jp","Hakata Mentai! Pirikarako-chan","Wow! Wow! Wubbzy!"],
        "game1407":["Ichigo Mashimaro", "Ichigo 100%", "Gal-gaku. II: Lucky Stars", "Strawberry Shortcake's Berry Bitty Adventures"],
        "game1408":["Totally Spies","Star vs. the Forces of Evil","Steven Universe","Phineas and Ferb"],
        "game1409":["Kim Possible", "The Legend of Korra", "Dexter's Laboratory", "Numb Chucks"],
        "game1410":["Pickle and Peanut", "Planet Sheen", "Fanboy & Chum Chum", "My Little Pony: A New Generation"]
    },[
        "Youkai Watch", "Mono no Kami-sama Cocotama", "Ojamajo Doremi Na-i-sho", "Bonobono", "Kaiju Step Wandabada", "Hakata Mentai! Pirikarako-chan", "Gal-gaku. II: Lucky Stars", "Jewelpet: Magical Change", "Beyblade Burst Sparking", "Eiga Precure Dream Stars!"
    ], gamebg="bg playground.jpg", randsong = True,fortniteloli=True) from _call_initgame_4
    ""
    "..."
    "......."
    "...................!"
    play sound "audio/alarm.mp3" 
    $ renpy.pause(3.0, hard=True)
    "So... bright..."
    scene bg bedroom2 with fade
    play music "audio/bgm11.mp3" volume 0.2 fadein 1.0 fadeout 1.0
    $ renpy.notify('Now playing: Comic Girls')
    "Just as the early morning sunlight filled the room through the windows beside me, I opened my eyes..."
    "Carried by a gentle breeze, a cherry blossom petal made its way onto the palm of my hand..."
    "Spring..."
    "Despite having lived here my entire life, never before had I seen the small town of Toyosato blanketed in a fluttering ocean of pink"
    "Like a scene from a movie... the Tokyo from 5 Centimeters per Second comes to mind..."
    "And in that sort of cliché sense, starting today, I would finally become a high school student."
    "With that, I closed the door behind me, and made my way to the entrance ceremony."
    play sound "audio/door.mp3"
    stop music fadeout 1.0
    $ renpy.pause(0.6, hard=True)
    scene black with fade
    $ renpy.notify('Now playing: Akebi-chan no Sailor Fuku')
    $ renpy.movie_cutscene("newbeginning.webm")
    play sound "audio/bell.mp3"
    scene bg musicroom with Fade(3.0, 0.0, 3.0)
    "It was on that day, however, that I met them..."
    "Looking for a club to join, I climbed the stairs up to the music room..."
    scene bg musicroom2 with fade
    show kon_ritsu with moveinright:
        xalign 0.9
        yalign 1.0
    rit "Ah! You're the freshman aren't ya? I see you brought your guitar, do you play?"
    show kon_mio with moveinleft
    "Mio" "We're just about to practice too, why don't you stay for a bit"
    show kon_mugi with moveinleft:
        xalign 0.1
        yalign 1.15
    "Mugi" "And perhaps stay for some tea as well~"
    "You" "Ehhhh.... I don't know that many songs though, compared to you guys I'm a total beginner!"
    rit "Relax~ We mostly play anime openings around here, so there's gotta be at least some you recognise..."
    rit "How's about you sit through our practice today, then you can decide if you wanna join us"
    "Mugi" "Oh~ Tea's ready!"
    rit "Well, we'll get started {i}eventually...{/i}"
    scene bg perform with fade
    rit "Well then, after 12 entire cakes and the entire Asian continent's worth of tea gone, let's get started!"
    call initgamenodd({
        "game1501":["rakudai kishi no cavalry","chivalry of a failed knight","yrlavac on ihsik iadukar","thgink deliaf a fo yrlavihc"],
        "game1502":["baka to test to shoukanjuu","baka & test: summon the beasts","uujnakuohs ot tset ot akab","stsaeb eht nommus :tset & akab"],
        "game1503":["nanbaka", "the numbers","akabnan","srebmun eht"],
        "game1504":["amagami ss+","+ss imagama"],
        "game1505":["2.43: seiin koukou danshi volley-bu","2.43: seiin high school boys volleyball team","ub-yellov ihsnad uokuok niies :34.2","maet llabyellov syob loohcs hgih niies :34.2"]
    },gamebg="bg perform.jpg", keion=True) from _call_initgamenodd_6
    centered "You begin to feel lightheaded..."
    play sound "audio/drop.mp3"
    ""
    "..."
    "........."
    "..................?!"
    call thirddream from _call_thirddream
    scene bg ruins with fade
    show shik1 at right with moveinright
    hik "Congrats! For getting every song right you've managed to finish 7th in today's Ranked Death Match!"
    hik "{s}Though half of those songs were namedrops anyway{/s}"
    j "So that means I've done it? I've beat everyone? I've saved my clan?"
    hik "lol no that was just todays game you have to come back here every day without fail for the next month and pray your connection never dies"
    hik "also only the top 3 get rewarded anyway soo"
    hik "but hey at least you're not dead"
    j "I'm starting to wish I... {cps=*0.5}was{/cps}{cps=*0.25}...{/cps}"
    scene black 
    $ renpy.pause(0.3, hard=True)
    scene bg ruins
    $ renpy.pause(0.3, hard=True)
    scene black with fade
    scene black 
    $ renpy.pause(0.3, hard=True)
    scene bg ruins
    $ renpy.pause(0.3, hard=True)
    scene black with fade
    scene black 
    $ renpy.pause(0.3, hard=True)
    scene bg ruins
    $ renpy.pause(0.3, hard=True)
    scene black
    play sound "audio/drop.mp3"
    ""
    centered "The ringing grows louder..."
    "..."
    "......."
    "..............?"
    scene bg movies with Fade(2.0, 0.0, 2.0)
    "Club Leader" "Alright minna-san, welcome to the biweekly Ouran High School Anime Society groupwatch!"
    "Club Leader" "Today we'll be watching, by popular demand, the latest episode (#1122) of Crayon Shin-chan!"
    play sound "audio/legalanime.mp3" volume 0.5
    "Club Member #1" "I've got my popcorn ready"
    "Club Member #2" "You gonna join us, Jin?"
    "Club Member #3" "We better start soon... Jin looks so bored he might just actually start watching Love Live unironically"
    j "You know of all the nightmares so far this is probably the scariest..."
    scene black
    centered "Oi...."
    centered "He's really out cold huh..."
    centered "I guess it can't be helped then..."
    scene bg bedroom 
    show noe3 at right
    show kom3 at left
    "..."
    noe "Oh, there you are!"
    kom "We thought you were a goner..."
    noe "I know I said to get some good rest but I didn't mean to sleep in till noon..."
    kom "And you were sweating and mumbling to yourself the whole time too... What happened?"
    "..."
    noe "Eh...?! Another nightmare?"
    kom "The spirit of the {b}SOLID GOLD HIBIKI{/b} must be getting stronger..."
    noe "This is bad... If this gets any worse... it's gonna... *gasp*"
    kom "No... it can't be..."
    noe "We have to save him..."
    noe "Before..."
    noe "{cps=*0.3}Before he becomes... an Inserts only player{/cps}"

    ## Rapid-Fire Sequence

    # Final Nightmare

    python:
        rhythm_game_scores_list = []
        for i in persistent.rhythm_game_high_scores.values():
            rhythm_game_scores_list.append(i[0])
        avg_rhythm_game_score = int(round((sum(rhythm_game_scores_list) / len(rhythm_game_scores_list) / 1000),0))
        gamepoints += avg_rhythm_game_score * 2
    ""
    scene black with fade
    centered "~ to be continued ~"
    centered "Thanks for playing till the end!"
    centered "Total XP: {b}[globalpoints]{/b}"
    return

label initgame(songdict, anslist, gamebg="bg ingame.jpg", randsong = False, fortniteloli=False):
    image gamebg = "[gamebg]"
    scene gamebg
    $ gamepoints = 0
    $ currentsong = 1
    $ numofsongs = len(songdict)
    while currentsong <= numofsongs:
        if randsong:
            $ randnum = renpy.random.randint(1000, 5000)
            narrator "Song [currentsong] of [randnum]"
        else:
            narrator "Song [currentsong] of [numofsongs]"
        if fortniteloli and currentsong == 8:
            scene bg playground distorted with Fade(5.0, 0.0, 5.0)
        $ songaudio = (list(songdict.items()))[currentsong-1][0]
        $ renpy.music.play("audio/" + songaudio + ".mp3")
        $ option1 = (list(songdict.items()))[currentsong-1][1][0]
        $ option2 = (list(songdict.items()))[currentsong-1][1][1]
        $ option3 = (list(songdict.items()))[currentsong-1][1][2]
        $ option4 = (list(songdict.items()))[currentsong-1][1][3]
        menu:
            "[option1]":
                $ savedans = option1
            "[option2]":
                $ savedans = option2
            "[option3]":
                $ savedans = option3
            "[option4]":
                $ savedans = option4
        if fortniteloli and currentsong > 7:
            $ remsongs = 10 - currentsong
            $ ansstr = anslist[currentsong-1]
            show mar1 at right with moveinright
            mar "Areee~? Looks like everyone has their weakness after all... And yours just happens to be [ansstr]~"
            if remsongs > 0:
                mar "Just [remsongs] more and it's my win! Fufufu"
                hide mar1 with moveoutright
            else:
                stop music fadeout 1.0
                mar "And with that~"
                scene black with fade
                play sound "audio/shing.mp3"
                mar "Sayounara nii-chan"
                return
        elif savedans == anslist[currentsong-1]:
            $ gamepoints += 10
            narrator "Correct! Current score: [gamepoints]"
        else:
            narrator "Nope... Current score: [gamepoints]"
        if fortniteloli and currentsong == 3:
            j "wtf why are they all new zoomer and kids shows"
            show mar3 at right with moveinright
            mar "the person who made this game is like 11"
            j "explains the dry ass humor"
            mar "haha baby shark go brrrrrrrr"
            hide mar3 with moveoutright
        $ currentsong += 1
    $ globalpoints += gamepoints
    stop music fadeout 1.0
    scene black with fade
    return

#{"game201":["Option 1", "Option 2", "Option 3", "Option 4"],
#"game202":["Option 1", "Option 2", "Option 3", "Option 4"],
#"game203":["Option 1", "Option 2", "Option 3", "Option 4"]}

#["Option 2", "Option 3", "Option 1"]

screen noddinput():
    window:
        vbox:
            text "Your answer:"
            input

screen cp_button():
    fixed:
        imagebutton idle "cp_button.png" focus_mask True xpos 1580 ypos 35 action Call("cp_button") hovered [Play("sound","audio/click.mp3")] alt "cp"

label initgamenodd(songdict, gamebg="bg ingame.jpg", randsong=False, indonesia=False, keion=False):
    image gamebg = "[gamebg]"
    scene gamebg
    $ gamepoints = 0
    $ currentsong = 1
    $ numofsongs = len(songdict)
    while currentsong <= numofsongs:
        if not randsong:
            narrator "Song [currentsong] of [numofsongs]"
        else:
            $ randnum = renpy.random.randint(1000, 5000)
            narrator "Song [currentsong] of [randnum]"
        $ songaudio = (list(songdict.items()))[currentsong-1][0]
        $ renpy.music.play("audio/" + songaudio + ".mp3")
        if indonesia:
            show indonesianamq with zoomin:
                xalign 0.5
                yalign 0.5
        call screen noddinput
        $ ans = _return.lower().strip()
        if ans in (list(songdict.items()))[currentsong-1][1]:
            $ gamepoints += 15
            narrator "Correct! Current score: [gamepoints]"
        else:
            narrator "Nope... Current score: [gamepoints]"
            $ allans = " / ".join((list(songdict.items()))[currentsong-1][1])
            narrator "Correct answer(s):\n[allans]"
        if indonesia:
            hide indonesianamq
        if keion and currentsong == 1:
            "You" "Wait... why did that song sound so weird...?"
            rit "Mm? We were just playing like we normally do, as part of the {b}Reverse Music Club{/b}"
            rit "We've still got 4 songs to go, so enjoy the show!"
        $ currentsong += 1
    $ globalpoints += gamepoints
    stop music fadeout 1.0
    scene black with fade
    return

# {"game201":["Ans1", "Ans2"],
# "game202":["Ans1"]}

label mizukibattle:
    scene bg shrineblur with fade
    narrator "--- Boss information ---\nName: Mizuki"
    narrator "Rules: 10 second time limit; 3 lives"
    narrator "Specialty: Quick-Time"
    show smiz at right with moveinright
    miz "Hope you're ready! I know I am~"
    $ gamepoints = 0
    $ currentsong = 1
    $ numofsongs = 10
    $ songdict = {
        "game501" : ["Flip Flappers", "Shokugeki no Souma: San no Sara", "Chuunibyou demo Koi ga Shitai! Ren", "Trinity Seven"],
        "game502" : ["Toaru Kagaku no Railgun S", "Owari no Seraph: Nagoya Kessen-hen", "Black Bullet", "Toaru Kagaku no Railgun T"],
        "game503" : ["Kekkaishi", "Kokkoku", "Kekkai Sensen", "Kakkou no Iinazuke"],
        "game504" : ["Magia Record: Mahou Shoujo Madoka☆Magica Gaiden", "Classroom☆Crisis", "Demi-chan wa Kataritai", "Denpa Kyoushi"],
        "game505" : ["Mahouka Koukou no Rettousei", "Back Arrow", "Genei wo Kakeru Taiyou", "Qualidea Code"],
        "game506" : ["Mewkledreamy", "Waccha PriMagi!", "Idol Time PriPara", "Kiratto Pri☆chan"],
        "game507" : ["Hanasaku Iroha", "Non Non Biyori Nonstop", "Bakuman.", "Sankarea"],
        "game508" : ["Senki Zesshou Symphogear G", "Senki Zesshou Symphogear GX", "Senki Zesshou Symphogear XV", "Senki Zesshou Symphogear AXZ"],
        "game509" : ["Yuusha-Oh GaoGaiGar", "Yuusha-Oh GaoGaiGar Final", "Yuusha-Oh GaoGaiGar Final Grand Glorious Gathering", "Gintama'"],
        "game510" : ["Tottoko Hamtarou", "Tottoko Hamtarou: Ham-Ham Paradi-chu! Hamtarou to Fushigi no Oni no Ehonto", "Tottoko Hamtarou: Ham-Ham Land Daibouken", "Tottoko Hamtarou Anime Dechu!"]
    }
    $ anslist = ["Chuunibyou demo Koi ga Shitai! Ren","Toaru Kagaku no Railgun T","Kokkoku","Magia Record: Mahou Shoujo Madoka☆Magica Gaiden","Qualidea Code","Waccha PriMagi!","Bakuman.","Senki Zesshou Symphogear GX","Yuusha-Oh GaoGaiGar","Tottoko Hamtarou Anime Dechu!"]
    $ dial = ["Not bad, but can you do 9 more?","","Be sure to take your time\nJust not too much time~","","You're doing better than I thought\nThe last guy didn't make it this far","","Looks like I'll have to get serious with you","Only hard songs from here on out","I've saved my special attack for last...","a"]
    $ lives = 3
    while currentsong <= numofsongs and lives > 0:
        $ ontime = True
        $ savedans = ""
        narrator "Song [currentsong] of [numofsongs]"
        $ songaudio = (list(songdict.items()))[currentsong-1][0]
        $ renpy.music.play("audio/" + songaudio + ".mp3")
        $ option1 = (list(songdict.items()))[currentsong-1][1][0]
        $ option2 = (list(songdict.items()))[currentsong-1][1][1]
        $ option3 = (list(songdict.items()))[currentsong-1][1][2]
        $ option4 = (list(songdict.items()))[currentsong-1][1][3]
        $ timeleft = 10
        $ timer_range = 10
        $ timer_jump = "outoftime"
        show screen countdown
        menu:
            "[option1]":
                $ savedans = option1
            "[option2]":
                $ savedans = option2
            "[option3]":
                $ savedans = option3
            "[option4]":
                $ savedans = option4
        hide screen countdown
        if not savedans:
            label outoftime:
                $ ontime = False
                $ lives -= 1
                narrator "Too slow... Current score: [gamepoints]\nLives: [lives]"
        if savedans == anslist[currentsong-1] and ontime:
            $ gamepoints += 10
            narrator "Correct! Current score: [gamepoints]\nLives: [lives]"
        elif ontime:
            $ lives -= 1
            narrator "Nope... Current score: [gamepoints]\nLives: [lives]"
        if dial[currentsong-1]:
            if currentsong >= 7:
                hide smiz
                show smizangry at right 
            $ currentdial = dial[currentsong-1]
            miz "[currentdial]"
        $ currentsong += 1
    if lives > 0:
        $ xpgain = int(round(gamepoints * (0.5+(0.5 * lives)),0))
        $ globalpoints += xpgain
        stop music fadeout 1.0
        scene black with fade
        return
    else:
        stop music fadeout 1.0
        miz "Oh! I almost didn't notice"
        miz "Looks like it's my win! Not like I had any doubts though~"
        miz "Now then..."
        scene bg dead with Fade(2.0, 0.0, 2.0)
        show smizangry at right
        $ renpy.pause(1.8, hard=True)
        miz "{cps=5}Goodbye{/cps}"
        $ MainMenu(confirm=False)()

label daytbattle:
    scene bg karaokedark with fade
    menu:
        "Please choose your difficulty"
        "Free (20 pts)":
            $ pointgoal = 20
            $ multiplier = 0.5
        "Easy (30 pts)":
            $ pointgoal = 30
            $ multiplier = 1.0
        "Medium (40 pts)":
            $ pointgoal = 40
            $ multiplier = 1.33
        "Hard (50 pts)":
            $ pointgoal = 50
            $ multiplier = 1.67
        "Expert (65 pts)":
            $ pointgoal = 65
            $ multiplier = 2.25
        "Lunatic (80 pts)":
            $ pointgoal = 80
            $ multiplier = 2.83
    narrator "--- Boss information ---\nName: Daytona"
    narrator "Rules: 20 second time limit; Quick-Draw Style"
    narrator "{size=-8}The faster you answer the more points you receive:{/size}{w}{size=-13}\nWithin 7 seconds - 7 pts\nWithin 10 seconds - 5 pts\nWithin 15 seconds - 3 pts\nWithin 20 seconds - 1 pt{/size}{w}\nRequired points: {b}[pointgoal] pts{/b}"
    narrator "Flex bonus: +2 pts for using the longest valid name\nStreak bonus: +1 pt per song in longest streak\nShortcut penalty: -5 pts for each deleted answer"
    narrator "Specialty: Title-Deletion\n{i}{size=-8}Shortened titles such as 'LasDan', 'EnStars', 'Genkoku', 'Yu-sibu', 'Haifuri', 'TsureKano' etc. are {b}not{/b} valid answers for this battle.{/size}{/i}"
    show dayt at left with moveinleft
    $ gamepoints = 0
    $ currentsong = 1
    $ numofsongs = 12
    $ currentstreak = 0
    $ streaks = [0]
    $ songdict = {
        "game601":["tensei shitara slime datta ken", "that time i got reincarnated as a slime"],
        "game602":["shigatsu wa kimi no uso", "your lie in april", "shigatsu wa kimi no uso: moments", "your lie in april: moments"],
        "game603":["sora yori mo tooi basho", "a place further than the universe"],
        "game604":["dungeon ni deai o motomeru no wa machigatteiru darou ka","is it wrong to try to pick up girls in a dungeon?"],
        "game605":["ore no imouto ga konnani kawaii wake ga nai","my little sister can't be this cute!"],
        "game606":["boku wa tomodachi ga sukunai"],
        "game607":["my teen romantic comedy snafu","yahari ore no seishun love come wa machigatteiru.","my teen romantic comedy snafu too!","yahari ore no seishun love come wa machigatteiru. zoku", "my teen romantic comedy snafu climax!","yahari ore no seishun love come wa machigatteiru. kan"],
        "game608":["my next life as a villainess: all routes lead to doom!","otome game no hametsu flag shika nai akuyaku reijou ni tensei shiteshimatta...","my next life as a villainess: all routes lead to doom! x","otome game no hametsu flag shika nai akuyaku reijou ni tensei shiteshimatta... x"],
        "game609":["ore no kanojo to osananajimi ga shuraba sugiru"],
        "game610":["shuumatsu nani shitemasu ka? isogashii desu ka? sukutte moratte ii desu ka?","worldend: what are you doing at the end of the world? are you busy? will you save us?"],
        "game611":["shimoneta to iu gainen ga sonzai shinai taikutsu na sekai","shimoneta: a boring world where the concept of dirty jokes doesn't exist"],
        "game612":["isekai wa smartphone to tomo ni.","in another world with my smartphone"],
        "game613":["watashi ga motenai no wa dou kangaete mo omaera ga warui!","no matter how i look at it, it's you guys' fault i'm not popular!"],
        "game614":["rikei ga koi ni ochita no de shoumei shitemita.","science fell in love, so i tried to prove it"],
        "game615":["watashi, nouryoku wa heikinchi de tte itta yo ne!","didn't i say to make my abilities average in the next life?!"],
        "game616":["uchi no ko no tame naraba, ore wa moshikashitara maou mo taoseru kamo shirenai.","if it's for my daughter, i'd even defeat a demon lord"],
        "game617":["saikin, imouto no yousu ga chotto okashiin da ga.","recently, my sister is unusual."],
        "game618":["uchi no maid ga uzasugiru!"],
        "game619":["ore no nounai sentakushi ga, gakuen love come o zenryoku de jama shiteiru","my mental choices are completely interfering with my school romantic comedy"],
        "game620":["jinrui wa suitai shimashita","humanity has declined"],
        "game621":["onii-chan dakedo ai sae areba kankei nai yo ne"],
        "game622":["rokudenashi majutsu koushi to akashic records","akashic records of bastard magical instructor"],
        "game623":["koi to yobu ni wa kimochi warui"],
        "game624":["tada-kun wa koi o shinai","tada never falls in love"],
        "game625":["ore ga suki nano wa imouto dakedo imouto ja nai", "my sister, my writer"]
    }
    # God my spaghetti code makes Ege's look pristine in comparison lul
    $ illegalans = {"game601":["tensura"],"game602":["kimiuso", "kimiuso: moments"],"game603":["yorimoi"],"game604":["danmachi"],"game605":["oreimo"],"game606":["haganai"],"game607":["oregairu", "oregairu zoku", "oregairu kan"],"game608":["hamefura", "hamefura x"],"game609":["oreshura"],"game610":["sukasuka"],"game611":["shimoseka"],"game612":["isesuma"],"game613":["watamote"],"game614":["rikekoi"],"game615":["noukin"],"game616":["uchinoko"],"game617":["imocho."],"game618":["uzamaid!"],"game619":["noucome"],"game620":["jintai"],"game621":["oniai"],"game622":["rokuaka"],"game623":["koikimo"],"game624":["tadakoi"],"game625":["imoimo"]}
    $ dial = ["I've got a toothbrush with your name on it","I deleted it (yaoi!!! on ice) and ege made me readd it","the last time i played amq was in january i think", "(real Dayt quote) did you know that Hitler was an animal lover and was actually a huge advocate for more laws protecting animals", "wtf a furry that looks decent", "Yes the idol jihen fan base is so trash", "thats why i back catbox adn not amq amq is trash catbox is god","time to ban jax for playing osu","if youre getting anythign right in 5 sec youre cheating anyway jsut not with shazam", "saro wtf", "oh my god these titles are giving me cancer","the reason quickdraw is so unplayed is because it legimitaly is a typing test"]
    while len(songdict) > numofsongs:
        $ popped = renpy.random.randint(1, len(songdict))
        $ poppedkey = list(songdict.keys())[popped-1]
        $ songdict.pop(poppedkey)
        $ songtup = list(songdict.items())
        $ renpy.random.shuffle(songtup)
        $ songdict = dict(songtup)
    while currentsong <= numofsongs:
        $ i = 0
        $ flexans = []
        $ longestlen = 0
        $ currentques = (list(songdict.items()))[currentsong-1][0]
        $ currentans = (list(songdict.items()))[currentsong-1][1]
        $ currentillegal = illegalans[currentques]
        while i < len(currentans):
            if len(currentans[i]) > longestlen:
                $ flexans = [currentans[i]]
                $ longestlen = len(currentans[i])
            elif len(currentans[i]) == longestlen:
                $ flexans.append(currentans[i])
            $ i += 1
        narrator "Song [currentsong] of [numofsongs]"
        $ timeleft = 20
        $ timer_range = 20
        show screen countdown2
        $ starttime = gettime.time()
        $ renpy.music.play("audio/" + currentques + ".mp3")
        call screen noddinput
        $ ans = _return.lower().strip()
        $ endtime = gettime.time()
        hide screen countdown2
        $ timedif = endtime - starttime
        $ timedifrnd = round(timedif, 2)
        $ timepoints = 7 if timedif <= 7 else 5 if timedif <= 10 else 3 if timedif <= 15 else 1 if timedif <= 20 else 0
        if currentques == "game606" and _return.strip() == "hagAnaI":
            dayt "heh nice, still wrong tho"
        if ans in currentillegal:
            $ gamepoints -= 5
            $ streaks.append(currentstreak)
            $ currentstreak = 0
            dayt "Looks like you entered in an answer I Thanos snapped, better luck next time"
            narrator "{size=-5}Answer score: 0 ([timedifrnd]s)\nFlex bonus: 0\nPenalty: -5{b}\nCurrent score: [gamepoints] points{/b} (Streak: 0){/size}"
        elif ans in currentans:
            $ currentstreak += 1
            narrator "Correct answer!"
            $ gamepoints += timepoints
            if ans in flexans:
                $ gamepoints += 2
                narrator "{size=-5}Answer score: [timepoints] ([timedifrnd]s)\nFlex bonus: 2\nPenalty: 0{b}\nCurrent score: [gamepoints] points{/b} (Streak: [currentstreak]){/size}"
            else:
                narrator "{size=-5}Answer score: [timepoints] ([timedifrnd]s)\nFlex bonus: 0\nPenalty: 0{b}\nCurrent score: [gamepoints] points{/b} (Streak: [currentstreak]){/size}"
        else:
            narrator "Nope... That ain't right..."
            $ streaks.append(currentstreak)
            $ currentstreak = 0
            $ allans = " / ".join(currentans)
            narrator "Correct answer(s):\n{size=-8}[allans]{/size}"
            narrator "{size=-5}Answer score: 0 ([timedifrnd]s)\nFlex bonus: 0\nPenalty: 0{b}\nCurrent score: [gamepoints] points{/b} (Streak: 0){/size}"
        if dial[currentsong-1]:
            $ currentdial = dial[currentsong-1]
            dayt "[currentdial]"
        $ currentsong += 1
    stop music fadeout 1.0
    $ streaks.append(currentstreak)
    $ highstreak = max(streaks)
    $ totalpoints = gamepoints + highstreak
    narrator "Game points: [gamepoints]\nHighest streak: [highstreak]\n{b}Total points: [totalpoints] points{/b}"
    if totalpoints >= pointgoal:
        $ weightedpoints = totalpoints * multiplier
        $ xpgain = int(round(weightedpoints,0))
        $ globalpoints += xpgain
        narrator "You win!"
        dayt "wtf bet you copy pasted half of those anyway"
        hide dayt with moveoutleft
        show shi2 with moveinright
        shi "Yayy~ Now I'll never have to read the pins ever again thanks to you!!"
    else:
        dayt "Well, well, well, looks like you couldn't handle it after all"
        dayt "Say goodbye to Shiina, and yourself."
        $ MainMenu(confirm=False)()
    scene black with fade
    return

label gameshow:
    $ prizes = [0, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]
    $ prizelevel = 0
    $ currentquestion = 1
    $ numofquestions = 10
    $ questions = {
        "How many song segments were played?":["12", "14", "16", "18"],
        "Which anime's opening was played as a start sample?":["Usagi Drop", "Amagi Brilliant Park", "Little Witch Academia", "Stella no Mahou"],
        "What anime's opening was the 5th song that was played?":["Umineko no Naku Koro ni", "91 Days", "pet", "Scan2Go"],
        "Which of the following anime did NOT have its opening play?":["Shadows House", "Fate/kaleid liner Prisma☆Illya 2wei!", "Ano Hi Mita Hana no Namae o Boku-tachi wa Mada Shiranai.", "Hakata Tonkotsu Ramens"],
        "Which anime's opening had the longest played sample?":["Amagi Brilliant Park", "Little Busters!", "Macross Dynamite 7", "Little Busters! EX"],
        "Which artist performed more than one song that was played?":["Minami Kuribayashi", "TRUE", "Kishida Kyoudan &THE Akeboshi Rockets", "TK from Ling Tosite Sigure"],
        "In which position did the non-Japanese song play?":["6th","8th","9th","11th"],
        "In which position did the instrumental song play?":["12th", "13th", "14th", "15th"],
        "How many anime played have a number in the title?":["1", "2", "3", "4"],
        "The opening to which anime played twice?":["Hakata Tonkotsu Ramens","Kikou Shoujo wa Kizutsukanai","Ghost Hunt","The World of GOLDEN EGGS"],
    }
    $ answers = ["C","B","A","A","D","C","C","C","D","B"]
    narrator "..."
    narrator "......"
    narrator ".........?"
    play music "audio/bgm04.mp3" fadein 1.0 fadeout 1.0 volume 0.2
    $ renpy.notify('Now playing: Buzzer Beater')
    scene bg gameshow with fade
    show gsyuk at left with moveinleft
    gsyuk "And here we have our next contestant on... {b}Who Wants to Be An AMQ Booli?{/b}"
    j "W-where am I...?"
    gsyuk "The rules are simple! You listen to the copyrighted music, you answer some lazily-written questions! Get them all right and the million's yours!"
    gsyuk "That's before taxes of course, tehe~"
    gsyuk "Our special guest here has clocked in over 6300 hours on AMQ since December of 2017, and has a promising guess rate of 31.52\%"
    gsyuk "Let's see if they've got what it takes to become the world's next certified AMQ booli!"
    j "Ayo that's a lotta money I could win... That's like 2 whole ten-pulls in Genshin..."
    gsyuk "Now... shush, shush."
    stop music
    gsyuk "You're about to hear a 96-second audio clip full of bits and pieces of AMQ songs! Now pay attention, cus it's not gonna play a second time!"
    gsyuk "Take down some notes, cram it all in your head, do whatever! Just be prepared for the 11 questions afterwards~"
    gsyuk "Good luck!!"
    hide gsyuk with moveoutleft
    window hide
    play sound "audio/gameshow.mp3" fadein 1.0 fadeout 1.0
    $ timeleft = 96
    $ timer_range = 96
    show screen countdown2
    $ renpy.pause(96, hard=True)
    hide screen countdown2
    stop sound fadeout 1.0
    show gsyuk at right with moveinright
    gsyuk "Ready? Let's get this cursed show on the road~"
    play music "audio/bgm05.mp3" fadein 1.0 fadeout 1.0 volume 0.2
    $ renpy.notify('Now playing: Nana Maru San Batsu')
    while currentquestion <= numofquestions:
        $ questiontext = list(questions.keys())[currentquestion-1]
        $ option1 = list(questions.values())[currentquestion-1][0]
        $ option2 = list(questions.values())[currentquestion-1][1]
        $ option3 = list(questions.values())[currentquestion-1][2]
        $ option4 = list(questions.values())[currentquestion-1][3]
        $ correctanswer = answers[currentquestion-1]
        narrator "Question [currentquestion] of 11"
        menu:
            "[questiontext]"
            "[option1]":
                $ selectedans = "A"
            "[option2]":
                $ selectedans = "B"
            "[option3]":
                $ selectedans = "C"
            "[option4]":
                $ selectedans = "D"
        if selectedans == correctanswer:
            gsyuk "Your answer is{cps=*0.5}.....{/cps} CORRECT!"
            $ prizelevel += 1
        else:
            gsyuk "Your answer is{cps=*0.5}.....{/cps} incorrect..."
            gsyuk "Let's keep going though~ You've still got big money to win!"
        $ currentprize = prizes[prizelevel]
        gsyuk "Current earnings: {b}[currentprize] notes{/b}"
        $ currentquestion += 1
    gsyuk "...And now for the final question"
    stop music fadeout 1.0
    gsyuk "Get ready, this is the biggest one yet!"
    menu:
        "What do you think of Yukari?"
        "I love Yukari!!!!":
            gsyuk "Wha-!!"
        "I only ever use Yukari skins, the rest are trash":
            gsyuk "Now that I can agree with"
        "Every day I wake up and bow down to my shrine of Yukari merch consisting of 30 copies of the same silhouette shirt made from pre-shrunk 100\% Cotton and available for only $28.12 before shipping":
            gsyuk "Ok this is... mildly concerning... but..."
        "Ew furry avatar":
            gsyuk "..."
            scene black
            gsyuk "Get out of my game show"
            centered "DrNyanpasu Ending"
            show drnyanpasu at truecenter with fade
            ""
            $ MainMenu(confirm=False)()
    $ prizelevel += 1
    $ currentprize = prizes[prizelevel]
    $ xpgain = prizelevel * 10
    $ globalpoints += xpgain
    gsyuk "I-I'm glad you think so, of course I was just asking this for a friend nya-"
    gsyuk "Ahem"
    gsyuk "Your answer is{cps=*0.5}.....{/cps} CORRECT!"
    gsyuk "Congratulations! You are now officially the world's next certified AMQ BOOLI and {b}[currentprize] notes{/b} richer!!"
    gsyuk "{cps=*0.5}Richer!! ... {/cps}{cps=*0.25} richer ...{/cps}{cps=*0.125} r i c h e r . . . . .{/cps}"
    scene black with Fade(2.0, 0.0, 2.0)
    return

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

label badteammate:
    $ gamepoints = 0
    $ currentsong = 1
    $ numofsongs = 10
    $ songlist = [
        ("game901","bt01.png", "Y"),
        ("game902","bt02.png", "Y"),
        ("game903","bt03.png", "N"),
        ("game904","bt04.png", "Y"),
        ("game905","bt05.png", "N"),
        ("game906","bt06.png", "N"),
        ("game907","bt07.png", "N"),
        ("game908","bt08.png", "Y"),
        ("game909","bt09.png", "N"),
        ("game910","bt10.png", "Y"),
        ("game911","bt11.png", "Y"),
        ("game912","bt12.png", "Y"),
        ("game913","bt13.png", "Y"),
        ("game914","bt14.png", "N"),
        ("game915","bt15.png", "Y"),
        ("game916","bt16.png", "N")
    ]
    $ correctdial = ["how tf did you know that","bro quit sweating so hard","how much anime have you seen tf","go touch grass"]
    $ wrongdial = ["even i knew that","tf my teammates trolling","*starts reciting the entire wikipedia list of ethnic slurs*","can we kick this guy wtf who even are they"]
    while len(songlist) > numofsongs:
        $ songlist.pop(renpy.random.randint(1, len(songlist))-1)
        $ renpy.random.shuffle(songlist)
    scene bg main with fade
    gm "Welcome to Bad Teammate! Powered by Shinomiya Group"
    gm "Once upon a time, you accidentally joined a team lobby full of single-digit level Hibiks!"
    gm "Ignoring the shocking fact they didn't kick you out and call you racial slurs within a nanosecond of you clicking Ready..."
    gm "They don't know anything!"
    gm "Help determine if your teammate's answer is correct in the short short time you have to think..."
    gm "Be quick! You need to act fast to let it slide or invalidate their answers to save you from complete embarrassment!"
    gm "{size=-8}(Becuase you've already tied up an unhealthy chunk of your self-worth into this meaningless memory and typing game){/size}"
    gm "Good luck out there! Let's play~"
    "Game settings: Song plays for 5 seconds, you have 5 seconds after that to respond with Yes or No"
    scene bg ingame with Fade(2.0, 0.0, 2.0)
    while currentsong <= numofsongs:
        narrator "Song [currentsong] of [numofsongs]"
        window hide
        $ timeleft = 5
        $ timer_range = 5
        $ timer_jump = "btans"
        $ songaudio = songlist[currentsong-1][0]
        $ renpy.music.play("audio/" + songaudio + ".mp3")
        show screen countdown
        $ renpy.pause(5.0, hard=True)
        label btans:
            $ timeleft = 5
            $ timer_range = 5
            $ timer_jump = "btoutoftime"
            show screen countdown
            $ teamans = songlist[currentsong-1][1]
            image teamans = "[teamans]"
            show teamans:
                xalign 0.5
                yalign 0.6
                xzoom 2.0 
                yzoom 2.0
            menu:
                "Accept your teammate's answer?"
                "Yes":
                    hide screen countdown
                    hide teamans
                    $ bt_currentans = "Y"
                "No":
                    hide screen countdown
                    hide teamans
                    $ bt_currentans = "N"
            if bt_currentans == songlist[currentsong-1][2]:
                $ randdial = renpy.random.choice(correctdial)
                $ gamepoints += 10
                "Good job! Current score: {b}[gamepoints] points{/b} (+10)"
                "Guest-56941" "[randdial]"
            else:
                $ randdial = renpy.random.choice(wrongdial)
                $ gamepoints -= 10
                "Mmmm no... Current score: {b}[gamepoints] points{/b} (-10)"
                "Guest-56941" "[randdial]"
            hide teamans
        if False:
            label btoutoftime:
                hide teamans
                $ gamepoints -= 5
                "Rip too slow... Current score: {b}[gamepoints] points{/b} (-5)"
        $ currentsong += 1
    stop music fadeout 1.0
    scene bg main with fade
    gm "Game complete! Total score: {b}[gamepoints] points{/b}"
    show bt_kick at truecenter with zoomin
    gm "Thank you for playing Bad Teammate!"
    $ globalpoints += gamepoints
    scene black with fade
    return
    
label indonesianamq:
    scene bg main with fade
    gm "Welcome to Indonesian AMQ Simulator!"
    gm "A brand-new state-of-the-art game that lets you experience what it's like to play AMQ in Indonesia!"
    gm "Heralded as absolutely accurate by many of our loyal players, we hope you'll enjoy it too!"
    gm "Let's begin shall we~"
    scene bg ingame with fade
    window hide
    call initgamenodd({
        "indonesianamq1":["hai akko desu"],
        "indonesianamq2":["shin chou bakumatsu shounen seiki takamaru","chou bakumatsu shounen seiki takamaru"],
        "indonesianamq3":["seito shokun!"],
        "indonesianamq4":["onegai! samia don","please! psammea-don","the psammead"],
        "indonesianamq5":["tama & friends: sagase! mahou no punipuni stone"],
        "indonesianamq6":["time patrol bon"],
        "indonesianamq7":["hanasaka tenshi tenten-kun"],
        "indonesianamq8":["chinzei hachirou tametomo"],
        "indonesianamq9":["superbook","anime oyako gekijou"],
        "indonesianamq10":["one punch man"]
    }, indonesia=True) from _call_initgamenodd_4
    "Total points: {b}[gamepoints] pts{/b}"
    if gamepoints > 0:
        gm "So, how many playthroughs have you done? Two? Three? Seventeen?"
        gm "Maybe you should try the other minigames, they're actually playable somewhat..."
    else:
        gm "Wowww, look at all those solo points you missed, tough luck"
    gm "Thanks for playing Indonesian AMQ Simulator! We hope you enjoyed it~"
    scene black with fade
    return

label ritsubattle:
    scene bg arcade with fade
    menu:
        "Please choose your difficulty"
        "Litterbox (5 lives, long sample)":
            $ lives = 5
            $ sample = 1.5
            $ totalsample = 5
            $ multiplier = 0.5
        "Easy (3 lives, long sample)":
            $ lives = 3
            $ sample = 1.5
            $ totalsample = 5
            $ multiplier = 1.0
        "Medium (3 lives, normal sample)":
            $ lives = 3
            $ sample = 1
            $ totalsample = 4
            $ multiplier = 1.5
        "Hard (2 lives, normal sample)":
            $ lives = 2
            $ sample = 1
            $ totalsample = 4
            $ multiplier = 1.75
        "Impossible (2 lives, short sample)":
            $ lives = 2
            $ sample = 0.5
            $ totalsample = 3
            $ multiplier = 2.25
        "Inazuma Eleven (1 life, short sample)":
            $ lives = 1
            $ sample = 0.5
            $ totalsample = 3
            $ multiplier = 2.5
    $ guesstime = totalsample - sample
    narrator "--- Boss information ---\nName: Ritsu"
    narrator "Rules: [sample]s sample, [guesstime]s guessing time"
    narrator "Specialty: ?????"
    show rit2 at right with moveinright
    rit "Let's see how long you last Buni"
    $ gamepoints = 0
    $ currentsong = 1
    $ numofsongs = 20
    $ songdict = {
        "game1001":["Michiko to Hatchin","Great Pretender","Baccano!","Hakumei to Mikochi"],
        "game1002":["Maou-jou de Oyasumi","Gochuumon wa Usagi Desu ka?","Tsurezure Children","Genjitsu Shugi Yuusha no Oukoku Saikenki"],
        "game1003":["Sakura Trick","B Gata H Kei","Kiss × Sis","Amaama to Inazuma"],
        "game1004":["Momokuri","Acchi Kocchi","Last Period: Owarinaki Rasen no Monogatari","Mikakunin de Shinkoukei"],
        "game1005":["Deatte 5-byou de Battle","Jibaku Shounen Hanako-kun","Mahou Shoujo Tokushusen Asuka","Inou-Battle wa Nichijou-kei no Naka de"],
        "game1006":["Minami-ke: Tadaima","Mahou Sensei Negima!","Strike Witches","Love Lab"],
        "game1007":["Beastars","JoJo no Kimyou na Bouken","Megalobox","One Piece Film: Gold"],
        "game1008":["Itai no wa Iya nano de Bougyoryoku ni Kyokufuri Shitai to Omoimasu.","Kuma Kuma Kuma Bear","Mayo Chiki!","Ore, Twintail ni Narimasu."],
        "game1009":["Kingdom","3D Kanojo Real Girl","Black Clover","Fairy Tail: Final Season"],
        "game1010":["Peter Grill to Kenja no Jikan","Musaigen no Phantom World","Kaijin Kaihatsu-bu no Kuroitsu-san","Mairimashita! Iruma-kun"],
        "game1011":["Machikado Mazoku 2-choume","Tamako Market","Hibike! Euphonium","Girls und Panzer"],
        "game1012":["Hamatora","Hamtaro","Re:␣Hamatora","Devil Survivor 2 The Animation"],
        "game1013":[".hack//Intermezzo","xxxHOLiC","Koukaku Kidoutai","Aoi Bungaku Series"],
        "game1014":["Gangsta.","Dimension W","Gantz","Super Crooks"],
        "game1015":["Full Metal Panic? Fumoffu","Kino no Tabi: The Beautiful World","Ookami to Koushinryou II","Mushoku Tensei: Isekai Ittara Honki Dasu"],
        "game1016":["Fate/Grand Order: Zettai Majuu Sensen Babylonia","Kekkai Sensen & Beyond","Yozakura Quartet: Hana no Uta","Kaze ga Tsuyoku Fuiteiru"],
        "game1017":["Free!: Take Your Marks","A3! Season Spring & Summer","TsukiPro the Animation","The iDOLM@STER SideM"],
        "game1018":["Dororo","Durarara!!","Dorohedoro","Ninja Hattori-kun"],
        "game1019":["Boku-tachi no Remake","BanG Dream! 2nd Season","Bermuda Triangle: Colorful Pastrale","Cardfight!! Vanguard"],
        "game1020":["Osananajimi ga Zettai ni Makenai Love Come","Boku-tachi wa Benkyou ga Dekinai!","Midara na Ao-chan wa Benkyou ga Dekinai","Jaku-Chara Tomozaki-kun"],
        "game1021":["Ore dake Haireru Kakushi Dungeon: Kossori Kitaete Sekai Saikyou","Sono Bisque Doll wa Koi o Suru","Okaa-san Online","Gundam Build Divers Re:RISE"],
        "game1022":["Hanayamata","Ochikobore Fruit Tart","Futsuu no Joshikousei ga Locodol Yattemita OVA","Senryuu Shoujo"],
        "game1023":["Hidamari Sketch × Honeycomb","Kono Bijutsu-bu ni wa Mondai ga Aru!","GA: Geijutsuka Art Design Class","Sketchbook: Full Color's"],
        "game1024":["Koisuru Asteroid","Honzuki no Gekokujou: Shisho ni Naru Tame ni wa Shudan o Erandeiraremasen","Tsuki ga Kirei","Chain Chronicle: Haecceitas no Hikari"],
        "game1025":["Long Riders!","To LOVE-Ru Darkness 2nd","Wakaba*Girl","Ao no Kanata no Four Rhythm"],
        "game1026":["Saki Zenkoku-hen","Date A Live IV","Dakara Boku wa, H ga Dekinai.","Maken-Ki! Two"],
        "game1027":["To LOVE-Ru","Okusama ga Seitokaichou!+!","Seitokai Yakuindomo*","Choujigen Game Neptune The Animation"],
        "game1028":["Bishounen Tanteidan","Kimi no Suizou o Tabetai","Wotaku ni Koi wa Muzukashii","Mix: Meisei Story"],
        "game1029":["Hidan no Aria AA","Btooom!","Aoki Hagane no Arpeggio: Ars Nova","Conception"],
        "game1030":["Sentouin, Hakenshimasu!","Ueno-san wa Bukiyou","Plunderer","Busou Shoujo Machiavellism"],
        "game1031":["Masamune-kun no Revenge","Hajimete no Gal","Oshiete! Galko-chan","Boku no Kanojo ga Majime Sugiru Shobitch na Ken"],
        "game1032":["Ousama Game The Animation","Rainbow: Nisha Rokubou no Shichinin","Enen no Shouboutai","EVIL OR LIVE"],
        "game1033":["Daiya no Ace: Second Season","Prince of Stride: Alternative","Hand Shakers","Ple Ple Pleiades: Clementine Toubou-hen"],
        "game1034":["Hitorijime My Hero","Grand Blue Dreaming","Sasaki to Miyano","Udon no Kuni no Kin-iro Kemari"],
        "game1035":["Sakamichi no Apollon","Hachimitsu to Clover","3-gatsu no Lion","Dance Dance Danseur"],
        "game1036":["Senyoku no Sigrdrifa","Happy Sugar Life","Fuuka","Shichisei no Subaru"],
        "game1037":["Working'!!","Servant × Service","Ore o Suki nano wa Omae Dake ka yo","Sore ga Seiyuu!"],
        "game1038":["Peach Boy Riverside","Shinka no Mi: Shiranai Uchi ni Kachigumi Jinsei","Darker than Black: Ryuusei no Gemini","Vivy: Fluorite Eye's Song"],
        "game1039":["Shoujo☆Kageki Revue Starlight: Rondo Rondo Rondo","Lapis Re:LiGHTs","Princess Connect! Re:Dive Season 2","Oshi ga Budoukan Ittekuretara Shinu"],
        "game1040":["Choujin Koukousei-tachi wa Isekai demo Yoyuu de Ikinuku Youdesu!","Kenja no Mago","Tejina Senpai","Uzaki-chan wa Asobitai!"],
        "game1041":["Leadale no Daichi nite","Saihate no Paladin","Zero kara Hajimeru Mahou no Sho","Kenja no Deshi o Nanoru Kenja"],
        "game1042":["Yokohama Kaidashi Kikou","Shingetsutan Tsukihime","Tsukuyomi: Moon Phase","Abenobashi Mahou☆Shoutengai"],
        "game1043":["Date A Bullet","Hajime no Ippo","Zombie-Loan","The Big O"],
        "game1044":["Harukana Receive","Kami Nomi zo Shiru Sekai: 4-nin to Idol","Magical Star Kanon 100%","Kannagi"],
        "game1045":["Mashiro no Oto","Tsurune: Kazemai Koukou Kyuudou-bu","Dokyuu Hentai HxEros","Dr. Stone Special Episode: Ryusui"],
        "game1046":["Death March kara Hajimaru Isekai Kyousoukyoku","Arifureta Shokugyou de Sekai Saikyou","Assassins Pride","Girly Air Force"]
    }
    $ dial = ["Faster~","","","*insert gamer girl dialogue here, idk does it look like i have a discord gf or smth","","This is... definitely one of the moments of all time","um ackshualy its op 42 of meitantei conan :nerd_emoji:","","","imagine getting a gaming setup and using it to play amq all day, just sell that gpu already","youre welcome for all that shitty audio compression btw","","komugi asked me to leave her discordhere go add her Komugi#9780","","my favorite ranked meme is when catbox fucking dies","","you look like the kind of person to always, without fail, submit alfa-x for evangelion","yearly reminder to clean your room","...",""]
    while len(songdict) > numofsongs:
        $ popped = renpy.random.randint(1, len(songdict))
        $ poppedkey = list(songdict.keys())[popped-1]
        $ songdict.pop(poppedkey)
        $ songtup = list(songdict.items())
        $ renpy.random.shuffle(songtup)
        $ songdict = dict(songtup)
    while currentsong <= numofsongs and lives > 0:
        python:
            ontime = True
            savedans = ""
            optionslist = (list(songdict.items()))[currentsong-1][1]
            currentans = optionslist[0]
            renpy.random.shuffle(optionslist)
            option1 = optionslist[0]
            option2 = optionslist[1]
            option3 = optionslist[2]
            option4 = optionslist[3]
            songaudio = (list(songdict.items()))[currentsong-1][0]
            timeleft = totalsample
            timer_range = totalsample
            timer_jump = "outoftime_ritsu"
        narrator "Song [currentsong] of [numofsongs]"
        $ renpy.sound.play("audio/" + songaudio + ".mp3")
        show screen countdown
        $ renpy.pause(sample, hard=True)
        $ renpy.music.set_pause(True, channel="sound")
        menu:
            "[option1]":
                $ savedans = option1
            "[option2]":
                $ savedans = option2
            "[option3]":
                $ savedans = option3
            "[option4]":
                $ savedans = option4
        hide screen countdown
        $ renpy.music.set_pause(False, channel="sound")
        if not savedans:
            label outoftime_ritsu:
                $ renpy.music.set_pause(False, channel="sound")
                $ ontime = False    
                $ lives -= 1
                rit "Heh... Too bad. Get better ears kid"
                narrator "Current score: [gamepoints]\nLives: [lives]"
        if savedans == currentans and ontime:
            $ gamepoints += 15
            narrator "Correct! Current score: [gamepoints]\nLives: [lives]"
        elif ontime:
            $ lives -= 1
            narrator "Nope... Current score: [gamepoints]\nLives: [lives]"
        if dial[currentsong-1]:
            $ currentdial = dial[currentsong-1]
            rit "[currentdial]"
        $ currentsong += 1
    stop sound fadeout 1.0
    if lives == 0:
        label death_ritsu:
            stop sound fadeout 1.0
            rit "Well, well, well..."
            rit "Time to banish you from the arcade after all."
            rit "/kill JinAxel"
            $ MainMenu(confirm=False)()
    else:
        hide rit2
        show rit6 at right
        rit "..."
        rit "......"
        rit "..............."
        rit "I hope you didn't think that's all I had in me."
        play music "audio/bgm08.mp3" fadeout 1.0 fadein 1.0 volume 0.2
        $ renpy.notify('Now playing: Boku no Hero Academia (OST)')
        rit "*friendship speech*"
        hide rit6
        show rit7 at right
        rit "It's not over yet."
        show anoe1 at left with moveinleft
        noe "Quick! Take this!"
        show muscle at truecenter with moveinleft
        hide anoe1 with moveoutleft
        "Item {b}:muscle:{/b} acquired!"
        "Effect: +1 life"
        $ lives += 1
        hide muscle with dissolve
        rit "It's time for round 2 baby."
        narrator "--- Boss information ---\nName: Ritsu"
        narrator "Specialty: Second-Form"
        stop music fadeout 1.0
        $ numofsongs = 25
        $ songdict = {
            "game1101":["wonder egg priority"],
            "game1102":["made in abyss","made in abyss recaps"],
            "game1103":["guilty crown"],
            "game1104":["goblin slayer"],
            "game1105":["date a live ii"],
        }
        $ songtup = list(songdict.items())
        $ renpy.random.shuffle(songtup)
        $ songdict = dict(songtup)
        while currentsong <= numofsongs and lives > 0:
            narrator "Song [currentsong] of [numofsongs]"
            $ songaudio = (list(songdict.items()))[currentsong-21][0]
            $ currentans = (list(songdict.items()))[currentsong-21][1]
            $ renpy.sound.play("audio/" + songaudio + ".mp3")
            $ renpy.pause(sample, hard=True)
            $ renpy.music.set_pause(True, channel="sound")
            window hide
            call screen noddinput
            $ renpy.music.set_pause(False, channel="sound")
            $ ans = _return.lower().strip()
            if ans in currentans:
                $ gamepoints += 20
                narrator "Correct! Current score: [gamepoints]\nLives: [lives]"
            else:
                $ lives -= 1
                narrator "Nope... Current score: [gamepoints]\nLives: [lives]"
                $ allans = " / ".join(currentans)
                narrator "Correct answer(s):\n{size=-8}[allans]{/size}"
            $ currentsong += 1
        stop sound fadeout 1.0
        if lives == 0:
            jump death_ritsu
        else:
            hide rit7
            show rit8 at right
            rit "Wait, what?"
            $ weightedpoints = gamepoints * multiplier
            $ globalpoints += int(round(weightedpoints,0))
            scene black with fade
            return

label thirddream:
    $ isdead = False
    centered "Year: 24XX"
    centered "Amidst the chaos and calamity of the Great Warring Epoch, warriors clash in the centre of what once was the Advanced Technological State"
    centered "Someone please help me I'm running out of AMQ lore to plagiarise"
    scene bg ruins with fade
    play music "audio/bgm12.mp3" volume 0.15 fadein 1.0 fadeout 1.0
    $ renpy.notify('Now playing: Hataage! Kemono Michi')
    "???" "And now... our next contender in the arena!!"
    show shik1 at right with moveinright
    hik "You're new to this whole thing right? Lemme tell you how everything works..."
    j "Have I been... isekai'd...?"
    hik "No, worse..."
    j "SO YOU'RE TELLING ME EVERYONE HERE'S A NANA MIZUKI FAN?!"
    hik "Ok maybe not {i}that{/i} bad... You're just in a fight to the death battle to save your clan from being wiped out entirely"
    j "Oh, so just another Tuesday, got it"
    hik "You only have one life though... Make a single mistake and it's game over for you, you got that?"
    j "Sure sure, I got this, how hard can it be?"
    hik "Looks like we're all good here then, lemme get your opponents in"
    hik "Shuuka! watashiii! Rukawa!!"
    stop music fadeout 1.0
    hide shik1 with moveoutright
    if False:
        label dream_death:
            stop music fadeout 1.0
            hide screen cp_button
            scene bg ruins with fade
            show shik1 at right with moveinright
            hik "Welp... Looks like you didn't have what it takes after all..."
            hik "You missed a free and now you're out of Box 1"
            hik "No amount of Shazamming can help you now... Goodbye."
            scene dreamdeathscreen with Fade(2.0, 0.0, 2.0)
            ""
            "...."
            "I have seen the other side... It can wait."
            scene bg ruins with fade
            $ isdead = True
    if isdead:
        "--- Death Match Begin Again ---"
    else:
        "--- Death Match Begin ---"
    $ gamepoints = 0
    $ currentsong = 1
    $ numofsongs = 12
    $ songdict = {
        "game1601":["animal 1"],
        "game1602":["space runaway ideon","densetsu kyojin ideon"],
        "game1603":["big x"],
        "game1604":["jetter mars"],
        "game1605":["aggretsuko: we wish you a metal christmas","aggressive retsuko: we wish you a metal christmas"],
        "game1606":["oh! super milk-chan", "the super milk chan show"],
        "game1607":["thermae romae novae"],
        "game1608":["uchuu senkan yamato","star blazers","uchuu senkan yamato 2","star blazers: the bolar wars","uchuu senkan yamato 3","star blazers: space battleship yamato 2199","uchuu senkan yamato 2199","space battleship yamato 2199: voyage of remembrance","uchuu senkan yamato 2199: tsuioku no koukai","space battleship yamato","space cruiser: guardian of the galaxy","star blazers: the quest for iscandar","uchuu senkan yamato 2205: aratanaru tabidachi"],
        "game1609":["wish"],
        "game1610":["winter sonata","fuyu no sonata"],
        "game1611":["iron man"],
        "game1612":["47 todoufuken r"],
        "game1613":["knights of sidonia: battle for planet nine", "sidonia no kishi: dai-kyuu wakusei seneki"],
        "game1614":["super dimension century orguss", "choujikuu seiki orguss"],
        "game1615":["skyers 5"],
        "game1616":["tetsujin 28-go", "gigantor"],
        "game1617":["soccer fever"],
        "game1618":["kenzen robo daimidaler","daimidaler the sound robot","daimidaler: prince vs. penguin empire"],
        "game1619":["chirin no suzu","ringing bell"],
        "game1620":["keroro"],
        "game1621":["the story of young hanada","hanada shounen-shi"],
        "game1622":["himitsu no akko-chan"],
        "game1623":["kemono to chat"]
    }
    while len(songdict) > numofsongs:
        $ popped = renpy.random.randint(1, len(songdict))
        $ poppedkey = list(songdict.keys())[popped-1]
        $ songdict.pop(poppedkey)
    $ songtup = list(songdict.items())
    $ renpy.random.shuffle(songtup)
    $ songdict = dict(songtup)
    while currentsong <= numofsongs:
        if currentsong == 1 and not isdead:
            show bnoe1 with moveinleft
            noe "Psst!! Hey! Hey!"
            j "Wha!! Noel!! I can't believe you're here! I must be dreaming :')"
            noe "Well, you kinda are..."
            noe "Anyway, I took a sneaky peek at what songs they were gonna play here, and I literally have no clue who even watches this shit"
            noe "So~~~ How's about we bend a rules a little?"
            noe "If you ever need help I'll DM you the answers, just don't let Steph find out"
            noe "Here's your handy dandy Co-Op Button, now good luck out there!"
            $ cpbutton_beforegame = True
            show screen cp_button
            hide bnoe1 with moveoutleft
        narrator "Song [currentsong] of [numofsongs]"
        $ currentques = (list(songdict.items()))[currentsong-1][0]
        $ currentans = (list(songdict.items()))[currentsong-1][1]
        $ renpy.music.play("audio/" + currentques + ".mp3")
        show screen cp_button
        $ cpbutton_beforegame = False
        $ ans = None
        while ans is None:
            call screen noddinput
            $ ans = _return
        $ ans = _return.lower().strip()
        hide screen cp_button
        if ans in currentans:
            $ gamepoints += 10
            narrator "Correct! Current score: [gamepoints]"
        else:
            narrator "Nope... That ain't right..."
            $ allans = " / ".join(currentans)
            if currentques == "game1608":
                narrator "Correct answer(s):\n{size=-12}[allans]{/size}"
            else:
                narrator "Correct answer(s):\n{size=-8}[allans]{/size}"
            jump dream_death
        $ currentsong += 1
    stop music fadeout 1.0
    hide screen cp_button
    $ globalpoints += gamepoints
    scene black with fade
    return

label cp_button:
    hide screen cp_button
    show bnoe1 at left with moveinleft
    noe "Hmmm... "
    $ currentansstr = currentans[0].upper()
    if cpbutton_beforegame:
        noe "Ok but, press it when a song's actually playing..."
    else:
        noe "This song sounds like {b}[currentansstr]{/b}!"
    hide bnoe1 with moveoutleft
    show screen cp_button
    return