import os

## This tool will go through the current working directory to list all directories it contains.
## It will then traverse each directory and rename the file within to it's parent directory name.

# get the current directory
current_dir = os.getcwd()

# list all subdirectories
sub_dirs = [
    f for f in os.listdir(current_dir) if os.path.isdir(os.path.join(current_dir, f))
]

for dirname in sub_dirs:
    # get the path to the current directory
    dir_path = os.path.join(current_dir, dirname)

    # list all files in this directory
    files = [f for f in os.listdir(dir_path)]

    for filename in files:
        if filename == "+page.md":
            old_path = os.path.join(dir_path, filename)
            new_path = os.path.join(dir_path, dirname + ".md")

            # rename the file
            os.rename(old_path, new_path)
