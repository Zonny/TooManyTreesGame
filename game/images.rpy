#Animations for all scenes
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
    
    image boy = Image("images/boy.PNG")
    image girl = Image("images/girl.PNG")
    image black = "#000"
    image bg school = Image("school.PNG")
    image bg genderChoice = Image("images/startMenuBG.PNG")
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
    image boy large = im.FactorScale("images/boy.PNG", 4.0)
    image girl large = im.FactorScale("images/girl.PNG", 4.0)
    
    #Characters
    define narrator = Character('Narrator')
    define inner_t_norm = Character("Inner Thought", show_side_image='mainavatar_normal')
    define inner_t_cry = Character("Inner Thought", show_side_image='mainavatar_cry')
    define inner_t_smile = Character("Inner Thought", show_side_image='mainavatar_smile')
    define e = Character('Eileen', color="#c8ffc8", ctc="nextButton")
    define mainCharacter = Character("[name]", color="#c8ffc8", window_left_padding=160, show_side_image=Image("images/main_character_boy_head.PNG", xalign=0.0,yalign=.85))
    
jump begin_script