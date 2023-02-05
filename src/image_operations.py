from src.myimage import MyImage
import math


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
    # create a blank copy of src dimensions
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
    width, height = src.size                    # get width and height seperately                            
    img = MyImage(src.size)                     # create a blank copy of src dimensions

    mask = open(maskfile, 'r').read().splitlines()
    mask = list(map(int, mask))                 # produces a list of int values of the file contents
    n = mask[0]                                 # n: matrix size for nxn
    mask = mask[1:]                             # listing matrix values in a list

    # calculating sum of mask values for weighted average
    mask_sum = 0
    for i in mask:
        mask_sum += i

    origin = n//2                               # center of mask appears at n//2,n//2 position in matrix

    for x in range(width):                      # looping over the pixels of the image
        for y in range(height):
            # weighted r,g,b values
            wr = 0
            wg = 0
            wb = 0

            # looping over rows and columns of mask ie a nxn matrix
            for i in range(n):
                for j in range(n):
                    index = n * i + j           # index of element we want to access from mask list
                    x_ = x + i - origin         # gives row coordinate of image with mask
                    y_ = y + j - origin         # gives col coordinate of image with mask

                    if x_ >= 0 and x_ < width and y_ >= 0 and y_ < height:       # check edges
                        r, g, b = src.get(x_, y_)
                        wr += r * mask[index]
                        wg += g * mask[index]
                        wb += b * mask[index]

            if average:                         # for weighted averge
                img.set(x, y, (wr // mask_sum, wg // mask_sum, wb // mask_sum))
            else:
                img.set(x, y, (wr, wg, wb))     # for weighted sum

    src.show()
    img.show()
    return img


def resize(src: MyImage) -> MyImage:
    """Returns an image which has twice the dimensions of src.

    The new image has twice the dimensions of src. src is not modified.

    Args:
    - src: the image which needs to be resized.

    Returns:
    an image twice the size of src.
    """

    original_width, original_height = src.size # dimensions of original image

    new_width = original_width * 2  # dimensions of enlarged image
    new_height = original_height * 2

    resulting_image = MyImage((new_width, new_height)) # new object created for enlarged image

    for row in range(original_height): # looping over each pixel of the original image instead of enlarged image to avoid excessive looping
        for column in range(original_width):

            # getting the rgb values of the particular row and column using the get function of MyImage
            current_red, current_green, current_blue = src.get(
                row, column)

            # setting the pixel values on the enlarged image's corresponding coordinates
            resulting_image.set(row * 2, column * 2,
                                (current_red, current_green, current_blue))

            if column < original_width - 1:  # if not the last column

                red_right, green_right, blue_right = src.get(
                    row, column + 1)  # rgb values of next pixel on the right

                average_red = int((current_red + red_right) / 2)
                average_green = int((current_green + green_right) / 2)
                average_blue = int((current_blue + blue_right) / 2)

                resulting_image.set(row * 2, (column * 2) + 1,
                                    (average_red, average_green, average_blue))  # setting the rgb values for the blank block betweent the two coloured blocks

            else:
                resulting_image.set(row * 2, (column * 2) + 1,
                                    (current_red, current_green, current_blue))  # setting the same rgb values as the block on the left for the last column

            if row < original_height - 1:  # if not the last row

                # rgb values of the next pixel of the block below
                red_down, green_down, blue_down = src.get(row + 1, column)

                average_red = int((current_red + red_down) / 2)
                average_green = int((current_green + green_down) / 2)
                average_blue = int((current_blue + blue_down) / 2)

                resulting_image.set(
                    (row * 2) + 1, column * 2, (average_red, average_green, average_blue))  # setting the rgb values for the blank block betweent the two coloured blocks

                if column < original_width - 1:  # if not the last column

                    red_bottom_right, green_bottom_right, blue_bottom_right = src.get(
                        row + 1, column + 1)

                    average_red = int(
                        (current_red + red_down + red_right + red_bottom_right) / 4)
                    average_green = int(
                        (current_green + green_down + green_right + green_bottom_right) / 4)
                    average_blue = int(
                        (current_blue + blue_down + blue_right + blue_bottom_right) / 4)

                resulting_image.set(
                    (row * 2) + 1, (column * 2) + 1, (average_red, average_green, average_blue))  # setting the rgb values for the diagonal block

            if row == original_height - 1:

                resulting_image.set(
                    (row * 2) + 1, column * 2, (current_red, current_green, current_blue))  # setting the same rgb values as the blocks above for the last row
                if column < original_width:
                    resulting_image.set(
                        (row * 2) + 1, (column * 2) + 1, (current_red, current_green, current_blue))  # setting the same rgb values as the blocks above for the last row

    return resulting_image
