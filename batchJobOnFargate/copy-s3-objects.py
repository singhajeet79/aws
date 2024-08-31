import boto3

def copy_s3_objects(source_bucket, destination_bucket):
    """Copies objects from one S3 bucket to another.

    Args:
        source_bucket (str): The name of the source S3 bucket.
        destination_bucket (str): The name of the destination S3 bucket.
    """

    s3 = boto3.client('s3')

    paginator = s3.get_paginator('list_objects_v2')
    for page in paginator.paginate(Bucket=source_bucket):
        for obj in page['Contents']:
            key = obj['Key']
            copy_source = {
                'Bucket': source_bucket,
                'Key': key
            }

            s3.copy(copy_source, destination_bucket, key)
            print(f"Copied {key} from {source_bucket} to {destination_bucket}")

if __name__ == "__main__":
    source_bucket = "your-source-bucket-ajeet-01"
    destination_bucket = "your-destination-bucket-ajeet-01"

    copy_s3_objects(source_bucket, destination_bucket)
