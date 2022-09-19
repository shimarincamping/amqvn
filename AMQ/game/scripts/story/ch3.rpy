label ch3:
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
    
    call initgame(game_settings["ch3"]["game1"], "bg bedroom.jpg") from _call_initgame_2
    
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

    show rit smug at left
    rit "I'll have ya know I set the world reck'rd for all these here games... I'm, kind of what they call a big deal"
    j "Oh, I didn't see any scores earlier on Arse though"
    
    $ renpy.music.set_pause(True, channel="music")

    show rit think at left
    rit "No one plays that game, it's broken af"
    rit "{size=-10}... Keeps telling me I missed when I CLEARLY HIT THEM NOTES I TELL YA*@^!{/size}"
    narrator "(Least salty osu player)"
    rit "I asked the loser in charge to fix that thing like three months ago, but you know how it is... soon™ (just like Ege fiixing tpyos)"
    
    show noe arcade think at right
    noe "Wait, so you're saying Ege didn't make this game?"
    rit "Please, that's just as believable as him saying 'people play AMQ for the avatars'"
    rit "Ahem- ANYWAY!"
    
    $ renpy.music.set_pause(False, channel="music")

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

    show rit smile at left
    rit "{size=-7}H-Honocchi!! I told you to call me Risu, remember!{/size}"
    hon "Ah~ my bad..."
    hon "Anyway... Kyouko's ready to pick us up, let's go~"
    rit "Ah"

    show rit smug at left
    rit "Well I guess that can't be helped, see ya next time Anti"
    
    hide hon smile with moveoutright
    hide rit smug with moveoutright
    show noe arcade sparkle at left with moveinleft
    noe "Looks like Komugi and Mizuki aren't done yet... Let's go grab dinner then~ You did great back there!"

    scene black with Fade(3.0, 0.0, 3.0)