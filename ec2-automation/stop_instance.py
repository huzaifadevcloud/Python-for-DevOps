import boto3

Instance_id = str(input("Enter the EC2 Instance ID to stop: "))
region = str(input("Enter the AWS Region: "))

ec2 = boto3.resource('ec2')

def stop_instance(Instance_id):
    try:
        instance = ec2.Instance(Instance_id)
        response = instance.stop()
        print(f"Instance {Instance_id} is stopping...")
        return response
    except Exception as e:
        print(f"Error stopping instance {Instance_id}: {e}")


stop_instance(Instance_id)