import os
import re
import shutil

from rich.console import Console

import file_extensions

console = Console()


def move2directorys(path: str) -> None:
    """move2directorys: Moves created folder from path, to their corresponding directory's.

    Args:
        path (str): The original path provided by the user.
    """
    # To make sure the user typed in the correct path.
    while True:
        try: 
            folders = os.listdir(path)
            for file in os.listdir(path):
                filename, _ = os.path.splitext(file)
                prefix = filename.split()[0]
                # Where user will choose the directory the want to move the file to.
                match prefix:
                    case prefix if prefix in file_extensions.image_extensions:
                        images_dir = console.input(
                            rf"[bold white]Enter Path for[/] [bold yellow]{prefix}:[/] ")
                        move2image_dir(filename, images_dir)
                    case prefix if prefix in file_extensions.video_extensions:
                        video_dir = console.input(
                            rf"[bold white]Enter Path for[/] [bold yellow]{prefix}:[/] ")
                        move2video_dir(filename, video_dir)
                    case prefix if prefix in file_extensions.audio_extensions:
                        audio_dir = console.input(
                            rf"[bold white]Enter Path for[/] [bold yellow]{prefix}:[/] ")
                        move2audio_dir(filename, audio_dir)
                    case prefix if prefix in file_extensions.document_extensions:
                        document_dir = console.input(
                            rf"[bold white]Enter Path for[/] [bold yellow]{prefix}:[/] ")
                        move2application_dir(filename, document_dir)
                    case prefix if prefix in file_extensions.application_extensions:
                        application_dir = console.input(
                            rf"[bold white]Enter Path for[/] [bold yellow]{prefix}:[/] ")
                        move2application_dir(filename, application_dir)
            directory_name = re.split(r"[\\/]", path)
            console.print(
                f"Successfully moved {len(folders)} [bold yellow]<{directory_name[-1]}>[/] Folders to {len(folders)}"
                f" directory's on your PC.", style='bold green')
            break
        except FileNotFoundError:
            console.print(">> Please enter a directory/path", style="bold red")


def move2image_dir(image_folder: str, images_path: str) -> None:
    """move2image_dir: Move the created image folders, to the image path the user provides.

    Args:
        image_folder (str): The created image_folder from main.py.
        images_path (str): The image path the user wants to move the image_folder to.
    """
    shutil.move(image_folder, images_path)


def move2video_dir(video_folder: str, video_path: str) -> None:
    """move2video_dir: Moves the created video folders to the video path the user provides.

    Args:
        video_folder (str): The created video_folder from main.py.
        video_path (str): The video path the user wants to move the video_folder to.
    """
    shutil.move(video_folder, video_path)


def move2audio_dir(video_folder: str, audio_path: str) -> None:
    """move2audio_dir: Moves the created audio folders to the audio path the user provides.

    Args:
        video_folder (str): The created audio_folder from main.py.
        audio_path (str): The audio path the user wants to move the audio_folder to.
    """
    shutil.move(video_folder, audio_path)


def move2document_dir(document_folder: str, document_path: str) -> None:
    """move2document_dir: Moves the created document folders to the document path the user provides.

    Args:
        document_folder (str): The created document_folder from main.py.
        document_path (str): The document path the user wants to move the document_folder to.
    """
    shutil.move(document_folder, document_path)


def move2application_dir(application_folder: str, application_path: str) -> None:
    """move2application_dir: Moves the created application folders to the application path the user provides.

    Args:
        application_folder (str): The created application_folder from main.py.
        application_path (str): The application path the user wants to move the application_folder to.
    """
    shutil.move(application_folder, application_path)


if __name__ == '__main__':
    move2directorys()
