# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image boy = Image("images/boy.PNG")
image girl = Image("images/girl.PNG")
image black = "#000"
image bg school = Image("school.PNG")
image bg genderChoice = Image("images/startMenuBG.PNG")
# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8", ctc="nextButton")
# The game starts here.
label start:
    scene black with dissolve
    image boy large = im.FactorScale("images/boy.PNG", 4.0)
    image girl large = im.FactorScale("images/girl.PNG", 4.0)
    show boy large with dissolve:
        xpos 0.2 ypos 0.15
    show girl large with dissolve:
        xpos 0.5 ypos 0.15
    "{cps=20}Hello. Are you a boy or a girl?{/cps}"
    menu:
        "Boy":
            jump choice1_boy
        "Girl":
            jump choice1_girl
    label choice1_boy:
        define mainCharacter = Character("[name]", color="#c8ffc8", window_left_padding=160, show_side_image=Image("images/main_character_boy_head.PNG", xalign=0.0,yalign=.85))
        python: 
            name = renpy.input("{cps=20}What is your name?{/cps}")
            name = name.strip()
            if not name:
                name = "Kyle"
        "{cps=20}Hello, [name]!{/cps}"
        mainCharacter "Testing..."
        jump choice1_done
        
    label choice1_girl:
        python:
            name = renpy.input("{cps=20}What is your name?{/cps}")
            name = name.strip()
        jump choice1_done
        
    label choice1_done:
        scene
    return

