# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define narrator = Character('Narrator', color="#c8ffc8")
define pov = Character("[povname]")

#NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO

init:
    image bg_basketball = im.Scale('images/basketball.PNG', width = 800, height= 450, yalign=0.0)
    image ball_rack = Image('images/BannedStory_image.PNG', ypos=450, xpos=600)
    image snowing = SnowBlossom('images/snow.PNG', count = 50)
    
    image char1:
        xalign .25 yalign .7
        "images/char1_shooting/shoot1_0.PNG"
        pause .5
        "images/char1_shooting/shoot1_1.PNG"
        pause 0.5
        "images/char1_shooting/shoot1_2.PNG"
        pause .5
        repeat

    #image new_basketball = Image(bg_basketball, yalign=0.0)
    #image bg_basketball = Image('basketball.PNG', yalign=0.0, ysize = 800)

# The game starts here.
label start:
    scene bg_basketball
    show snowing
    show char1
        
    narrator "Welcome to the 2015 annual autism app jam competition."
    show ball_rack:
        xalign 1.0 yalign .70
        linear 5.0 xalign 0.0
        
    narrator "The boss to beat is Ayrton AKA Altron."
    
    show ball_rack:
        xalign 0.0 yalign .70

        linear 2.5 xalign 1.0
    
    python:
        
        povname = renpy.input("Hello Nerd. We need your name: ")

    narrator "Ball Rack BACK"
    
    pov "Hi. I am ready to jam. Ball Rack"
    
    narrator "Cool. I'll meet you behind 7-11."
    return

# Alvin's Comment