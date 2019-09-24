#!/usr/bin/python3

import os
import google.cloud.storage
import sys

print(sys.argv[1])
print('main.py runnning ')
# Create a storage client.
storage_client = google.cloud.storage.Client()

# TODO (Developer): Replace this with your Cloud Storage bucket name.
bucket_name = 'python-file-upload-test'
bucket = storage_client.get_bucket(bucket_name)

# TODO (Developer): Replace this with the name of the local file to upload.
source_file_name = sys.argv[1]
blob = bucket.blob(os.path.basename(source_file_name))

# Upload the local file to Cloud Storage.
blob.upload_from_filename(source_file_name)

print('File {} uploaded to {}.'.format(
    source_file_name,
    bucket))
