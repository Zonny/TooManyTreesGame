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

    
    #Alvin's images
    image bg_dream_thoughtcloud = im.Scale('images/backgrounds/dream_thoughtcloud.PNG',width = 800, height= 550, yalign=0.0)
    image bg_basketball = im.Scale('images/backgrounds/basketball.PNG', width = 550, height= 250, yalign=0.2, xalign = .5)
    
    #Returns a list of string names in a directory with path+nameoffile
    python:
       main_standing = dir_filenames('images/characters/main_standing/')
        
    image main_char_stand:
        xalign .5 yalign .27

        'images/characters/main_standing/alert_0.png'
        #main_standing[0]
        pause .5
        'images/characters/main_standing/alert_1.png'
        #main_standin[1]
        pause .5
        'images/characters/main_standing/alert_2.png'
        #etc
        pause .5
        'images/characters/main_standing/alert_3.png'
        pause .5
        'images/characters/main_standing/alert_4.png'

        repeat
        
    image friend_1_stand:
        xalign .20 yalign .45
        
        'images/characters/blue_standing/alert_0.png'
        #main_standing[0]
        pause .5
        'images/characters/blue_standing/alert_1.png'
        #main_standin[1]
        pause .5
        'images/characters/blue_standing/alert_2.png'
        #etc
        pause .5
        'images/characters/blue_standing/alert_3.png'
        pause .5
        'images/characters/blue_standing/alert_4.png'
        repeat
        
    image friend_2_stand:
        xalign .35 yalign .45
        
        'images/characters/browcut_standing/alert_0.png'
        #main_standing[0]
        pause .5
        'images/characters/browcut_standing/alert_1.png'
        #main_standin[1]
        pause .5
        'images/characters/browcut_standing/alert_2.png'
        #etc
        pause .5
        'images/characters/browcut_standing/alert_3.png'
        pause .5
        'images/characters/browcut_standing/alert_4.png'
        repeat
    
    image friend_3_stand:
        xalign .65 yalign .45
        
        'images/characters/golden_standing/alert_0.png'
        #main_standing[0]
        pause .5
        'images/characters/golden_standing/alert_1.png'
        #main_standin[1]
        pause .5
        'images/characters/golden_standing/alert_2.png'
        #etc
        pause .5
        'images/characters/golden_standing/alert_3.png'
        pause .5
        'images/characters/golden_standing/alert_4.png'
        repeat
    
    image friend_4_stand:
        xalign .80 yalign .45
        
        'images/characters/nice_standing/alert_0.png'
        #main_standing[0]
        pause .5
        'images/characters/nice_standing/alert_1.png'
        #main_standin[1]
        pause .5
        'images/characters/nice_standing/alert_2.png'
        #etc
        pause .5
        'images/characters/nice_standing/alert_3.png'
        pause .5
        'images/characters/nice_standing/alert_4.png'
        repeat

    image main_char_jump:
        xalign .5 yalign .45

        'images/characters/main_jumping/alert_0.png'
        #main_standing[0]
        pause 1.5
        'images/characters/main_jumping/jump_0.png'
        easeout .3 yalign .3
        #main_standin[1]
        
        easeout .3 yalign.45

        repeat
        
    image friend_1_jump:
        xalign .20 yalign .45
        
        'images/characters/blue_jumping/alert_0.png'
        #main_standing[0]
        pause .75
        'images/characters/blue_jumping/jump_0.png'
        easeout .3 yalign .3
        #main_standin[1]
        
        easeout .3 yalign.45

        repeat
        
    image friend_2_jump:
        xalign .35 yalign .45
        
        'images/characters/browcut_jumping/alert_0.png'
        #main_standing[0]
        pause .40
        'images/characters/browcut_jumping/jump_0.png'
        easeout .3 yalign .3
        #main_standin[1]
        
        easeout .3 yalign.45

        repeat
        
    image friend_3_jump:
        xalign .65 yalign .45
        
        'images/characters/golden_jumping/alert_0.png'
        #main_standing[0]
        pause .65
        'images/characters/golden_jumping/jump_0.png'
        easeout .3 yalign .3
        #main_standin[1]
        
        easeout .3 yalign.45

        repeat
        
    
    image friend_4_jump:
        xalign .80 yalign .45
        
        'images/characters/nice_jumping/alert_0.png'
        #main_standing[0]
        pause .3
        'images/characters/nice_jumping/jump_0.png'
        easeout .3 yalign .3
        #main_standin[1]
        
        easeout .3 yalign.45

        repeat
    
    image mainavatar_smile = im.Scale(Image("images/avatars/main/smile.png"), 125, 125, xalign = .02, yalign = .95)
    image mainavatar_cry = im.Scale(Image("images/avatars/main/cry.png"),125, 125, xalign = .02, yalign = .95)
    image mainavatar_normal = im.Scale(Image("images/avatars/main/normal.png"), 125,125, xalign = .02, yalign = .95)
    
    #Characters
    define narrator = Character('Narrator')
    define inner_t_norm = Character("Inner Thought", show_side_image='mainavatar_normal')
    define inner_t_cry = Character("Inner Thought", show_side_image='mainavatar_cry')
    define inner_t_smile = Character("Inner Thought", show_side_image='mainavatar_smile')
label start:
    call dream_scene
    
    return

label dream_scene:
    scene bg_dream_thoughtcloud
    show bg_basketball
    show main_char_stand
    inner_t_norm "zzz...zZZ"
    
    hide mainavatar_normal
    inner_t_cry "I.. need.. teammates.zzzZZ"
    
    show friend_1_stand:
        alpha 0
        linear 1 alpha 1.0
    show friend_2_stand:
        alpha 0
        linear .5 alpha 1.0
    show friend_3_stand:
        alpha 0
        linear .6 alpha 1.0
    show friend_4_stand:
        alpha 0
        linear .8 alpha 1.0
    inner_t_cry "zz..ZZZ"
    
    show main_char_stand:
        alpha 1
        linear .3 alpha 0.0
    hide main_char_stand
    hide friend_1_stand
    hide friend_2_stand
    hide friend_3_stand
    hide friend_4_stand
    
    
    
    show main_char_jump:
        alpha 0
        linear .3 alpha 1
    show friend_1_jump
    show friend_2_jump
    show friend_3_jump
    show friend_4_jump
    inner_t_smile "I FOUND TEAMMATES! COOOL!!"
    
    return
    

