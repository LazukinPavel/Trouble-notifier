import json
import os
import tempfile
import boto3

from config import BUCKET_NAME


def write_json(data, filename):
    with open(filename, 'a') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def upload_to_s3(filename, folder='telegram_chat_ids/'):
    s3 = boto3.resource('s3')
    if filename.startswith('/tmp/'):
        s3_filename = filename[5:]
    else:
        s3_filename = filename
    s3.meta.client.upload_file(filename, BUCKET_NAME, f"{folder}{filename}", ExtraArgs={'ACL': 'public-read'})

    return {
        "status": "success",
        "s3_filename": s3_filename,
        "s3_folder": folder
    }


def get_file_link(filename, folder='telegram_chat_ids/'):
    client = boto3.client('s3')
    if filename.startswith('/tmp/'):
        filename = filename[5:]
    filename = f'{folder}{filename}.json'
    print(filename)
    # content = client.head_object(Bucket=BUCKET_NAME, Key=filename)
    bucket_location = client.get_bucket_location(Bucket=BUCKET_NAME)
    filepath = f"https://s3-{bucket_location['LocationConstraint']}.amazonaws.com/{BUCKET_NAME}/{filename}"

    return filepath

