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
![console-script](https://i.imgur.com/An933hI.png)

Output Sample: 
![output-sample](https://i.imgur.com/SS5Vnp3.png) 


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
2. run <code>pictosquare -dir <i>(Your Image Directory Path)</i></code> 
3. visit “picToSquare” folder within the directory specified for your images. 

Running Examples: 
-----------------


1. Basic Script Usage: 

	<code>python src/index.py -dir C://UserName/FolderToBeResized</code> 

2. Custom Colours: 

	<code>python src/index.py -dir C://UserName/FolderToBeResized -color black</code>


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
    - Optionally set the image size of the watermark by setting its percentage at the end of the filename. Example “watermark**20**.png” implying watermark that’s sized 20% of the image. 
    - End the filename with an optional placement. 
        Positions Include: 
    	- “-bl” - bottom left (default) 
    	- “-br” - bottom right 
    	- “-tl” - top left 
    	- “-tr” - top right 

    	Usage: “watermark **-bl**.png” (without spaces!) 
- Set a custom background color for specific images. 
  - Add a “#hexcode” at the end of the filename from your folder and watch the script add that to the specific image. Usage: “imagename **#eeeeeeee**.png” (without spaces!) 
- Set a custom background that is neither “black” not “white” for all images. 
  - Add “-color **hex-code**” to the end of your request. 
  - Example: <code>python src/index.py -dir C://UserName/FolderToBeResized -color ***cccccc*** </code> 
- Pick Dominant Colour For Every Image: (Powered by [ColorThief](https://github.com/fengsp/color-thief-py))
    
    Set colour to "thief".
    
    Run: <code>python src/index.py -dir C://UserName/FolderToBeResized -color thief</code> 

Future Plans 
------------


- Probably turn this into an installable package. 
- Add a friendly GUI to perform the same actions. 


Credits
----------


- [Colorthief by @fengsp](https://github.com/fengsp/color-thief-py)
- Image Credits (For Previews Attached): [Unsplash.com](htps://unsplash.com) 
- Code Help: 
- “Image Processing in Python with Pillow” - [Blog Post on auth0](https://auth0.com/blog/image-processing-in-python-with-pillow/)
- [As Mackay](https://stackoverflow.com/users/7891828/as-mackay) & [Joseph](https://stackoverflow.com/users/9994064/joseph)’s snippet on this [stack overflow post](https://stackoverflow.com/questions/44231209/resize-rectangular-image-to-square-keeping-ratio-and-fill-background-with-black/44231784) 

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

Changelog
----------

- 28/05/2019
    - Added colorThief Support.
    - Code hygiene changes.
- 18/05/2019
    - Added progressbar + tqdm dependency.
    - Fixed FolderFetcher.py to reflect the above stated dependency.
    - Fixed ReadMe file typos.
