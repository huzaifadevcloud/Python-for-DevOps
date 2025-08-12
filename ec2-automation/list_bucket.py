import boto3

s3 = boto3.client("s3")
response = s3.list_buckets()

# Save the names of the buckets in a list
bucket_names = [] 

for bucket in response["Buckets"]: #here Buckets is in a dictornyand its a key consist to more key init named Name and CreationDate
    try:
        print(bucket["Name"], bucket["CreationDate"])
        bucket_names.append(bucket["Name"])
    except Exception as e:
        print(f"Error accessing bucket {bucket['Name']}: {e}")


def delete_bucket(bucket_name):
    try:
        s3.delete_bucket(Bucket=bucket_name)
        print(f"Bucket {bucket_name} deleted successfully.")
    except Exception as e:
        print(f"Error deleting bucket {bucket_name}: {e}")

for bucketName in bucket_names:
    try:
        print(f"Deleting bucket: {bucketName}")
        delete_bucket(bucketName)
    except Exception as e:
        print(f"Error deletion of bucket: {bucketName} - {e}")
print("Bucket deletion process completed.")