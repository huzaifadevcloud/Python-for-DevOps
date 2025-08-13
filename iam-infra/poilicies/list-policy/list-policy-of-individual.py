import boto3

iam = boto3.client('iam')

user_name = str(input("Enter the IAM user name to list policies for: "))

response = iam.list_attached_user_policies(UserName=user_name)

print(f"Policies attached to user '{user_name}':")
for i, policy in enumerate(response['AttachedPolicies'], start=1):
    print(f"{i}. {policy['PolicyName']} ({policy['PolicyArn']})")

print(f"Total policies: {len(response['AttachedPolicies'])}")
