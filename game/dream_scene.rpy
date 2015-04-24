label dream_scene:

    scene bg_dream_thoughtcloud

    image main_char_standing = ConditionSwitch("gender == 'male'", "male_char_standing",
                                        "gender == 'female'", "female_char_standing")
    image main_char_jumping = ConditionSwitch("gender == 'male'", "male_char_jumping",
                                        "gender == 'female'", "female_char_jumping")
    show bg_dream_thoughtcloud

    show bg_basketball
    label dream_scene_sad:
        show main_char_standing
        inner_t_norm "zzz...zZZ"
        

        hide mainavatar_normal
        inner_t_cry "I.. need.. teammates.zzzZZ"
            
        menu:
            "Choose an expression"
            "Sad":
                jump dream_scene_happy
                
            "Happy":
                jump dream_scene_sad
            
            "Angry":
                jump dream_scene_sad
                
            "Surpise":
                jump dream_scene_sad
    

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

    label dream_scene_happy:
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
        
        menu:
            "Choose an expression"
            "Sad":
                jump dream_scene_happy
            
            "Happy":
                jump dream_scene_end
            
            "Angry":
                jump dream_scene_happy
            
            "Surprise":
                jump dream_scene_happy
        
        label dream_scene_end:
            return
