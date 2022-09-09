screen noddinput():
    window:
        vbox:
            text "Your answer:"
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

label countdown(duration, timer_jump=None, alignment={"xalign":0.5, "yalign":0.93, "xmaximum":1000}):
    $ time_left = duration
    $ timer_range = duration
    
    show screen countdown(timer_jump, alignment)

screen countdown(timer_jump, alignment):
    if timer_jump:
        timer 0.01 repeat True action If(time_left > 0, true=SetVariable('time_left', time_left - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    else:
        timer 0.01 repeat True action If(time_left > 0, true=SetVariable('time_left', time_left - 0.01), false=[Hide('countdown')])
    
    bar value time_left range timer_range xalign alignment["xalign"] yalign alignment["yalign"] xmaximum alignment["xmaximum"] at alpha_dissolve 
    
    if timer_jump:
        zorder 99