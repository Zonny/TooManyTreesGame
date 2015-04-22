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
            if folder_name in name_list and (filename.lower().find('.png') != -1):
                result.append(filename)
            
        return result
        
    def FactorScaleAll(image_list, scale):
        '''
        Returns a scaled the list of images using FactorScale with specified size for animation purposes
        '''
        result = []
        for i in range(len(image_list)):
            result.append(im.FactorScale(image_list[i], scale))
        
        return result

label start:
    #call intro
    #call dream_scene
    call bus_stop_scene
    return


    