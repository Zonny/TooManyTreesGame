label dream_scene:
    show bg_dream_thoughtcloud
    image main_char_standing = ConditionSwitch("gender == 'male'", "male_char_standing",
                                        "gender == 'female'", "female_char_standing")
    image main_char_jumping = ConditionSwitch("gender == 'male'", "male_char_jumping",
                                        "gender == 'female'", "female_char_jumping")
    show bg_basketball
    label dream_scene_sad:
        show main_char_standing
        c_main_blinking "zzz...zZZ"
        

        hide mainavatar_normal
        c_main_crying "I.. need.. teammates for the basketball game.zzzZZ"
            
        menu:
            "How should you be feeling?"
            "Sad":
                narrator_correct "Correct! You are feeling sad because you need teammates for the basketball game."
                
            "Happy":
                narrator_incorrect "Your character does not look happy right now."
                narrator_incorrect "Choose again."
                jump dream_scene_sad
            
            "Angry":
                narrator_incorrect "If you cannot find teammates you should not be angry!"
                narrator_incorrect "Choose again."
                jump dream_scene_sad
                
            "Surpise":
                narrator_incorrect "Your character does not look too surprised."
                narrator_incorrect "Choose again."
                jump dream_scene_sad
              
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


    label dream_scene_happy:
        $renpy.pause(1, hard=True)
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
        c_main_smiling "I FOUND TEAMMATES! COOOL!!"
        
        menu:
            "You have teammates! How are you feeling now?"
            "Sad":
                narrator_incorrect "You obtained what you needed. You should not be sad!"
                narrator_incorrect "Choose again."
                jump dream_scene_happy
            
            "Happy":
                narrator_correct "Awesome! You should be happy to make friends and teammates!"
                jump dream_scene_end
            
            "Angry":
                narrator_incorrect "You should not be angry when you make new friends and teammates."
                narrator_incorrect "Choose again."
                jump dream_scene_happy
            
            "Surprise":
                narrator_incorrect "Everyone does not seemed surprised."
                narrator_incorrect "Choose again."
                jump dream_scene_happy
        
        label dream_scene_end:
            return
