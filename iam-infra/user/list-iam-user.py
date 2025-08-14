import boto3

# Create an IAM client
iam = boto3.client('iam')

response = iam.list_users()
users = response['Users']
print(f"List of IAM Users:{users[0]['UserName']}")