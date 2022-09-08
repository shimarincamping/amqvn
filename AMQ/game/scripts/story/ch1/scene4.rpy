label ch1sc4:
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