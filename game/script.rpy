# Main Character
define ray   = Character("Ray Zealsphere", color="#ff0000")
define elise = Character("Elise Fonillia", color="#fffb00")
define zack  = Character("Zack Salkelberg", color="#ff9900")

# Side Character
define kenneth = Character("Kenneth Daberth", color="#0051ff")
define ann = Character("Kurtney", color="#ffb5b5") 

# Type Writer Effect
init python:
    def type_writer(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/writer.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

# The game starts here.          
label start:
    
    play sound "audio/case.mp3" fadeout 0.5

    scene black
    with fade

    with dissolve
    show text "{size=+10}{color=#ff0000}CASE 1:{/color}\n\nKenneth's Desperation{/size}{nw}" at truecenter
    with dissolve

    $ renpy.pause(5.0, hard=True)

    hide text
    with dissolve

    scene bg school
    with fade
    
    "{color=#00a62c}{cps=10}{color=#ff0000}Date:{/color} September.17,2020 \n{color=#ff0000}Location:{/color} School (\"Inside a certain clubroom.\") {/cps}{/color}" (callback=type_writer) 

    play sound "audio/next.wav" volume 0.2

    play music "audio/canon.ogg" fadeout 1.0 fadein 1.0 volume 0.3

    scene bg philippines
    with fade
    
    ray "{color=#00a62c}{i}\"A long, long time ago in a beautiful and peaceful country called Philippines....\"{/color}"

    scene bg duterte
    with fade

    ray "{color=#00a62c}{i}\"There was a president named Rodrigo Duterte has been approven a certain law on {color=#ff0000}April 17,2019{/color}....{/color}\""

    # !Important ~ Update the image.

    scene bg law
    with fade 

    ray "{color=#00a62c}{i}\"And that law is called {color=#ff0000}Republic Act 11313{/color} or also known as {color=#ff0000}Safe Space Act{/color}.{/color}\""

    # !Important ~ add a image of a men and woman that showing equility, security, and safety in private areas.

    ray "{color=#00a62c}{i}\"The law stated that both men and women must have equality, security and safety not only in private areas.....\"{/color}"

    # !Important ~ add a image of a streets, public spaces, online, workplaces, educational.

    ray "{color=#00a62c}{i}\"but also on the streets, public spaces, online, workplaces, educational and training institutions.....\"{/color}"

    scene bg clubroom
    with fade

    play music "audio/Time for Rest.ogg" fadein 0.5 volume 0.3

    ray "Hmm....very intriguing, no matter how many times I read this, it really always enlighten me."

    ray "I guess I should read this again more later especially about the information of potential penalties and consequences to anyone who violated this law."

    play sound "audio/information.wav" volume 0.2

    "New Information has been added."

    "If you wanna learn more about \"Safe Space Act\" click the button at the top right corner of the screen."

    # !Important ~ add a general log button on the top right corner of the screen for the information you just learn.

    play sound "audio/doorknock.mp3"

    "{i}\"Knock! Knock!\""

    stop sound

    show elise talking with dissolve

    elise "Hey Ray sorry am late...."

    $ timeout = 10
    $ timeout_label = renpy.random.choice(['qt001a', 'qt001b','qt001c'])

    show elise surprise 

    elise "Huh?! Your reading that again? How many times your gonna read that over and over again, Ray?"

    menu:

        elise "{color=#00a62c}\"Huh?! Your reading that again? How many times your gonna read that over and over again, Ray?\"{/color}"

        "Your late!":
            jump qt001a

        "Don't worry, I am just reading this to past time.":         
            jump qt001b

        "Well, this is a reminder to myself.":            
            jump qt001c

label qt001a:
        ray "Your late!"
        show elise sad
        elise "Yeah...just like I said I'm really sorry, Also geesh no need to shout."
        ray "Well, I hope you remember the rules and the punishment to anyone whose late."
        jump section2

label qt001b:
        ray "Don't worry, I'm just only reading this to past time."
        show elise happy
        elise "Okay...whatever you say, weirdo hahaha."
        ray "......."
        jump section2

label qt001c:
        ray "Well, this is a reminder to myself."
        show elise happy
        elise "Hahaha, true you should always read that because if you don't you might violate that law hahaha."
        ray "....."
        jump section2

label section2:

    hide elise
    
    play sound "audio/ring.ogg" volume 0.5

    window hide

    show phonecall at truecenter with dissolve

    window show dissolve

    "{i}\"Ray's phone start ringing loudly!\""

    stop sound

    hide phonecall with dissolve

    play sound "audio/punch.ogg"

    zack "GENERAL!!!! The client’s accusation is real!!! I also already gathered some {color=#ff9900}evidences{/color} and {color=#ff9900}recorded the scene{/color}!!!!!!!" with vpunch

    zack "Go to the backside of the gym now!!! Hurry!!! before he do something bad to the client!!!"

    ray "I see, as always good work Major.Zack."

    zack "Ohh really thanks General hahaha!...wait...Please! just hurry up General."

    ray "Don't worry, we will arrive in the scene in no time."

    ray "Lieutenant.Elise! Get ready, we got a case to complete."

    elise "Okay! Just give me a sec. Also! Like I told you don't call me Lieutenant! Geesh!"

    ray "Whatever you say, anyway let’s make a haste Lieutenant.Elise!"

    elise "........"

    scene bg gym
    with dissolve

    play sound "audio/footsteps.mp3"

    "{i}\"Ray and Elise arrived at the scene.\""

    stop sound

    ray "How's the scene? Major.Zack."

    zack "Finally both of you are here! Anyway look overthere!!"

    "{i}Ray and Elise look at the direction his pointing."

    # !Important ~ update the of image Kenneth and Ann Deadly Situation.

    play music "audio/suspense.ogg" fadein 0.5 fadeout 0.5 volume 0.5

    scene black
    with fade

    scene crime
    with fade

    $ renpy.pause(1.0, hard=True)

    voice "audio/kennethLine001.mp3"

    kenneth "Hehehe, Oh come on baby why are you playing so hard to get hehehe..."

    play sound "audio/breathe.mp3"

    "{i}\"Kenneth's breathe heavily through his mouth.\""

    stop sound

    voice "audio/kurtney.ogg"

    ann "Noo!! Please just get away from me! Stop following me!!"

    voice "audio/kennethLine002.mp3"

    kenneth "Hehehe…Ohh come on, don’t you understand! How much I am really obsess to you. Hehehe..."

    voice "audio/kennethLine003.mp3"

    kenneth "I already giving you a lot of hints of how much I love you by {color=#ff0000}staring{/color} at you romantically."

    voice "audio/kurtney.ogg" 

    ann "Please anyone help me!!...."

    play music "audio/Time for Rest.ogg" fadein 0.5 fadeout 0.5 volume 0.5

    scene bg gym
    with fade

    ray "Hmmm….. it seems this man is really desperate."

    zack "Yeah he is also very creepy, we better give him the right punishment General."

    elise "You two! What are you doing?!"

    elise "Just step up to the scene already before this become more worst than it already is!"

    ray "A wise decision, Lieutenant.Elise. I commended you for thinking that."

    elise "Geesh!! Just do something already!!"

    play sound "audio/punch.ogg"

    "{i}\"Elise smack Ray's head." with vpunch

    stop sound

    ray "Aww! I am already planning to do that, calm your nerves Lieutenant."

    $ timeout = 7
    $ timeout_label = renpy.random.choice(['qt002a','qt002b'])

    menu:    
        
        "{i}\"How will you approach the scene?\""
        
        "Approach Aggresively":
            jump qt002a
            
        "Approach Politely":
            jump qt002b

label qt002a:
    "{i}Ray approach the scene aggresively."
    ray "Hold it right there! belligerent scum!"
    jump section3

label qt002b:
    "{i}Ray approach the scene politely."
    ray "Hold it right there! crimi...GOOD SIR!"
    jump section3 

label section3:

    voice "audio/kennethLine004.mp3"

    kenneth "Huhhh?!! How long have you been guys standing there!"

    ray "Hahaha....It seems you are not expecting anyone, Mr.Kenneth Dabert."

    voice "audio/kennethLine005.mp3"

    kenneth "Huhhh?!! How do you know my name! Don't tell me you guys are the student council officers!"

    ray "Hmm... Sorry to disappoint but no you are wrong about that."

    voice "audio/kennethLine006.mp3"

    kenneth "Th-then just tell me who are you guys!!!"

    voice "audio/kennethLine007.mp3"

    kenneth "Also ho...how did you find us here! I am pretty sure no one is following us when we get here."

    ray "Hahaha!! As always, that’s Major.Zack for you. Despite being a airhead, he knowns the right ways to secretly sneak up to his target."

    ray "That’s why I always give you those assignments to secretly investigates potential suspects."

    zack "Hahaha, thanks general."

    elise "Why are you even thanking that idiot, he just call you an airhead you know."

    voice "audio/kennethLine008.mp3"

    kenneth "Sus-suspect!!! You sound like your saying I did something illegal eyy."

    voice "audio/kennethLine009.mp3"

    kenneth "Anyway just tell me! Who are you guys, suddenly treating me as a suspect. What a bunch of bronze players."

    ray "Well my humble apologies for our rudeness, Mr.Kenneth Dabert. I guess before we proceed on this case we should introduce ourselves first."

    ray "Well then Major.Zack, you may now proceed this introduction first."

    zack "Oh I need to introduce myself right? Okay! my name is Major.Zack. Nice to meet you!"

    # !Important ~ add image of Zack Salkelberg showcasing his skills.

    ray "{i}{color=#00a62c}(\"Zack Salkelberg aka Major.Zack, from class 3-C. Despite being a airhead like I mention earlier.\"){/color}"

    ray "{i}{color=#00a62c}(\"Major.Zack has a proficient skills on concealing his presence. Which give him the perfect role for spy mission investigations and also gathering evidence.\"){/color}"

    ray "Thank for that wonderful and simple introduction Major.Zack, as I expected from you."

    zack "Hehehe thanks General."

    ray "Now Lieutenant.Elise, the stage is all yours."

    elise "Okay…fine..Also! How many times you I gonna tell you stop calling me Lieutenant!"

    elise "It’s really embarrassing you know, especially when there are other people around us!"

    elise "Ohh! Sorry about that! My name is Elise Fonillia, A third year student. Please to meet you."

    # !Important ~ add image of Elise Fonillia showcasing his skills.

    ray "{i}{color=#00a62c}(\"Elise Fonillia aka Lieutenant.Elise, from class 3-B.\"){/color}"

    ray "{i}{color=#00a62c}(\"Like many other people say “Don't judge a book by its cover” and that applies to Lieutenant.Elise.\"){/color}"

    ray "{i}{color=#00a62c}(\"She maybe look like a normal highschool student but don’t get fool by that.\"){/color}"

    ray "{i}{color=#00a62c}(\"Ever since I meet Lieutenant.Elise I notice that she has a strenght more than to a six-footer gorilla.\"){/color}"

    ray "Thank you for that wonderful and elegant introductions Lieutenant.Elise."

    ray "Well then ladies and gentlemens, as for the next introduction will be next is....."

    elise "....."

    zack "Go General! Yahoo!!!"

    ray "The last but not the least.....The tactician, the strategist, the mastermind, the leader of the {color=#ff0000}HBB Club{/color}!!..."

    ray "It is I! General.Ray Zealsphere,from class 3-A! at your service!!...."

    zack "OOHH YEAHH!! WUHH HOOO!!! GOO GENERAL!"

    elise "How stupid... I really hate that all high and mighty cocky attitude of yours! I don’t really understand why I even going along with you guys..."

    ray "Don’t say that Lieutenant.Elise, I may be your General but am still a human who got feelings that can be easily shatter like a wine glass."

    voice "audio/kennethLine010.mp3"

    kenneth "HEHEHEHE!!! What the hell!!! HEHEHEHE!!!!..." with vpunch

    voice "audio/kennethLine011.mp3"

    kenneth "You guys are not the student council afterall!!! To be honest I almost got scared....but That's not a problem anymore! Hehehe!!!"

    ray "Hahahaha how foolish of you, we maybe not the student council officers of this school but we still have the right authorities to bring justice to your actions!!"

    ray "Also this student council that you afraid of... let just say that we the {color=#ff0000}HBB Club{/color} might have some connection to them."

    ray "So in case you want to say hello to them,  just ask.\nI could call them anytime you want, Mr.Kenneth Daberth."

    voice "audio/kennethLine012.mp3"

    kenneth "Wha..What do you mean?! In the first place I did not do anything wrong!! Hehehe....that's right!"

    ann "That's not true!!! Mr.Ray please help me!!! Everything I said yesterday with you guys is true."

    ray "Don’t worry, dear client, we hear your humble words that’s why we're here to bring the truth and justice!"

    ray "Major.Zack! Bring me the document files!"

    zack "YES SIR!!!"

    play sound "audio/page.mp3"

    "{i}\"Zack's gave Ray a certain document file.\""

    stop sound

    ray "Hmmm I see, very intriguing I must say."

    voice "audio/kennethLine013.mp3"

    kenneth "Wh-what is that document for huh?! Tell me, is it something to do with me right now HUH?!!!!"

    ray "Hold your horses Mr.Kenneth Dabert. Don't worry I will read this document out loud for you."

    play sound "audio/page.mp3"

    "\"Ray start reading the document.\""

    stop sound

    # !Important ~ add a image of a document about Kenneth Dabert.

    ray "Hmmm I see, Mr.Kenneth Daberth, from class 2-C. Yesterday at 5:27 PM, you got a accusation from this humble lady, she stated here that you been {color=#ff0000}staring{/color} and {color=#ff0000}stalking{/color} her lately."

    voice "audio/kennethLine014.mp3"

    kenneth "Ah..Ahh well so what!!! It’s not like I did something illegal!"

    ray "Well sorry to disappoint you, but you did something illegal and violated a law."

    voice "audio/kennethLine015.mp3"

    kenneth "Huu..Huh?! What are you even saying and kind of law did I even violated in the first place!"

    ray "Mr.Kenneth Daberth, are you perhaps familiar to a law called Republic Act No......"

    ray "......Ahhh..........."

    voice "audio/kennethLine016.mp3"

    kenneth "Huh?! why are you suddenly become silent!!! Just tell me already!!!!"

    elise "Hey Ray, don't tell me you just forgot the law that you almost always reading everyday!"

    ray "No! your mistaken Lieutenant.Elise, Am just trying to ahhh.... mediate! that right, to relax my mind."

    elise "Really I hope your not lying Ray... or else..."

    ray "Hahaha don't worry, I am done mediating now. I will now tell what law Mr.Kenneth Daberth violated."


    $ timeout = 10
    $ timeout_label = renpy.random.choice(['qt003a','qt003b','qt003d'])

label firstQuestion:

    menu:

        ray "{color=#00a62c}(\"This is bad, what is that law No. again?\"){/color}"

        "Re-semiprivate Act 12345":
            jump qt003a

        "Reprivate Act 22244":
            jump qt003b

        "Republic Act 11313":
            jump qt003c

        "Rebuild Act 11202":          
            jump qt003
label qt003a:
        ray "The name of the law that you violated is Re-semiprivate Act 12345!"
        elise "Wait! Ray...are you serious, I told you if your lying...."
        "{i}\"Elise's starting to raise his first.\""
        ray "Wait that was a joke hehehehe.....This time no more jokes okay so calm down Lieutenant.Elise."
        elise "......."
        jump firstQuestion

label qt003b:
        ray "The name of the law that you violated is Reprivate Act 22244!"
        elise "Wait! Ray...what you even saying, I told you if your lying...."
        "{i}\"Elise's starting to raise his first.\""
        ray "Wait that was a joke hehehehe.....This time no more jokes okay so calm down Lieutenant.Elise."
        elise "......."
        jump firstQuestion

label qt003c:
        ray "The name of the law that you violated is {color=#ff0000}Republic Act 11313!{/color}"
        elise "Hmph!! so you actually still remember it. Geesh I almost got a free hit right on his face, how disappointing."
        ray "{i}{color=#00a62c}(\"What! she actually just wants to hit me on my face. Just how much do you hate me Lieutenant Elise.\"){/color}"
        jump section4

label qt003d:
        ray "The name of the law that you violated is Rebuild Act 11202!"
        elise "Wait! Ray...are you even for real! I still remember the law that your trying to say, I told you if you lying...."
        "{i}\"Elise's starting to raise his first.\""
        ray "Wait that was a joke hehehehe.....This time no more jokes okay so calm down Lieutenant.Elise."
        ray "{color=#00a62c}(\"Geesh...if you know the answer just say it.... No as the leader I should be the one to say this.\"){/color}"
        elise "......."
        jump firstQuestion

label section4:

    voice "audio/kennethLine017.mp3"

    kenneth "Republic Act 11369...ahh! Damn!! What does that law even mean!! Are you sure your not making this up!!"

    elise "Come on Ray, be more specific!"

    zack "You got this General!"

    ray "O..Okay calm down everyone, I got this."

    $ timeout = 10
    $ timeout_label = renpy.random.choice(['qt004a','qt004b','qt004d'])

    menu secondQuestion:

        ray "{color=#00a62c}Of course I know this, Republic Act 11313 is also known as....{/color}"

        "Safe Place Act":
            jump qt004a

        "Safe Guard Act":
            jump qt004b

        "Safe Space Act":
            jump qt004c

        "Safe Security Act":
            jump qt004d

label qt004a:
    ray "Well the law you violated is {color=#ff0000}Republic Act 11313{/color}, and it also known as Safe Place Act!"
    zack "Really? I am pretty sure it sounds more like something to do with stars in the galaxy, General."
    ray "Ohh?! Am just joking! Hahaha!"
    elise "....."
    kenneth "Just tell me already!!!"
    jump secondQuestion

label qt004b:
    ray "Well the law you violated is {color=#ff0000}Republic Act 11313{/color}, and it also known as Safe Guard Act!"
    zack "Safe Guard Act? Sounds like something I used to wash my hands after collecting some evidence, General."
    ray "Ohh?! Am just joking! Hahaha!"
    elise "....."
    kenneth "Just tell me already!!!"
    jump secondQuestion

label qt004c:
    ray "Well the law you violated is {color=#ff0000}Republic Act 11313{/color}, and it also known as Safe Space Act!"
    zack "Yeah! That's right, {color=#ff0000}Safe Space Act{/color}! I really like the naming of this law."
    ray "I also agree, Major.Zack."
    jump section5

label qt004d:
    ray "Well the law you violated is {color=#ff0000}Republic Act 11313{/color}, and it also known as Safe Security Act!"
    zack "Safe Security Act? Hmmm? General I feel like that's not the right term as far as I remember."
    ray "{color=#00a62c}(\"What! That's wrong! Am pretty sure that's the right term. I guess am the airhead not Major.Zack.\"){/color}"
    ray "Am just joking! Hahaha!"
    elise "....."
    kenneth "Just tell me already!!!"
    jump secondQuestion

label section5:

    kenneth "Safe Space Act?"

    ray "It seems your not familiar about what is Safe Space Act, Mr.Kenneth Daberth."

    kenneth "Hell if I know!"

    ray "Then if you please, let me enlighten you about what is this {color=#ff0000}Safe Space Act{/color} that am I speaking of."

    kenneth "Hmm! Sure! Why not! It’s not like I did something wrong anyway hehehe!!!"

    ray "Ohh am not sure about. Now then let me start to explain this to you, Good Sir."

    ray "{color=#ff0000}Republic Act 11313{/color} or also known as {color=#ff0000}Safe Space Act{/color}, is a law that has been approved by our president on {color=#ff0000}April 17,2019{/color}."

    ray "Well, according to this law it stated that {color=#ff0000}intrusive leering{/color} and {color=#ff0000}stalking{/color} is a violation to humans rights."

    kenneth "Wh...What the hell!!.. I had no idea...."

    ray "Now then, let me tell you the potential consequences that a guilty party have to face for anyone who violated this law."

    kenneth "...Co..Come ON! tell me! Afterall I didn't do anything wrong!"

    ray "Well, for the {color=#ff0000}first offenders{/color}, violating this law could punish you by a 1000 pesos fine."

    kenneth "What?! you serious bruh?!"

    ray "Also a community service of twelve hours inclusive of attendance to a Gender Sensitivity Seminar to be conducted by the PNP in coordination with the LGU and the PCW."

    kenneth "What?! community service! like I have time for that!"

    ray "Ohh, Also don't get me wrong this punishment I mentions is just for doing violation acts like {color=#ff0000}intrusive learing{/color}..."

    ray "...while the case of doing things like {color=#ff0000}stalking{/color} to someone has more hasher punishment compare to this one like I mention ealier."

    kenneth "!!!!!"

    ray "Hmmm.... it seems you finally have some grasp about what is this law called Safe Space Act."

    ray "Also as I reminder I only mention the punishment for the first offenders, Mr.Kenneth Daberth."

    ray "I wonder what will happen more if you violated this law more, well I only guarantine you that it will be of course become much more worse."

    kenneth ".....heheh...hehhehe....heheheh.....HEHEHEHEHE!!!!!"

    ray "Hmmm? Mr.Kenneth Daberth, are you feeling well right now? It seems you need medical assistance right now."

    kenneth "HEHEHEHE!!! WHERE IS YOUR EVIDENCE THAT I DID THOSE THINGS TO THIS UGLY WOMAN????!!!"

    ann "!!!!"

    kenneth "THIS UGLY WOMAN ACCUSATION IS NOT ENOUGH TO PROVE THAT I REALLY DID THOSE THINGS TO HER!!"

    ray "Well, that’s true Mr.Kenneth Daberth."

    kenneth "GOOD! This is stupid am leaving! Hehehehe...\n{color=#00a62c}(\"GG EZ...hehe...I guess I should go home and play a one match of PoP to forget what happen here. Hehe...\""

    zack "Ahh! His leaving!"

    ray "Hold up! Mr.Kenneth Daberth! You may have the right to remain silent but we have the evidence to prove that your not innocent!"

    ray "So are you sure you wanna leave, or else maybe tomorrow the Student Council might have give you a visit."

    kenneth "!!!!"

    zack "Wait really!!! We have the evidence General?!!!"

    elise "......"

    ray "Hahaha....have you already forgotten, Major.Zack. You mention earlier that you already manage to gathered some evidence for this case."

# Flashback part:
    play sound "audio/flash.mp3"

    scene white
    with dissolve
    
    scene bg flash
    with dissolve

    play sound "audio/ring.ogg" volume 0.5

    "{i}\"Ray's phone start ringing loudly!\""

    stop sound

    zack "GENERAL!!!! The client’s accusation is real, I also already gathered some {color=#ff9900}evidences{/color} and {color=#ff9900}recorded the scene{/color}!!!!!!!" with vpunch

    play sound "audio/flash.mp3"

    scene white
    with dissolve

    scene bg gym
    with dissolve

    zack "Oh yeah! I finally remember I did in fact gathered some evidences!...but..."

    ray "But what? Major.Zack."

    zack "General, Well its true I manage to gathered a lot of evidences here right now in my evidence pouch archive."

    ray "Hahaha, That's good to know Major.Zack, you are really doing your job properly. I respect that."

    zack "Haha.. Thanks General, but the my problem right now is that I don't know the evidence you want me to present right now."

    ray "It’s fine Major.Zack, that’s one of your flaws but I understand. But don’t worry, be reasure because I got you covered."

    ray "Afterall, if your job is to spy and gathered some evidences. Then my job is to used those information you gathered to show and revealed them the truth and justice."

    zack "Wow, that's awesome General!"

    elise "Hmph! How stupid you guys are."

    ray "Hoo? Don't worry Lieutenant.Elise, soon you will get your moment to shine."

    elise "....."

    kenneth "HEY!! YOU GUYS STOP FOOLING AROUND!! JUST SHOW ME THAT EVIDENCE YOUR TALKING ABOUT!!"

    zack "General! Hurry! What evidence you want me to present?!"

    ray "Well then, I will tell you the evidence that will prove that Mr.Kenneth Daberth did in fact is not innocent!"

    kenneth "COME ON SHOW ME!!!"

    ray "Major.Zack, show me all the evidences that you manage to gathered!"

    zack "Yes SIR!!!"

    "{i}\"Zack shows you all the evidence he gathered.\""

    ray "{color=#00a62c}(\"Haha...as always Major.Zack. Some of the things here are not even could be consider as evidence for this case. Some are just trash!\"){/color}"

    ray "{color=#00a62c}(\"Well okay then, Time to show the culprit the evidences!\"){/color}"

label evidence:
    
    $timeout = 10
    $timeout_label = renpy.random.choice(['ed001a', 'ed001b','ed001c'])

    menu: 
        
        ray "{color=#00a62c}(\"Let's see here, What evidence I should show to prove Mr.Kenneth Daberth is not innocent.\"){/color}"

        "{image=peel.png}\nBanana Peal":
            jump ed001a

        "{image=wrapper.png}\nCandy Wrapper":
            jump ed001b

        "{image=leaf.png}\nLeaf":
            jump ed001c

        "{image=phone.png}\nZack's Phone":
            jump ed001d

label ed001a:
    ray "The evidence that will prove you guilty Mr.Kenneth Dabert is this {color=#ff9900}BANANA PEEL{/color}!!!"
    kenneth "BANANA PEEL?! HAHAHA!! HOW DOES IT WILL EVEN PROVE AM NOT INNOCENT EYY!!! STUPID BRONZE PLAYER!!!"
    elise "Hey! Are you trying to mess with me huh?! RAY!!"
    ray "No..Noo am just showing the banana peel, afterall it look kinda delicious! But too bad it looks like someone already ate it."
    elise "....."
    ray "{color=#00a62c}(\"I...I better show the evidence real quick before Lieutenant.Elise might do something!!\"){/color}"
    jump evidence

label ed001b:
    ray "The evidence that will prove you guilty Mr.Kenneth Dabert is this {color=#ff9900}CANDY WRAPPER{/color}!!!"
    kenneth "A CANDY WRAPPER YOU SAY! How..NOOO I DIDN\'T SHOPLIFTED ANY CANDIES OKAY!!!"
    elise "Hey! What the are you doing?! Show the evidence already!"
    ray "Hahaha...I am just joking this time, Now I will show you the real evidence."
    elise "......"
    ray "{color=#00a62c}(\"I...I better show the evidence real quick before Lieutenant.Elise might do something!!\"){/color}"
    jump evidence

label ed001c:
    ray "The evidence that will prove you guilty Mr.Kenneth Dabert is this {color=#ff9900}LEAF{/color}!!!"
    kenneth "NO!! YOUR WRONG! I DON\'T SMOKE LEAF!!!"
    zack "AHA! General! This guy is a drug user!!!"
    ray "Hahaha...I don't think so Major.Zack."
    zack "Huh? Ohh your just joking again right General, Hahahaha."
    elise "......"
    ray "{color=#00a62c}(\"I...I better show the evidence real quick before Lieutenant.Elise might do something!!\"){/color}"
    jump evidence

label ed001d:
    ray "The evidence that will prove you guilty Mr.Kenneth Dabert is this {color=#ff9900}MAJOR.ZACK'S PHONE{/color}!!!"
    zack "What! Ohhh yeah... I remember I recorded some scene when this criminal is doing some bad things to our client General."
    elise "Huh?! Are you even serious, Zack. Why did you not just stop this creep already when he doing some bad things to our client."
    zack "Ahh! Well I think its for the best to gathered some evidence instead because even if I tell this criminal to stop he won't listen...Also am scared to stop him alone haha.."
    zack "Also am pretty sure he will just find another moment again to do some bad things again to our client. So I guess its better to follow the General's Order."
    elise "HUH?! Your kidding right! Do you even call yourself a man!"
    zack "Sorry maybe I did the wrong action afterall, I guess I should stop him before even I don't have the strenght like a goril...."
    ray "SILENT!! Major.Zack! I understand what your trying to say. But sometimes, there are times you really need to step up before its to late, remember this. "
    zack "Wow, that sounds amazing, okay copy that General! I will take a note about this."
    elise "....don't have the strenght like a goril..what are you even trying to say Zack, could you just say it again this idiot suddenly interrupted you."
    ray "THAT'S! enough for talk now Lieutenant.Elise. We still need to prove why Zack's Phone is the reason why Mr.Kenneth Daberth is guilty."
    elise "....."
    jump section6

label section6:

    kenneth "YEAH! YOU GUYS STOP FOOLING AROUND ALREADY! WHY IS THAT PHONE IS THE EVIDENCES EYY?!! I STILL HAVE A DATE TO ATTEND SOON!! HURRY UP!!!"

    ray "Sorry about that Mr.Kenneth Daberth I guess you have to cancel that date, though I highly doubt it."

    ray "Well the reason why Zack's Phone is the evidence that will prove you guilty is already obvious."

    ray "And I am pretty sure you already know it."

    kenneth "!!!!...NO I DON'T KNOW!!!"

    ray "Okay, then let's ask Major.Zack."

    zack "Need something? General."

    ray "Let me ask you, do you remember the phone call we had ealier. Do remember that you mention that you recorded the some scene right."

    zack "Ohh yeah, I almost forget that I recorded him lately for evidence while this criminal has been desperately {color=#ff0000}stalking{/color} and {color=#ff0000}staring{/color} the client."

    ray "Okay then, let's play that video."

    "{i}\"Zack play the video he recorded on his phone.\""

    # !Important ~ Add a image of Kenneth Daberth stalking and staring activities.

    kenneth "NOOO!! BUT HOW?! I AM REALLY PRETTY SURE NO ONE IS AROUND US."

    ray "Hahahahah, as always good work Major.Zack, not even the slightless I doubt your work. {color=#00a62c}(\"Phew...thank god, He actually managed to record a scene for evidence.\"){/color}"

    zack "Thank you GENERAL!!!"

    ray "Well are you satisfied now Mr.Kenneth Daberth or will you still deny your actions. If that's the case then am telling you this will become much more worse for you, Good Sir."

    ray "Hmm??"
    
    kenneth "Hooo...Hooyoyoyoyoyo...This is BAD!!!!!! MY MOTHER WILL SPANK MY ASS AT THIS RATE IF SHE FIND OUT WHAT I DID!!!"

    elise "Hahahahaha!!!....Ahh sorry...."

    ray "Mr.Kenneth Daberth, based on the investigation and evidence it seems the verdict is clear. I guess it's about time to wrap this thing up."

    ann "Finally....."

    $ timeout = 7
    $ timeout_label = renpy.random.choice(['qt005a','qt005b'])

    menu verdict:

        "{i}\"Is Mr.Kenneth Daberth {color=#ff0000}Guilty{/color} or {color=#ff9900}Innocent{/color}\""

        "Guilty":
            jump qt005a
        "Innocent":
            jump qt005b

label qt005a:
    ray "Mr.Kenneth Daberth, YOU ARE FOUND GUILTY!!! The court is now adjourned."
    kenneth "NOOO!!!!!!" with vpunch    
    jump section7

label qt005b:
    ray "Mr.Kenneth Daberth, congratulation you won the case. You are found innocent. The court is now adjourned."
    kenneth "WHAT!! REALLY!!!...I thought am busted already....."
    elise "RAY!!!! STOP JOKING AROUND!!! ARE YOU REALLY GONNA LET A CRIMINAL ESCAPE!!!!"
    "Elise smack Ray's Head." with vpunch
    ray "AWWW!!! I'M SORRY!! OKAY!! OKAYY!! THIS TIME I WILL NOT MESS AROUND!!!"
    ray "{color=#00a62c}(\"Okay....No more messing around this time I will tell the truth.\")"
    jump verdict

label section7:

    ray "And lastly, this case is COM!!...."

    zack "General!!!!!! The suspect is escaping!!!!!!!"

    ray "Ahhh! Right when I finally able to say my favorite line!!! This man deserve a harsh punishment!!! Lieutenant Elise, requesting for back-up!"

    elise "Geeshh! Am already here what are you even talking about. Anyway, I got this. Zack hand me that {color=#ff9900}Banana Peel{/color} in your evidence pouch or whatever you called that bag is."

    zack "YES MAAM!"

    # !Important ~ Add a image of Kenneth Daberth escaping desperately.

    kenneth "I BETTER RUN FAST!!!!, IMAGINE!!! IMAGINE IT!!! LIKE AM USING THE SKILL FLASHSTEPPPP LIKE IN THE GAME of PoP!!!! HEEHEHEHEH!!!!!!! I CAN FEEL IT!!!! I AM RUNNING SO FAST YAHOO!!!!! I WILL ESCAPE THIS IN NO TIME!!!"

    zack "Wow...his really fast!!!"

    ray "Hmm...his already about approximately 52 meters away from us."

    elise "Don't worry I got this, Even his already in the other side of the planet I can still throw this {color=#ff9900}Banana Peel{/color} in front of his feet to lose his balance."

    ray "Hmph! Hahaha! True, I never doubt your strenght Lieutenant.Elise. Afterall you have more strenght than a 6-footer gorilla. AHH!"

    ray "{color=#00a62c}(\"Damnn!!..I can't believe I say that out loud. I hope she doesn't heared me......\"){/color}"

    # !Important ~ Add a image of Elise Fonillia throwing a banana peal.

    elise "TAKE THIS!!!!!!"

    kenneth "AWWWW MAMA DON’T HIT MEE!!!!!"

    ray "It seems the culprit is already experiencing the punishment of what he did."

    ray "I guess the time has come."

    zack "YES SIR!"

    elise "......."

    play sound "audio/punch.ogg"

    ray "THIS CASE IS COMPLETE {color=#00a62c}(\"Yeah finally hahaha...\"){/color}" with vpunch

    stop sound

    ann "Ahh excuse meee Ahh Mr.Ray and everyone, thank you very much for helping me."

    ray "No worries, it’s our duty to help our people, right everyone?"

    zack "YES SIR!!"

    elise "......."

    ray "Ahhh Lieutenant.Elise? Somethings wrong? You seems awfully quiet.... are you perhaps already hungry?"

    elise "Ray.... how many times do I have to tell you don't call me Lieutenant, but still you won't listen and NOW!!!..."

    ray "heyy....calm down...."

    elise "AND NOW! You just compare me to a GORILLA!!!!"

    ray "ohhh….ohhhhh come on Lieutenant.Elise, Am just joking you know."

    ray "Afterall a leader must also show his humor sometimes to his subordinates right? right Major.Zack?"

    zack "YES SIR!!!"

    ray "Is that the only thing you can say right now!! At least say something else, I also save your sorry ass earlier."

    zack "YES SIR!!!! Thank you very much for saving me!!!"

    elise "......"

    ann "Ahh excuse me.....to be honest looks like Mr.Ray also need to get punished for verbally abusing Miss.Elise."

    ray "WH..WHAT I JUST HELP YOU! YOU KNOW! ATLEAST SHOW SOME GRATITUDE!"

    ann "sor..Sorry!!!....Please don't hit me!!!"

    elise "....RAAYY!!!!"

    "{i}\"Elise slowly approach Ray intensely.\""

    ray "Hey calm down Lieutenant.Elise! Anyone please help or alteast somebody stop her!! CALL THE ANIMAL CONTROL DEPARTMENT!! PLEASE!!! AHHHHH!!!"

    "{i}\"On that day, all the students heard a short loud scream throughout the campus.\""

    ray "AH!.................................................."

    "{i}\"And that's the only beginning of the HBB Club story.\""

    scene black
    with fade

    centered "END...."

    # This ends the game.

    return
