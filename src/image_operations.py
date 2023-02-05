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
    mask = list(map(int,mask))                  # produces a list of int values of the file contents
    n = mask[0]                                 # n: matrix size for nxn
    mask = mask[1:]                             # listing matrix values in a list

    mask_sum = 0                                # calculating sum of mask values for weighted average
    for i in mask:
        mask_sum += i

    for x in range(width):
        for y in range(height):
            r_sum = 0
            g_sum = 0
            b_sum = 0
            for i in range(n):
                for j in range(n):
                    x_ = x + i - (n // 2)
                    y_ = y + j - (n // 2)
                    if 0 <= x_ < width and 0 <= y_ < height:
                        r, g, b = src.get(x_, y_)
                        r_sum += r * mask[n * i + j]
                        g_sum += g * mask[n * i + j]
                        b_sum += b * mask[n * i + j]
                        
            if average:
                img.set(x, y, (r_sum // mask_sum, g_sum // mask_sum, b_sum // mask_sum))
            else:
                img.set(x, y, (r_sum, g_sum, b_sum))

    return img    

    # for x in range(width):                      # looping over the pixels of the image using x,y coordinates
    #     for y in range(height):  
    #         r, g, b = src.get(x,y)

    #         index = math.ceil((n**2)/2)         # index of origin in mask list
    #         dist = n - n//2                     # distance from origin in mask

    #         wr = r * mask[index]
    #         wg = g * mask[index]
    #         wb = b * mask[index]

    #         # trasversing around the mask origin
    #         for d in range(dist):

    #             up = index - (d+1)*n            # index of value above origin in mask list
    #             down = index + (d+1)*n          # index of value below origin in mask list
    #             left = index - d                # index of value to the left of origin in mask list
    #             right = index + d               # index of value to the right of origin in mask list

    #             # check from top
    #             if y - d >= 0:
    #                 r, g, b = src.get(x,y-d)
    #                 wr += r * mask[up]
    #                 wg += g * mask[up]
    #                 wb += b * mask[up]

    #             # check from bottom
    #             if y + d <= height:
    #                 r, g, b = src.get(x,y+d)
    #                 wr += r * mask[down]
    #                 wg += g * mask[down]
    #                 wb += b * mask[down]    

    #             # check from right
    #             if x + d <= width:
    #                 r, g, b = src.get(x+d,y)
    #                 wr += r * mask[right]
    #                 wg += g * mask[right]
    #                 wb += b * mask[right]

    #             # check from left
    #             if x - d >= 0:
    #                 r, g, b = src.get(x-d,y)
    #                 wr += r * mask[left]
    #                 wg += g * mask[left]
    #                 wb += b * mask[left]  

    #             # check diagonals
    #             if  y - d >= 0 and x + d <= width:  # check from top and right
    #                 r, g, b = src.get(x+d,y-d)
    #                 wr += r * mask[up+1]
    #                 wg += g * mask[up+1]
    #                 wb += b * mask[up+1]

    #             if  y - d >= 0 and x - d >= 0:      # check from top and left
    #                 r, g, b = src.get(x-d,y-d)
    #                 wr += r * mask[up-1]
    #                 wg += g * mask[up-1]
    #                 wb += b * mask[up-1]    

    #             if  y + d <= height and x + d <= width: # check from bottom and right
    #                 r, g, b = src.get(x+d,y+d)
    #                 wr += r * mask[down+d+1]
    #                 wg += g * mask[down+d+1]
    #                 wb += b * mask[down+d+1]    

    #             if  y - d >= 0 and x + d <= width:  # check from bottom and left
    #                 r, g, b = src.get(x-d,y+d)
    #                 wr += r * mask[down-d-1]
    #                 wg += g * mask[down-d-1]
    #                 wb += b * mask[down-d-1]    

    #         if average == True:                     # mask with weighted average
    #             img.set(x, y, (wr//mask_sum, wg//mask_sum, wb//mask_sum))
    #         else:                                   # mask with weighted sum
    #             img.set(x, y, (wr, wg, wb))

    # return img  


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

            rgb_value = src.get(row, column)

            resulting_image.set(row * 2, column * 2, rgb_value)

    for row in range(new_height):
        for column in range(new_width):

            if row % 2 != 0:  # blank rows
                if row != new_height - 1:
                    red_left, green_left, blue_left = resulting_image.get(
                        row - 1, column)
                    red_right, green_right, blue_right = resulting_image.get(
                        row + 1, column)
                    
                    average_red = int((red_left + red_right) / 2)
                    average_green = int((green_left + green_right) / 2)
                    average_blue = int((blue_left + blue_right) / 2)

                    resulting_image.set(
                        row, column, (average_red, average_green, average_blue))

                else:
                    resulting_image.set(
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
    resulting_image.show()

    return resulting_image
