from base_parser import BaseParser

class IndeedLinkParser(BaseParser):
    def __init__(self, base_url, name_of_parser):
        super().__init__(base_url)
        self.name_of_parser = name_of_parser

link_parser = IndeedLinkParser('https://indeed.com', 'Link Parser')
res = link_parser.get('https://www.indeed.com/jobs?q=python&l=New%20York%2C%20NY&vjk=5f2fbaaa634be72b')
print(res)

