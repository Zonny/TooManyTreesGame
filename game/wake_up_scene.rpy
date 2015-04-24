# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
init:
    define e = Character('Eileen', color="#c8ffc8")
    image main_character_head = im.Scale("images/main_character_boy_head.png", 125, 125, xalign = .02, yalign = .95)
    define main = Character("AJKLF:JSKFLSDJ", color="#c8ffc8", window_left_padding=160, show_side_image='main_character_head')
    image bg bedroom = im.FactorScale("images/bedroom.png", 2.5)
    image bg clock = im.FactorScale("images/clock.png", 2.5)
    image blink eye1 = im.FactorScale("images/blinkingEye1.png",2.0)
    image blink eye2 = im.FactorScale("images/blinkingEye2.png", 2.0)
    image blink eye3 = im.FactorScale("images/blinkingEye3.png", 2.0)

# CHARACTER HAS NO NAME. CHANGE THE CODE TO GET THE NAME



   # python:
        # a_mainM_smile = dir_filename('main_smile')
        # image a_mainM_smiling..     
        
# The game starts here.
label wake_up_scene:
    window show
    show blink eye1
    pause 1.0
    main "ZZZzzzz..."
    scene bg bedroom
    show blink eye2
    pause .25
    show blink eye3
    pause .25
    show blink eye2
    pause .25
    show blink eye1
    pause 1.0
    show blink eye2
    pause .25
    show blink eye3
    pause .25
    show blink eye2
    pause .25
    show blink eye3
    pause .1
    hide blink eye3
    main "I'm so tired..."
    show bg bedroom
    main "What time is it..?"
    show bg clock
    main "It's 7 o'clock."
    
    menu:
        "I should get ready for school.":
            jump choice2_good
        "I want to continue sleeping.":
            jump choice2_bad
    
    label choice2_good:
        main "Yea, I should probably get ready for school."
        return
    label choice2_bad:
        main "Sleeping more seems like a bad idea. I might be late for school."
        jump loopBack
        
    
    label loopBack:
    menu:
        "I should get ready for school.":
            jump choice2_good
        "I want to continue sleeping.":
            jump choice2_bad
    
    
        
    
