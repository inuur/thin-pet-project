from PIL.Image import Image
from io import BytesIO

import numpy as np


def image_stream_from_array(np_array):
    img_object = Image.fromarray((np_array * 255).astype(np.uint8))
    image_byte_stream = BytesIO()
    img_object.save(image_byte_stream, 'JPEG')
    image_byte_stream.seek(0)
    return image_byte_stream
