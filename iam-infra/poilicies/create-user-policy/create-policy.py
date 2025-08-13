import boto3 

# Create an IAM client
client = boto3.client('iam')

Policy_name = str(input("Enter the name of the policy: "))
Role_name = str(input("Enter for whom you want to create the policy: ")).lower()

# Define the policy document paths based on the role
if Role_name == 'developer':
    developer_policy_path = '../policy-documents/DevelopersPolicy.json'
    # Read the policy documents
    with open(developer_policy_path, 'r') as file:
        policy_json = file.read()
    
    key = 'DeveloperPolicy'
    value = 'DeveloperPolicy'

elif Role_name == 'devops':
    devOps_policy_path = '../policy-documents/DevOpsPolicy.json'
    # Read the policy documents
    with open(devOps_policy_path, 'r') as file:
        policy_json = file.read()

    key = 'DevOpsPolicy'
    value = 'DevOpsPolicy'
else:
    raise ValueError("Invalid role name. Please enter 'developer' or 'devops'.")

response = client.create_policy(
    PolicyName=Policy_name,
    PolicyDocument=policy_json,
    Description='',
    Tags=[
        {
            'Key': key,
            'Value': value
        },
    ]
)
print(f"Policy {Policy_name} created successfully for {Role_name}", response['Policy']['Arn'])