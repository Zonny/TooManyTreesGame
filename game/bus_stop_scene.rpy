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

label bus_stop_scene:
    show bg_bus_stop_scene
    show bs_estella_sitting_norm:
        xalign .32 yalign .60

    "It is a beautiful day today!"
    "Estella is waiting for the bus to arrive."
    
    show bs_oneal_walking_norm:
        xalign 1.2 yalign .60
        linear 8 xalign .5
        "bs_oneal_standing_norm"
    
    show bs_main_walking_norm:
        xalign 1.3 yalign .615
        linear 8 xalign .6
        "bs_main_standing_norm"
    
    "You and Oneal are walking towards the bus stop."
    
    "Both: Hi!"
    show bs_oneal_standing_smile:
        xalign .5 yalign .6
    
    show bs_main_standing_smile:
        xalign .6 yalign .615
    hide bs_main_walking_norm
    hide bs_oneal_walking_norm
    
    "Estella: Hi!"
    hide bs_estella_sitting_norm
    show bs_estella_standing_smile:
        xalign .32 yalign .6

    "Both: What is your name?"
    show bs_main_standing_norm:
        xalign .6 yalign.615
    
    show bs_oneal_standing_norm:
        xalign .5  yalign .6
    
    hide bs_main_standing_smile
    hide bs_oneal_standing_smile
    "Estella: My name is Estella!"
    show bs_estella_standing_norm:
        xalign .32 yalign .6
    
    "You: Hi! My name is asdasd"
    
    "Oneal: Hi! My name is asdfdsa"
    
    "Both: Would you like to join our basketball team?"
    show bs_oneal_standing_smile:
        xalign .5 yalign .6
    
    show bs_main_standing_smile:
        xalign .6 yalign .615
    
    hide bs_main_standing_norm
    hide bs_oneal_standing_norm
    "Testing"
    show bs_school_bus_moving:
        xalign 1 yalign .57
        easein 5 xalign .3
        
        bs_vip_bus[0]
    
    return