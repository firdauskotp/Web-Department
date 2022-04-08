
#define convos
define f = Character("Firdaus", color="#ce291d", what_color="#ce291d")
define n = Character("Nasrin", color="#ce1dce", what_color="#ce1dce")
define a = Character("Ahmed", color="#1bb2d8", what_color="#1bb2d8")
define p = Character("[player_name]")
define w = Character("Waiter")

#define locations
image school_class = im.Scale("locations/class.jpg",1920,1080)
image coffee = im.Scale("locations/coffeeshopfront.jpg",1920,1080)
image field = im.Scale("locations/field.png",1920,1080)
image cafe = im.Scale("locations/rasel-cafe.jpg",1920,1080)
image school = im.Scale("locations/School-Gate.jpg",1920,1080)
image error = im.Scale("codes/result.png",1920,1080)

#define location with sprites

#firdaus
image fhc = im.Scale("port_loc/fird_happy_cafe.png",1920,1080)
image fnc = im.Scale("port_loc/fird_neutral_cafe.png",1920,1080)
image fsc = im.Scale("port_loc/fird_smile_cafe.png",1920,1080)
image fskc = im.Scale("port_loc/fird_smirk_cafe.png",1920,1080)

#firdaus with drinks
image fhcd = im.Scale("port_loc/fird_happy_cafe_drink.png",1920,1080)
image fncd = im.Scale("port_loc/fird_neutral_cafe_drink.png",1920,1080)
image fscd = im.Scale("port_loc/fird_smile_cafe_drink.png",1920,1080)
image fskcd = im.Scale("port_loc/fird_smirk_cafe_drink.png",1920,1080)

#nasrin
image ncc = im.Scale("port_loc/nasrin_confused_class.png",1920,1080)
image nhc = im.Scale("port_loc/nasrin_happy_class.png",1920,1080)
image nsc = im.Scale("port_loc/nasrin_smile_class.png",1920,1080)

#define nasrin sprites
image ns = "nasrin/nasrin_smile.png"
image nc = "nasrin/nasrin_confused.png"
image nh = "nasrin/nasrin_happy.png"

#define ahmed sprites
image ah = "ahmed/ahmed_happy.png"
image an = "ahmed/ahmed_neutral.png"
image asc = "ahmed/ahmed_scowl.png"
image asm = "ahmed/ahmed_smile.png"

#define firdaus sprites
image fh = "fird/fird_happy.png"
image fn = "fird/fird_neutral.png"
image fsmile = "fird/fird_smile.png"
image fsmirk = "fird/fird_smirk.png"

#define variables
default var_name = 0
default var_name_times = 0
default firdaus_hobbies = 0
default firdaus_checker = 0
default nasrin_checker = 0
default ahmed_checker = 0
default firdaus_first_event_checker = 0
default nasrin_coding = 0
default firdaus_telegram = 0
default gender = ""
default final_trio = 0

