import os
import re
import shutil

import file_extensions


def arrange_folders(path: str) -> None:
    """arrange_folders: Move created folders in path to their appropriate folder.

    Args:
        path (str): The original path provided by the user.
    """
    for file in os.listdir(path):
        filename, _ = os.path.splitext(file)
        prefix = filename.split()[0]
        # Arrange each folder to their specified general folder format.
        match prefix:
            case prefix if prefix in file_extensions.video_extensions:
                arrange_videofiles(filename)
            case prefix if prefix in file_extensions.audio_extensions:
                arrange_audiofiles(filename)
            case prefix if prefix in file_extensions.image_extensions:
                arrange_imagefiles(filename)
            case prefix if prefix in file_extensions.document_extensions:
                arrange_documentfiles(filename)
            case prefix if prefix in file_extensions.application_extensions:
                arrange_applicationfiles(filename)


def arrange_videofiles(video_folder: str) -> None:
    """arrange_videofiles: Moves the created video folders to the created all_videofolder_name.

    Args: 
        video_folder (str): The created video_folder from main.py. 
    """
    all_videofolder_name = "Video Files"
    if not os.path.exists(all_videofolder_name):
        os.mkdir(all_videofolder_name)
    shutil.move(video_folder, all_videofolder_name)


def arrange_audiofiles(audio_folder: str) -> None:
    """arrange_audiofiles: Moves the created audio folders to the created all_audiofolder_name.

    Args:
        audio_folder (str): The created audio_folder from main.py.
    """
    all_audiofolder_name = "Audio Files"
    if not os.path.exists(all_audiofolder_name):
        os.mkdir(all_audiofolder_name)
    shutil.move(audio_folder, all_audiofolder_name)


def arrange_imagefiles(image_folder: str) -> None:
    """arrange_imagefiles: Moves the created image folders to the created all_imagefolder_name.

    Args:
        image_folder (str): The created image_folder from main.py.
    """
    all_imagefolder_name = "Image Files"
    if not os.path.exists(all_imagefolder_name):
        os.mkdir(all_imagefolder_name)
    shutil.move(image_folder, all_imagefolder_name)


def arrange_documentfiles(document_folder: str) -> None:
    """arrange_documentfiles: Moves the created document folders to the created all_documentfolder_name.

    Args:
        document_folder (str): The created document_folder from main.py.
    """
    all_documentfolder_name = "Document Files"
    if not os.path.exists(all_documentfolder_name):
        os.mkdir(all_documentfolder_name)
    shutil.move(document_folder, all_documentfolder_name)


def arrange_applicationfiles(application_folder: str) -> None:
    """arrange_applicationfiles: Moves the created application folders to the created all_applicationfolder_name.

    Args:
        application_folder (str): The created application_folder from main.py.
    """
    all_applicationfolder_name = "Application Files"
    if not os.path.exists(all_applicationfolder_name):
        os.mkdir(all_applicationfolder_name)
    shutil.move(application_folder, all_applicationfolder_name)


if __name__ == '__main__':
    arrange_folders()
