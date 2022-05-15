import json
import os

import numpy as np
import requests
from django.core.files import File

from geo.models import ThinSection
from ..models import ImageAnalyze
from ..util.image import image_stream_from_array


def analyze_by_type(analysis_type, thin_section_id):
    service_endpoint = f"{os.getenv('NEURAL_NETWORK_SERVICE_URL')}{analysis_type}/{thin_section_id}/"
    response = requests.get(service_endpoint)
    json_response = json.loads(response.content)
    image_byte_array = np.asarray(json_response['img'])
    image_stream = image_stream_from_array(image_byte_array)
    image_analyze = ImageAnalyze.objects.create(
        thin_section=thin_section_id,
        image_type=analysis_type,
        report=None
    )
    thin_section = ThinSection.objects.get(pk=thin_section_id)
    file_name = f'{thin_section.name}{analysis_type}.jpg'
    image_analyze.image.save(file_name, File(image_stream))
    image_stream.close()
    return image_analyze


def color_analyze(thin_section_id):
    return analyze_by_type('color', thin_section_id)


def cover_analyze(thin_section_id):
    return analyze_by_type('cover', thin_section_id)


def full_analysis(thin_section_id):
    pass
