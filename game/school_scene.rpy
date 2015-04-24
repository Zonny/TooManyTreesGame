init:
    image sc_bg_school = im.Scale('school.PNG',width = 800, height= 450, yalign=0.0)
    python:
        sc_bus_driving = dir_filenames("school_bus")
    
    image sc_bus_drive:
        sc_bus_driving[0]
        pause .25
        sc_bus_driving[1]
        pause .25
        repeat

label school_scene:
    show sc_bg_school
    
    show sc_bus_drive:
        xalign 1
        yalign .61
        easein 3 xalign .5
        sc_bus_driving[0]
        
    pause 3
    
    
    show bs_main_standing_norm:
        zoom .5
        xalign .5
        yalign .64
    
    show bs_oneal_standing_norm:
        zoom .5
        xalign .55
        yalign .63
    
    show bs_estella_standing_norm:
        zoom .5
        xalign .45
        yalign .63
        
    hide sc_bus_drive   
       
    show sc_bus_drive:
        xalign .5
        yalign .61
        easeout 3 xalign -.5
    pause 3
  
        
    
    