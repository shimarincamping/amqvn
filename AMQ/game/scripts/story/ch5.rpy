label ch5:
    centered "And so... Our four heroes went on a search for any clues leading to {b}SOLID GOLD HIBIKI{b}'s whereabouts..."
    $ renpy.notify('♪ Kuroshitsuji')
    play music "audio/bgm13.mp3" volume 0.2 fadein 1.0 fadeout 1.0
    
    scene searching1 with Fade(2.0, 0, 2.0)
    
    scene searching2 with Fade(2.0, 0, 2.0)
    
    scene searching3 with Fade(2.0, 0, 2.0)
    
    scene bg desert with Fade(2.0, 0, 2.0)
    
    show noe think at right with moveinright
    noe "This thing's harder to find than a good post in #feature-ideas"
    
    show kom think with moveinleft
    kom "And... this desert is... getting really hot..."
    
    show miz happy at left with moveinleft
    miz "Guys, guys, look what I found~"
    
    stop music fadeout 1.0
    hide noe think with moveoutleft
    hide kom think with moveoutleft
    hide miz happy with moveoutleft
    kom "Whoa!! There's like an entire oasis out here"
    miz "Yeah, it was behind that funny looking bush"
    kom "I'm literally burning hotter than chat when Steph hears Everybody Everybody, I say we jump in"
    noe "But... did any of you bring swimsuits even?"
    kom "It's the fanservice episode, so of course we did for some reason god only knows"
    miz "VN logic duh" 
    
    show kom mizugi at right with moveinleft
    show noe mizugi with moveinleft
    show miz mizugi at left with moveinleft
    kom "Phew! I'm already feelin' much better"
    
    scene black
    
    "Eagles (real dev)" "Wait a minute we can't be giving away this scene for FREE, wtf"
    "Eagles (real dev)" "Swimsuit specials go for at least $12.99, everyone knows that"
    "Eagles (real dev)" "Even Ege would happily charge people to show off PNG booba, no no no"
    
    scene bg desert
    
    show kom censored at right
    show noe censored 
    show miz censored at left
    noe "Now then~ Let's get this beach episode on the road!"
    
    play music "audio/bgm14.mp3" fadeout 1.0 fadein 1.0 volume 0.2
    $ renpy.notify('♪ Non Non Biyori Vacation')
    
    "Noel, Komugi, Mizuki" "Yayyy!!!!"
    hide miz censored with moveoutleft
    hide noe censored with moveoutleft
    hide kom censored with moveoutleft
    
    stop music
    
    "???" "Who there dare enter my swamp?!"
    
    show aka mad with moveinleft
    miz "Whoa whoa whoa whoa I'm not ready for my tentacle scene debut yet"
    aka "Shut it, Mizuki"
    noe "Wait, you two know each other?"
    miz "N-no....?"
    kom "Everyone knows nobody remembers half of the avatars after Marine anyway"
    aka "..."
    aka "{size=-8}Just for that I'm making it hell for you later. Have fun with that.{/size}"
    aka "{size=-1}C{/size}{size=-3}'m{/size}{size=-4}on{/size}{size=-5}...{/size}{size=-7} We{/size}{size=-8} we{/size}{size=-9}nt {/size}{size=-10}to m{/size}{size=-12}iddl{/size}{size=-13}e s{/size}{size=-15}cho{/size}{size=-16}ol to{/size}{size=-18}gether...{/size}{w}\n{b}AHEM-{/b}"

    show aka base 
    aka "something something you trespassed on my territory yadda yadda beat me at AMQ now"
    noe "God these segues into AMQ battles are really starting to feel forced"
    aka "Hey, you chossse to play this bad game"
    miz "At least it's still a better experience than playing FTF"
    kom "So what happens if we lose, we die or...?"

    show aka sparkle
    aka "Aha no grrl, it's just something, like, far worse, or something... I'm just, like, quirky like that"

    show aka base
    aka "But before that, just making sure, your name isn't {b}Spear{/b} is it?"
    
    menu:
        aka "But before that, just making sure, your name isn't {b}Spear{/b} is it?{fast}"
        "Who?":
            $ currentmonth = gettime.localtime(gettime.time())
            $ punishment = "padoru" if currentmonth.tm_mon == 12 else "normal"
            aka "Ok good..."
        "Maybe...":
            $ punishment = "mii"
            aka "Kinda cringe but alright..."
    
    aka "Prepare to wish you were never born"
    
    scene black with fade
    
    call initgamenodd(game_settings["ch5"]["game1"], gamebg="bg desert.png", akane=True) from _call_initgamenodd_7
    
    scene bg desert with fade
    
    show aka mad at right with moveinright
    aka "I don't know how you're ssstill alive after all that, usually my punishment venom is enough to make anyone mentally regress into a League player"
    "???" "Oh god, where did it run off to, Hikari's gonna kill me if he finds ou-"
    
    show chi shock at left with moveinleft
    chi "There you are!!"
    chi "I've been... looking... EVERYWHERE... No one must know about this experimen-"
    "She notices you and your party of idiots wearing light beam censors"

    show chi smug at left
    chi "a"
    chi "Oh my god! It's really you!! I can't believe I finally get to meet you, you're practically the talk of the town!!"
    chi "You're that AMQ booli aren't you?! You're my personal hero aaaaa!!!"
    j "Omg really?"
    chi "lol no"
    chi "Also you really shouldn't be sneaking into high schools, someone's gonna get the wrong idea"
    chi "I'm Chika by the way, president of the science club"
    j "Did, you just say, school?"
    j "Who builds a school... in a desert... in the middle of nowhere"
    chi "The highway's to your left"
    j "oh... :monkey:"
    noe "Hey! hey! Remember our mission!"
    j "R-right!! We came all the way out here to see if anyone has any leads to where {b}the illusive SOLID GOLD HIBIKI{/b} might be"

    show chi think at left
    chi "Hmmm... well personally no, but I know just the {s}chuuni{/s} expert who might in the {b}Occult Research Club{/b}..."
    chi "By the way, did you know the average AMQ player loses 8 braincells every time they hear a Lucky Star karaoke ending? Fascinating stuff."
    kom "Are we really gonna go with her? She looks like she has a few screws loose herself..."
    miz "Hey, hey. A lead is a lead. Even if it comes from Ms. Knockoff Rio Futaba"
    
    scene black with fade
    
    "You make your way into the school building..."
    
    scene bg corridor with fade
    
    show chi smug at right with moveinright
    chi "... We're almost there, is there any club you'd like to check out before we get there?"
    
    menu:
        "Let's take a look at the Art Club!":
            scene black with fade
            call artclub from _call_artclub
        "How about your club?":
            scene black with fade
            call scienceclub from _call_scienceclub
        "No, thanks...":
            chi "Fun fact: 72.4\% of the average AMQ player's vocabulary consists of calling other players a crude amalgamation of their name and the word 'god'"
            chi "Allow me to demonstrate: *ahem* godyoshi here to carry us time to afk :place_of_worship:"
    
    scene bg corridor
    
    show chi smug at right
    chi "Well then, let's get going now!"
    chi "Also did you know that based on my research, 100\% of all AMQ players talk to themselves less than LOLwarZ?"
    
    scene bg occult with fade
    play sound "audio/bgm17.mp3" fadeout 1.0 fadein 1.0 volume 0.3
    $ renpy.notify('♪ Magatsu Wahrheit (Off-Music)')
    
    show skur with dissolve
    show cauldron with dissolve:
        xalign 0.5 yalign 0.99
    kur "... three parts mandrake root... two sheets of scorpion skin... five drops ginseng extract... and finally... one bottle of teazri's tears..."
    kur "I've done it..."
    kur "With this elixir, I'll be the most powerful being known to humanity!"
    
    play sound "audio/knock.mp3"
    $ renpy.pause(2, hard=True)
    
    j "Yo is this the occult research cl-"
    j "Holy- what the fuck is that smell?"
    kur "AMQ juice."
    j "AMQ what?"
    kur "Juice... y'know the drinking kind"
    j "No... how about no..."
    "..."
    kur "Oh? The {b}SOLID GOLD HIBIKI{/b}, you say?"
    kur "Why yes, I did stumble upon that name in one of my grimoires..."
    kur "But the lock is guarded by a terrifying curse... and an equally terrifying troll...!!!! *evil laughter*"
    
    show miy knight at right with moveinright
    miy "Hey, uh, I'm gonna go buy lunch from the school store, you need anything?"
    kur "Oh, speak of the devil, there she is right now"
    
    hide miy knight with moveoutright
    j "Haven't I... seen you two before?"
    kur "{size=-15}no no you havent and if you have you will pretend like you havent.{/size}\n"
    j "O-oh ok..."
    kur "You better be prepared to face her off once she gets back from buying yakisoba pan."
    j ":skull:"

    $ proceed = False
    while not proceed:
        menu:
            "Ege's Spirit" "It's recommended you save your game before fighting bosses; dying means you lose your current save data"
            "Begin fight":
                $ proceed = True
            "Maybe later...":
                kur "She'll be back any minute now..."
    
    scene black
    
    j "Whoa... what happened? Why'd it get so dark all of a sudden?!"
    kur "It's starting..."
    
    call kurikobattle from _call_kurikobattle
    
    centered "I suppose I can tell you the story..."
    centered "A long time ago... in a mystical land far, far away{w} named \"Denmark\"..."
    
    $ dial_eng = [
        "The year was 2017... and a man named Egerod \"Rasmus\" Leth had big ideas...",
        "What a time to be alive that was... when AnimeMusicQuiz opened its doors to the world",
        "The good ol' days... when Rent-a-Girlfriend just released its first volume... and Yuri on Ice!!! won the Anime Awards... and there was no one to laugh at you for missing Gintama in ranked...",
        "Wouldn't it be nice if we could turn back time to when AMQ used Dailymotion as a video source, and Astolfo's Bizarre Adventure was real?",
        "... Just playing with your pals in a random pub room, with these iconic classic avatars...",
        "Then it all changed... when the Ticket System attacked",
        "On that day, humanity received a grim reminder of what it means to be scammed by gacha...",
        "And with that, came in a wave of avatars I've only ever seen 3 people max use...",
        "Solid Gold Hibiki wasn't impressed either... What ever happened to the AMQ he came to know and love?!",
        "... And that's when he went missing. Some say he was banned, some say he was starting to become too opinionated and toxic... some say he was both and was actually named ErVex",
        "The secret is buried here in this grimoire, in hopes that no mortal soul will ever lay eyes upon this knowledge",
        "... Fearing what the next big update could do to his sanity, he went into hiding...",
        "... Deep in the AMQ source code, a place he knew he would never be willingly seen or touched ever again..."
    ]
    
    $ dial_amq = [
        "The ear is 2017. And I has a big curios idea !",
        "Doing that time, AMQ finaly was launched to take over every local in the world!!",
        "Their was good thing to happen in that year, KanoKari first volume releases, Yaoi on Ice!!! won the Anime-Awards and no ranked to delay four a hour because Catbox went down again",
        "Trough AMQ is not different! Using Daily motion as video sorce with adds and 100percent legit Jojo?",
        "Even have fluffy kistsune for all you're fluffing needs!",
        "But then I introduce the high sort after feature off whaling for images",
        "Papa Ege confident everyone feel in love with it at first site",
        "Then I maked so much avatar I can justify raiisng the Drive Donasion too 600 $",
        "But my april fool's' joke where not so happy with this change",
        "Just like a guess account after hearing OnegaiSnyaiper, they dissapear!",
        "Secret is buried in this book with is...",
        "The Gold Hibiki Original and not the Purple Hibiki DVDR went into hiding...",
        "A place his not suppose to bee... the AMQ spageti code"
    ]
    
    $ dial_wee = [
        "Nen wa 2017 desu. Toaru otoko wa BIGGU AIDIA ga arimasu.",
        "Sono toki, EI EMMU KYUU wa sekai ni OOPUN shimashita...",
        "Taun iku, 'Sewa-A-Pacar' baru saja rilis; Yuri di Atas Es menangkan Penghargaan Enime, Dan tidak ada yang menawarkan Anda bila Anda gagal Gintama seketika Peringkat ber-Rank",
        "Aujourd'hui, je fais du fromage a la ferme d'Astolfo... Mercy bowcoop",
        "avec les avatars classique!",
        "Zhao shang hao zhong guo xian zai wo you bing qi ling; wo hen xi huang bing qi ling dang shi xu du yu",
        "Humani'y rehseev'd ai grimm rema'aindahr uv whot it maens tuh be scahm'd boih gaht'chuh",
        "J'aime la raclette, mais Solide Golde Hibikee ne aimer pas la raclette",
        "E então, o Hibiki de ouro maciço desapareceu...",
        "Oh no no no อย่างนี้ไม่ดีOh no no no อย่างนี้สงสัยไม่ดีOh no no no อย่างนี้น่ากลัว คงจะเป็นฝันร้าย",
        "nae-ga olsu-opsul-korago i-jen kurolsu op-tago chebal kuman-harago narul tarrae-ji..",
        "Latebat etiam... Alicubi nusquam inveniri potuit. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "En el código fuente de AMQ..."
    ]
    
    menu:
        "Please choose your language"
        "English":
            $ storydial = dial_eng
        "AMQlish":
            $ storydial = dial_amq
        "Cringe":
            $ storydial = dial_wee
    
    $ dial1 = storydial[0]
    $ dial2 = storydial[1]
    $ dial3 = storydial[2]
    $ dial4 = storydial[3]
    $ dial5 = storydial[4]
    $ dial6 = storydial[5]
    $ dial7 = storydial[6]
    $ dial8 = storydial[7]
    $ dial9 = storydial[8]
    $ dial10 = storydial[9]
    $ dial11 = storydial[10]
    $ dial12 = storydial[11]
    $ dial13 = storydial[12]
    
    play music "audio/bgm18.mp3" fadein 1.0 fadeout 1.0 volume 0.3
    
    scene story1 with fade
    $ renpy.notify('♪ Strait Jacket')
    
    "[dial1]"
    
    scene story2 with fade
    
    "[dial2]"
    "[dial3]"
    
    scene story3 with fade
    
    "[dial4]"
    
    scene story4 with fade
    
    "[dial5]"
    
    scene story5 with fade
    
    "[dial6]"
    "[dial7]"
    
    scene story6 with fade
    
    "[dial8]"
    
    show donation:
        xalign -0.5 yalign 0.45
        linear 1.0 xalign 0.0001
    
    $ renpy.pause(1.5, hard=True)
    
    show qualityavatar with dissolve:
        xalign 0.3 yalign 0.61
    "[dial9]"
    
    scene story7 with fade
    
    "[dial10]"
    "[dial11]"
    
    scene story8 with fade
    
    "[dial12]"
    
    scene story9 with fade
    
    "[dial13]"
    
    scene black with Fade(3, 0, 3)
    stop music fadeout 1.0