label start:


    scene school with dissolve

    play music "audio/Mattari.mp3" fadein 3.0 volume 0.5


    show ns:
        right

    n "Good day!"

    n "May I know your name?"

    while var_name==0:

        $ player_name = renpy.input("Please input your name")
        $ player_name = player_name.strip()

        if player_name == "":
            hide ns
            show nc:
                right

            p "Good day! My name is [player_name]"

            n "Are you sure? Or maybe you forgot to input your name"
            p "Oops, let me try again"

            $ var_name_times +=1
            
        else:
            hide nc
            show ns:
                right

            $ var_name = 1

    p "Good day! My name is [player_name]"

    if var_name_times >0:
        hide ns
        show nh:
            right

        if var_name_times == 1:
            n "Well, that took you around [var_name_times] try!"
        else:
            n "Well, that took you around [var_name_times] tries!"

        p "Sorryyyy"

        n "It's okay"

        hide nh
        show ns:
            right

    else:
        hide ns
        show nh:
            right

        n "That's a nice name! Nice to meet you!"

        p "Thank you! Nice to meet you too!"

        hide nh
        show ns:
            right

    n "May I also know your gender?"

    menu:
        "Male":
            $ gender = "male"
        "Female":
            $ gender = "female"

    n "My name is Nasrin, I am a manager of Kidocode's Web Department"

    p "A manager?"

    n "Yes, we have three managers for this department including myself"

    n "The other two are Ahmed and Firdaus"

    p "Aren't their pictures supposed to be sliding in somewhere here during introduction?"

    hide ns
    show nc:
        right

    n "Yeappp but they are in different places now"

    p "Ahh, makes sense"

    hide nc
    show ns:
        right

    n "Anyways, we will be explaining to you about the web department, and some of our speciality"

    p "Not all of it?"

    n "That will take a long time, and will be better to be discussed face to face, or virtually face to face"

    p "Hmm, true. Even with an overview, I get to know what the department is about"

    hide ns
    show nh:
        right

    n "Indeed!"

    n "Now, it is your turn, [player_name], to pick which manager you wish to talk to"

    menu:
        "Nasrin":
            n "Alright, please meet me in the class 5-A"

            p "Got it!"

            jump lblNasrin
        "Firdaus":
            n "Firdaus will be at the coffee shop on the right from here"

            p "Ahh, he likes coffee it seems?"

            n "A lot!"

            p "Interesting... Wait, may I have a picture of him?"

            n "Nah, no need. He is obvious to spot. He always wears a jacket and almost everything black"

            p "In this hot weather?"

            n "Especially in this hot weather"

            jump lblFirdaus
        "Ahmed":
            n "Ahmed will be at the football pitch on the left from here"

            p "Oh he plays football?"

            n "Yeah, and he is mainly setting it up for a colleague event there"

            p "Wow, I want to go have a look!"

            n "Alright, here is a picture of him."

            jump lblAhmed

        "End":

            stop music fadeout 3.0

            play music "audio/DFInstrumental.mp3" fadein 3.0 volume 0.5
            p "I'm sorry but I gotta go for now, I might have a more thorough look in the future"

            n "It's okay, take care of yourself, and never stop learning!"

            p "Thank you!"

            return

    

    #labels

    label lblNasrin:
        if nasrin_checker == 1:
            stop music fadeout 3.0
            play music "audio/fe3hteatime.mp3" fadein 3.0 volume 0.5
            jump label_Nasrin_Chat

        stop music fadeout 3.0
        play music "audio/Fire Emblem Awakening OST - Conquest.mp3" fadein 3.0 volume 0.5

        scene school_class with dissolve

        p "Hmm"

        scene nsc

        n "Class is in session!"

        p "YIKES"

        scene nhc

        n "That scared you? Ahaha"

        p "I am having flashbacks"

        n "Hahaha"

        p "Please don't do that again"

        n "Hehehe"

        n "So, now that we are here, are you ready to start your class?"

        p "For...?"

        n "You need to take an exam before getting selected to be an intern!"

        p "No way..."

        n "Yes you do! Okay, is HTML a programming language?"

        menu:
            "Yes":
                scene ncc
                n "You failed"
                p "What? Why?"
                n "HTML IS A MARKUP LANGUAGE!"
                n "NOT A PROGRAMMING LANGUAGE"
                p "Oh... I forgot"
                n "Doesn't matter, you failed"
            "No":
                scene nsc
                n "Good, you found out the trick!"
                p "Yeahh, it is a markup language"
                n "Indeed, but you still fail"
                p "Why?!"
                n "Why not?"
        scene nsc
        n "Just kidding, there is no such test"
        p "0-0"
        scene ncc
        p "Q_Q"
        p "T_T"

        n "Can you stop overreacting?"
        p "Okay :<"
        scene nhc
        stop music fadeout 3.0
        n "Alright, now, may I ask"
        p "Yes?"
        play music "audio/fe3hteatime.mp3" fadein 3.0 volume 0.5
        n "What questions do you have for me?"
        jump label_Nasrin_Chat





    label label_Nasrin_Chat:
        menu:
            "Can you give a brief introduction about yourself?":
                n "Sure"
                n "My name is Nasrin, I have been in KidoCode for a long time. I am the Senior Software Developer here"
                p "Wow...so you are not a trainer?"
                n "Nope!"
                p "Wow, I see."
                scene ncc
                n "See...what?"
                if firdaus_checker == 1 and not ahmed_checker == 1:
                    p "Why Firdaus calls you boss"
                    n "Please, don't take over his habit."
                elif ahmed_checker == 1 and not firdaus_checker == 1:
                    p "Why Ahmed refers to you as boss"
                    n "He is the one that started this whole trend"
                    p "It is a good compliment though"
                    n "I guess"
                elif firdaus_checker == 1 and ahmed_checker == 1:
                    p "Why both the guys call you boss"
                    n "Ahh...yes. Please just don't take over their habit"
                    p "It is a good compliment though"
                    n "Yeah...I guess. But still, don't continue the trend"
                    p "I'll try not to"
                else:
                    p "That you are a master of coding!"
                    n "Not really, no"
                    p "Yes you are!"
                    n "Sigh"
                scene nhc
                n "Anyways"
                p "(She just shrugged it off)"
                n "I am one of the managers of the Web Department"
                n "I hope to see you here one day!"
                p "Hopefully!"
                p "But can you tell me the programming languages and how you get good at them?"
                n "I can, but not on this option!"
                p "Alright, I'll have a look at the other options"
                n "But... I will give a spoiler"
                p "That is"
                n "My advice for being good in programming is pretty cliché"
                p "Will it be useful?"
                n "Of course, don't worry!"
                scene ncc
                n "Hmm what else..."
                p "I am thinking as well."
                p "Hmm... Maybe..."
                p "What's your favourite beverage?"
                scene nhc
                n "Brilliant idea!"
                n "Are you listening to this song?"
                p "Yeah, what's wrong with it?"
                n "Well, this song is from Fire Emblem Three Houses."
                n "This track plays during some specific events, but from the title itself, you will know what is my favourite beverage!"
                p "You expect me to search the entire soundtrack for it?"
                n "Yep!"
                p "Sigh"
                

                $ nasrin_coding = 1
                jump label_Nasrin_End_Convo
            "Purpose of Web Department":
                n "Well, a number of things, really"
                n "Firstly, we want to encourage people to study more on web development"
                p "I see, how is that usually?"
                n "Well, we have workshops!"
                p "Workshops?"
                n "Yeah, usually carried out by each of us managers or some members of the web department"
                scene nhc
                n "It is free, and we try to engage with the participants as much as we can!"
                p "That sounds interesting!"
                n "Yeah, you can enjoy the recordings of the workshop as well"
                n "So far we have a few workshops already like React, Telegram bot and web development as well as serverless application"
                p "That is a lot!"
                n "Indeed! And they also contribute to us in terms of questions"
                p "Questions?"
                n "Yeah, our department is also creating question for students"
                n "The students are related to web development, like HTML, CSS, JS"
                p "Ahh, so I can contribute a lot by joining?"
                scene nsc
                n "Indeed, you can ^_^"
                n "And who knows"
                n "You might be able to make your own workshop as well"
                n "I can't wait to participate in it if I have free time"
                p "Alright, and I would like to join all three managers' workshops as well!"
                n "That's the spirit"
                n "And overall, our community is pretty helpful"
                n "If any issues occur, don't hesitate to ask your teammates or the managers"
                n "We are always ready to help!"
                p "That is good to hear. Now I know I won't be targeted"
                scene nhc
                n "Ahaha of course you won't"
                n "Unless of course you really screw up"
                n "Just joking"
                scene ncc
                n "Unless..."
                p "0-0"
                jump label_Nasrin_End_Convo
            "What is your specialty?":
                n "Well..."
                p "Well..."
                n "There's a lot! But I can name some of them"
                p "Sure"
                n "I am mainly a fullstack developer"
                n "Do you know what that means?"
                menu:
                    "Yep...wow!":
                        p "How are you that good in both front-end and back-end development!"
                        scene nsc
                        n "You need to see another option of mine!"
                        p "I see..."
                    "Not really...":
                        n "It means I know more of front-end and back-end development"
                        n "Meaning both the interface and the logic that processes the data of the application"
                        p "Wow..."
                scene nhc
                n "Mainly I am good in Python and JavaScript"
                n "But I am also good in MongoDB and Firebase. Also, serverless applications!"
                p "Wha..."
                n "MongoDB and Firebase are more to database. Serverless is..."
                n "Well, imagine running an application on cloud!"
                p "Wait, so not on local?"
                n "Nope, there is no need to manage servers. Just build and run the applications!"
                n "But contrary to the name, there are still servers but they are abstracted away from the development"
                p "What? How?"
                n "Haha, you can search more about it"
                n "{a=https://www.serverless.com/}Here is a resource for you. This is a clickable message. {/a}"
                p "Thanks"
                n "I also know about Telegram bots"
                if firdaus_telegram == 1:
                    p "I see, same with Firdaus?"
                    n "Yeah, but he uses a different API called Telepot, I use Python-Telegram-Bot"
                    n "But most of the expected output is the same"
                    p "I see"
                else:
                    p "I see, that is interesting"
                if nasrin_coding ==1:
                    p "You really are a master!"
                    scene ncc
                    n "Please stop it, [player_name]"
                jump label_Nasrin_End_Convo
            "Any advice?":
                stop music fadeout 3.0
                play music "audio/Ryūtarō Naruhodō ~ Objection! 2017 - The Great Ace Attorney 2 Music Extended.mp3" fadein 3.0 volume 0.5
                scene nhc
                n "Well, you may have heard it a thousand times before. But practice. Practice makes perfect!"
                if nasrin_coding == 1:
                    p "Yeah but can I really master coding like you from practice only?"
                    scene ncc
                    n "I am not really a master in that"
                    p "Yes you are, you're the boss"
                    n "Please don't let me get started on that..."
                    n "Anyways"
                    scene nhc
                else:
                    p "Can practicing really make me master coding?"
                n "It depends on how you practice!"
                p "How..."
                n "Well, you need to read the documentation first!"
                p "Is it really important to read the documentation when I can do the coding on the go? Then search for the errors or methods?"
                scene ncc
                n "Well, you can but... Imagine this"
                n "You are stuck on a problem, you spend your time googling for the solution."
                n "But if you read the documentation beforehand, you already know the solution, and can move on with the code"
                p "It saves time until the point I really need help, right?"
                scene nsc
                n "Indeed!"
                n "It is important to practice the coding as well a lot. What I mean by this is involve yourself in projects."
                n "Sometimes reading only will not let you understand the full concept."
                n "You need to apply what you have learnt."
                n "And don't think about failure. It is normal."
                p "Normal?"
                n "You need to fail to succeed."
                p "I never really understand, why is it like that?"
                n "Well, mainly because once you fail, you know how it fails, and you know how to overcome it!"
                n "That is why troubleshooting and debugging are two imporant aspects in development!"
                p "I see, I never thought of it that way..."
                n "And another thing is, sometimes it is better to ask someone more experienced as well."
                p "But everything is online."
                n "Yes, but having a teacher will make what you are learning way easier. You can directly learn instead of having to search for some answers online that might not solve your problem."
                p "That is true."
                p "I guess I need all the resources I can get"
                n "Never burn out your passion on learning something new, it is really important for you to grow"
                p "I will keep that in mind as I continue learning my development."
                n "Great! I hope to see you on the big stage some day!"
                p "I won't disappoint you!"
                if nasrin_coding == 1:
                    p "But..."
                    n "Yes?"
                    p "I really want to see you guys in action!"
                    scene ncc
                    n "Sorry?"
                    p "How you are a master in coding, how Firdaus and Ahmed are able to help"
                    p "I want to see it"
                    if firdaus_checker == 1 and ahmed_checker == 1:
                        n "Are you sure you want to see us in action?"
                        menu:
                            "YEAH":
                                $ final_trio = 1
                                n "Maybe if you meet some of the requirements, you can"
                                p "Hmm... I see"
                            "On second thought...":
                                $ final_trio = 0
                                n "I thought so."
                                p "Sorry :/"
                                scene nsc
                                n "No worries!"
                    else:
                        scene nsc
                        n "Sorry, you are not worthy yet!"
                        p "Sorry?"
                        n "You need to complete some requirements with both Firdaus and Ahmed first to access this"
                        p "What are they?"
                        n "If I tell you, it wouldn't be a hard earned scene!"
                        p "I guess that is true..."
                stop music fadeout 3.0
                play music "audio/fe3hteatime.mp3" fadein 3.0 volume 0.5
                jump label_Nasrin_End_Convo


            "Your socials":
                n "I don't really show my socials. But for professional ones..."
                n "{a=https://my.linkedin.com/in/nasrintohidi}Here is my LinkedIn{/a}"
                n "Feel free to connect there"
                p "Thank you!"
                n "{a=https://github.com/ntohidi}Here is my GitHub as well!{/a}"
                p "Got it, thanks again!"
                n "No problem!"


            "That is all":
                $ nasrin_checker = 1
                scene nhc

                n "Alright, what's your next step, [player_name]?"
                menu:
                    "Meet Firdaus":
                        if firdaus_checker == 0:
                            n "Firdaus will be at the coffee shop from the right of the school"

                            p "Ahh, he likes coffee it seems?"

                            n "A lot!"

                            p "Interesting... Wait, may I have a picture of him?"

                            n "Nah, no need. He is obvious to spot. He always wears a jacket and almost everything black"

                            p "In this hot weather?"

                            n "Especially in this hot weather"
                            jump lblFirdaus
                        else:
                            n "Fird should still be in the cafe"
                            p "Why does he always wear that jacket though"
                            n "It's just the way that he is. Along with that coffee addiction of his"
                            p "Okay..."
                            jump lblFirdaus
                    "Meet Ahmed":
                        if ahmed_checker == 0:
                            n "Ahmed will be at the football pitch on the left of the school"

                            p "Oh he plays football?"

                            n "Yeah, and he is mainly setting it up for a colleague event there"

                            p "Wow, I want to go have a look!"

                            n "Alright, here is a picture of him."

                            jump lblAhmed

                        else:
                            n "Ahmed should still be at the football pitch. How is his progress with the event though?"
                            p "He got the items but...you know"
                            n "He is alone isn't he?"
                            p "Yeah..."
                            scene ncc
                            n "Well, what do you expect when we have to stay in our respective ports haha"
                            p "True..."
                            if firdaus_checker == 1:
                                p "Firdaus is still on his coffee break as well"
                                n "You can expect him there till tomorrow I guess"
                                p "0-0"
                            jump lblAhmed

                    "I think that's all from me, thank you!":
                        n "Alright, it's time we go to the ending!"
                        jump lblEnd

    label label_Nasrin_End_Convo:
        scene nhc
        n "Do you have any other questions?"
        jump label_Nasrin_Chat
                


    label lblFirdaus:
        if firdaus_checker == 1:
            stop music fadeout 3.0
            play music "audio/09 _ Asougi Kazuma - Samurai With A Mission (Dai Gyakuten Saiban Soundtrack).mp3" fadein 3.0 volume 0.5
            jump label_Firdaus_chat

        stop music fadeout 3.0
        scene coffee with dissolve
        play music "audio/BakerStreet.mp3" fadein 3.0 volume 0.5

        p "Where is he? Has he entered the cafe?"

        p "Might as well wait a bit longer"

        p "Wait a second, I think I spot someone almost entering"

        show fn with moveinright:
            center

        p "Hmm, matches the description"

        p "Excuse me"

        hide fn
        show fsmile:
            center
        f "Yes?"
        p "Are you the web department manager?"
        hide fsmile
        show fsmirk:
            center
        f "Seeing as how you approached me I guess one of the other trainers gave a very...detailed explanation on my appearance?"

        p "Yeah"

        f "Lol. Anyways, you must be [player_name]?"

        p "Yeppp"

        f "Alright, let's go in the cafe and discuss further"

        stop music fadeout 3.0
        scene cafe with dissolve
        play music "audio/BakerStreet.mp3" fadein 3.0 volume 0.5

        f "Alright, let's have a seat!"

        hide fh
        scene fhc

        f "Don't be shy, order anything you want"
        p "I never ordered here before"
        f "Alright, it's okay. I'll order for you"
        f "Waiter, can we get two large coffee fraps? And don't go easy on the caffeine!"
        w "The usual eh? Sure..."
        p "0_0"
        f "You will enjoy that drink"
        p "I won't be enjoying sleeping and the price!"
        
        scene fskc

        f "Yeah, considering you are going to have to pay for me too, since you want to talk to me about the department"
        p "WHAT?!"

        scene fhc
        f "Hahaha it's a joke, relax"
        p "How should I know, I never met you before!"
        f "Ahahaha"

        scene fsc
        f "Is that our order?"
        w "Yes Fird, this is your order."

        scene fhc
        f "Wohoo, thanks Ad.."
        w "No saying my name on this public game, please"

        scene fnc
        f "Oh, sorry"
        w "It's alright, anyways here are your drinks!"
        
        scene fscd
        f "Thanks!"
        p "Thank you ^_^"
        w "Alright, I'll leave you two. I guess this is another meeting"
        p "Wait... how did you?"

        scene fncd
        stop music fadeout 3.0
        f "Not important yet"
        w "He always ask people to have a meeting with him here as an excuse for coffee"
        f "OIIII"
        play sound "audio/Venti's ehe.mp3"
        w "Ehe I'll leave now"
        p "0-0"

        f "Anyways, now that the coffee is here. It is time..."
        p "Time for..."
        f "You want to meet me to ask me some questions right?"

        scene fhcd
        play music "audio/09 _ Asougi Kazuma - Samurai With A Mission (Dai Gyakuten Saiban Soundtrack).mp3" fadein 3.0 volume 0.5


        f "Now is the time, ask me any question that comes to mind!"

        jump label_Firdaus_chat

    label label_Firdaus_chat:

        menu:
            "Can you give a brief introduction about yourself?":
                scene fncd
                f "I can, but nah"
                p "Why?"
                f "Private"
                p "Alright..."
                scene fskcd
                f "Just kidding"
                p "Do you always make jokes like that?"
                f "Most of the time! Anyways, I'll answer your question briefly"
                p "(So he does not want to disclose personal information)"
                f "My name is Firdaus. I have been in KidoCode since 2018. I started as an intern here"
                p "An intern eh?"
                scene fhcd
                f "Yeah, I was an intern here. Then I became a part timer and sometimes full time here"
                p "Why did you switch between being a part timer and full timer?"
                f "Because I was still studying haha"
                p "0-0"
                scene fncd
                f "Wassup?"
                p "Don't you feel tired multitasking?"
                scene fhcd
                f "Lol"
                p "Why are you laughing?"
                f "I have a few people asking me that haha"
                f "Well, it depends on how you manage your time. I had moments where I even worked or interned while working here"
                p "You don't feel tired?"
                f "Not really, mostly because I love what I am doing. But sometimes you need your break as well haha"
                p "I...see..."
                f "Remember that time management is key. Master that, and you can master multitasking"
                p "Thanks"
                f "Hmm, what else do I introduce? Ahh, yes. I used to study computer engineering. But best part, I came from a pure science background"
                p "What made you pursue programming then? And how did you cope?"
                f "I have passion for programming since I was a teenager, but don't really have the exposure. Hence when I entered uni, I tried researching more about programming"
                p "Ahh I see"
                f "The best part is I have some friends who helped me along the way, too many to name them. They are like my companions, my allies in battle"
                p "Wow, they really mean that much to you?"
                f "Yeahh, also it is important to have people like that to motivate you further"
                f "And the most important, study for knowledge, not for grades"
                p "There's a difference?"
                scene fskcd
                f "Yeahh, there is. If you study for grades, you will not enjoy what you are learning, and you may forget them"
                p "And if I study for knowledge, I will understand more and want to learn more?"
                f "Exactly. This world has a lot of things to be studied. Programming is just the same, the more we study, the more there is to study, the more we want to study"
                f "That is how innovation comes, new devices, new programming languages, new developments"
                f "The possibilities!"
                p "Wow, that is...amazing"
                f "Indeed!"
                $ firdaus_hobbies = 1
                jump label_Firdaus_End_Convo

            "What are your hobbies?" if firdaus_hobbies == 1:
                if firdaus_first_event_checker == 0:
                    p "Wait what?"
                    scene fskcd
                    f "What's up? You got spooked?"
                    p "Was there always this option?"
                    f "Nope, you unlocked it by asking for my introduction! Let's call this an easter egg shall we? One of...a few"
                    p "I see...sooo....your hobbies?"
                    $ firdaus_first_event_checker = 1
                scene fskcd
                f "My hobbies are a bit diversed. i like to program and watch videos during my free time"
                f "I also love to watch and play football or futsal, as well as watching anime"
                p "Wow...that's a lot haha"
                p "What team do you support?"
                f "Manchester United and Borussia Monchengladbach"
                p "Borussia what?"
                scene fhcd
                f "AHAHAHHA I always get that. People always expect me to say Bayern or Dortmund, or lately Leipzig. But trust me, watch the other teams of Bundesliga"
                f "And you will enjoy it a lot!"
                p "Alright, I'll trust you"
                f "And let's play some futsal or sports if you join us here"
                p "Sounds like a plan!"
                f "Or we can play some games!"
                p "What kinda games do you play?"
                scene fscd
                f "If modern games, FIFA, Genshin Impact, Phasmophobia, stuff like that"
                f "But I am mostly a retro gamer, those old games haha"
                p "Interesting, what is your favourite game?"
                f "Fire Emblem 4: Genealogy of the Holy War"
                f "And Fire Emblem in general, even played the gacha game and got their merch haha"
                p "Wow, you are a real...fanatic"
                scene fskcd
                f "Hahaha yeahh!"
                jump label_Firdaus_End_Convo

            "When was the Web Department established?":
                scene fhcd
                f "The web department was established around the third quarter of 2021"
                f "There were many departments that were established that time, and among them were us"
                f "The three of us are the first managers."
                p "By three of you, I think you meant Ahmed and Nasrin as the other two?"
                scene fscd
                f "Indeed!"
                f "Who knows in the future there will be more managers here as well"
                f "But don't forget all three of us haha"
                p "Ahah alright"
                f "Well, that's all of my explanation for the web department!"
                p "That's it?"
                scene fskcd
                f "I need to leave some info for the other managers to explain"
                p "Yeah, I guess you do have a point"
                jump label_Firdaus_End_Convo



            "What's your specialty?":
                scene fscd
                f "Ahh, well, my specialty is Python, but lately I have been trying out new things with JavaScript Frameworks and so on"
                p "Python? It can be used to create websites?"
                f "Why did you assume websites?"
                p "Because you are the manager of the web department"
                scene fhcd
                f "Well, it doesn't have to be websites specifically. You can say that anything that involves an application that functions online is considered part of the web department"
                f "That's my opinion on it haha"
                p "Applications?"
                f "Yeah, mobile applications, web applications and so on"
                p "You have a poitn"
                scene fskcd
                f "I guess I do have a 'poitn', my friend"
                p "POINT, not poitn... :("
                f "AHAHAHA, alright, anyways"
                scene fhcd
                f "Yes, you can use Python for websites such as Flask and Django frameworks. You can also use FastAPI for backend development"
                p "wow, that is interesting to know"
                f "It is, isn't it? hahaha"
                f "My other specialties are mobile app development, some cybersecurity, and telegram bots"
                $ firdaus_telegram = 1
                f "But mostly related to IOT"
                p "Internet of Things is interesting indeed"
                p "But what kinda IOT if you don't mind me asking?"
                f "Usually involving Raspberry Pi or Arduino, I like to build stuff with them. Program them in a way that might help people"
                p "Ahh interesting. May I know more about that?"
                scene fscd
                f "Yeah, you can, but maybe when you meet me in real life. Too much to explain here ahaha"
                p "Yeah, that is true haha"
                scene fncd
                f "You know what else Python is used for?"
                p "What is it?"
                scene fskcd
                f "Creating this game!"
                p "Really?"
                f "Yeah! Using an application called RenPy"
                p "And hosted using..."
                f "AWS, more specifically route 53 and s3"
                p "Can you tell me how to do it?"
                f "I usually use online tutorials for hosting, but for creating the game, you can have a look at the RenPy documentation"
                p "Can you teach me?"
                f "I could if we meet face to face, again, too much to teach if through this game lol"
                p "True (Sigh I tried to trick him but I can't)"
                jump label_Firdaus_End_Convo
            "Your socials or repositories":
                scene fncd
                f "Well most of them are private for now, but you can have a look at my LinkedIn"
                p "Sure, can you share me the link?"
                f "I could, but I am not sure if I can make links clickable here lol"
                p "I can copy paste"
                stop music fadeout 3.0
                scene fskcd
                play music "audio/Fire Emblem The Sacred Stones - 12 Determination.mp3" fadein 3.0 volume 0.5
                f "Such determination" 
                p "What is that change of music?"
                f "It is called Determination, it is in the game, Fire Emblem 8: The Sacred Stones"
                if firdaus_hobbies == 1:
                    p "I knew it, and not from Undertale"
                    scene fhcd
                    p "Because that is your favourite game franchise"
                    f "Indeed! Good that you remembered, alright back to the original audio"
                    stop music fadeout 3.0
                    p "What is this audio name by the way?"
                    play music "audio/09 _ Asougi Kazuma - Samurai With A Mission (Dai Gyakuten Saiban Soundtrack).mp3" fadein 3.0 volume 0.5
                    f "Samurai With a Mission from The Great Ace Attorney"
                    f "Actually this current style, I kinda based it on a cutscene from that game"
                    p "The style of us sitting here?"
                    f "Yeah, please tell me if you caught the reference!"
                else:
                    p "I thought it was Determination from Undertale"
                    f "Ahaha, no no, it is from Fire Emblem"
                    f "But I know people will think that the music is from Undertale due to the name haha"
                    stop music fadeout 3.0
                    play music "audio/09 _ Asougi Kazuma - Samurai With A Mission (Dai Gyakuten Saiban Soundtrack).mp3" fadein 3.0 volume 0.5
                scene fhcd
                f "Anyways, I think I can link them  here. Just click on which of this social platforms you wanna look at"
                f "Note that my website isn't complete yet for hosting, once it is done, it will be available in these options"
                f "{a=https://www.linkedin.com/in/muhammad-firdaus-badauraudine-793a501b0/}LinkedIn{/a}"
                f "{a=https://github.com/firdauskotp}GitHub{/a}"
                f "{a=https://www.youtube.com/channel/UCGiQ0y1j29wgFBV-k7bY8BA}My first Youtube Channel for gaming and so{/a}"
                f "{a=https://www.youtube.com/channel/UCMZijMRqWQjSV3oUxXQIQpA}My Programming Tutorial Youtube Channel{/a}"
                f "For now, these are all of my socials, feel free to have a look!"
                jump label_Firdaus_End_Convo
            "Any advice":
                stop music fadeout 3.0
                scene fhcd
                play music "audio/Leif's Theme ~ Leif's Army, Seeking Victory - Fire Emblem - Thracia 776 (Extended).mp3" fadein 3.0 volume 0.5

                f "Well for me, always manage your time properly."
                if firdaus_hobbies == 1:
                    p "I see, because of how you can manage jobs and classes while working right?"
                    f "Indeed!"
                    f "If I can manage my time between those periods, I am sure you can as well!"
                    p "That is true"
                else:
                    p "Do you have experience in that?"
                    scene fskcd
                    f "I do! But to see more upon it, check out my introduction!"
                    p "Can't you tell me now?"
                    f "Too lazy!"
                    p "Sigh, fine"
                    f "And once you are done, click back this option!"
                    p "Sigh...sure"
                    scene fhcd
                f "Make a schedule of your tasks that are from top priorities to the lowest priorities"
                f "But don't forget to have fun in the process"
                p "But wouldn't it be distracting?"
                f "It can, but only on how you handle it."
                f "Remember [player_name], we are only human. We need our rest time as well as work time"
                f "Imagine a motorbike that you always use without rest, what would happen?"
                p "The petrol will be drained, as well as other things that we need to top up back to get it working like normal again"
                scene fscd
                f "Bingo kiddo"
                f "Same like humans, if we use up all our energy, we will get burnt out to the point the things we enjoy, we don't!"
                p "Wow, I never thought about it that way! And how did you get that analogy?"
                scene fskcd
                f "I literally just made it up! But the important thing is the message right?!"
                p "You must be joking!"
                f "Nope! (Author's Note: I really did just made up this analogy while writing this part lol. Maybe I can be the new Mark Goldbridge?)"
                p "I...I see"
                scene fhcd
                f "Anyways, when you are having fun, you have some relax time, and you may find some inspiration as well"
                f "Imagine those games or movies you are playing, you may have an inspiration to code something about that, or write a story about that or so"
                p "Story I can accept, but coding?"
                f "Imagine you are watching a show and see the main character struggle with something. You might think to yourself..."
                f "Hmm, maybe if there exists a device like this, the circumstances can be prevented"
                f "You then proceed to research about it or make the device, or at least explain your idea(s) in your group of friends and attempt to make it"
                f "As you can see, there are many possibilities!"
                p "Now I know how you got some of your ideas"
                stop music fadeout 3.0
                scene fskcd
                f "Ehehe"
                scene fhcd
                play music "audio/Fire Emblem - Rekka No Ken Soundtrack (Remastered) - Companions.mp3" fadein 3.0 volume 0.3
                f "Friends and colleagues, they are very important"
                f "Remember to choose wise friends, not only will they help you grow but you can also be a better human"
                f "Always push your friends to be better, politely that is. For example, if you have a friend who likes mobile application, maybe make an app and show him"
                f "Ask him for advice. It will indirectly push both him and you to be better"
                f "And if your friend shows you something he made"
                f "You can take it as motivation and inspiration as well"
                f "Remember, your friends are your allies. Healthy competition is good. I emphasize"
                f "HEALTHY COMPETITION"
                if firdaus_hobbies ==1:
                    p "Wow, I see"
                    p "I remember you saying that your friends are allies in your battle"
                    p "Now I am beginning to see why"
                    f "Indeed, if you got some companions like that, both of you could grow better"
                else:
                    p "Wow, alright"
                    scene fskcd
                    f "Too much to take in?"
                    p "Kinda, but I get the gist of it"
                    f "That's good"
                scene fhcd
                stop music fadeout 3.0
                play music "audio/09 _ Asougi Kazuma - Samurai With A Mission (Dai Gyakuten Saiban Soundtrack).mp3" fadein 3.0 volume 0.5
                f "Anyways, that's all the advice from me for now"
                jump label_Firdaus_End_Convo
                
            "That is all, thank you!":
                scene fhcd
                $ firdaus_checker = 1
                f "No problem ^_^"
                f "Here are the manager list again. What do you want to do next?"
                menu:
                    "Nasrin":
                        if nasrin_checker == 0:
                            f "The boss should be in class 5-A of tha school where you started your journey"
                            p "Alright, thanks!"
                            p "Eh, the boss?"
                            f "Ahahah"
                            p "??"
                        else:
                            f "The boss should still be in class 5-A"
                            p "Got it, thanks!"
                        jump lblNasrin
                    "Ahmed":
                        if ahmed_checker == 0:
                            f "I bet he is waiting for me at the football pitch not far from here"
                            p "Where is it?"
                            f "I'll write for you the location"
                            p "Thanks but, you said he is waiting for you?"
                            f "Yeah, I'll be there soon."
                            p "Alright..."
                            f "And here is his photo!"
                            p "Why does this picture look like some meme material?"
                            f "Trust me, it is!"
                            p "Err...okay..."
                        else:
                            f "Ahmed should still be at the football pitch"
                            p "And you still did not meet him yet"
                            f "I will after this game ends"
                            p "Sigh, alright"
                        jump lblAhmed
                    "That is all for me":
                        f "Alright, let's jump to the main credits"
                        jump lblEnd


    
    label label_Firdaus_End_Convo:
        f "Do you have any more questions to ask?"
        jump label_Firdaus_chat
                

    label lblAhmed:
        if ahmed_checker == 1:
            stop music fadeout 3.0
            play music "audio/Tobias Gregson ~ The Great Detective's Great Foe - The Great Ace Attorney Chronicles.mp3" fadein 3.0 volume 0.5
            jump label_Ahmed_chat
        stop music fadeout 3.0
        scene field
        play music "audio/London - The Great Ace Attorney Music Extended.mp3" fadein 3.0 volume 0.5
        p "Hmm, where is he?"
        p "What kinda field is this?"
        p "Too many questions, too little time!"
        p "Ahh, is that?"
        show asm with moveinright:
            center
        a "Heyy"
        p "Oh hey, Ahmed, right?"
        hide asm
        show ah:
            center
        a "Yup, you must be [player_name]"
        p "Yes that is me!"
        a "Nice to meet you habibi"
        p "Habibi?"
        a "Yeah, it is Arabic, usually we use that for greeting brothers."
        if gender=="female":
            p "I'm not a guy though"
            a "It's okay, I'll still call you habibi"
            p "Haha, alright"
            p "But I can call you habibi Ahmed as well, deal?"
            a "Why not?"
        else:
            p "Ahh I see, may I use that word?"
            a "Why not?"
            p "Alright habibi Ahmed"
            a "That's more like it"
        p "What are you doing here habibi?"
        p "I heard about some sort of event?"
        a "Yeah, we want to organise a football tournament for web department."
        a "There will be two teams, one led by me, the other by Firdaus"
        if firdaus_checker ==1:
            p "I met Firdaus at the"
            hide asm
            show asc:
                center
            a "Coffee shop, and he said he will join later on right?"
            p "Something kinda like that."
            a "Just let him be, it is another code for I will be doing everything here"
            p "Do you want me to talk to him?"
            hide asc
            show ah:
                center
            a "Nah, he has to stay in his port in the cafe for his character arc"
            p "I...guess so"
            p "Anyways"
        p "Wow...a football tournament eh? But only two teams?"
        a "Yeah, more like a final. It is mostly for fun!"
        p "Oh, I see. To build morale?"
        a "Bingo!"
        a "So, habibi, I heard you have some questions to ask?"
        stop music fadeout 3.0
        p "Yep, I have some questions"
        play music "audio/Tobias Gregson ~ The Great Detective's Great Foe - The Great Ace Attorney Chronicles.mp3" fadein 3.0 volume 0.5
        a "Don't be shy, go ahead and ask them"

    label label_Ahmed_chat:
        python:
            def ahmed_scenes(sprite):
                renpy.scene("field")
                renpy.show(sprite)
            # def ahmed_neutral_func():
            #     scene field
            #     show an:
            #         center
            # def ahmed_scowl_func():
            #     scene field
            #     show asc:
            #         center
            # def ahmed_smile_func():
            #     scene field
            #     show asm:
            #         center
        menu:
            "Can you briefly introduce yourself":
                $ ahmed_scenes("ah")
                # scene field
                # show ah:
                #     center
                a "Heyy, my name is Ahmed"
                a "I'm from Egypt!"
                p "Wow, like Moh..."
                $ ahmed_scenes("asc")
                a "Salah, right?"
                p "Yeah! Why you look so sad?"
                a "Because it is pretty obvious what people look at Egypt as"
                p "Isn't it a good thing?"
                a "It is, but there is more stuff to Egypt you know?"
                p "True"
                $ ahmed_scenes("asm")
                a "And I am not in Egypt anymore!"
                p "Eh? Oh you're in Malaysia still?"
                p "Used to, but no longer, I am in Turkey now!"
                if firdaus_checker == 1:
                    a "I have a deal with Firdaus when I come back to Malaysia though"
                    p "Let me guess, coffee?"
                    a "Yep, of course!"
                    p "Does he ever get bored of it?"
                    a "Never!"
                else:
                    p "When will you come back?"
                    a "I am not sure, but soon, maybe!"
                    p "Hopefully we can meet!"
                    a "Looking forward to it!"
                a "I am also interested in programming, usually I am more of a front-end developer"
                p "Oh, can you tell me more, habibi?"
                a "Nah, you need to pick my other option to know more! You can't trick me easily habibi"
                p "Hmm... Alright"
                a "Hahaha"
                a "I sometimes watch anime and play games as well. And I used to play futsal with the guys"
                p "Firdaus?"
                a "Yup!"
                a "Oh, I've also been in KidoCode since 2019."
                p "Wow, that is a long time!"
                $ ahmed_scenes("ah")
                a "Indeed, time flies"
                a "Now I am one of the three managers of the web department that you will meet in this game!"
                p "I see I see"
                p "Even before you are a manager, you have the passion for web development?"
                a "Of course!"
                $ ahmed_scenes("an")
                a "Habibi..."
                p "Yes?"
                a "Remember, without passion, it is hard to do what you love"
                a "You will give up easily when you reach an obstacle"
                a "No matter what, make sure you have the passion for something, and find the correct people who can grow your passion"
                if firdaus_checker == 1:
                    p "Same as"
                    $ ahmed_scenes("ah")
                    a "What Firdaus said?"
                    p "Kinda"
                    a "Yeah, we kinda have similar thoughts"
                else:
                    p "I see"
                    $ ahmed_scenes("ah")
                    a "Remember to always follow your passion as long as it is something that is good and legal"
                    p "I see a minor disclaimer there"
                    a "Ahaha"

                jump label_Ahmed_End_Convo
            "Who are involved in the Web Department?":
                a "There are two roles that are"
                a "Managers and Executors"
                p "Executors?"
                $ ahmed_scenes("an")
                a "They are involved in executing"
                p "0-0"
                $ ahmed_scenes("ah")
                a "Tests and instructions!"
                p "Oh... what kinda tests and instructions?"
                a "Well, executors are like the moderators"
                a "We, the managers are like admins"
                a "We give them some tasks like creating and testing some tasks and reporting back to us on their findings"
                a "They really help us out a lot, and I am proud to have good executors in our department!"
                p "Wow, I see..."
                p "And managers have a lot of work to do?"
                a "Yeah, we make workshops, train executors and web department members, and most importantly..."
                a "We will interview web department candidates!"
                p "So if I join, one of you three will interview me?"
                a "Indeed! And if Firdaus interviews you, you might not even meet him"
                p "His camera isn't working?"
                $ ahmed_scenes("asm")
                a "It is, but..."
                a "You have to see for yourself!"
                p "Sounds ominous!"
                a "It isn't, but you have to see it to believe it!"
                p "0-0"
                a "For now, those are the introductions of the roles involved in the Web Department"

                jump label_Ahmed_End_Convo
            "What's your specialty?":
                a "My specialty is more to front-end development"
                a "Specifically, JavaScript!"
                p "Wow, so you work with JavaScript frameworks as well?"
                $ ahmed_scenes("asm")
                a "Yeah, for now I am focusing on React and Vue"
                p "Ahh I see, are they useful?"
                a "Depends on what you are using for"
                a "You can have a look at the documentation and examples to see if you want to use those frameworks or use others"
                if nasrin_checker==1:
                    p "Nasrin said the same thing"
                    a "Oh, the boss! Yeah, I know she will say something like that!"
                    p "She doesn't like being called boss"
                    a "I know"
                    p "But yo still do it?"
                    a "Of course!"
                    p "0-0"
                p "Alright, thanks for the advice habibi"
                $ ahmed_scenes("ah")
                a "No problem, habibi"
                a "I also try a lot of new things. I used to try applications like Telegram bot like the other two managers"
                p "How can you handle a lot of things at the same time?"
                a "Not the same time, [player_name]"
                a "You need to make a schedule on what to learn and when"
                a "The method you use to learn is also imporant"
                a "Depending on those factors, you can properly plan in what order you should learn what you are planning to"
                p "I see, in that way, I can properly understand what I am learning on"
                $ ahmed_scenes("asm")
                a "Indeed!"
                jump label_Ahmed_End_Convo
            "Any advice?":
                stop music fadeout 3.0
                play music "audio/Fire Emblem - Path of Radiance -- Rally the Spirit.mp3" fadein 3.0 volume 0.5
                a "Well, some people do not want to join web development"
                p "Why?"
                a "They find it hard without even trying."
                a "Which is why, I advise this"
                $ ahmed_scenes("asm")
                a "Do you like puzzles?"
                a "What about solvintg an issue?"
                a "Maybe even innovate?"
                p "What if someone likes at least one of them?"
                a "Well, you should start development"
                p "Eh, there's a connection?"
                a "Of course!"
                a "Whatever is connected to development is considered innovative, creative or problem solving"
                a "See what apps are developed, they are all innovations from previous versions or different applications that have issues"
                a "Or problem solving, when there is an issue, developers will try to solve that issue in terms of programming"
                a "This is split into two, one is they can develop something to solve a problem or"
                a "Work on a current project that have a problem to solve the issue"
                a "As you can see, they are all connected!"
                p "Wow, I never thought about it that way"
                p "But what if that person don't like solving an issue, a puzzle or innovate?"
                $ ahmed_scenes("an")
                a "Hmm"
                a "Good question"
                $ ahmed_scenes("ah")
                a "Which of course I can asnwer!"
                a "You need to change your perspective!"
                p "Change perspectives?"
                a "Yeah, of course, those things can be boring, but try changing it to..."
                a "What if I went into this issue, I want something to solve this issue"
                a "So why not I create something to help me in the future?"
                p "I see, so put yourself in the same shoe as the problem?"
                a "Yes!"
                a "If you do it like that, you will be more motivated"
                a "Originally, it is to learn to solve an issue you are facing"
                a "But indirectly, you will help others when you publish your development"
                p "That is a good rebuttal to my question"
                p "Thank you, you literally opened a new perspective for me"
                a "No worries!"
                stop music fadeout 3.0
                play music "audio/Tobias Gregson ~ The Great Detective's Great Foe - The Great Ace Attorney Chronicles.mp3" fadein 3.0 volume 0.5
                jump label_Ahmed_End_Convo
            "What are your socials?":
                $ ahmed_scenes("an")
                a "I don't really share them, sorry"
                p "I see, it's okay"
                a "But..."
                $ ahmed_scenes("ah")
                a "I can share you my LinkedIn!"
                p "Ahh, I see."
                a "You can click the link after this to redirect to my LinkedIn"
                a "{a=https://www.linkedin.com/in/ahmad-tawfiq-8ba147126/}LinkedIn{/a}"
                a "And also my"
                a "{a=https://github.com/medo94my}GitHub{/a}"
                p "Thank you!"
                p "I will have a look!"
                a "Sure, feel free to, my friend"
                jump label_Ahmed_End_Convo
            "That is all from me":
                $ ahmed_checker = 1
                a "Alright, habibi"
                f "Who do you wanna talk to next? Or you don't have any questions for all three of us"
                menu:
                    "Nasrin":
                        if nasrin_checker == 0:
                            a "The boss should be in class 5-A of tha school where you started your journey"
                            p "Why do you call her boss?"
                            a "Hmm, that is a secret"
                            p "Whaa"
                            a "Too late, I am transporting you to the class"
                            p "Wha...wait!"
                        else:
                            a "You want to talk to the boss again? She should still be in the class"
                            p "Got it, thanks!"
                        jump lblNasrin
                    "Firdaus":
                        if firdaus_checker == 0:
                            $ ahmed_scenes("asc")
                            a "He should be here helping me"
                            p "I am not surprised, seems like a lot of work"
                            a "It is, anyways, Firdaus likes to go over the caffeine limit"
                            a "You can find him in a cafe not that far from here"
                            $ ahmed_scenes("ah")
                            a "You can exercise while walking"
                            p "Is it that far?"
                            a "No, let me show it to you on your smartphone's map"
                            p "This is far!"
                            a "It's okay, I am sure a treat awaits you there"
                            p "What?!"
                        else:
                            $ ahmed_scenes("asc")
                            a "Sigh"
                            p "He is still in the cafe right?"
                            a "Yeah, and I will have to do his part soon..."
                            p "That's upsetting"
                            $ ahmed_scenes("asm")
                            a "Ahaha, it's okay, don't worry"
                            p "...Alright..."
                        jump lblAhmed
                    "That is all for me, thank you habibi":
                        a "Alright, no problem! Let's go!s"
                        jump lblEnd
                jump label_Ahmed_End_Convo
            
    label label_Ahmed_End_Convo:
        scene field
        show ah:
            center
        a "If you have any other questions, don't worry, you can ask me"
        jump label_Ahmed_chat




    label lblEnd:
        stop music fadeout 3.0
        play music "audio/DFInstrumental.mp3" fadein 3.0 volume 0.5
        scene school
        show nh:
            center
        show fh with moveinleft:
            left
            
        show ah with moveinright:
            right
        
        n "Thank you for trying this game, [player_name]!"
        a "We hope to see you some day!"
        f "And even if you don't, never stop improving!"
        p "Thank you everyone for your time"
        p "I learnt not only about the Web Department, but also more about you guys"
        p "And thank you for the advice as well!"
        n "No worries, see you!"
        p "Good bye!"
        if final_trio == 1:
            stop music fadeout 3.0
            p "Sorry guys, I just remembered"
            hide nh
            hide fh
            hide ah
            show nc:
                center
            show fsmirk:
                left
            show asc:
                right
            n "Oh..."
            f "I have a bad feeling..."
            a "Is it extra work?"
            p "Yeah, sorry, I am wondering..."
            f "Here it comes, guys"
            n "Prepare"
            a "*Praying*"
            p "(Why are these guys overdramatic)"
            p "Well, it has something to do with this issue"
            jump lblTeamUp
        else:
            return

    label lblTeamUp:

        scene error with dissolve

        p "So my friends and I were working on a project and we have this error"

        scene school with dissolve

        show nc:
            center
        show fsmirk:
            left
        show asc:
            right
        p "can you..."

        hide nc
        hide fsmirk
        hide asc

        show nh:
            center
        show fsmile:
            left
        show ah:
            right

        p "Guys..."
        
        stop music fadeout 3.0
        play music "audio/Overture to Pursuit ~ Omen 2017 - The Great Ace Attorney 2 Music Extended.mp3" fadein 3.0 volume 0.8

        n "We know what to do next, it's okay"
        p "Huh?"
        hide nh
        show nc:
            center
        a "Yeah, just listen to the boss here"
        f "She knows"
        n "I TOLD YOU NOT TO CALL ME THAT!"
        a "Oopsie"
        f "Old habits die hard"
        n "Sigh"
        hide nc
        show nh:
            center
        n "Anyways, let us have a look shall we?"

        stop music fadeout 3.0

        f "Oh it's kinda like another video game reference!"
        a "It's the same one as one of the reference in you mentioned earlier?"
        f "Yeah!"

        n "Enough guys! Because..."

        a "Got"
        f "it"

        n "It's time..."
        play music "audio/Partners ~ The Game is Afoot! - The Great Ace Attorney 2 Music Extended.mp3" fadein 3.0 volume 0.8

        n "for the web department managers to take the main stage!"

        scene error

        show nh with moveinleft:
            right
            ypos 1.3

        n "Let's debug here first"
        n "What can we find out from here?"
        p "Err..."
        n "Haha, it's okay"
        n "This is showing Error 500, which is an Internal Server Error"
        n "I see someone is eager, take the stage!"

        hide nh with moveoutright
        show fsmile with moveinright:
            center
            ypos 1.3

        f "Well, one of the most common issues with an Error 500 is there is something wrong in the back end"
        f "Let me have a look at the back end"
        hide fsmile
    
        show fn:
            center
            ypos 1.3
        f "Hmm"
        f "There seems to be a typo here"
        f "You are currently receiving data from a variable that doesn't exist"
        p "Ah I did not notice that!"

        hide fn
        show fsmile:
            center
            ypos 1.3

        f "Chill, we sometimes tend to overlook things"
        f "That is why code review exists, bro"

        if gender == "female":
            p "Bro?"
            f "Eh sorry, sis"
            p "Sigh"

        show nh with moveinleft:
            right
            ypos 1.3

        n "Yeah, but now you need to test it"
        p "Alright"
        p "Wow, it is working now! Thanks!"
        f "HAHAHAHAHAHA"
        p "Eh?"
        n "It is now fully solved yet"
        p "Wha..."
        f "Let's call him"
        n "Yeah! Come on and show the problem!"

        hide fn with moveoutright
        hide nh with moveoutright
        show ah with moveinleft:
            center
            ypos 1.3

        a "There is no data shown yet"
        a "And also, look at the different responsiveness, it doesn't look responsive at all!"
        p "Oops"
        a "You are doing the same mistake as Firdaus sometimes"

        show fn with moveinleft:
            right
            ypos 1.3

        f "That's a low blow, bro"

        hide fn with moveoutleft

        a "Obviously!"
        a "Well, let's check your CSS"
        a "Are you using a framework or vanilla CSS?"
        p "Vanilla HTML, CSS and JS. I haven't implemented any CSS frameworks"

        hide  ah
        show asc:
            center
            ypos 1.3

        a "I see, generally it is better to use frameworks"
        p "I need to redo it with bootstrap or Angular/React, right?"
        f "ANGULAR ANGULAR ANGULAR!!"
        n "Firdaus please keep quiet!"
        f "UwU okay"
        a "Well..."

        hide asc
        show asm:
            center
            ypos 1.3
        
        a "Not really!"
        p "Eh? How?"
        a "Well, you can use something called media queries"

        show nh with moveinleft:
            center
            ypos 1.3
        
        n "It is generally better to use media queries"
        a "I personally like to use bootstrap though, but true"
        p "Really? I thought bootstrap was the way to go?"    
        n "It is, but there was advice from someone in the front-end development field that bootstrap is for wireframe"
        hide nh
        hide asm
        show asc:
            center
            ypos 1.3
        show nc:
            left
            ypos 1.3
        f "Two people actually lol. And media queries is the real thing to help, or some other frameworks I guess"
        f "Wireframe is like the blueprint of the website"
        f "Unless I heard it wrongly that is"
        f "L0L"
        a "If you were gonna cut in at least..."
        n "show yourself, not hide around shouting!"
        f "Nope, too shy, bye"
        n "Sigh, anyways, continue on Ahmed"

        hide nc with moveoutleft

        hide asc
        show ah:
            center
            ypos 1.3
        


        return
