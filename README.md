Arachnida 🕷️
Arachnida is a Python-based toolset for web scraping and metadata extraction, designed for efficient data retrieval and analysis. The project consists of two main utilities:

Spider: A web scraper to download images and documents recursively from websites.
Scorpion: A metadata analyzer to extract EXIF and other attributes from image files.
Features
Spider
Recursive Scraping: Crawl through websites to download supported files (e.g., images, PDFs, and DOCX).
Depth Control: Set the recursion depth for targeted scraping.
Custom Paths: Specify download directories for organized data storage.
Silent Mode: Suppress output for seamless operation.
Scorpion
Metadata Extraction: Extract EXIF and metadata from supported image formats (e.g., JPG, PNG, BMP).
Batch Processing: Analyze individual files or entire directories.
Detailed Attributes: View creation dates, camera details, and more.
Installation
Clone this repository:
bash
Copy code
git clone https://github.com/arash039/python-projects.git
cd python-projects/arachnida
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Usage
Spider
bash
Copy code
# Recursive scraping
python3 spider.py -r <URL>

# Set recursion depth
python3 spider.py -r <URL> -l <DEPTH>

# Specify download path
python3 spider.py -r <URL> -p <PATH>

# Silent mode
python3 spider.py -r <URL> -S

# Help
python3 spider.py -h
Downloaded files are stored in the /data directory, and logs are available in /logs.

Scorpion
bash
Copy code
# Analyze specific files
python3 scorpion.py FILE1 FILE2 ...

# Analyze all files in a directory
python3 scorpion.py -d <DIRECTORY>
