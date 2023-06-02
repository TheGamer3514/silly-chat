import re, os, requests
from giffy import data, converter, downloader
from giffy.scraper import extract_url, check_url
from colorama import Fore, Style, init
websites = data.data
convert = converter.convert
download = downloader.download
def main(url_input):
    try:
        if 'http' not in url_input:
            url_input = 'https://' + url_input
        GIF_RES = None
        for one in websites:
            child = websites[one]
            r, idx = child['re']
            if re.match(r, url_input):
                ID = re.split(r, url_input)[idx].replace('/', '-')
                if child['scrape']:
                    GIF_RES = extract_url(url_input, child['scrape'])
                    if not GIF_RES:
                        return
                else:
                    GIF_RES = child['op'].format(ID)
            else:
                continue
            name = '{}.{}'.format(ID, child['ext'])
            if not check_url(GIF_RES):
                return
            download(GIF_RES, name)
            if child['ext'] != 'gif':
                convert(name)
            else:
                pass
            return name
        raise ValueError("Invalid Image URL")
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    main(input('URL: '), True, True)
