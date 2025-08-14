import boto3

iam = boto3.client('iam')

# List IAM policies attached to a specific user and roles in the aws-account
user_name = str(input("Enter the IAM user name to list policies for: "))
account_id = "936335589231"
policies = iam.list_attached_user_policies(UserName=user_name)

roles = iam.list_roles()['Roles']
for role in roles:
        role_name = role['RoleName']
        print(f"Roles are {role_name}.")

print(f"Policies attached to user '{user_name}':")

for i, policy in enumerate(policies['AttachedPolicies'], start=1):
    print(f"{i}. {policy['PolicyName']} ({policy['PolicyArn']})")

print(f"Total policies: {len(policies['AttachedPolicies'])}")
