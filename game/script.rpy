# The game starts here.
label start:
    call intro
    call dream_scene
    return
    

label intro:    
    scene black with dissolve
    show boy large with dissolve:
        xpos 0.2 ypos 0.15
    show girl large with dissolve:
        xpos 0.5 ypos 0.15
    "{cps=20}Hello. Are you a boy or a girl?{/cps}"
   
    menu:
        "Boy":
            jump choice1_boy
        "Girl":
            jump choice1_girl
    
    label choice1_boy:
        python: 
            name = renpy.input("{cps=20}What is your name?{/cps}")
            name = name.strip()
            if not name:
                name = "Kyle"
        "{cps=20}Hello, [name]!{/cps}"
        mainCharacter "Testing..."
        jump choice1_done
        
    label choice1_girl:
        python:
            name = renpy.input("{cps=20}What is your name?{/cps}")
            name = name.strip()
        jump choice1_done
        
    label choice1_done:
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
    


