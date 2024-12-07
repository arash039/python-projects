# Arachnida 🕷️

**Arachnida** is a Python-based toolset for web scraping and metadata extraction, designed for efficient data retrieval and analysis. The project consists of two main utilities:

1. **Spider**: A web scraper to download images and documents recursively from websites.
2. **Scorpion**: A metadata analyzer to extract EXIF and other attributes from image files.

## Features

### Spider
- **Recursive Scraping**: Crawl through websites to download supported files (e.g., images, PDFs, and DOCX).
- **Depth Control**: Set the recursion depth for targeted scraping.
- **Custom Paths**: Specify download directories for organized data storage.
- **Silent Mode**: Suppress output for seamless operation.

### Scorpion
- **Metadata Extraction**: Extract EXIF and metadata from supported image formats (e.g., JPG, PNG, BMP).
- **Batch Processing**: Analyze individual files or entire directories.
- **Detailed Attributes**: View creation dates, camera details, and more.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/arash039/python-projects.git
   cd python-projects/arachnida
   ```
2. Install dependencies:
   ``` bash
   pip install -r requirements.txt
   ```
## Usage

### Spider
The **Spider** utility scrapes websites for supported file types (e.g., images, PDFs, DOCX) and downloads them.

#### Commands:
- **Recursive scraping**:
  ```bash
  python3 spider.py -r <URL>
  python3 spider.py -r <URL> -l <DEPTH>
  python3 spider.py -r <URL> -p <PATH>
  python3 spider.py -r <URL> -p <PATH>
  ```
### Scorpion
The Scorpion utility extracts and displays metadata from images.
#### Commands:
   ``` bash
   python3 scorpion.py FILE1 FILE2 ...
   ```



   
   
