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
    img = MyImage(src.size)                     # create a blank copy of src dimensions

    for x in range(width):                      # looping over the pixels using x,y coordinatess
        for y in range(height):      
            r, g, b = src.get(x, y)             # get the rgb components at x,y coordinates 
            if red == True:
                r = 0
            if green == True:
                g = 0
            if blue == True:
                b = 0
            else:
                r = 0    
            img.set(x, y, (r, g, b))            # use MyImage setter function to set new rgb values
    return img                 


def rotations(src: MyImage) -> MyImage:
    """Returns an image containing the 4 rotations of src.

    The new image has twice the dimensions of src. src is not modified.

    Args:
    - src: the image whose rotations have to be stored and returned.

    Returns:
    an image twice the size of src and containing the 4 rotations of src.
    """
    original_width = src.size[0]
    original_height = src.size[1]

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
    mask = list(map(int,mask))                  # produces a list of int values of the file contents
    n = mask[0]                                 # n: matrix size for nxn
    mask = mask[1:]                             # listing matrix values in a list

    mask_sum = 0                                # calculating sum of mask values for weighted average
    for i in mask:
        mask_sum += i

    origin = n//2                               # center of mask appears at n//2,n//2 position in matrix

    for x in range(width):                      # looping over the pixels of the image
        for y in range(height):
            # weighted r,g,b values
            wr = 0
            wg = 0
            wb = 0

            for i in range(n):                  # looping over rows and columns of mask ie a nxn matrix
                for j in range(n):
                    index = n * i + j           # index of element we want to access from mask list
                    x_ = x + i - origin
                    y_ = y + j - origin

                    if x_ >= 0 and x_ < width and y_ >= 0 and y < height:       # check edges
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

    original_width = src.size[0]
    original_height = src.size[1]

    new_width = original_width * 2
    new_height = original_height * 2

    resulting_image = MyImage((new_width, new_height))

    for row in range(original_width):
        for column in range(original_height):
            # looping over each pixel to set rgb values

            rgb_value = src.get(row, column)

            # 1st image (rotated 90 degrees anticlockwise) on 1st row, 1st column
            resulting_image.set(row * 2, column * 2, rgb_value)

    for row in range(new_width):
        for column in range(new_height):

            if column % 2 != 0:  # blank columns
                if column != new_width:
                    red1 = (resulting_image.get(row, column - 1))[0]
                    green1 = (resulting_image.get(row, column - 1))[1]
                    blue1 = (resulting_image.get(row, column - 1))[2]

                    red2 = (resulting_image.get(row, column + 1))[0]
                    green2 = (resulting_image.get(row, column + 1))[1]
                    blue2 = (resulting_image.get(row, column + 1))[2]

                    average_red = int((red1 + red2) / 2)
                    average_green = int((green1 + green2) / 2)
                    average_blue = int((blue1 + blue2) / 2)

                    resulting_image.set(
                        row, column, (average_red, average_green, average_blue))
                    # resulting_image.set(row, column, 0.5 *
                    #                     (resulting_image.get(row, column - 1) + resulting_image.get(row, column + 1)))
                else:
                    resulting_image.set(
                        row, column, (int(red1 / 2), int(green1 / 2), int(blue1 / 2)))
                    # resulting_image.set(row, column, 0.5 *
                    #                     (resulting_image.get(row, column - 1)))
                    # if row != new_width:
                    #     resulting_image.set(row, column, 0.5 * (resulting_image.get(
                    #         row - 1, column) + resulting_image.get(row + 1, column)))
                    # else:
                    #     resulting_image.set(row, column, 0.5 * (resulting_image.get(
                    #         row - 1, column)))
            # else:
            if row % 2 != 0:  # blank rows
                if row != new_height:
                    red1 = (resulting_image.get(row - 1, column))[0]
                    green1 = (resulting_image.get(row - 1, column))[1]
                    blue1 = (resulting_image.get(row - 1, column))[2]

                    red2 = (resulting_image.get(row + 1, column))[0]
                    green2 = (resulting_image.get(row + 1, column))[1]
                    blue2 = (resulting_image.get(row + 1, column))[2]

                    average_red = int((red1 + red2) / 2)
                    average_green = int((green1 + green2) / 2)
                    average_blue = int((blue1 + blue2) / 2)

                    resulting_image.set(
                        row, column, (average_red, average_green, average_blue))
                    # resulting_image.set(row, column, 0.5 *
                    #                     (resulting_image.get(row, column - 1) + resulting_image.get(row, column + 1)))
                else:
                    resulting_image.set(
<<<<<<< HEAD
                        row, column, (average_red, average_green, average_blue))
            if column % 2 != 0:  # blank columns
                if column != new_width - 1:

                    red_left, green_left, blue_left = resulting_image.get(
                        row, column - 1)
                    red_right, green_right, blue_right = resulting_image.get(
                        row, column + 1)

                    average_red = int((red_left + red_right) / 2)
                    average_green = int((green_left + green_right) / 2)
                    average_blue = int((blue_left + blue_right) / 2)

                    resulting_image.set(
                        row, column, (average_red, average_green, average_blue))
                else:
                    resulting_image.set(
                        row, column, (int(red_left / 2), int(green_left / 2), int(blue_left / 2)))
            if column % 2 != 0:  # blank columns
                if column != new_width - 1:

                    red_left, green_left, blue_left = resulting_image.get(
                        row, column - 1)
                    red_right, green_right, blue_right = resulting_image.get(
                        row, column + 1)

                    average_red = int((red_left + red_right) / 2)
                    average_green = int((green_left + green_right) / 2)
                    average_blue = int((blue_left + blue_right) / 2)

                    resulting_image.set(
                        row, column, (average_red, average_green, average_blue))
                else:
                    resulting_image.set(
                        row, column, (int(red_left / 2), int(green_left / 2), int(blue_left / 2)))
    # src.show()
    # resulting_image.show()
=======
                        row, column, (int(red1 / 2), int(green1 / 2), int(blue1 / 2)))
            #         resulting_image.set(row, column, 0.5 * (resulting_image.get(
            #             row - 1, column) + resulting_image.get(row + 1, column)))
            #     else:
            #         resulting_image.set(row, column, 0.5 * (resulting_image.get(
            #             row - 1, column)))
>>>>>>> parent of 2fe6ada (Merge branch 'main' of https://github.com/CS-201-Spring-2023/hw1-hw1-l2-group-6)

    return resulting_image
