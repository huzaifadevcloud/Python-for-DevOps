import boto3

# Create an IAM client
client = boto3.client('iam')

user_name = str(input("Enter the name of the user to attach the policy: "))
policy_arn = str(input("Enter the ARN of the policy to attach: "))

# Attach the created policy to the specified role    
def attach_policy(): 
    try:
        response = client.attach_user_policy(UserName=user_name, PolicyArn=policy_arn)
        return response
    except Exception as e:
        print(f"Error attaching policy: {e}")


attach_policy()
print(f"Policy {policy_arn} attached successfully to user {user_name}.")