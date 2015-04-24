init:
    python:
       
        bs_estella_sit_norm = FactorScaleAll(dir_filenames('bus_stop_estella_sitting'), 1.6)
        bs_estella_sit_smile = FactorScaleAll(dir_filenames('bs_estella_sit_smile'), 1.6)
        bs_estella_stand_norm = FactorScaleAll(dir_filenames('bs_estella_stand_norm'), 1.6)
        bs_estella_stand_smile = FactorScaleAll(dir_filenames('bs_estella_stand_smile'), 1.6)
        bs_vip_bus = FactorScaleAll(dir_filenames('school_bus'), 1.7)
        bs_oneal_walk_norm = FactorScaleAll(dir_filenames('bs_oneal_walk_norm'), 1.1)
        bs_oneal_stand_norm = FactorScaleAll(dir_filenames('bs_oneal_stand_norm'), 1.1)
        bs_oneal_walk_smile = FactorScaleAll(dir_filenames('bs_oneal_walk_smile'), 1.1)
        bs_oneal_stand_smile = FactorScaleAll(dir_filenames('bs_oneal_stand_smile'), 1.1)
        bs_mainM_walk_norm = FactorScaleAll(dir_filenames('bs_mainM_walk_norm'), 1.6)
        bs_mainM_stand_norm = FactorScaleAll(dir_filenames("bs_mainM_stand_norm"), 1.6)
        bs_mainM_walk_smile = FactorScaleAll(dir_filenames('bs_mainM_walk_smile'), 1.6)
        bs_mainM_stand_smile = FactorScaleAll(dir_filenames('bs_mainM_stand_smile'), 1.6)
        bs_mainF_walk_norm = FactorScaleAll(dir_filenames('bs_mainF_walk_norm'), 1.6)
        bs_mainF_stand_norm = FactorScaleAll(dir_filenames("bs_mainF_stand_norm"), 1.6)
        bs_mainF_walk_smile = FactorScaleAll(dir_filenames('bs_mainF_walk_smile'), 1.6)
        bs_mainF_stand_smile = FactorScaleAll(dir_filenames('bs_mainF_stand_smile'), 1.6)        
    
    image bg_bus_stop_scene = im.Scale("images/backgrounds/bus_stop.png",width = 800, height= 450, yalign=0.0)
    image bs_estella_sitting_norm:
        bs_estella_sit_norm[0]
        pause .5
        
        bs_estella_sit_norm[1]
        pause .5
        
        bs_estella_sit_norm[0]
        pause 2.5
        
        repeat
    
    image bs_estella_standing_smile:
        bs_estella_stand_smile[0]
    
    image bs_estella_standing_norm:
        bs_estella_stand_norm[0]
        pause .4
        bs_estella_stand_norm[1]
        pause .4
        bs_estella_stand_norm[0]
        
        pause 3
        repeat
        
    image bs_school_bus_moving:
        bs_vip_bus[0]
        pause .25
        bs_vip_bus[1]
        pause .25
        repeat

    image bs_mainM_walking_norm:
        bs_mainM_walk_norm[0]
        pause .25
        bs_mainM_walk_norm[1]
        pause .25
        bs_mainM_walk_norm[2]
        pause .25
        bs_mainM_walk_norm[3]
        pause .25
        bs_mainM_walk_norm[0]
        pause .25
        bs_mainM_walk_norm[1]
        pause .25
        bs_mainM_walk_norm[2]
        pause .25
        bs_mainM_walk_norm[3]
        pause .25
        bs_mainM_walk_smile[0]
        pause .25
        bs_mainM_walk_smile[1]
        pause .25
        bs_mainM_walk_smile[2]
        pause .25
        bs_mainM_walk_smile[3]
        pause .25
        
        repeat
        
    image bs_mainM_standing_norm:
        bs_mainM_stand_norm[0]
        pause .5
        bs_mainM_stand_norm[1]
        pause .5
        bs_mainM_stand_norm[0]
        
        pause 2.5
        repeat
    
    image bs_mainM_standing_smile:
        bs_mainM_stand_smile[0]
        
    image bs_mainF_walking_norm:
        bs_mainF_walk_norm[0]
        pause .25
        bs_mainF_walk_norm[1]
        pause .25
        bs_mainF_walk_norm[2]
        pause .25
        bs_mainF_walk_norm[3]
        pause .25
        bs_mainF_walk_norm[0]
        pause .25
        bs_mainF_walk_norm[1]
        pause .25
        bs_mainF_walk_norm[2]
        pause .25
        bs_mainF_walk_norm[3]
        pause .25
        bs_mainF_walk_smile[0]
        pause .25
        bs_mainF_walk_smile[1]
        pause .25
        bs_mainF_walk_smile[2]
        pause .25
        bs_mainF_walk_smile[3]
        pause .25
        
        repeat
    
    image bs_mainF_standing_norm:
        bs_mainF_stand_norm[0]
        pause .5
        bs_mainF_stand_norm[1]
        pause .5
        bs_mainF_stand_norm[0]
        
        pause 2.5
        repeat
    
    image bs_mainF_standing_smile:
        bs_mainF_stand_smile[0]
        
    image bs_oneal_standing_norm:
        bs_oneal_stand_norm[0]
        pause .5
        bs_oneal_stand_norm[1]
        pause .5
        bs_oneal_stand_norm[0]
        pause 2.5
        repeat
    
    image bs_oneal_standing_smile:
        bs_oneal_stand_smile[0]

    image bs_oneal_walking_norm:
        bs_oneal_walk_norm[0]
        pause .25
        bs_oneal_walk_norm[1]
        pause .25
        bs_oneal_walk_norm[2]
        pause .25
        bs_oneal_walk_norm[3]
        pause .25
        bs_oneal_walk_norm[0]
        pause .25
        bs_oneal_walk_norm[1]
        pause .25
        bs_oneal_walk_norm[2]
        pause .25
        bs_oneal_walk_norm[3]
        pause .25
        bs_oneal_walk_smile[0]
        pause .25
        bs_oneal_walk_smile[1]
        pause .25
        bs_oneal_walk_smile[2]
        pause .25
        bs_oneal_walk_smile[3]
        pause .25
        repeat
        
    image bs_main_walking_norm = ConditionSwitch("gender == 'male'", 'bs_mainM_walking_norm',
                                            "gender == 'female'", 'bs_mainF_walking_norm')

    image bs_main_standing_norm = ConditionSwitch("gender == 'male'", 'bs_mainM_standing_norm',
                                            "gender == 'female'", 'bs_mainF_standing_norm')

    image bs_main_standing_smile = ConditionSwitch("gender == 'male'", 'bs_mainM_standing_smile',
                                            "gender == 'female'", 'bs_mainF_standing_smile')


    
