# Kindroid Image Scraping and Metadata Tool

## Introduction

Kindroid, a popular AI image generation tool, lacks a mass download feature. However, users can leverage their browser's download capability to save all generated pictures to a folder. Unfortunately, this results in a collection of images without proper organization. The Kindroid Image Scraping and Metadata Tool is designed to address this limitation.

This Python script allows users to extract image prompts from the downloaded HTML file and inject them into the corresponding JPEG files. By doing so, you can seamlessly integrate the prompts with the images themselves. This enables compatibility with various image cataloging tools such as Lightroom, Digikam, etc. The image prompts are stored directly in the JPEG metadata, making them visible in the cataloging software and providing an organized way to manage and explore your Kindroid-generated images.

## Prerequisites

- Python 3.x
- [ExifTool](https://exiftool.org/)

## Setup

1. **Install Python:**
   - Ensure Python 3.x is installed on your machine. If not, download and install Python from https://www.python.org/downloads/.
   - During installation, make sure to check the option that adds Python to your system's PATH.

1. **Download ExifTool**:
   Download and install ExifTool from [https://exiftool.org/](https://exiftool.org/).

2. **Download kindroid_metadata_tool.py**
   Download kindroid_metadata_tool.py from this repository

3. **Install Dependencies**
   ```bash
   pip install beautifulsoup4
   ```
## Usage

1 . **Generate HTML Page with Kindroid**
   - Open Kindroid AI image generation tool in your web browser.
   - Scroll down to load all the images you'd like to download.
   - Right-click on the page and select "Save Page As."
   - Save the HTML file to a folder on your local machine. The default filename should be "Kindroid - Your Personal Artificial Intelligence Companion.html."
   - Ensure the complete webpage, including images, is saved by selecting the appropriate option in the save dialog.
2. **Run the script**
   - Place kindroid_metadata_tool.py in the same directory.
   - Ensure exiftool is available in the PATH, or place it in the same folder.
   - Run the command:
     ```bash
     python kindroid_metadata_tool.py
     ```
3. **View Results**
   - The `output` directory will contain all the images with the prompts injected in the JPEG files.
   - Load these images into your favorite image cataloging program. I use DigiCam.


   
