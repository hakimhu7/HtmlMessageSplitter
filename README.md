# HTML Message Splitter

The HTML Message Splitter is a Python tool designed to break down long HTML messages into smaller fragments while maintaining their structure. It ensures that each fragment retains the correct tag structure and remains valid HTML.This README provides clear instructions on how to install and use the HTML Message Splitter tool.

## Functionality

The `split_html_message` function in the script works as follows:

- **Split HTML Content**: It splits HTML content into smaller fragments based on a specified maximum length.
- **Preserve Structure**: It preserves the structure of HTML, ensuring that fragments remain valid.
- **Handle Nested Tags**: It correctly manages nested tags, closing and reopening them as necessary.
- **Support Various HTML Elements**: It supports a variety of HTML elements, including paragraphs, lists, and inline styles.

## Installation

To use the HTML Message Splitter, follow these steps:

1. **Install Python**: Make sure you have Python installed on your computer. You can download it from [Python's official website](https://www.python.org/downloads/).

2. **Install BeautifulSoup Library**: Open your command line interface (CLI) and run the following command to install the BeautifulSoup library:
   pip install beautifulsoup4
   
4. **Download the Script**: Download the `split.py` script from this repository. 

## Usage

1. **Define Maximum Length**: Set the maximum length (in characters) for each fragment by modifying the `max_len` variable in the script.

2. **Set HTML Content**: Open the `split.py` script in a text editor and locate the `input_file_path` variable. Replace the content within the variable with the directory of the txt file that contains the html content you wish to split.

3. **Run the Script**:
   - Open Command Prompt (cmd) on your Windows system.
   - Navigate to the directory where the `split.py` script is located. You can use the `cd` command to change directories.
   - Once you're in the correct directory, execute the script by running the following command:

     ```
     python split.py
     ```



