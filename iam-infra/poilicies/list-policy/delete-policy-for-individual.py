import boto3


iam = boto3.client('iam')

UserName = str(input("Enter the IAM user name to delete policies for: "))

def delete_user_policies(UserName):
    try:
        # List attached policies for the user
        attached_policies = iam.list_attached_user_policies(UserName=UserName)
        
        if not attached_policies['AttachedPolicies']:
            print(f"No attached policies found for user '{UserName}'.")
            return
        
        # Detach each policy
        for policy in attached_policies['AttachedPolicies']:
            iam.detach_user_policy(UserName=UserName, PolicyArn=policy['PolicyArn'])
            iam.delete_policy(PolicyArn=policy['PolicyArn'])
            print(f"Detached and Deleted policy {policy['PolicyName']} from user {UserName}.")
        
        print(f"All policies detached from user '{UserName}'.")
    except Exception as e:
        print(f"Error deleting policies for user {UserName}: {e}")

def detach_role_from_user(UserName):
    try:
        # List roles attached to the user
        roles = iam.list_roles()['Roles']
        
        for role in roles:
            role_name = role['RoleName']
            iam.detach_role_policy(RoleName=role_name, PolicyArn=role['Arn'])
            print(f"Detached role {role_name} from user {UserName}.")
        
        print(f"All roles detached from user '{UserName}'.")
    except Exception as e:
        print(f"Error detaching roles for user {UserName}: {e}")

# Call the function to delete user policies
delete_user_policies(UserName)
detach_role_from_user(UserName)