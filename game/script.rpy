# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define narrator = Character('Narrator', color="#c8ffc8")
define pov = Character("[povname]")
define coach = Character('Coach', color="#c688c0")


init:
     image coach = Image('images/coach.png')
    # image main_male = Image("images/main_male.PNG")
    # image main_female = Image("images/main_female.PNG")
    
label start:
    
    scene coach_scene
    scene bg_basketball
    
label coach_scene:
    show coach at center
    
    
   
    coach "What gender are you?"
    hide coach
        
    #show main_male at left
    #show main_female at right
    menu:
        "Male":
                $ gender = "male"
                #image main_char_img = main_male
                #hide main_female
        "Female":
                $ gender = "female"
                #image main_char_img = main_female
                #hide main_male
    
    coach "We're going to need your name too!"
    python:    
        povname = renpy.input("")
    
    coach "Great [povname] lets begin the story!"
    return
    
label basketball: