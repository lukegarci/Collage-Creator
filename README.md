# Collage-Creator

Collage Creator is a Python-based program that allows you to load an image and apply various transformations such as flipping, color inversion, black-and-white conversion, and applying a rainbow filter. It then lets you display these manipulated images side-by-side in a collage for easy comparison.
Prerequisites

To use Collage Creator, you'll need the following Python libraries:

    numpy
    PIL (from Pillow library)
    matplotlib

    Usage

    Place your image file (e.g., pic.jpg) in the same directory as the script.
    Run the Python script:
        The program will prompt you to select one of the following image manipulations:
        InvertColor: Inverts the colors of the image.
        FlipImage: Flips the image vertically.
        RainbowFilter: Applies a rainbow-like effect to the image.
        BlackAndWhite: Converts the image to black-and-white.

    You'll also be asked to choose the position (0-3) for the manipulated image to be displayed on a 4-panel collage.

    After making your selection, the modified image will be shown alongside other manipulated images in the collage.

Methods
import_image(file_name)

    Imports an image from the file path provided.

flip_image(image)

    Flips the image vertically.

invert_color(image)

    Inverts the colors of the image.

black_white(image)

    Converts the image to black-and-white by averaging the RGB values.

rainbow_filter(image)

    Applies a rainbow-like color filter to the image by adjusting RGB channels.

image_manipulations(image)

    Interactive method that prompts the user to apply image manipulations and arrange them in a 4-part collage.
