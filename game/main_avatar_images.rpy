#python:
#    a_mainM_smile = dir_filenames('mainM_smile')
#image a_mainM_smile:
#       a_mainM_smie[0]
#       pause 0.5
#       
#       repeat


#define main_smile = Cha:
init -996:
    python:
        a_oneal_blink = dir_filenames('a_oneal_blink')

    image oneal_blinking:
        xalign .5 yalign .28
        a_oneal_blink[0]
        pause 0.5
        a_oneal_blink[1]
        pause 0.5
        a_oneal_blink[2]
        pause 0.5
        a_oneal_blink[3]
        pause 0.5
        a_oneal_blink[4]
        pause 0.5
        repeat
    