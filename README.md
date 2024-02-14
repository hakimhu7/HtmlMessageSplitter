
# HTML Message Splitter

The HTML Message Splitter is a Python tool that splits HTML messages into fragments while keeping their structure.
It tackles the issue of sending messages that exceed the maximum length by guaranteeing that each fragment retains the correct tag structure and HTML validity.

## Functionality

The split_html_message function in the script operates as follows:

1.Parses the HTML content using BeautifulSoup.

2.Iterates through all elements (tags and text nodes) in the parsed HTML.

3.Splits the HTML content into smaller fragments based on the specified maximum length.

4.Handles both text nodes and HTML tags appropriately, ensuring fragments do not exceed the maximum length.

5.Returns a list of HTML message fragments.


## Installation

To use the HTML Message Splitter, follow these steps:

1. Ensure you have Python installed on your system.
2. Install the BeautifulSoup library using pip:
   pip install beautifulsoup4
3.Download the split.py script from this repository.

## Usage

1. Place the HTML content you want to split inside the source_html variable in the script.
2. Define the maximum length (max_len) for each fragment:

   ***max_len = 4096***  ##*define the length here*

   ***fragments = split_html_message(source_html, max_len)***

    ***for fragment in fragments:***
        ***print("Fragment:", fragment)***
        ***print("===")***
    
3. Execute the script
