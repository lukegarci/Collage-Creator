import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import PIL


class ImageManipulation:

    def import_image(self, file_name):
        my_image = PIL.Image.open(file_name)
        return my_image  # .resize((256,256))

    def flip_image(self, image):

        # Turn image into an array
        image_array = np.array(image)

        # Get the x and y dimensions of the image
        x_dim = image_array.shape[0]
        y_dim = image_array.shape[1]

        # Create array of zeros of the same size as the original image
        # The zeros will be overwritten
        flipped_image_array = np.zeros(image_array.shape)

        # Go through each pixel in X and Y
        for x in range(x_dim):
            for y in range(y_dim):

                flipped_image_array[x_dim - x - 1, y, :] = image_array[x, y, :]

        flipped_image = PIL.Image.fromarray(flipped_image_array.astype(np.uint8))

        # Return the flipped image
        return flipped_image
    def invert_color(self, image):

        # Turn image into an array
        image_array = np.array(image)

        # Get the x and y dimensions of the image
        x_dim = image_array.shape[0]
        y_dim = image_array.shape[1]

        # Create array of zeros of the same size as the original image
        # The zeros will be overwritten
        invert_color_array = np.zeros(image_array.shape)

        # Go through each pixel in X and Y
        for x in range(x_dim):
            for y in range(y_dim):

                invert_color_array[x, y, 0] = 255 - image_array[x, y, 0]
                invert_color_array[x, y, 1] = 255 - image_array[x, y, 1]
                invert_color_array[x, y, 2] = 255 - image_array[x, y, 2]

        invert_color_image = PIL.Image.fromarray(invert_color_array.astype(np.uint8))

        # Return the flipped image
        return invert_color_image

    def black_white(self, image):
        image_array = np.array(image)

        x_dim = image_array.shape[0]
        y_dim = image_array.shape[1]

        bw_array = np.zeros((x_dim, y_dim), dtype=np.uint8)

        # Go through each pixel in X and Y
        for x in range(x_dim):
            for y in range(y_dim):
                # average of RGB channels
                grayscale_value = np.mean(image_array[x, y])
                # value for each channel in the black and white array
                bw_array[x, y] = grayscale_value

        # creates black and white image by stacking the grayscale values
        bw_image = np.stack((bw_array,) * 3, axis=-1)

        # convert the array back to PIL Image
        bw_image = PIL.Image.fromarray(bw_image)

        return bw_image

    def rainbow_filter(self, image):
        image_array = np.array(image)

        # gets the x/y dimensions of the image
        x_dim = image_array.shape[0]
        y_dim = image_array.shape[1]

        # creates an array to store the new modified image
        rainbow_image_array = np.zeros(image_array.shape)

        for x in range(x_dim):
            for y in range(y_dim):
                rainbow_image_array[x, y, 0] = (image_array[x, y, 0] + 75) % 256  # Red channel
                rainbow_image_array[x, y, 1] = (image_array[x, y, 1] + 180) % 256  # Green channel
                rainbow_image_array[x, y, 2] = (image_array[x, y, 2] + 83) % 256  # Blue channel

        rainbow_image = PIL.Image.fromarray(rainbow_image_array.astype(np.uint8))
        # returns the image with rainbow effect
        return rainbow_image
    def image_manipulations(self, image):
        # applies the image manipulations to a variable
        original_image = self.import_image(image)
        flipped_image = self.flip_image(original_image)
        inverted_color_image = self.invert_color(original_image)
        rainbow_filter = self.rainbow_filter(original_image)
        black_white_filter = self.black_white(original_image)
        # creates the plot and sets the variable for the loop to 0
        fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(12, 3))
        counter = 0
        while counter < 1:
            print("What manipulation? Choose from [InvertColor, FlipImage, RainbowFilter, BlackAndWhite]")
            mod = input()
            if mod == "InvertColor":
                print("Where do you want it? Choose from [0-3]")
                pos = int(input())
                axes[pos].imshow(inverted_color_image)
                axes[pos].set_title("Inverted Color Image")
                counter = counter + 1
            elif mod == "FlipImage":
                print("Where do you want it? Choose from [0-3]")
                pos = int(input())
                axes[pos].imshow(flipped_image)
                axes[pos].set_title("Flipped Image")
                counter = counter + 1
            elif mod == "RainbowFilter":
                print("Where would you like it? Choose from [0-3]")
                pos = int(input())
                axes[pos].imshow(rainbow_filter)
                axes[pos].set_title("Rainbow Filter")
                counter = counter + 1

            elif mod == "BlackAndWhite":
                print("Where would you like it? Choose from [0-3]")
                pos = int(input())
                axes[pos].imshow(black_white_filter)
                axes[pos].set_title("Black and White Filter")
                counter = counter + 1

            else:
                print('try again')

        for ax in axes:
            ax.axis('off')

        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    image_manip = ImageManipulation()
    image_manip.image_manipulations('pic.jpg')
