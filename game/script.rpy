# The game starts here.
init -999 python:
    import os
   
    pregame_path = renpy.list_files()
    def dir_filenames(folder_name):
        '''
        Give a folder_name. Try to be as specific as possible.
        '''
        result = []
        for filename in pregame_path:
            name_list = filename.split('/')
            if folder_name in name_list:
                result.append(filename)
            
        return result
        

label start:
    #call intro
    
   # call dream_scene
    
    call neighbor_scene
    #call main_avatar_images
    return


    
