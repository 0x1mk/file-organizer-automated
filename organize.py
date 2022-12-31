import os

# Set the directories ## set your own directories
downloads_dir = '/home/mk/Downloads'
data_center_dit = '/home/mk/Desktop/data_center'
##
image_dir = os.path.join(data_center_dit, 'images')
video_dir = os.path.join(data_center_dit, 'videos')
pdf_dir = os.path.join(data_center_dit, 'pdfs')
datasets_dir = os.path.join(data_center_dit, 'datasets')

# Create the directories if they don't exist
if not os.path.exists(image_dir):
    os.makedirs(image_dir)
if not os.path.exists(video_dir):
    os.makedirs(video_dir)
if not os.path.exists(pdf_dir):
    os.makedirs(pdf_dir)
if not os.path.exists(datasets_dir):
    os.makedirs(datasets_dir)

# Get a list of all the files in the downloads directory
files = os.listdir(downloads_dir)

# Iterate through the list of files
for file in files:
    # Get the file's full path
    file_path = os.path.join(downloads_dir, file)

    # Check if the file is a regular file (not a directory)
    if os.path.isfile(file_path):
        # Get the file's extension
        _, file_extension = os.path.splitext(file)

        # Move the file to the appropriate directory based on its extension
        if file_extension in ['.jpg', '.png', '.gif', '.webp', '.jpeg', '.svg']:
            destination_dir = image_dir
        if file_extension in ['.mp4', '.avi', '.mkv', '.MOV']:
            destination_dir = video_dir
        elif file_extension == ['.pdf']:
            destination_dir = pdf_dir
        if file_extension == ['.csv', '.json', '.xml']:
            destination_dir = datasets_dir
        else:
            # print('all files are organized')
            continue

        # Move the file to the destination directory
        os.rename(file_path, os.path.join(destination_dir, file))
