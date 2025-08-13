import boto3
import os
from datetime import datetime, timedelta


# ==========================
# AWS Credentials (No aws configure needed)
# ==========================
accessKey = input("Enter AWS Access Key: ").strip()
secretKey = input("Enter AWS Secret Key: ").strip()
if not accessKey or not secretKey:
    raise ValueError("AWS Access Key and Secret Key are required.")
regionName = input("Enter AWS Region (default: us-east-1): ").strip()
bucketName = input("Enter S3 Bucket Name: ").strip()
if not regionName:
    regionName = "us-east-1"  # Default region if not provided

AWS_ACCESS_KEY = accessKey
AWS_SECRET_KEY = secretKey
REGION_NAME =  regionName
BUCKET_NAME = bucketName
LOGS_FOLDER_LOCAL = "/home/huzaifa/devOps/python_automation_projects/python-masterclass/iam-infra/poilicies/list-policy"


# ==========================
# S3 Client
# ==========================
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=REGION_NAME
)

# ==========================
# Create Bucket if it doesn't exist
# ==========================
try:
    s3_client.create_bucket(
        Bucket=BUCKET_NAME,
        CreateBucketConfiguration={"LocationConstraint": REGION_NAME}
    )
    print(f"Bucket '{BUCKET_NAME}' created.")
except Exception as e:
    print(f"error: {e}")

# ==========================
# Upload Logs from Last Week
# ==========================
one_week_ago = datetime.now() - timedelta(days=7)



for file_name in os.listdir(LOGS_FOLDER_LOCAL):
    file_path = os.path.join(LOGS_FOLDER_LOCAL, file_name)

    if os.path.isfile(file_path):
        #modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
        #if modified_time >= one_week_ago:  # Only last week's files
        s3_key = f"logs/{file_name}"
        s3_client.upload_file(file_path, BUCKET_NAME, s3_key)
        print(f"📤 Uploaded: {file_name}")
        

# ==========================
# List All Objects in the Bucket
# ==========================
print("\n📂 Objects in S3 Bucket:")
response = s3_client.list_objects_v2(Bucket=BUCKET_NAME)

if "Contents" in response:
    for obj in response["Contents"]:
        print(f" - {obj['Key']} ({obj['Size']} bytes)")
else:
    print("No objects found in the bucket.")
