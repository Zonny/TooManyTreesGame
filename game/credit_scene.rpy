label credits:
    window hide
    python:
        credits = dir_filenames("credits")
    
    image credit_scene1 = Image(im.Scale('images/Credits1.png',800,600)) 
    image credit_scene2 = Image(im.Scale('images/Credits2.png',800,600)) 
    
    scene credit_scene1 with fade
    pause 3
    scene credit_scene2 with fade
    
    $renpy.pause(4, hard=True)
    return