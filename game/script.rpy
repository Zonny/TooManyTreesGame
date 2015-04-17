# You can place the script of your game in this file.

## Declare images below this line, using the image statement.
## eg. image eileen happy = "eileen_happy.png"

#============================DECLARING VARIABLES=========================================
## Declare characters used by this game.
#define narrator = Character('Narrator', color="#c8ffc8")
#define pov = Character("[povname]")

#init:
#    image bg_basketball = im.Scale('images/basketball.PNG', width = 800, height= 450, yalign=0.0)
#    image ball_rack = Image('images/BannedStory_image.PNG', ypos=450, xpos=600)
#    image snowing = SnowBlossom('images/snow.PNG', count = 50)
#    #image new_basketball = Image(bg_basketball, yalign=0.0)
#    #image bg_basketball = Image('basketball.PNG', yalign=0.0, ysize = 800)

#=========================CHAR ANIMATION=================================================
#    image char1:
#        xalign .25 yalign .7
#        "images/char1_shooting/shoot1_0.PNG"
#        pause .5
#        "images/char1_shooting/shoot1_1.PNG"
#        pause 0.5
#        "images/char1_shooting/shoot1_2.PNG"
#        pause .5
#        repeat

#    image walk_animation = Animation("images/walk1_0.PNG",.25,
#                                     "images/walk1_1.PNG", .25,
#                                     "images/walk1_2.PNG", .25,
#                                     "images/walk1_3.PNG", .25,
#                                     "images/walk2_0.PNG", .25,
#                                     "images/walk2_1.PNG", .25,
#                                     "images/walk2_2.PNG", .25,
#                                     "images/walk2_3.PNG", .25)



## The game starts here.
#label start:
#===============================Displaying images=============================
#    scene bg_basketball
#    show snowing
#    show char1
#================================Moving picture================================
#    narrator "Welcome to the 2015 annual autism app jam competition."
#    show walk_animation:
#        xalign 1.0 yalign .70
#        linear 10.0 xalign 0.0
    
#    show ball_rack:
#        xalign 1.0 yalign .70
#        linear 5.0 xalign 0.0
        
#    narrator "The boss to beat is Ayrton AKA Altron."
    
#    show ball_rack:
#        xalign 0.0 yalign .70

#        linear 2.5 xalign 1.0
#============================Grab user input======================================
#    python:
        
#        povname = renpy.input("Hello Nerd. We need your name: ")

#    narrator "Ball Rack BACK"
    
#    pov "Hi. I am ready to jam. Ball Rack"
    
#    narrator "Cool. I'll meet you behind 7-11."
#    return

## Alvin's Comment

init python:
    game_path = 'C:\Users\Alvin\Documents\Renpy\TooManyTreesGame\game'
    def dir_filenames(path):
        import os
        result = []
        for filename in os.listdir(game_path + '/' + path):
            result.append(path + '/' + filename)
        
        print result
            
        return result
        
init:
    #Characters
    define narrator = Character('Narrator')
    
    #Alvin's images
    image bg_dream_thoughtcloud = im.Scale('images/backgrounds/dream_thoughtcloud.PNG',width = 800, height= 550, yalign=0.0)
    image bg_basketball = im.Scale('images/backgrounds/basketball.PNG', width = 550, height= 250, yalign=0.2, xalign = .5)
    
    #Returns a list of string names in a directory with path+nameoffile
    python:
       main_standing = dir_filenames('images/characters/main_standing/')
        
    image main_char:
        xalign .5 yalign .27

        'images/characters/main_standing/alert_0.png'
        pause .5
        'images/characters/main_standing/alert_1.png'
        pause .5
        'images/characters/main_standing/alert_2.png'
        pause .5
        'images/characters/main_standing/alert_3.png'
        pause .5
        'images/characters/main_standing/alert_4.png'

        repeat
        
label start:
    call dream_scene
    
    return

label dream_scene:
    scene bg_dream_thoughtcloud
    show bg_basketball
    show main_char
    
    narrator "Hello"
    return
    

