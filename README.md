# Vimeo Toolkit



## Overview
This is a very basic toolkit for preparing your content to be embeded in a very basic website.
 The use case, which I found myself in, is that you want to provide links to videos rather than directly embed the 
 player into your site. But, you don't want to link to vimeo.com because you either don't want their branding, or 
 don't want to encourage sharing.
 
The tools allow you to pull the ids of all your videos, and then use that to generate a folder of html files that 
contain nothing but the embed code for each of your videos. It also allows you to change the settings on your videos
so that they will be embeddable in your domain, but not visible on vimeo.com.

## How to use
_This software is far from end user ready, and has been open-sourced out of principle, rather than released for production. Use at your own discretion and risk. And, ideally only use to help you develop your own tools._ 

Follow instructions under set up, and then run the functions in the order below. The 

## Set up
### Prequresites
Pip install the requirements file.
### Authentication
Place keys in a .env file using the template provided
### Settings
You'll need to put the domain you're hosting the html files in the .env file too
## Functions
### 1. Get CSV of uploaded videos
To get csv 'videos.csv', containing uri, name and description of all videos, run:

    python base.py --get-vids
    
### 2. Build Html files with embedded plays
To get  an html file for each video with an embedded player:

    mkdir html
    python base.py --build-html
    
### 3. Set video privacy settings
The settings needed to take videos off of vimeo.com and embedable are:

    privacy:
        'view':'disable',
        'embed':'whitelist',
        'download':False,
        'comments':'nobody'

To apply this to all videos in the cached csv filed, run:

    python base.py --set-privacy
    
### 4. Add Domain to allow list
In order for the embeded player to work, you need to update the video's embed allow list. To do this, run:

    python base.py --set-domain 
