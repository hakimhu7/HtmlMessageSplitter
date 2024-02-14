
# HTML Message Splitter

The HTML Message Splitter is a Python tool that splits HTML messages into fragments while keeping their structure.
It tackles the issue of sending messages that exceed the maximum length by guaranteeing that each fragment retains the correct tag structure and HTML validity.

## Functionality

The split_html_message function in the script operates as follows:

- Splits HTML content into fragments based on a specified maximum length.
- Preserves HTML structure, ensuring that fragments remain valid HTML.
- Handles nested tags correctly, closing and reopening them as needed.
- Supports a variety of HTML elements, including paragraphs, lists, and inline styles.

## Installation

To use the HTML Message Splitter, follow these steps:

1. Ensure you have Python installed on your system.
2. Install the BeautifulSoup library using pip:
   
   pip install beautifulsoup4
   
3.Download the split.py script from this repository.

## Usage

1. Place the HTML content you want to split inside the source_html variable in the script.
2. Define the maximum length (max_len) for each fragment:
3. Execute the script
