import boto3 # Import the Boto3 library for AWS SDK
import time # Import the time module for time-related functions

# Input an IAM user 
userName = str(input("Enter the IAM user name you want to delete: "))

# Create an IAM client
iam = boto3.client('iam')

def lst_iam_users():
    try:
        # List all IAM users
        response = iam.list_users()
        users = response['Users']
        print("List of IAM Users:")
        for user in users:
            print(user['UserName'])
    except Exception as e:
        print(f"An error occurred while listing IAM users: {e}")

# Function to delete an IAM user
# This function deletes an IAM user if it exists
def delete_iam_user(user_name):

    # Wait before deleting the user
    print("Waiting 30 seconds before deleting the IAM user...")
    time.sleep(30)
    # Delete the login profile
    try:
        iam.delete_login_profile(UserName=user_name)  
        print(f"Login profile for user '{user_name}' deleted successfully.")
    except iam.exceptions.NoSuchEntityException:
        print(f"Login profile for user '{user_name}' does not exist.")

    # Delete the key associated with the user
    try:
        access_keys = iam.list_access_keys(UserName=user_name)['AccessKeyMetadata']
        for key in access_keys:
            iam.delete_access_key(UserName=user_name, AccessKeyId=key['AccessKeyId']) # AccessKeyMetadata is a list of dictionaries containing information which is stored in key during iteration thats why using key['AccessKeyId'] to get access key
            print(f"Access keys for user '{user_name}' deleted successfully.")
    except iam.exceptions.NoSuchEntityException:
        print(f"No access keys found for user '{user_name}'.")
        
    # Finally, delete the user
    try:
        iam.delete_user(UserName=user_name)
        print(f"IAM user '{user_name}' deleted successfully.")
    except iam.exceptions.NoSuchEntityException:
        print(f"User '{user_name}' does not exist.")
    
    # List all IAM users after deletion 
    lst_iam_users()  


delete_iam_user(userName)