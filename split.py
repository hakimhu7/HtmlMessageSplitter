from bs4 import BeautifulSoup
from typing import Generator

MAX_LEN =  4096

def split_html_message(html_message: str, max_len: int = MAX_LEN, encoding: str = 'utf-8') -> Generator[str, None, None]:
    def append_fragment(fragment):
        if fragment.strip():  # Exclude empty fragments
            yield fragment

    soup = BeautifulSoup(html_message, 'html.parser', from_encoding=encoding)
    current_fragment = ''
    current_len =  0

    for element in soup.descendants:
        if isinstance(element, str):
            while element:
                remaining_len = max_len - current_len
                if len(element) <= remaining_len:
                    current_fragment += element
                    current_len += len(element)
                    element = ''
                else:
                    current_fragment += element[:remaining_len]
                    yield from append_fragment(current_fragment)
                    current_fragment = ''
                    current_len =  0
                    element = element[remaining_len:]
        else:
            tag_html = str(element)
            if len(current_fragment) + len(tag_html) <= max_len:
                current_fragment += tag_html
                current_len += len(tag_html)
            else:
                yield from append_fragment(current_fragment)
                current_fragment = tag_html
                current_len = len(tag_html)

    yield from append_fragment(current_fragment)

def main():
    input_file_path = "C:\\Users\\User\\Downloads\\source.txt"

    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
        return

    max_len =  4096

    fragments_generator = split_html_message(html_content, max_len)
    fragment_number =  1
    for fragment in fragments_generator:
        print(f"Fragment #{fragment_number}: {len(fragment)} chars")
        print(fragment)
        print("=" *  20)
        fragment_number +=  1

if __name__ == "__main__":
    main()
