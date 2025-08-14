import boto3

# Create an IAM client
iam = boto3.client('iam')

response = iam.list_users()
users = response['Users']

#print=(f"Iam Users:{users[0]['UserName']}")
for user in users:
    print(user['UserName'])