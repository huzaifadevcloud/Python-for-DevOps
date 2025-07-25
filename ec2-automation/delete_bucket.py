import boto3


s3 = boto3.client("s3")  # Needs credentials
response = s3.list_buckets()

def delete_bucket(bucket_name):
    try:
        s3.delete_bucket(Bucket=bucket_name)
        print(f"Bucket {bucket_name} deleted successfully.")
    except Exception as e:
        print(f"Error deleting bucket {bucket_name}: {e}")


delete_bucket("response") 