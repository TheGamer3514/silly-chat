import os
def convert(input_file):
    optimize=False
    # Expected output GIF file
    output_file = ''.join(input_file.split('.')[:-1]) + '.gif'
    # FFMPEG video2gif -no optimization
    ffmpeg = '"split [o1] [o2];[o1] palettegen [p];[o2] fifo [o3];[o3] [p] paletteuse" {}'
    if optimize:
        # FFMPEG video2gif -with optimization
        ffmpeg = '"fps=10,scale=320:-1:flags=lanczos,split [o1] [o2];[o1] palettegen [p];[o2] fifo [o3];[o3] [p] paletteuse" {}'
    #os.system(('ffmpeg -hide_banner -loglevel panic -y -i {} -filter_complex ' + ffmpeg).format(input_file, output_file))