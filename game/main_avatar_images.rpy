
init -996:
    python:
        #main female character
        a_female_blink = dir_filenames('a_female_blink')
        a_female_smile = dir_filenames('a_female_smile')
        a_female_cry = dir_filenames('a_female_cry')
        #main male character
        a_male_blink = dir_filenames('a_male_blink')
        a_male_smile = dir_filenames('a_male_smile')
        a_male_crying = dir_filenames('a_male_cry')
        a_male_walking = dir_filenames('a_male_walking')
        #oneal
        a_oneal_blink = dir_filenames('a_oneal_blink')
        a_oneal_smile = dir_filenames('a_oneal_smile')
        a_oneal_crying = dir_filenames('a_oneal_cry')
        #estella
        a_estella_blink = dir_filenames('a_estella_blink')
        a_estella_smiling = dir_filenames('a_estella_smile')
        a_estella_crying = dir_filenames('a_estella_cry')
        a_estella_bewild = dir_filenames('a_estella_bewildered')
    
    
    image male_blinking:
        xalign .02 yalign .96
        im.FactorScale(a_male_blink[0],2.3)
        pause 0.4
        im.FactorScale( a_male_blink[1],2.3)
        pause 0.4
        im.FactorScale( a_male_blink[2],2.3)
        pause 0.3
        repeat
        
    image male_crying:
        xalign .02 yalign .96
        im.FactorScale(a_male_crying[0],2.3)
        pause 0.3
        im.FactorScale(a_male_crying[1],2.3)
        pause 1.2
        
    image male_smiling:
        xalign .02 yalign .96
        im.FactorScale(a_male_smile[0],2.3)
        pause 0.3
        im.FactorScale(a_male_smile[1],2.3)
        pause 1.2
        repeat
    
    image female_blinking:
        xalign .015 yalign .96
        im.FactorScale(a_female_blink[0],2.0)
        pause 0.3
        im.FactorScale(a_female_blink[1],2.0)
        pause 0.3
        im.FactorScale(a_female_blink[2],2.0)
        pause 0.3
        repeat
    
    image female_smiling:
        xalign .015 yalign .96
        im.FactorScale(a_female_smile[0],2.0)
        pause 0.3
        im.FactorScale(a_female_smile[1],2.0)
        pause 1.2
        repeat
        
    image female_crying:
        xalign .015 yalign .96
        im.FactorScale(a_female_cry[0],2.0)
        pause 0.3
        im.FactorScale(a_female_cry[1],2.0)
        pause 1.2
        
    image estella_blinking:
        xalign .05 yalign 1.0
        im.FactorScale(a_estella_blink[0],2.1)
        pause 0.4
        im.FactorScale(a_estella_blink[1],2.1)
        pause 0.4
        im.FactorScale(a_estella_blink[2],2.1)
        pause 0.4
        repeat
        
    image estella_smiling:
        xalign .05 yalign 1.0
        im.FactorScale(a_estella_blink[0],2.1)
        pause 0.3
        im.FactorScale(a_estella_smiling[2],2.1)
        pause 1.2
        repeat
        
    image estella_crying:
        xalign .05 yalign 1.0
        im.FactorScale(a_estella_crying[0],2.1)
        pause 0.3
        im.FactorScale(a_estella_crying[1],2.1)
        pause 1.2
        repeat
        
    image estella_bewildered:
        xalign .05 yalign 1.0
        im.FactorScale(a_estella_bewild[1],2.1)
        pause 0.3
        im.FactorScale(a_estella_bewild[0],2.1)
        pause 1.2
        repeat
        
    image oneal_blinking:
        xalign .015 yalign .96
        im.FactorScale(a_oneal_blink[0],1.8)
        pause 0.3
        im.FactorScale(a_oneal_blink[1],1.8)
        pause 0.3
        im.FactorScale(a_oneal_blink[2],1.8)
        pause 0.3
        repeat
        
    image oneal_smiling:
        xalign .015 yalign .96
        im.FactorScale(a_oneal_smile[0],1.8)
        pause 0.3
        im.FactorScale(a_oneal_smile[3],1.8)
        pause 0.5
        im.FactorScale(a_oneal_smile[3],1.8)
        pause 0.5
        im.FactorScale(a_oneal_smile[3],1.8)
        pause 0.5
        repeat
        
    image oneal_crying:
        xalign .015 yalign .96
        im.FactorScale(a_oneal_crying[0],1.8)
        pause 0.4
        im.FactorScale(a_oneal_crying[1],1.8)
        pause 2.0
        repeat
    
    
    #male main character 
    define c_male_blinking = Character('You',window_left_padding = 160, show_side_image = 'male_blinking', xalign = 0.0, yalign =1.0)
    define c_male_crying = Character('You',window_left_padding = 160, show_side_image = 'male_crying', xalign = 0.0, yalign =1.0)
    define c_male_smiling = Character('You',window_left_padding = 160, show_side_image = 'male_smiling', xalign = 0.0, yalign =1.0)
    #female main character
    define c_female_blinking = Character('You',window_left_padding = 160, show_side_image = 'female_blinking', xalign = 0.0, yalign =1.0)
    define c_female_crying = Character('You',window_left_padding = 160, show_side_image = 'female_crying', xalign = 0.0, yalign =1.0)
    define c_female_smiling = Character('You',window_left_padding = 160, show_side_image = 'female_smiling', xalign = 0.0, yalign =1.0)
    #estella
    define c_estella_bewildered = Character('Estella', window_left_padding = 160, show_side_image = 'estella_bewildered', xalign =0.0, yalign= 1.0)
    define c_estella_blinking = Character('Estella', window_left_padding = 160, show_side_image = 'estella_blinking', xalign =0.0, yalign= 1.0)
    define c_estella_crying = Character('Estella', window_left_padding = 160, show_side_image = 'estella_crying', xalign =0.0, yalign= 1.0)
    define c_estella_smiling = Character('Estella', window_left_padding = 160, show_side_image = 'estella_smiling', xalign =0.0, yalign= 1.0)
    #oneal
    define c_oneal_crying = Character('Oneal',window_left_padding=160, show_side_image= 'oneal_crying', xalign = 0.0, yalign = 1.0)
    define c_oneal_smiling = Character('Oneal', window_left_padding = 160, show_side_image = 'oneal_smiling',xalign = 0.0, yalign =1.0)
    define c_oneal_blink = Character('Oneal',window_left_padding=160, show_side_image= 'oneal_blinking', xalign = 0.0, yalign = 1.0)
    
        