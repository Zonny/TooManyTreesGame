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
            gender = 'male'
            if not name:
                name = "Kyle"
        "{cps=20}Hello, [name]!{/cps}"
        mainCharacter "Testing..."
        jump choice1_done
        
    label choice1_girl:
        python:
            name = renpy.input("{cps=20}What is your name?{/cps}")
            name = name.strip()
            gender = 'female'
        jump choice1_done
        
    label choice1_done:
        return



