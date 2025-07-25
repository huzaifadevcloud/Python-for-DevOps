import boto3

s3 = boto3.client("s3")  # Needs credentials
response = s3.list_buckets()


for bucket in response["Buckets"]: #here Buckets is in a dictornyand its akey consist to more key init named Name and CreationDate
    try:
        print(bucket["Name"], bucket["CreationDate"])
    except Exception as e:
        print(f"Error accessing bucket {bucket['Name']}: {e}")


def delete_bucket(bucket_name):
    try:
        s3.delete_bucket(Bucket=bucket_name)
        print(f"Bucket {bucket_name} deleted successfully.")
    except Exception as e:
        print(f"Error deleting bucket {bucket_name}: {e}")


delete_bucket("response") 