define config.rollback_enabled = False
define config.has_autosave = False

init python:
    import time as gettime
    rhythm_game_songs = [
        Song('Seishun wa Non-stop!', 'audio/sb69.mp3', 'audio/sb69.beatmap.txt'),
        Song('Tokimeki Experience!', 'audio/bandori.mp3', 'audio/bandori.beatmap.txt'),
        Song('Colorful Dreams! Colorful Smiles!', 'audio/lovelive.mp3', 'audio/lovelive.beatmap.txt'),
        Song('Onegai! Cinderella', 'audio/imas.mp3', 'audio/imas.beatmap.txt'), 
        Song('Make debut!', 'audio/umamusume.mp3', 'audio/umamusume.beatmap.txt')
    ]
    
    #config.has_quicksave = False
    #config.has_autosave = False
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
    $ global_points = 0
    
    call mizukibattle

    call op
    call ch1

    scene bg karaoke with fade
    kom "Let's get this started then! I'll go first"
    scene bg karaokedark
    show kom base at right with moveinright
    show mic1:
        xalign 0.8
        yalign 1.05
    kom "Here I go..."
    $ renpy.notify('♪ Kekkai Sensen & Beyond (Kamishiro)')
    play sound "audio/karaoke1.mp3" fadein 1.0 fadeout 1.0
    $ renpy.pause(5.0, hard=True)
    miz "{i}Oooh!{/i} I know this one!{p=5.0}{nw}"
    noe "You're killin it!{p=5.0}{nw}"
    miz "Letsgooooo{p=59.5}{nw}"
    stop sound fadeout 1.0
    hide kom base with moveoutright
    show miz happy at right behind mic1 with moveinright
    miz "Step aside and I'll show you guys how it's {i}really{/i} done~"
    $ renpy.notify('♪ M3: Sono Kuroki Hagane (Daytona)')
    play sound "audio/karaoke2.mp3" fadein 1.0 fadeout 1.0
    "{p=5.0}{nw}"
    kom "I guess this isn't too bad... {w=3.0}\n{size=-8}{i}Though mine was better... obviously...{/i}{/size}{p=5.0}{nw}"
    noe "The voice of an angel... honSugoi {p=56.5}{nw}"
    stop sound fadeout 1.0
    hide miz happy with moveoutright
    miz "Thank you, thank you~ I knew you guys would love it"
    noe "Oh, my turn already?"
    show noe appears at right behind mic1 with moveinright
    noe "Well, I'm not really the best at singing but I'll give this my best shot~✰"
    hide noe appears
    show noe sparkle at right behind mic1
    $ renpy.notify('♪ Yu-Gi-Oh! (Shuuka)')
    play sound "audio/karaoke3.mp3" fadein 1.0 fadeout 1.0
    "{p=8.0}{nw}"
    miz "Who told you you couldn't sing, Noel? You're already waaaay better than Komugi here {p=5.0}{nw}"
    kom "{size=+10}{b}Oi!{/b}{/size}{w=3.0}\n...But you are pretty good though...{p=5.0}{nw}"
    j "B-boku no kirakira pikapika kagayaku aidoru!!!!!!{p=6.0}{nw}"
    narrator "(Still least cringe weeb){p=50.0}{nw}"
    stop sound fadeout 1.0
    hide noe sparkle with moveoutright
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
    show miz happy at left behind mic2 with moveinleft:
        xzoom -1.0
    show kom base at right behind mic1 with moveinright 
    $ renpy.notify('♪ Sewayaki Kitsune no Senko-san (ChriS)')
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
    show noe sparkle at right
    show mic1:
        xalign 0.8
        yalign 1.05
    $ renpy.notify('♪ Bakemonogatari (???)')
    play sound "audio/karaoke5.mp3" fadein 1.0 fadeout 1.0
    narrator "{i}...And the karaoke room continues...{/i}{p=88.0}{nw}"
    stop sound fadeout 1.0
    scene bg karaokedark with Fade(2.0, 0.0, 2.0)
    show miz happy
    show kom base at left with moveinleft
    show noe appears at right with moveinright
    noe "Hey, hey! It's your turn now~"
    miz "Sing something for us will ya?"
    kom "C'mon, can't be that bad amirite?"
    narrator "You take a deep breath{cps=3}......{/cps}"
    $ renpy.notify('♪ Eromanga Sensei (Jack Parkson)')
    play sound "audio/karaoke6.mp3" fadein 1.0 fadeout 1.0
    show badsub:
        yalign 0.00
    "{p=3.0}{nw}"
    hide noe appears 
    show noe think at right
    noe "...{p=5.0}{nw}"
    hide kom base
    show kom think at left
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
    show miz happy
    show kom think at left
    show noe think at right
    noe "{cps=3}.....{/cps} That was... really somethin alright... ahah"
    j "Never again..."
    play sound "audio/knock.mp3"
    $ renpy.pause(2.5, hard=True)
    kom "Mm? Who could that be..."
    hide miz happy with moveoutleft
    hide kom think with moveoutleft
    hide noe think with moveoutleft
    show shi tehe with moveinleft
    shi "Hiiii~ I heard y'all were doing a karaoke room so I stopped by"
    shi "The name's Shiina, you can call me Shi or Ina"
    hide shi tehe
    show shi sing
    shi "So, you're the guy who spends 10 hours a day in their room guessing anime songs?"
    shi "Why don't 'cha try guessing the stuff I'm gonna sing then!"
    shi "You'd be surprised at my immaculate vocal range, I tell ya"
    "Ege's Spirit" "Warning: This is not true and Shiina's voice is impossible to listen to"
    shi "Let's get started then shall we~ I promise it'll be easy breezy~"
    scene black
    narrator "The following songs' vocals have been generated with text-to-speech software. They sound horrible. Good luck."
    call initgamenodd({"shiina01":["lucky star"],"shiina02":["blend-s"], "shiina03":["boku no hero academia", "my hero academia"], "shiina04":["sword art online ii"], "shiina05":["gon"]}, gamebg="bg karaokedark.jpg") from _call_initgamenodd_2
    scene bg karaoke
    show shi sing with fade
    shi "That was so much fun!! Glad you guys let me join~"
    shi "Oh, that reminds me, I came here to ask you guys for help"
    show kom base at right with moveinright
    kom "Sure, whadaya need?"
    hide shi sing
    show shi tehe 
    shi "Well, it's no big deal really, there's just some dude who's been chasing me since morning"
    j "Chasing you?! That doesn't seem safe!"
    play sound "audio/knock.mp3"
    $ renpy.pause(2.5, hard=True)
    "???" "I FINALLY FOUND YOU SHIINA GET OVER HERE!"
    play music "audio/bgm03.mp3" fadein 1.0 fadeout 1.0 volume 0.25
    $ renpy.notify('♪ Gun X Sword')
    show dayt at left with moveinleft:
        yalign 0.9
    j "Hold up! Who are you? Why are you after her!"
    narrator "{i}The (possibly) only act of heroic bravery our protagonist will ever display{/i}"
    dayt "Well, she comitted the HEINOUS crime of requesting a SEASONAL INSERT in #database-fixes"
    shi "B-but it's already been out for 2 months-"
    dayt "WAS IT EVEN CREDITED?"
    hide shi tehe
    show shi shock
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
    show noe sparkle at right with moveinright:
    noe "But you did great today!! {size=-1}A{/size}{size=-3}si{/size}{size=-4}de{/size} {size=-5}fr{/size}{size=-7}om {/size}{size=-8}th{/size}{size=-9}at {/size}{size=-10}sin{/size}{size=-12}gin{/size}{size=-13}g e{/size}{size=-15}arl{/size}{size=-16}ier{/size}{size=-18}...{/size}"
    noe "Be sure to get some rest now~ Tomorrow we'll be off to the arcade!"
    noe "... For training purposes of course"
    noe "Good night now~"
    hide noe sparkle with moveoutright
    menu:
        "Sleep":
            scene black with Fade(3.0, 0.0, 3.0)
    call gameshow from _call_gameshow
    scene bg bedroom
    j "... {w} I gotta stop watching all that Jewelpet, I swear it's driving me insane"
    "???" "Oh~ You're finally awake! Took you long enough..."
    show noe appears at right with moveinright
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
    show noe sparkle at right with moveinright
    noe "How was it? I threw in a few curveballs for ya in there!"
    noe "Well, now that that's out of the way, let's get going~☆"
    hide noe sparkle with moveoutright
    scene bg arcade with fade 
    show noe arcade appears at right with moveinright
    noe "Here we are!"
    play music "audio/bgm07.mp3" fadein 1.0 fadeout 1.0 volume 0.08
    $ renpy.notify('♪ Gamers!')
    noe "Isn't this great~? The fresh sweet smell of sweat, sweaty people, questionable pizza and a random kid's birthday party"
    noe "Of course {i}you've{/i} never been here though so let me show you around!"
    j "Eh- Shouldn't we wait for Komugi and Mizuki to arrive at least?"
    noe "Mm? Oh, well Mizuki's busy prepping for New Year's... something about stealing all the lucky fortunes for herself..."
    j "Oh so Komugi's probably doing the same thing then..."
    noe "lol no she failed math class so she's stuck with Hikari-sensei learning polynomials or something kekw"
    noe "So anyway, it's just the two of us today~"
    hide noe arcade appears
    show noe arcade sparkle with fade:
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
    show noe arcade appears at right with moveinright
    noe "See? Even someone like you can have fun outdoors, I knew you had it in ya mhm"
    "???" "So I heard there's a new god in town..."
    play music "audio/bgm06.mp3" fadein 1.0 fadeout 1.0 volume 0.2
    $ renpy.notify('♪ Hakaima Sadamitsu')
    show rit cheese at left with moveinleft
    rit "Ah, I've heard of ye alright... You're that Yolowolf something kid aren't cha?"
    j "Uhhh"
    rit "Names Ritsu, but they call me Risu, cus I'm fast, like a squirrel."
    narrator "(Least cringe gamer)"
    rit "First time around these parts I reckon, mineas?"
    j "Uhhh..."
    hide rit cheese
    show rit smug at left
    rit "I'll have ya know I set the world reck'rd for all these here games... I'm, kind of what they call a big deal"
    j "Oh, I didn't see any scores earlier on Arse though"
    $ renpy.music.set_pause(True, channel="music")
    hide rit smug
    show rit think at left
    rit "No one plays that game, it's broken af"
    rit "{size=-10}... Keeps telling me I missed when I CLEARLY HIT THEM NOTES I TELL YA*@^!{/size}"
    narrator "(Least salty osu player)"
    rit "I asked the loser in charge to fix that thing like three months ago, but you know how it is... soon™ (just like Ege fiixing tpyos)"
    hide noe arcade appears
    show noe arcade think at right
    noe "Wait, so you're saying Ege didn't make this game?"
    rit "Please, that's just as believable as him saying 'people play AMQ for the avatars'"
    rit "Ahem- ANYWAY!"
    $ renpy.music.set_pause(False, channel="music")
    hide rit think
    show rit smug at left
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
    show rit sweat at left with moveinleft
    rit "...I guess you *cough* really are sumthin... WinAxel..."
    rit "B..but mark my words Mael!! I'll get 'cha some day!!"
    j "(Man... and she almost got my name right there)"
    "???" "There you are~ finally found you-"
    show hon smile at right with moveinright
    hon "Ricchan~"
    hide rit sweat
    show rit smile at left
    rit "{size=-7}H-Honocchi!! I told you to call me Risu, remember!{/size}"
    hon "Ah~ my bad..."
    hon "Anyway... Kyouko's ready to pick us up, let's go~"
    rit "Ah"
    hide rit smile
    show rit smug at left
    rit "Well I guess that can't be helped, see ya next time Anti"
    hide hon smile with moveoutright
    hide rit smug with moveoutright
    show noe arcade sparkle at left with moveinleft
    noe "Looks like Komugi and Mizuki aren't done yet... Let's go grab dinner then~ You did great back there!"
    scene bg dinner with Fade(2.0, 0.0, 2.0)
    show noe arcade sparkle with moveinleft
    noe "Uwaa~ I'm starving, what're you gonna order?"
    menu:
        noe "I think I'm having the Tropical-Rouge PanCake Tower!"
        "Cheese Gyuudon":
            noe "Oooh that looks yummy, do you get this often?"
            hide noe arcade sparkle
        "Tuna Tataki":
            noe "Look at the price! Where'd you get the money for that...{w}{s}i thought u were a neet{/s}"
            hide noe arcade sparkle
        "AMQ Player Salad":
            "{i}Garlic sautéed premium-grade Cheeto Puffs in an aromatic salted caramel Mountain Dew vinaigrette{/i}{w}\nLimited time only: Comes with free tendies!"
            hide noe arcade sparkle
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
    show mar pirate think with moveinright:
        yalign 0.4
        xalign 0.5
    play music "audio/bgm09.mp3" fadein 1.0 fadeout 1.0 volume 0.2
    $ renpy.notify('♪ Mouretsu Pirates')
    mar "Who do you think ye are... steeping foot in MY WATERS?"
    hide mar pirate think
    show mar pirate sparkle:
        yalign 0.4
        xalign 0.5
    mar "Best ye speak up before I splice ye into smithereens"
    j "W-who are you?"
    hide mar pirate sparkle
    show mar pirate angry:
        yalign 0.4
        xalign 0.5
    mar "THE LEVEL OF DISRESPECT COMING FROM YER TRAP"
    mar "I'm the feared Nightmare Lancer of the Tyrant's Eye - Deus Highest Death Impact of the Seventh Resilience Crest Master of Spinjitsu Houshou Fitzgerald Lalatina Marine the Swashbuckler"
    hide mar pirate angry
    show mar pirate sparkle:
        yalign 0.4
        xalign 0.5
    mar "Now remember that ok?"
    mar "Repeat after me!"
    mar "Night-"
    j "N-night..."
    scene bg playground
    stop music fadeout 1.0
    show mar excite
    mar "-mare Lancer"
    j "Who is this... sassy lost child?"
    hide mar excite
    show mar angry
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
    $ renpy.notify('♪ Comic Girls')
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
    show hik scholar at right with moveinright
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
    show noe think at right
    show kom think at left
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
    scene black with fade

    # Continue here for 0.1.9 content

    python:
        rhythm_game_scores_list = []
        for i in persistent.rhythm_game_high_scores.values():
            rhythm_game_scores_list.append(i[0])
        avg_rhythm_game_score = int(round((sum(rhythm_game_scores_list) / len(rhythm_game_scores_list) / 1000),0))
        game_points += avg_rhythm_game_score * 2
    ""
    scene black with fade
    centered "~ to be continued ~"
    centered "Thanks for playing till the end!"
    centered "Total XP: {b}[global_points]{/b}"
    return