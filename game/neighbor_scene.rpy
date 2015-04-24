label neighbor_scene:

    $b = 'Oneal'
    image black = "#000000"
    show black with vpunch
    show black with hpunch
    define b = Character('Oneal')

    show bg_neighbor
    show oneal_fallen at Position(xpos = 500, ypos = 400)
    show oneal_backpack at Position(xpos = 250 , ypos=450)
   

label help:


        
        c_oneal_crying '...ow...'
        menu:
            'Looks like he needs help!':

                narrator_correct '*You help Oneal up*'
                narrator_correct 'Good job!'
                jump happy
            'Ignore':
                narrator_incorrect 'He really needs help!'
                narrator_incorrect "How about we try something different?."
                jump help
                
        return 
label happy:
    hide oneal_fallen
    hide oneal_backpack

    
    show bg_neighbor
    show oneal_smile at Position(xpos = 500, ypos =400)
    c_oneal_smiling 'Thank you for helping me, friend!'
    
    

    