# 📘 DevOps Automation with Python — Documentation & Blog Resources

This document lists high-quality resources to help you learn how to:
- 🔁 Automate AWS EC2 instance management using Python
- 📥 Fetch logs from Jenkins API
- 💾 Compress and upload logs to Amazon S3 using Python

---

## 🖥️ 1. Manage AWS EC2 Instances with Python (Start/Stop on Schedule)

- [AWS Boto3 Official EC2 Docs (Start/Stop)](https://docs.aws.amazon.com/code-library/latest/ug/python_3_ec2_code_examples.html?utm_source=chatgpt.com)  
- [DevOpsHint - Start/Stop AWS EC2 using Python Boto3](https://www.devopshint.com/start-and-stop-aws-ec2-instance-using-python-boto3/?utm_source=chatgpt.com)  
- [Medium - Lambda Python Script to Start/Stop EC2 Instances](https://medium.com/%40101awscloud/lambda-python-script-to-start-and-stop-ec2-instances-d8dee1921f97?utm_source=chatgpt.com)  
- [GitHub - EC2 Automation Scripts by Pramit](https://github.com/Pramit-on-Cloud079/aws-ec2-automation?utm_source=chatgpt.com)

---

## 📥 2. Fetch Jenkins Logs using Python API

- [CodeRivers - Mastering Jenkins API with Python](https://coderivers.org/blog/jenkins-api-python/?utm_source=chatgpt.com)  
- [python-jenkins Documentation](https://python-jenkins.readthedocs.io/en/latest/?utm_source=chatgpt.com)  
- [python-jenkins Examples](https://python-jenkins.readthedocs.io/en/latest/examples.html?utm_source=chatgpt.com)  
- [IAM-J - Sample Script to Fetch Jenkins Logs using Python](https://iam-j.github.io/jenkins/python-sample-script-to-jenkins/?utm_source=chatgpt.com)

---

## 💾 3. Compress Logs and Upload to S3 with Python

- [StackOverflow - Compress File While Uploading to S3](https://stackoverflow.com/questions/71804163/compress-a-file-while-uploading-to-s3?utm_source=chatgpt.com)  
- [GitHub - aws_logging_handlers (stream logs to S3)](https://github.com/omrikiei/aws_logging_handlers?utm_source=chatgpt.com)  
- [StackOverflow - Stream Data to S3 with aioboto3](https://stackoverflow.com/questions/79164471/whats-the-most-efficient-way-to-stream-data-to-s3-using-aioboto3?utm_source=chatgpt.com)

---

## 📦 BONUS: Processing Existing Logs in S3

- [GitHub - python-s3-logs (Merge & Read Logs)](https://github.com/kmkingsbury/python-s3-logs?utm_source=chatgpt.com)  
- [StackOverflow - Write Logs to S3 from Memory in Python](https://stackoverflow.com/questions/51070891/how-can-i-write-logs-directly-to-aws-s3-from-memory-without-first-writing-to-std?utm_source=chatgpt.com)

---

## ✅ Suggested Learning Plan

1. **Automate EC2 Start/Stop**
   - Use Boto3 or Lambda with CloudWatch Events
   - Follow DevOpsHint blog and clone GitHub scripts

2. **Interact with Jenkins API**
   - Use `python-jenkins` or `requests` to fetch job logs
   - Explore endpoints like `/job/<job>/lastBuild/logText/progressiveText`

3. **Compress and Upload Logs**
   - Use Python’s `gzip` or `tarfile` to compress logs
   - Upload using `boto3.client('s3').put_object(...)`
   - For real-time logging, explore `aws_logging_handlers`

---

