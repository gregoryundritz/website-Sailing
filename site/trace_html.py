import sys
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []

    def handle_starttag(self, tag, attrs):
        if tag not in {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}:
            self.tags.append((tag, self.getpos()[0]))

    def handle_endtag(self, tag):
        if tag in {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}:
            return
        if not self.tags:
            print(f"Error at line {self.getpos()[0]}: Unexpected end tag </{tag}>")
            return
        last, line = self.tags.pop()
        if last != tag:
            print(f"Error at line {self.getpos()[0]}: Mismatched tag. Expected </{last}> (opened at {line}), but got </{tag}>")
            recovered = False
            for i in range(len(self.tags)-1, -1, -1):
                if self.tags[i][0] == tag:
                    print(f"  -> Recovered by popping up to {tag} opened at {self.tags[i][1]}")
                    self.tags = self.tags[:i]
                    recovered = True
                    break
            if not recovered:
                self.tags.append((last, line))

parser = MyHTMLParser()
with open('/home/gregory/Voilier/site/de/kontakt.html', 'r', encoding='utf-8') as f:
    parser.feed(f.read())

if parser.tags:
    print("Unclosed tags remaining:")
    for t in parser.tags:
        print(f"<{t[0]}> opened at {t[1]}")
