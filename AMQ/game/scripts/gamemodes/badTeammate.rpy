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