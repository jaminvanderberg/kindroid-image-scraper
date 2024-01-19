from bs4 import BeautifulSoup
import os
import shutil
import subprocess
import datetime

def scrape_prompts_from_html(html_file_path):
    prompts = []

    with open(html_file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        img_tags = soup.find_all('img')

        for img_tag in img_tags:
            alt_text = img_tag.get('alt', '').strip()
            if alt_text:
                prompts.append({'filename': os.path.basename(img_tag['src']), 'prompt': alt_text})

    return prompts

def copy_and_set_prompts(prompts, source_directory, output_directory):
    total_files = len(prompts)
    processed_count = 0

    # Sort files based on modified date in reverse order
    prompts.sort(key=lambda x: os.path.getmtime(os.path.join(source_directory, x['filename'])), reverse=True)

    for prompt_info in prompts:
        filename = prompt_info['filename']
        prompt = prompt_info['prompt']

        # Process only images that start with "users_"
        if filename.lower().startswith('users_'):
            source_path = os.path.join(source_directory, filename)
            output_path = os.path.join(output_directory, filename)

            # Copy the image to the output directory
            shutil.copy2(source_path, output_path)

            # Run exiftool command to set description metadata without creating backup files
            command = ['exiftool', '-P', '-overwrite_original', '-Description=' + prompt, output_path]
            subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Update the modified date and created date using os.utime
            os.utime(output_path)

            processed_count += 1

            # Calculate and print the percentage of completion
            percentage_done = (processed_count / total_files) * 100
            print(f"Processed {processed_count}/{total_files} files ({percentage_done:.2f}%): {filename}")

if __name__ == "__main__":
    # Specify the path to your HTML file, source image directory, and output image directory
    html_file_path = 'Kindroid - Your Personal Artificial Intelligence Companion.html'
    source_image_directory = 'Kindroid - Your Personal Artificial Intelligence Companion_files'
    output_image_directory = 'output'

    # Ensure the output directory exists, create if not
    os.makedirs(output_image_directory, exist_ok=True)

    # Scrape prompts from HTML file
    prompts = scrape_prompts_from_html(html_file_path)

    # Copy images to the output directory and set prompts with ExifTool
    copy_and_set_prompts(prompts, source_image_directory, output_image_directory)
