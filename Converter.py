import os
import json
from PIL import Image
import pillow_heif

pillow_heif.register_heif_opener()

def get_heic_files(before_folder):

    heic_files = []

    try:
        # Ensure the folder exists
        if not os.path.exists(before_folder):
            raise FileNotFoundError(f"The folder {before_folder} does not exist.")

        # List all files in the folder
        for filename in os.listdir(before_folder):
            if filename.lower().endswith('.heic'):
                heic_files.append(os.path.join(before_folder, filename))

    except Exception as e:
        print(f"An error occurred: {e}")

    return heic_files

def load_config(config_file):

    try:
        # Ensure the configuration file exists
        if not os.path.exists(config_file):
            raise FileNotFoundError(f"The configuration file {config_file} does not exist.")

        # Read the JSON configuration file
        with open(config_file, 'r') as file:
            config = json.load(file)

        return config

    except json.JSONDecodeError:
        print("Error: The configuration file is not a valid JSON.")
    except Exception as e:
        print(f"An error occurred: {e}")

def convert_heic_to_jpg(heic_files, config, after_folder):

    quality = config.get("quality", 85)
    resolution_percent = config.get("resolution_percent", 100)
    overwrite = config.get("overwrite", False)

    if not os.path.exists(after_folder):
        os.makedirs(after_folder)

    total_files = len(heic_files)
    completed_files = 0

    for heic_file in heic_files:
        try:
            # Open the HEIC image
            with Image.open(heic_file) as img:
                # Resize the image based on the resolution percentage
                new_size = (int(img.width * (resolution_percent / 100)), 
                            int(img.height * (resolution_percent / 100)))
                img = img.resize(new_size, Image.LANCZOS)

                # Prepare the output file path
                jpg_file = os.path.join(after_folder, os.path.splitext(os.path.basename(heic_file))[0] + '.jpg')

                # Check if overwrite is allowed
                if not overwrite and os.path.exists(jpg_file):
                    print(f"File {jpg_file} already exists. Skipping...")
                    completed_files += 1
                    print_progress(completed_files, total_files)
                    continue

                # Save the image in JPG format
                img.convert('RGB').save(jpg_file, 'JPEG', quality=quality)
                print(f"Converted {heic_file} to {jpg_file} with quality {quality}.")
                completed_files += 1
                print_progress(completed_files, total_files)

        except Exception as e:
            print(f"An error occurred while converting {heic_file}: {e}")

def print_progress(completed, total):
    print(f"Progress: {completed}/{total} files converted.")

# Testing part
if __name__ == "__main__":
    before_folder = './before'  # Assuming the folder path
    after_folder = './after'
    
    heic_files = get_heic_files(before_folder)

    if heic_files:
        print("Found the following HEIC files:")
        for file in heic_files:
            print(file)
    else:
        print("No HEIC files found.")

    config_file = './config.json'  # Assuming the config file path
    config = load_config(config_file)
    # print(type(config))
    if config:
        print("Configuration loaded successfully:")
        for key, value in config.items():
            print(f"{key}: {value}")
    else:
        print("Failed to load configuration.")

    if heic_files and config:
        print("Starting the conversion process...")
        convert_heic_to_jpg(heic_files, config, after_folder)
    else:
        print("No HEIC files found or failed to load configuration.")
