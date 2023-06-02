import urllib.request
from colorama import Fore, Style, init
def reporthook(blocknum, blocksize, totalsize):
    readsofar = blocknum * blocksize
    percent = int((readsofar * 1e2 / totalsize) / 2)
    r_size = totalsize / 1024**2
    d_size = readsofar / 1024**2
    pgbar = '[{}{}] '.format('█' * percent, ' ' * (50 - percent)) + '[{0:.2f}/{1:.2f} MB]'.format(d_size, r_size)
def download(url, output_path):
    output_path = f"temp/{output_path}"
    opener = urllib.request.URLopener()
    opener.addheader('User-Agent', 'Mozilla/5.0')
    opener.retrieve(url, filename=output_path, reporthook=reporthook)
    outputpath = output_path.replace("temp/", "")