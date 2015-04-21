label neighbor_scene:
    $b = 'oneal'
    show bg_neighbor
    show oneal_fallen at Position(xpos = 500, ypos = 400)
    show oneal_backpack at Position(xpos = 250 , ypos=450)
   

label help:
       
        b '...ow...'
        menu:
            'Help Him':
                'Thank you'
                jump happy
            'Ignore':
                'He really needs help'
                jump help
                
        return 
label happy:
    hide oneal_fallen
    show bg_neighbor
    show oneal_smile at Position(xpos = 500, ypos =400)
    'Inside happy'
    show oneal_blinkng:
        alpha 0
        linear 1 alpha 1.0
    "avatar script"
    