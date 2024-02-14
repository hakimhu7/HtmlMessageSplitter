from bs4 import BeautifulSoup
from typing import Generator

DEFAULT_MAX_LEN = 4396

def split_html_message(html_message: str, max_len: int = DEFAULT_MAX_LEN) -> Generator[str, None, None]:
    soup = BeautifulSoup(html_message, 'html.parser')
    current_fragment = ''
    current_len = 0
    opened_tags = []

    def append_fragment(fragment):
        if fragment.strip():  # Exclude empty fragments
            yield fragment

    def close_opened_tags():
        nonlocal current_fragment, opened_tags
        # Close opened tags in reverse order
        for tag in reversed(opened_tags):
            current_fragment += f"</{tag}>"
        opened_tags.clear()

    def open_closed_tags():
        nonlocal current_fragment, opened_tags
        # Reopen closed tags
        for tag in opened_tags:
            current_fragment += f"<{tag}>"

    for element in soup.recursiveChildGenerator():
        if isinstance(element, str):
            remaining_len = max_len - current_len
            if len(element) <= remaining_len:
                current_fragment += element
                current_len += len(element)
            else:
                words = element.split()
                for word in words:
                    if len(word) + 1 > remaining_len:
                        close_opened_tags()
                        yield from append_fragment(current_fragment)
                        current_fragment = ''
                        current_len = 0
                        remaining_len = max_len
                    current_fragment += word + ' '
                    current_len += len(word) + 1
                    if current_len >= max_len:
                        close_opened_tags()
                        yield from append_fragment(current_fragment)
                        current_fragment = ''
                        current_len = 0
                        remaining_len = max_len
                open_closed_tags()
        else:
            tag_name = element.name
            tag_html = str(element)
            if len(current_fragment) + len(tag_html) <= max_len:
                current_fragment += tag_html
                current_len += len(tag_html)
                if tag_name in ['p', 'b', 'strong', 'i', 'ul', 'ol', 'div', 'span']:
                    opened_tags.append(tag_name)
            else:
                close_opened_tags()
                yield from append_fragment(current_fragment)
                current_fragment = tag_html
                current_len = len(tag_html)
                if tag_name in ['p', 'b', 'strong', 'i', 'ul', 'ol', 'div', 'span']:
                    opened_tags.append(tag_name)

    close_opened_tags()
    yield from append_fragment(current_fragment)

def main():
    input_file_path = r"C:\Users\User\Downloads\source.txt"  # Path to the HTML file

    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
        return

    fragments_generator = split_html_message(html_content)
    for fragment_number, fragment in enumerate(fragments_generator, start=1):
        print(f"Fragment #{fragment_number}: {len(fragment)} chars")
        print(fragment)
        print("=" * 20)

if __name__ == "__main__":
    main()
