# The game starts here.
init:
    #Global variable
    python:
        gender = None
        name = None
        
label start:
    call intro
    
    call dream_scene
    
    call neighbor_scene
  #  call main_avatar_images
    return
    
