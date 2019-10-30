===========
PicToSquare
===========


.. image:: https://img.shields.io/pypi/v/pictosquare.svg
        :target: https://pypi.python.org/pypi/pictosquare

.. image:: https://img.shields.io/travis/hithismani/pictosquare.svg
        :target: https://travis-ci.org/hithismani/pictosquare

.. image:: https://readthedocs.org/projects/pictosquare/badge/?version=latest
        :target: https://pictosquare.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


picToSquare is an experimental script that makes use of Pillow to enter and make every picture in a directory “Instagram Ready” by framing ‘em up into a little square. 

This script was inspired by how there are multiple free/paid apps to accomplish this on the mobile app store, but none for desktop. Hope this made your social media routine a little less annoying!

*Tested On Windows 10 + Python 3.6 + PILLOW 6.0* 

Terminal Sample:

.. image:: https://i.imgur.com/An933hI.png

Output Sample: 

.. image:: https://i.imgur.com/SS5Vnp3.png


* Free software: MIT license

Advantages: 
-----------

- Does not compress or crop images. 
- Relatively quick. 
- Does not rename images. 
- Optionally set a background colour to either “white” or “black”. (Defaults to white if not set) 
- All pictures are resized into a “picToSquare” directory 

How It Works: 
-------------

1. pip install pictosquare
2. run
           
    pictosquare -dir *Your Image Directory Path*

3. visit “picToSquare” folder within the directory specified for your images. 


Running Examples: 
-----------------


1. Basic Script Usage: 

	pictosquare -dir C://UserName/FolderToBeResized

2. Custom Colours: 

	pictosquare -dir C://UserName/FolderToBeResized -color black


Points To Remember: 
-------------------


- This script requires a **folder** and does not work on single files. *(If you require this to work on a single file, just place it in a folder. Easy!)* 
- The script will ignore all files that are not .jpeg, or .jpg. With .png files it would attempt to do an Image.alpha_compose before squaring up the image. 
- This script tends to break on RGBA (Transparent) images. Some transparent images get ‘squared’ into an image with a transparent background instead of the colour specified. It’s recommended that you convert the .png image to a .jpeg to fix this. 
- Every image in your “picToSquare” folder will be overwritten if the filenames match. The script would not clean the Resized folder before each run. (But you can add that functionality yourself, if need be) 
- The script depends on Args (for the command line prompts) and PIL/Pillow. 

Experimental:
-------------

- Watermark each image. 
    - Save a .png image with the name “watermark.png” in the same directory you want the script to look up. The script would automatically watermark each picture with the watermarked image.
    - Optionally set the image size of the watermark by setting its percentage at the end of the filename.
        
        Example “watermark**20**.png” implying watermark that’s sized 20% of the image. 
    - End the filename with an optional placement. 
        Positions Include: 
    	- “-bl” - bottom left (default) 
    	- “-br” - bottom right 
    	- “-tl” - top left 
    	- “-tr” - top right 
    	    
            Example: Save file with “watermark **-bl**.png” (without spaces!) 
- Set a custom background color for specific images. 
  - Add a “#hexcode” at the end of the filename from your folder and watch the script add that to the specific image. Usage: “imagename **#eeeeeeee**.png” (without spaces!) 
- Set a custom background that is neither “black” not “white” for all images. 
  - Add “-color **hex-code**” to the end of your request. 
  - Example: 
    
    pictosquare -dir C://UserName/FolderToBeResized -color ***cccccc*** 

- Pick Dominant Colour For Every Image: `Powered by ColorThief <https://github.com/fengsp/color-thief-py>`_

    - Set colour to "thief".
    - Run: 
        pictosquare  -dir C://UserName/FolderToBeResized -color thief

Future Plans 
------------

- Probably turn this into an installable package. (Done!)
- Add a friendly GUI to perform the same actions. 

Credits
-------

Features & Depedencies:

- `PIL(low) <https://pillow.readthedocs.io/en/stable/>`_
- `Colorthief by @fengsp <https://github.com/fengsp/color-thief-py>`_
- `Image Credits (For Previews Attached) @Unsplash <htps://unsplash.com>`_

Code Help: 

- `Image Processing in Python with Pillow <https://auth0.com/blog/image-processing-in-python-with-pillow/>`_
- `As Mackay <https://stackoverflow.com/users/7891828/as-mackay>`_ & `Joseph <https://stackoverflow.com/users/9994064/joseph>`_  snippet on this `stack overflow post   <https://stackoverflow.com/questions/44231209/resize-rectangular-image-to-square-keeping-ratio-and-fill-background-with-black/44231784>`_

This package was easily adapted into a pip installable package using Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

Changelog
----------
- 30/10/2019
    - Made script PIP Installable.
    - Fixed many PNG file squaring issues.

- 28/05/2019
    - Added colorThief Support.
    - Code hygiene changes.
- 18/05/2019
    - Added progressbar + tqdm dependency.
    - Fixed FolderFetcher.py to reflect the above stated dependency.
    - Fixed ReadMe file typos.
