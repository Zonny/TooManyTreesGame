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
    import os
    
    pregame_path = renpy.list_files()
    def dir_filenames(folder_name):
        '''
        Give a folder_name. Try to be as specific as possible.
        '''
        result = []
        for filename in pregame_path:
            if filename.find(folder_name) != -1:
                result.append(filename)
            
        return result
        
init:

    
    #Alvin's images
    image bg_dream_thoughtcloud = im.Scale('images/backgrounds/dream_thoughtcloud.PNG',width = 800, height= 550, yalign=0.0)
    image bg_basketball = im.Scale('images/backgrounds/basketball.PNG', width = 550, height= 250, yalign=0.2, xalign = .5)
    
    #Returns a list of string names in a directory with path+nameoffile
    python:
       player_stand = dir_filenames('player_standing')
       player_jump = dir_filenames('player_jumping')
       estella_stand = dir_filenames('estella_standing')
       estella_jump = dir_filenames('estella_jumping')
       lance_stand = dir_filenames('lance_standing')
       lance_jump = dir_filenames('lance_jumping')
       hiruka_stand = dir_filenames('hiruka_standing')
       hiruka_jump = dir_filenames('hiruka_jumping')
       oneal_stand = dir_filenames('oneal_standing')
       oneal_jump = dir_filenames('oneal_jumping')
       
        
    image main_char_standing:
        xalign .5 yalign .28

        player_stand[0]
        pause .5
        player_stand[1]
        pause .5
        player_stand[2]
        pause .5
        player_stand[3]
        pause .5
        player_stand[4]

        repeat
        
    image oneal_standing:
        xalign .20 yalign .45
        
        oneal_stand[0]
        pause .5
        oneal_stand[1]
        pause .5
        oneal_stand[2]
        pause .5
        oneal_stand[3]
        pause .5
        oneal_stand[4]
        
        repeat
        
    image estella_standing:
        xalign .35 yalign .45
        
        estella_stand[0]
        pause .5
        estella_stand[1]
        pause .5
        estella_stand[2]
        #etc
        pause .5
        estella_stand[3]
        pause .5
        estella_stand[4]
        
        repeat
    
    image lance_standing:
        xalign .65 yalign .45
        
        lance_stand[0]
        pause .5
        lance_stand[1]
        pause .5
        lance_stand[2]
        pause .5
        lance_stand[3]
        pause .5
        lance_stand[4]
        
        repeat
    
    image hiruka_standing:
        xalign .80 yalign .45
        
        hiruka_stand[0]
        pause .5
        hiruka_stand[1]
        pause .5
        hiruka_stand[2]
        pause .5
        hiruka_stand[3]
        pause .5
        hiruka_stand[4]
        
        repeat

    image main_char_jumping:
        xalign .5 yalign .46
        
        player_jump[0]
        pause 1.5
        player_jump[1]
        easeout .3 yalign .3
        easeout .3 yalign.46

        repeat
        
    image oneal_jumping:
        xalign .20 yalign .45
        
        oneal_jump[0]
        pause .75
        oneal_jump[1]
        easeout .3 yalign .3
        easeout .3 yalign.45

        repeat
        
    image estella_jumping:
        xalign .35 yalign .45
        
        estella_jump[0]
        pause .40
        estella_jump[1]
        easeout .3 yalign .3
        easeout .3 yalign.45

        repeat
        
    image lance_jumping:
        xalign .65 yalign .45
        
        lance_jump[0]
        pause .65
        lance_jump[1]
        easeout .3 yalign .3
        easeout .3 yalign.45

        repeat
        
    
    image hiruka_jumping:
        xalign .80 yalign .45
        
        hiruka_jump[0]
        pause .3
        hiruka_jump[1]
        easeout .3 yalign .3
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
    show main_char_standing
    inner_t_norm "zzz...zZZ"
    
    hide mainavatar_normal
    inner_t_cry "I.. need.. teammates.zzzZZ"
    
    show oneal_standing:
        alpha 0
        linear 1 alpha 1.0
    show estella_standing:
        alpha 0
        linear .5 alpha 1.0
    show lance_standing:
        alpha 0
        linear .6 alpha 1.0
    show hiruka_standing:
        alpha 0
        linear .8 alpha 1.0
    inner_t_cry "zz..ZZZ"
    
    show main_char_standing:
        alpha 1
        linear .3 alpha 0.0
    hide main_char_standing
    hide oneal_standing
    hide estella_standing
    hide lance_standing
    hide hiruka_standing
    
    
    
    show main_char_jumping:
        alpha 0
        linear .3 alpha 1
    show oneal_jumping
    show estella_jumping
    show lance_jumping
    show hiruka_jumping
    inner_t_smile "I FOUND TEAMMATES! COOOL!!"
    
    return
    

