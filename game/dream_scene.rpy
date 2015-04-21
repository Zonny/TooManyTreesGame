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
    
