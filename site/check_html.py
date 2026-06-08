import sys
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.errors = []
        # self-closing tags
        self.void_elements = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}

    def handle_starttag(self, tag, attrs):
        if tag not in self.void_elements:
            self.tags.append(tag)

    def handle_endtag(self, tag):
        if tag in self.void_elements:
            return
        if not self.tags:
            self.errors.append(f"Unexpected end tag: {tag}")
            return
        last = self.tags.pop()
        if last != tag:
            self.errors.append(f"Mismatched tag: expected </{last}>, got </{tag}>")

parser = MyHTMLParser()
with open('/home/gregory/Voilier/site/de/kontakt.html', 'r', encoding='utf-8') as f:
    parser.feed(f.read())

if parser.errors:
    print("HTML validation errors found:")
    for err in parser.errors:
        print(err)
else:
    print("No obvious HTML mismatched tags found.")
