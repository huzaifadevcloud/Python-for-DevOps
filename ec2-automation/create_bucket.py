import boto3

# Create an S3 client
s3 = boto3.client("s3")  # Needs credentials

#Input for bucket name and region
bucketName = str(input("Enter Bucket Name: ")).strip()  # Remove any leading/trailing whitespace
bucketRegion = str(input("Enter AWS Region: "))

#Create a bucket
def create_bucket(bucketName, bucketRegion):
    try:
        s3.create_bucket(Bucket = bucketName, CreateBucketConfiguration={
        'LocationConstraint': bucketRegion})
        print(f"Bucket {bucketName} created successfully.")
    except Exception as e:
        print(f"Error creating bucket {bucketName}: {e}")

# Call the function to create the bucket
create_bucket(bucketName, bucketRegion)

#List existing buckets
response = s3.list_buckets()


for bucket in response["Buckets"]: #here Buckets is in a dictornyand its a key consist to more key init named Name and CreationDate
    try:
        print(bucket["Name"], bucket["CreationDate"])
    except Exception as e:
        print(f"Error accessing bucket {bucket['Name']}: {e}")
