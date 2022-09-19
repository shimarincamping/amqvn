label daytbattle:
    scene bg karaokedark with fade

    python:
        def calc_points(seconds):
            if seconds <= 7:
                return 7
            elif seconds <= 10:
                return 5
            elif seconds <= 15:
                return 3
            elif seconds <= 20:
                return 1
            return 0
    
    menu:
        "Please choose your difficulty"
        "Free (20 pts)":
            $ point_goal = 20
            $ multiplier = 0.5
        "Easy (30 pts)":
            $ point_goal = 30
            $ multiplier = 1.0
        "Medium (40 pts)":
            $ point_goal = 40
            $ multiplier = 1.33
        "Hard (50 pts)":
            $ point_goal = 50
            $ multiplier = 1.67
        "Expert (65 pts)":
            $ point_goal = 65
            $ multiplier = 2.25
        "Lunatic (80 pts)":
            $ point_goal = 80
            $ multiplier = 2.83
    
    narrator "--- Boss information ---\nName: Daytona"
    narrator "Rules: 20 second time limit; Quick-Draw Style"
    narrator "{size=-8}The faster you answer the more points you receive:{/size}{w}{size=-13}\nWithin 7 seconds - 7 pts\nWithin 10 seconds - 5 pts\nWithin 15 seconds - 3 pts\nWithin 20 seconds - 1 pt{/size}{w}\nRequired points: {b}[point_goal] pts{/b}"
    narrator "Flex bonus: +2 pts for using the longest valid name\nStreak bonus: +1 pt per song in longest streak\nShortcut penalty: -5 pts for each deleted answer"
    narrator "Specialty: Title-Deletion\n{i}{size=-8}Shortened titles such as 'LasDan', 'EnStars', 'Genkoku', 'Yu-sibu', 'Haifuri', 'TsureKano' etc. are {b}not{/b} valid answers for this battle.{/size}{/i}"
    
    show dayt at left with moveinleft

    $ song_list = game_settings["ch2"]["daytona"]
    $ renpy.random.shuffle(song_list)

    $ game_points = 0
    $ curr_song = 1
    $ song_count = 12

    $ curr_streak = 0
    $ max_streak = 0

    $ dial = [
        "I've got a toothbrush with your name on it",
        "I deleted it (yaoi!!! on ice) and ege made me readd it",
        "the last time i played amq was in january i think",
        "(real Dayt quote) did you know that Hitler was an animal lover and was actually a huge advocate for more laws protecting animals", 
        "wtf a furry that looks decent", 
        "Yes the idol jihen fan base is so trash", 
        "thats why i back catbox adn not amq amq is trash catbox is god",
        "time to ban jax for playing osu",
        "if youre getting anythign right in 5 sec youre cheating anyway jsut not with shazam", 
        "saro wtf", 
        "oh my god these titles are giving me cancer",
        "the reason quickdraw is so unplayed is because it legimitaly is a typing test"
    ]

    while curr_song <= song_count:
        $ song = song_list[curr_song-1]
        $ answer = ""
        
        $ penalty = 0
        $ flex = 0
        $ point = 0

        narrator "Song [curr_song] of [song_count]"

        call countdown(20.0, None, {"xalign":0.5, "yalign":0.1, "xmaximum":1350})

        $ renpy.music.play("audio/" + song["audio"] + ".mp3")
        
        call screen noddinput
        
        $ answer = _return.lower().strip()
        $ time_rounded = round(20 - time_left, 2)

        hide screen countdown
        
        if song["audio"] == "game606" and _return.strip() == "hagAnaI":
            dayt "heh nice, still wrong tho"

        if answer in song["illegal"]:
            $ curr_streak = 0
            $ penalty = -5

            dayt "Looks like you entered in an answer I Thanos snapped, better luck next time"
        
        elif answer in song["answer"]:
            $ curr_streak += 1
            $ point = calc_points(time_rounded)
            $ flex_answer = max(song["answer"], key=len)

            if answer == flex_answer:
                $ flex = 2
            
            narrator "Correct answer!"

        else:
            $ answers = " / ".join(song["answer"])
            $ curr_streak = 0
            
            narrator "Nope... That ain't right..."
            narrator "Correct answer(s):\n{size=-8}[answers]{/size}"
        
        $ max_streak = max(max_streak, curr_streak)
        $ game_points += (point + flex + penalty)

        narrator "{size=-5}Answer score: [point] ([time_rounded]s)\nFlex bonus: [flex]\nPenalty: [penalty]{b}\nCurrent score: [game_points] points{/b} (Streak: [curr_streak]){/size}"
        
        $ currentdial = dial[curr_song-1]
        if currentdial:
            dayt "[currentdial]"
        
        $ curr_song += 1
    
    stop music fadeout 1.0

    $ total_point = game_points + max_streak
    
    narrator "Game points: [game_points]\nHighest streak: [max_streak]\n{b}Total points: [total_point] points{/b}"
    
    if total_point >= point_goal:
        $ weighted_points = total_point * multiplier
        $ global_points += int(round(weighted_points,0))
        
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