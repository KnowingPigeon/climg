# climg

climg (**C**h**l**oe **Im**a**g**e) is a work-in-progress lossless, compressed, raster image format created to explore the implementation of image files in memory. The associated climgu (**climg u**ncompressed) is an uncompressed climg.

## Dependencies

The climg reader is temporarily using matplotlib as proper file reading/writing is prioritized. A more sophisticated renderer will be implemented.

## Usage

bmp_reader.py takes in a bitmap file and outputs an equivalent climgu file
climgu_writer.py can also be used to manually create a climgu, pixel by pixel, for testing purposes
climgu_reader.py takes in a climgu and renders it on screen

## climgu structure

climgu files have a short, 11 byte header followed by an uninterrupted list of color codes
- 0x00-0x03: image length in pixels
- 0x04-0x07: image height in pixels
- 0x08-0x0A: background color in hexadecimal
- 0x0B+: undelimited list of pixels stored as 3 bytes of hexadecimal and 1 byte of alpha channel transparency

Note: climgus and by extension climgs can be rendered with our without transparency. The inclusion of a dedicated background color attempts to solve a common issue found within other transparent image formats in which, upon being placed in a context where transparency is not possible, the background indiscriminately defaults to black or white, even when this harms the visibility of the image.

## TODO

- Bug fix: climgus converted from bitmaps currently appear mirrored and desaturated when rendered. Cause not yet known
- Faster renderer
- Conversion options to and from files other than bitmap
- Compression algorithm to create a true climg file
