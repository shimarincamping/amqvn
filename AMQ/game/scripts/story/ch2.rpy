label ch2:
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
    
    show noe think at right
    noe "...{p=5.0}{nw}"

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
    
    show shi sing
    shi "So, you're the guy who spends 10 hours a day in their room guessing anime songs?"
    shi "Why don't 'cha try guessing the stuff I'm gonna sing then!"
    shi "You'd be surprised at my immaculate vocal range, I tell ya"
    "Ege's Spirit" "Warning: This is not true and Shiina's voice is impossible to listen to"
    shi "Let's get started then shall we~ I promise it'll be easy breezy~"
    
    scene black
    narrator "The following songs' vocals have been generated with text-to-speech software. They sound horrible. Good luck."
    
    call initgamenodd(game_settings["ch2"]["shiina"], "bg karaokedark.jpg") from _call_initgamenodd_2
    
    scene bg karaoke
    
    show shi sing with fade
    shi "That was so much fun!! Glad you guys let me join~"
    shi "Oh, that reminds me, I came here to ask you guys for help"

    show kom base at right with moveinright
    kom "Sure, whadaya need?"

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