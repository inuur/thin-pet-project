import os
from abc import ABC

from storages.backends.s3boto3 import S3Boto3Storage


class ClientDocsStorage(S3Boto3Storage, ABC):
    bucket_name = os.getenv('YANDEX_CLIENT_DOCS_BUCKET_NAME')
    file_overwrite = False
    location = 'media'
