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