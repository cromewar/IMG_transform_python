# IMG Converter using Pillow, python library

This script takes all the IMG files from a **folder** and transform them to other file type such as JPEG PNG or Webp.

### Usage

Just place the python script side by side the folder containing your images and execute it giving **3** parameters:

* The folder containing your images
* the folder to save the output images (can be an existing or new folder)
* the file format you want for the images.

```shell
 python img_transform.py TargetFolder/ OutputFolder/ FileFormat
```

### example

```shell
python img_transform.py Sample/ new_folder/ png  
```

### Try it out

I highly recommend to test the script using the sample folder with the rocket launch img from Unsplash

https://unsplash.com - Origianl Image!
[Unsplash](https://unsplash.com/photos/Ptd-iTdrCJM)

### Final Note

This script is based on ZTM python course from Andrei Negoie with little improvements
