import os
import re
import shutil
import stat
import sys

from rich.console import Console

from arrange_folders import arrange_folders
from move2dirs import move2directorys

console = Console()


def main() -> None:
    """main: Where the user will provide the path, and choose what the want to do to the path.
    """
    console.print(" Welcome To The File Organizer ".center(50, "_"), style="bold blue")
    # To check if the user types in the correct path.
    while True:
        try:
            path = console.input(r"[bold yellow]Enter the directory/path you want to arrange:[/] ")
            arrange_path(path)
            console.print(
                "Do you want to move the arranged folders to it's corresponding directory?", style="bold white")
            while True:
                response = console.input("[bold white](Y or N)[/] [bold yellow]->[/] ")
                if response.lower() == "n":
                    return arrange_folders(path)
                elif response.lower() == 'y':
                    folders = os.listdir(path)
                    console.print("THE FOLDERS ARE: ", style="bold blue")
                    for idx, folder in enumerate(folders, start=1):
                        console.print(
                            f"[bold blue]\t{idx}[/] - [bold yellow]{folder}[/]")

                    console.print(
                        f"Provide the available path, to move these [bold blue]{len(folders)}[/]"
                        f" [bold yellow]Files[/] to the directory you want on your PC.", style="bold white"
                    )
                    return move2directorys(path)
                else:
                    console.print(">> Enter either (Y or N)", style="bold red")
        except FileNotFoundError:
            console.print(
                ">> Please enter a correct directory/path", style="bold red")
        except KeyboardInterrupt:
            sys.exit(0)
        except OSError:
            console.print(">> Please enter a directory/path", style="bold red")


def arrange_path(path: str) -> None:
    """arrange_path: Arrange to provide path by the user.

    Args:
        path (str): The path to be arranged.

    Returns:
        str: A message informing the user that the path has been arranged.
    """
    os.chdir(path)
    directory_files = os.listdir(path)
    # Exit, when path is empty.
    if len(directory_files) == 0:
        console.print("Empty Path", style="bold red")
        sys.exit(0)
    # Ignore system files/Hidden files and select only unhidden files.
    for file in directory_files:
        ign_sys_files = os.stat(file).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN
        if ign_sys_files or os.path.isdir(file):
            continue
        _, extension = os.path.splitext(file)
        extension = extension[1:]

        folder_name = f"{extension} Files"
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        shutil.move(file, folder_name)

    # Pick the path name and output the successful message.
    directory_name = re.split(r"[\\/]", path)
    console.print(
        f":thumbs_up: Successfully Arranged [bold yellow]<{directory_name[-1]}>[/]", style='bold green')


if __name__ == "__main__":
    main()
