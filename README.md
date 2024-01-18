# Kindroid Image Scraping and Metadata Tool

## Introduction

Kindroid, a popular AI image generation tool, lacks a mass download feature. However, users can leverage their browser's download capability to save all generated pictures to a folder. Unfortunately, this results in a collection of images without proper organization. The Kindroid Image Scraping and Metadata Tool is designed to address this limitation.

This Python script allows users to extract image prompts from the downloaded HTML file and inject them into the corresponding JPEG files. By doing so, you can seamlessly integrate the prompts with the images themselves. This enables compatibility with various image cataloging tools such as Lightroom, Digikam, etc. The image prompts are stored directly in the JPEG metadata, making them visible in the cataloging software and providing an organized way to manage and explore your Kindroid-generated images.

## Prerequisites

- Python 3.x
- [ExifTool](https://exiftool.org/)

## Setup

1. **Download ExifTool**:
   Download and install ExifTool from [https://exiftool.org/](https://exiftool.org/).

2. **Download kindroid_metadata_tool.py**
   Download kindroid_metadata_tool.py from this repository

3. **Install Dependencies**
   ```bash
   pip install beautifulsoup4
   ```
