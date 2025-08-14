#This script retrieves the login profile of an IAM user and optionally resets their password. Because if you forget password you cannot get it
#you need to reset it and also check whether account alias exists or not, if not it will create one.

import boto3
import string
import secrets

# Input an IAM user 
userName = input("Enter the IAM user name you want to get login details: ")

# Generate a random strong password
password_characters = string.ascii_letters + string.digits + string.punctuation
new_password = ''.join(secrets.choice(password_characters) for i in range(16))


# Create an IAM client
iam = boto3.client('iam')

def get_iam_user_login_details():
    try:
    
        # List the account alias
        account_alias = iam.list_account_aliases()['AccountAliases']
        
        if account_alias:
            print(f"Account Alias: {account_alias[0]}")
        else:
            print("⚠ No account alias found.")
            if input("Do you want to create one? (yes/no): ").lower() == 'yes':
                new_alias = input("Enter the new account alias: ")
                iam.create_account_alias(AccountAlias=new_alias)
                print(f" Account alias '{new_alias}' created successfully.")
            else:
                print("No account alias created.")

        # List all IAM users
        response = iam.list_users()
        users = response['Users']

        for user in users:
                # Check if the user exists
            if user['UserName'] == userName:
                userDetails = iam.get_login_profile(UserName=userName)

                if userDetails is not None:
                    print(f"Login Profile for {userName}:")
                    
                    try:
                        # Optionally, reset the password
                        iam.update_login_profile (
                        UserName=userName,
                        Password=new_password,
                        PasswordResetRequired=True
                        )
                        print(f"🔄 Password updated for user '{userName}' and Your New password: {new_password}")
                        
                    except iam.exceptions.NoSuchEntityException:
                        print(f"No login profile found for user {userName}.")
                        return None
                            
            return user
    except Exception as e:
        print(f"An error occurred while listing IAM users: {e}")

get_iam_user_login_details()