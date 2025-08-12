import boto3 # Import the Boto3 library for AWS SDK
import secrets # Import the secrets module for generating secure random numbers
import string # Import the string module for string operations
import time # Import the time module for time-related functions

# Input an IAM user 
userName = str(input("Enter the IAM user name you want to create: "))
# Generate a random strong password
password_characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(password_characters) for i in range(16))


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


# Function to create an IAM user with a login profile
# This function creates an IAM user and sets a login profile with a generated password
# It also updates the password policy to enforce strong passwords
def create_iam_user(user_name):
    try:
        iam.create_user(UserName=user_name)
        # Create a login profile for the user with the generated password
        iam.create_login_profile(UserName=user_name, Password=password, PasswordResetRequired=True)
        print(f"IAM user '{user_name}' and '{password}'created successfully.")
        update_password_policy()  # Update the password policy to enforce strong passwords
        lst_iam_users()  # List all IAM users
    except iam.exceptions.EntityAlreadyExistsException:
        print(f"User '{user_name}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to create an access key for the IAM user *(for CLI)
def create_access_key(user_name):
    try:
        # Create an access key for the user
        response = iam.create_access_key(UserName=user_name)
        access_key = response['AccessKey']
        print(f"Access Key ID: {access_key['AccessKeyId']}")
        print(f"Secret Access Key: {access_key['SecretAccessKey']}")
    except Exception as e:
        print(f"An error occurred while creating access key: {e}")

# Function to delete an IAM user
# This function deletes an IAM user if it exists
# It handles exceptions if the user does not exist or if there is an error during deletion
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

# Function to update the password policy
def update_password_policy():
    try:
        # Attach an account password policy for 90-day expiration
        # This is set at the account level, not per-user
        iam.update_account_password_policy(
        MinimumPasswordLength=12,
        RequireSymbols=True,
        RequireNumbers=True,
        RequireUppercaseCharacters=True,
        RequireLowercaseCharacters=True,
        AllowUsersToChangePassword=True,
        MaxPasswordAge=90
        )
        print("Password policy updated successfully.")
    except Exception as e:
        print(f"An error occurred while updating the password policy: {e}")

create_iam_user(userName)
create_access_key(userName)  # Create an access key for the user
delete_iam_user(userName)  # Delete the IAM user