data = {
    'Giphy':{
        're': (r'((http|https):\/\/)?(www\.)?giphy\.com\/gifs\/(([a-z-]+)(?<=-))?([a-zA-Z0-9-]+)', 6),
        'op': 'https://media.giphy.com/media/{}/source.gif',
        'ext': 'gif',
        'scrape': None
    },
    'Tenor':{
        're': (r'((http|https):\/\/)?(www\.)?tenor\.com\/view\/(.*)(?=-)-gif-(\d+)', 4),
        'op': None,
        'ext': 'gif',
        'scrape': 'soup.find("meta",  {"property":"og:image"})["content"]'
    },
    'Tenor : Source':{
        're': (r'((http|https):\/\/)?media\d\.tenor\.co\/images\/([a-f0-9]+)\/tenor\.gif', 3),
        'op': None,
        'ext': 'gif',
        'scrape': 'url_input'
    },
    'Gfycat':{
        're': (r'((http|https):\/\/)?(www\.)?gfycat\.com\/([a-z-]+)', 4),
        'op': None,
        'ext': 'gif',
        'scrape': 'soup.find("meta",  {"property":"og:url"})["content"]'
    },
    'Reaction GIFs':{
        're': (r'((http|https):\/\/)?(www\.)?reactiongifs\.com\/([a-z0-9-]+)', 4),
        'op': None,
        'ext': 'gif',
        'scrape': 'soup.find("meta",  {"property":"og:image"})["content"]'
    },
    'Imgflip':{
        're': (r'((http|https):\/\/)?(www\.)?imgflip\.com\/gif\/([a-z0-9]+)', 4),
        'op': 'https://i-download.imgflip.com/{}.gif',
        'ext': 'gif',
        'scrape': None
    },
    'Tumblr':{
        're': (r'((http|https):\/\/)?\w+\.tumblr\.com\/post\/(\d+)', 3),
        'op': None,
        'ext': 'gif',
        'scrape': 'soup.find("meta",  {"property":"og:image"})["content"][:-1]'
    },
    'Reddit':{
        're': (r'((http|https):\/\/)?((www|old)\.)?reddit\.com\/r\/(.*)(?<=comments\/)([a-z0-9_\/]+)', 6),
        'op': None,
        'ext': 'gif',
        'scrape': r'''(re.search(r'https:\/\/preview.redd.it\/([a-z0-9]+).gif\?s=[a-f0-9]+','''
                   '''requests.get(url_input+".json", headers={'User-Agent': 'Mozilla/5.0'}).text)).group(0)'''
    },
    'PANA.GIFS':{
        're': (r'((http|https):\/\/)?(www\.)?panagif\.com\/gif\/([A-Za-z0-9-]+)', 4),
        'op': None,
        'ext': 'gif',
        'scrape': 'soup.find("source",  {"type":"image/gif"})["src"]'
    },
    'Gifer':{
        're': (r'((http|https):\/\/)?(www\.)?gifer\.com(\/\w\w)?\/([A-Za-z0-9]+)', 5),
        'op': 'https://i.gifer.com/embedded/download/{}.gif',
        'ext': 'gif',
        'scrape': None
    },
    'SillyDev': {
        're': (r'((http|https):\/\/)?sillydev\.co\.uk\/uploads\/([A-Za-z0-9.-]+)', 3),
        'op': None,
        'ext': '',
        'scrape': 'url_input'
    }
}
globals()['data'] = data  # Add this line to export the `data` variable