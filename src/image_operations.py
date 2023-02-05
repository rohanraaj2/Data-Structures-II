from src.myimage import MyImage
import copy


def remove_channel(src: MyImage, red: bool = False, green: bool = False, blue: bool = False) -> MyImage:
    """Returns a copy of src in which the indicated channels are suppressed.

    Suppresses the red channel if no channel is indicated. src is not modified.

    Args:
    - src: the image whose copy the indicated channels have to be suppressed.
    - red: suppress the red channel if this is True.
    - green: suppress the green channel if this is True.
    - blue: suppress the blue channel if this is True.

    Returns:
    a copy of src with the indicated channels suppressed.
    """
    width, height = src.size                    # get width and height seperately
    img = MyImage(src.size)

    # looping over the pixels using x,y coordinatess
    for x in range(width):
        for y in range(height):
            # get the rgb components at x,y coordinates
            r, g, b = src.get(x, y)
            if red == True:
                r = 0
            if green == True:
                g = 0
            if blue == True:
                b = 0
            else:
                r = 0
            # use MyImage setter function to set new rgb values
            img.set(x, y, (r, g, b))
    return img


def rotations(src: MyImage) -> MyImage:
    """Returns an image containing the 4 rotations of src.

    The new image has twice the dimensions of src. src is not modified.

    Args:
    - src: the image whose rotations have to be stored and returned.

    Returns:
    an image twice the size of src and containing the 4 rotations of src.
    """
    original_width, original_height = src.size

    new_width = original_width * 2
    new_height = original_height * 2

    resulting_image = MyImage((new_width, new_height))

    for row in range(original_height):
        for column in range(original_width):

            # looping over each pixel to set rgb values

            # getting the rgb values of the particular row and column using the get function of MyImage
            rgb_value = src.get(row, column)

            # 1st image (rotated 90 degrees anticlockwise) on 1st row, 1st column
            resulting_image.set(original_height - 1 - column, row, rgb_value)

            # 2nd image (original / unrotated) on 1st row, 2nd column
            resulting_image.set(row, column + original_width, rgb_value)

            # 3rd image (upside down / rotated 180 degrees) on 2nd row, 1st column
            resulting_image.set(original_width - 1 - row + original_height,
                                original_height - 1 - column, rgb_value)

            # 4th image (rotated 270 degrees anticlockwise / 90 degrees clockwise) on 2nd row, 2nd column
            resulting_image.set(column + original_height,
                                original_height - 1 - row + original_width, rgb_value)

    return resulting_image


def apply_mask(src: MyImage, maskfile: str, average: bool = True) -> MyImage:
    """Returns an copy of src with the mask from maskfile applied to it.

    maskfile specifies a text file which contains an n by n mask. It has the
    following format:
    - the first line contains n
    - the next n^2 lines contain 1 element each of the flattened mask

    Args:
    - src: the image on which the mask is to be applied
    - maskfile: path to a file specifying the mask to be applied
    - average: if True, averaging should to done when applying the mask

    Returns:
    an image which the result of applying the specified mask to src.
    """


def resize(src: MyImage) -> MyImage:
    """Returns an image which has twice the dimensions of src.

    The new image has twice the dimensions of src. src is not modified.

    Args:
    - src: the image which needs to be resized.

    Returns:
    an image twice the size of src.
    """

    original_width, original_height = src.size

    new_width = original_width * 2
    new_height = original_height * 2

    resulting_image = MyImage((new_width, new_height))

    for row in range(original_height):
        for column in range(original_width):

            # getting the rgb values of the particular row and column using the get function of MyImage
            current_red, current_green, current_blue = src.get(
                row, column)

            resulting_image.set(row * 2, column * 2,
                                (current_red, current_green, current_blue))

            if column < original_width - 1:
                red_right, green_right, blue_right = src.get(row, column + 1)

                average_red = int((current_red + red_right) / 2)
                average_green = int((current_green + green_right) / 2)
                average_blue = int((current_blue + blue_right) / 2)

                resulting_image.set(row * 2, (column * 2) + 1,
                                    (average_red, average_green, average_blue))

            else:
                resulting_image.set(row * 2, (column * 2) + 1,
                                    (current_red, current_green, current_blue))

            if row < original_height - 1:
                red_down, green_down, blue_down = src.get(row + 1, column)

                average_red = int((current_red + red_down) / 2)
                average_green = int((current_green + green_down) / 2)
                average_blue = int((current_blue + blue_down) / 2)

                resulting_image.set(
                    (row * 2) + 1, column * 2, (average_red, average_green, average_blue))

                if column < original_width - 1:
                    red_bottom_right, green_bottom_right, blue_bottom_right = src.get(
                        row + 1, column + 1)

                    average_red = int(
                        (current_red + red_down + red_right + red_bottom_right) / 4)
                    average_green = int(
                        (current_green + green_down + green_right + green_bottom_right) / 4)
                    average_blue = int(
                        (current_blue + blue_down + blue_right + blue_bottom_right) / 4)

                resulting_image.set(
                    (row * 2) + 1, (column * 2) + 1, (average_red, average_green, average_blue))
            if row == original_height - 1:
                resulting_image.set(
                    (row * 2) + 1, column * 2, (current_red, current_green, current_blue))
                if column < original_width:
                    resulting_image.set(
                        (row * 2) + 1, (column * 2) + 1, (current_red, current_green, current_blue))

    # src.show()
    # resulting_image.show()

    return resulting_image
