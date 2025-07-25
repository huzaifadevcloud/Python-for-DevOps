import boto3

Instance_id = str(input("Enter the EC2 Instance ID to start: "))
region = str(input("Enter the AWS Region: "))

ec2 = boto3.resource('ec2')

def start_instance(Instance_id):
    try:
        instance = ec2.Instance(Instance_id)
        response = instance.start()
        print(f"Instance {Instance_id} is starting...")
        return response
    except Exception as e:
        print(f"Error starting instance {Instance_id}: {e}")

start_instance(Instance_id)