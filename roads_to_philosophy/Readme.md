# Roads to Philosophy

This Python script follows the "Getting to Philosophy" phenomenon on Wikipedia, where clicking the first valid link in an article often leads to the "Philosophy" page.

## How It Works
The script starts from a given Wikipedia article, finds the first valid link in the main content, and follows the chain of articles until it reaches "Philosophy" or encounters a dead end or loop.

## Requirements
This script requires the following Python packages:
- `requests`
- `beautifulsoup4`

You can install them using:
```sh
pip install requests beautifulsoup4
```

## Usage
Run the script from the command line with a Wikipedia article as an argument:
```sh
python roads_to_philosophy.py "Computer Science"
```

### Example Output
```
Computer Science
Mathematics
Quantity
Property (philosophy)
Philosophy
5 roads from Computer Science to philosophy
```

## Limitations
- May break if Wikipedia's structure changes.
- Some articles may not have a valid first link.
- Certain pages may cause infinite loops.


