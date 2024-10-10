# climg

climg (**C**h**l**oe **Im**a**g**e) is a work-in-progress lossless, compressed, raster image format created to explore the implementation of image files in memory. The associated climgu (**climg u**ncompressed) is an uncompressed climg.

## Dependencies

The climg reader is temporarily using matplotlib as proper file reading/writing is prioritized. A more sophisticated renderer will be implemented.

## Usage

bmp_reader.py takes in a bitmap file and outputs an equivalent climgu file
climgu_writer.py can also be used to manually create a climgu, pixel by pixel, for testing purposes
climgu_reader.py takes in a climgu and renders it on screen

## TODO

- Bug fix: climgus converted from bitmaps currently appear mirrored and desaturated when rendered. Cause not yet known
- Faster renderer
- Conversion options to and from files other than bitmap
- Compression algorithm to create a true climg file
