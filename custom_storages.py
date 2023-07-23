from djang.conf import settings
from storages.backends.s3boto3 import S3BotoStorage


class StaticStorage(S3BotoStorage):
    location.settings.STATICFILES_LOCATION


class MediaStorage(S3BotoStorage):
    location.settings.MEDIAFILES_LOCATION