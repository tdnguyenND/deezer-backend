from django.core.files.storage import DefaultStorage
from google.cloud.storage.blob import _API_ACCESS_ENDPOINT

from deezer import settings


class GoogleStorageService:
    def __init__(self, path_prefix):
        self.path_prefix = path_prefix
        self._init_private_storage()
        self._init_public_storage()

    def _init_private_storage(self):
        self._private_storage = DefaultStorage()

    def _init_public_storage(self):
        self._public_storage = DefaultStorage()
        self._public_storage.default_acl = 'publicRead'

    def _get_file_url(self, storage, file_path):
        if not file_path:
            return ""
        validated_file_path = storage.url(file_path).replace(_API_ACCESS_ENDPOINT, "").split("/", 2)[-1]
        bucket_name = storage.bucket.name
        full_url = _API_ACCESS_ENDPOINT.replace("://", "://{}.".format(bucket_name)) + "/" + validated_file_path
        return full_url

    def convert_private_file_path_to_signed_url(self, *args, **kwargs):
        return self._get_file_url(self._private_storage, *args, **kwargs)

    def get_public_url(self, file_path):
        return self._get_file_url(self._public_storage, file_path)

    def upload_private_file(self, *args, **kwargs):
        return self.upload_file(self._private_storage, *args, **kwargs)

    def upload_public_file(self, *args, **kwargs):
        return self.upload_file(self._public_storage, *args, **kwargs)

    def upload_file(self, storage, output_file_path, file):
        file_path = f'{self.path_prefix}{output_file_path}'
        storage.save(file_path, file)
        return self._get_file_url(storage, file_path)

    def delete_public_file(self, file_path):
        return self.delete_file(self._public_storage, file_path)

    def delete_private_file(self, file_path):
        return self.delete_file(self._private_storage, file_path)

    @staticmethod
    def delete_file(storage, file_path):
        bucket = storage.bucket
        return bucket.delete_blob(file_path)


google_storage_song_service = GoogleStorageService(settings.GS_SONG_BASE_DIR)
google_storage_picture_service = GoogleStorageService(settings.GS_PICTURE_BASE_DIR)
