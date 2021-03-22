from deezer.services import google_storage_song_service, google_storage_picture_service
from deezer.utils import generate_filename_with_timestamp


def upload_song_to_storage(song_file):
    storage_name = generate_filename_with_timestamp(song_file)
    return google_storage_song_service.upload_public_file(storage_name, song_file)


def upload_picture_to_storage(picture_file):
    storage_name = generate_filename_with_timestamp(picture_file)
    return google_storage_picture_service.upload_public_file(storage_name, picture_file)
