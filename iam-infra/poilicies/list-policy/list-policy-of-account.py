import boto3

# Create an IAM client
client = boto3.client('iam')
print(f"Listing all IAM policies in the account {client}...")

def list_policies(client):
    try:
        all_policies = []
        response = client.list_policies(
            Scope='All',                  # 'All', 'AWS', or 'Local'
            OnlyAttached=True,           # True = only attached policies / False = all policies of aws account
            PathPrefix='/',               # Filter by path
            PolicyUsageFilter='PermissionsPolicy',  # 'PermissionsPolicy' or 'PermissionsBoundary'
            MaxItems=500                  # Limit per page
        )
        all_policies.extend(response['Policies'])
        # Pretty-print with gaps #Instead of list all policy metadata only printing important details for readability
        for idx, policy in enumerate(all_policies): #enumerate helps you iterate in list 
            print(f"{idx}. Policy Name : {policy['PolicyName']}")
            print(f"   ARN         : {policy['Arn']}")
            print(f"   ID          : {policy['PolicyId']}")
            print(f"   Path        : {policy['Path']}")
            print("-" * 25)
        return response['Policies']
    except Exception as e:
        print(f"Error listing policies: {e}")
        return None

list_policies(client)
