screen noddinput(titletext="Your answer:"):
    window:
        vbox:
            xmaximum 1300 xpos 310
            text "\n[titletext]"
            input

screen cp_button():
    fixed:
        imagebutton idle "cp_button.png" focus_mask True xpos 1580 ypos 35 action Call("cp_button") hovered [Play("sound","audio/click.mp3")] alt "cp"

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

label countdown(duration, timer_jump=None, alignment={"xalign":0.5, "yalign":0.93, "xmaximum":1000}, number=False):
    $ time_left = duration
    $ timer_range = duration
    
    if number:
        show screen countdown_number(timer_jump, alignment)
    else:
        show screen countdown(timer_jump)

screen countdown(timer_jump, alignment):
    if timer_jump:
        timer 0.01 repeat True action If(time_left > 0, true=SetVariable('time_left', time_left - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    else:
        timer 0.01 repeat True action If(time_left > 0, true=SetVariable('time_left', time_left - 0.01), false=[Hide('countdown')])
    
    bar value time_left range timer_range xalign alignment["xalign"] yalign alignment["yalign"] xmaximum alignment["xmaximum"] at alpha_dissolve 

    if timer_jump:
        zorder 99

screen countdown_number(timer_jump):
    fixed:
        text "{color=#d9f5ff}{b}Time left:{/b}{/color}":
            xpos 230 ypos 420

    timer 1 repeat True action If(time_left > 0, true=SetVariable('time_left', time_left - 1), false=[Hide('countdown'), Jump(timer_jump)])
    if time_left <= 3:
        text str(time_left) xpos .25 ypos .35 color "#FF0000" size 200 at alpha_dissolve 
    else:
        text str(time_left) xpos .25 ypos .35 size 200 at alpha_dissolve

screen certificate(playername, tier, points):
    vbox:
        xsize 800
        ysize 200
        xalign 0.5
        yalign 0.57

        text "{color=#000}{b}[playername]{/b}{/color}":
            xalign 0.5
        text "{color=#000}{size=-10}[tier] {i}([points] pts){/i}{/size}{/color}":
            xalign 0.5
            yalign -0.92

screen sectionheader(number, subtext):
    fixed:
        text "{color=#fff}{b}{size=+40}{u}STAGE [number]{/u}{/size}{/b}{/color}":
            xpos 200 ypos 300
        text "[subtext]":
            xpos 200 ypos 420

screen songnumbertext(number, total):
    fixed:
        text "{color=#fff}{b}{size=+30}SONG {/size}{size=+100}[number]{/size}{/b}   OF [total]{/color}":
            xalign 0.15 ypos 250

screen correctscreen(inputtext):
    fixed:
        text "{color=#fff}{size=+100}{b}Correct!{/b}{/size}{/color}":
            xpos 200 ypos 150
        text "{color=#fff}Current points: [gamepoints] / [pointgoal]{/color}":
            xpos 210 ypos 310
        text "{color=#fff}{u}You answered:{/u}\n{size=-8}[inputtext]{/size}{/color}":
            xpos 150 ypos 400

screen wrongscreen(inputtext, answertext):
    fixed:
        text "{color=#fff}{size=+100}{b}Nope...{/b}{/size}{/color}":
            xpos 200 ypos 150
        text "{color=#fff}Current points: [gamepoints] / [pointgoal]{/color}":
            xpos 210 ypos 310
        text "{color=#fff}{u}You answered:{/u}\n{size=-8}[inputtext]{/size}{/color}":
            xpos 150 ypos 400
        text "{color=#fff}{u}Correct answers:{/u}\n{size=-8}[answertext]{/size}{/color}":
            xpos 150 ypos 500

screen answerlabel(text):
    fixed:
        text "{color=#ffade0}{b}>>> [text] <<<{/b}{/color}":
            xpos 210 ypos 130

screen notime():
    fixed:
        text "{color=#fff}{size=+100}{b}Out of time...{/b}{/size}{/color}":
            xpos 200 ypos 150
        text "{color=#fff}Current points: [gamepoints] / [pointgoal]{/color}":
            xpos 210 ypos 310

screen gameend(winlosemsg, textcolor):
    fixed:
        text "{color=#fff}{size=+100}{b}Game complete!{/b}{/size}{/color}":
            xpos 200 ypos 200
        text "{color=#fff}Total points: [gamepoints] / [pointgoal] {size=-9}([pointspercentage]%){/size}{/color}":
            xpos 210 ypos 360
        text "{color=[textcolor]}{size=+30}{b}[winlosemsg]{/b}{/size}{/color}":
            xpos 210 ypos 460