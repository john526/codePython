from PIL import Image

import numpy as np
def deletebackground(path):
    openLogo = Image.open(path).convert('RGBA') # path
    xFile = np.array(openLogo)
    r, g, b, a = np.rollaxis(xFile, axis=-1)
    r[a == 0] = 255
    g[a == 0] = 255
    b[a == 0] = 255
    xFile = np.dstack([r, g, b, a])

    return Image.fromarray(xFile)