#    define c_main_crying = ConditionSwitch("gender == 'male'", "c_male_crying",
#                                        "gender == 'female'", "c_female_crying")
    
#    define c_main_blinking = ConditionSwitch("gender == 'male'", c_male_blinking,
#                                        "gender == 'female'", c_female_blinking)
#    define c_main_smiling = ConditionSwitch("gender == 'male'", c_male_smiling,
#                                        "gender == 'female'", c_female_smiling)
label bus_stop_scene:
#    python:
#        if "gender == 'male'":
#            c_main_blinking = Character.c_male_blinking
#        else:
#            c_main_blinking = Character.c_female_blinking
        
    show bg_bus_stop_scene with fade
    show bs_estella_sitting_norm:
        xalign .32 yalign .60

    "It is a beautiful day today!"
    "Estella is waiting for the bus to arrive."
    
    show bs_oneal_walking_norm:
        xalign 1.2 yalign .60
        linear 6 xalign .5
        "bs_oneal_standing_norm"
    
    show bs_main_walking_norm:
        xalign 1.3 yalign .615
        linear 6 xalign .6
        "bs_main_standing_norm"
    
    "[name] and Oneal are walking towards the bus stop."
    $renpy.pause(6, hard=True)
    
    c_main_smiling "Hi!"
    c_oneal_smiling "Hi!"
    label bs_hi_estella:
        show bs_oneal_standing_smile:
            xalign .5 yalign .6
        
        show bs_main_standing_smile:
            xalign .6 yalign .615
        hide bs_main_walking_norm
        hide bs_oneal_walking_norm

    
        c_estella_smiling "Hi!"
        hide bs_estella_sitting_norm
        show bs_estella_standing_smile:
            xalign .32 yalign .6

        c_main_blinking "What is your name?"
        show bs_main_standing_norm:
            xalign .6 yalign.615
        
        show bs_oneal_standing_norm:
            xalign .5  yalign .6
        
        hide bs_main_standing_smile
        hide bs_oneal_standing_smile
        c_estella_blinking "My name is Estella!"
        show bs_estella_standing_norm:
            xalign .32 yalign .6
        
        c_main_smiling "Hi! My name is [name]"
        
        c_oneal_smiling "Hi! My name is Oneal"
        show bs_oneal_standing_smile:
            xalign .5 yalign .6
        
        show bs_main_standing_smile:
            xalign .6 yalign .615    
        
        hide bs_main_standing_norm
        hide bs_oneal_standing_norm
        menu:
            "How are you and Oneal feeling?"

            "Sad":
                narrator_incorrect "That is not what sadness looks like!"
                narrator_incorrect "Choose again."
                jump bs_hi_estella
            
            "Happy":
                narrator_correct "Exactly! You are happy to meet new friends"
            
            "Angry":
                narrator_incorrect "You should not be upset when meeting new people."
                narrator_incorrect "Choose again."
                jump bs_hi_estella
            
            "Surprise":
                narrator_incorrect "When you meet new people do not look surpised."
                narrator_incorrect "Choose again."
                jump bs_hi_estella
    
    label bs_estella_join_team:
        c_main_smiling "Would you like to join our basketball team?"
        show bs_oneal_standing_smile:
            xalign .5 yalign .6
        
        show bs_main_standing_smile:
            xalign .6 yalign .615
        
        hide bs_main_standing_norm
        hide bs_oneal_standing_norm
        
        c_estella_smiling "YEAH!!! I would love to join!"
        show bs_estella_standing_smile:
            xalign .32 yalign .6

        hide bs_estella_standing_norm
        
        menu:
            "How are you feeling now that you have made a new team member?"

            "Sad":
                narrator_incorrect "You should not be sad when you have made a new friend and teammate!"
                narrator_incorrect "Choose again."
                jump bs_estella_join_team
            
            "Happy":
                narrator_correct "Exactly! You are happy to meet new friends and a new member for the basketball team."
            
            "Angry":
                narrator_incorrect "You should not be upset when you meet new people."
                narrator_incorrect "Choose again."
                jump bs_estella_join_team
            
            "Surprise":
                narrator_incorrect "When you meet new people do not seem surpised."
                narrator_incorrect "Choose again."
                jump bs_estella_join_team

    c_estella_blinking "Looks like the bus is coming."
    label bus_animation:
        show bs_school_bus_moving:
            xalign 1.5 yalign .57
            easein 5 xalign .3
        
            bs_vip_bus[0]
        
            pause 4
            'bs_school_bus_moving'
            easeout 5 xalign -.7

        $renpy.pause(5, hard=True)
        hide bs_estella_standing_smile
        $renpy.pause(1, hard=True)     
        hide bs_oneal_standing_smile
        
        hide bs_main_standing_smile
        show bs_main_walking_norm:
            xalign .6 yalign .615
            linear 2 xalign .44
            "bs_main_standing_norm"
        $renpy.pause(2, hard = True)
        
        hide bs_main_walking_norm
        $renpy.pause(4, hard=True)


    return