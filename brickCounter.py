# notes: Brick counter
# modified: 04 04 17 08:56 Bhaumik mistry

import colorPicker


def displayColorInfo():
        """ This method is for the available colors
        and color selection

        Return: colorList(data_type): Some desc
        """
        # for color list use this
        print ('List of available colors')
        colorList = colorPicker.getColorAndValue()
        # print colorList
        return colorList


def testxx(image, gray_image, pixValArray):
        """ Some Description of the method
        Args:
            image(data_type): Some desc
            gray_image(data_type): Some desc
            pixValArray(data_type): Some desc
        """
        # TODO: RENAME the file
        # displayColorInfo()
        (h, w, rgb) = image.shape[:3]
        for pix in pixValArray:
            text = pix
