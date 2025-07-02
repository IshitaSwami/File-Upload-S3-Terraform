import os
import boto3
import tempfile
from app import app

def test_health_endpoint():
    client = app.test_client()
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.data == b"OK"

def test_file_upload_to_s3():
    bucket = os.getenv("S3_BUCKET")
    s3 = boto3.client("s3")

    # Create a temporary file to upload
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
        test_filename = os.path.basename(temp_file.name)
        temp_file.write(b"Test file content")

    # Upload using S3 client directly
    with open(temp_file.name, "rb") as f:
        s3.upload_fileobj(f, bucket, test_filename)

    # Verify the file exists in S3
    objects = s3.list_objects_v2(Bucket=bucket)
    keys = [obj['Key'] for obj in objects.get('Contents', [])]
    assert test_filename in keys
