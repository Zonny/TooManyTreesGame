label neighbor_scene:
    image black = "#000000"
    show black with vpunch
    show black with hpunch
    define b = Character('Oneal')
    show bg_neighbor
    show oneal_fallen at Position(xpos = 500, ypos = 400)
    show oneal_backpack at Position(xpos = 250 , ypos=450)
   

label help:
        
        c_male_blinking '...ow...'
        menu:
            'Looks like he needs help!':
                '*you help oneal up*'
                jump happy
            'Ignore':
                'He really needs help'
                jump help
                
        return 
label happy:
    hide oneal_fallen
    hide oneal_backpack
    show bg_neighbor
    show oneal_smile at Position(xpos = 500, ypos =400)
    b 'Thank you for helping me friend!'
    
    
    