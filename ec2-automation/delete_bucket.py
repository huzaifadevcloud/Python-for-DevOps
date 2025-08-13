import boto3


s3 = boto3.client("s3")  # Needs credentials
response = s3.list_buckets()

def delete_bucket(bucket_name):
    try:
        print("\n📂 Objects in S3 Bucket:")
        list_objects = s3.list_objects_v2(Bucket=bucket_name)

        if "Contents" in list_objects:
            for obj in list_objects["Contents"]:
                s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
                print(f"{obj['Key']}")
        else:
            print("No objects found in the bucket.")

        s3.delete_bucket(Bucket=bucket_name)
        print(f"Bucket {bucket_name} deleted successfully.")

    except Exception as e:
        print(f"Error deleting bucket {bucket_name}: {e}")


for bucket in response['Buckets']:
    print("Available Buckets:")
    bucketName = bucket['Name']
    print(f"{bucketName}")
    delete_bucket(bucketName)



