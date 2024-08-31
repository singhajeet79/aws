### Fargate Service with AWS Batch for S3 Object Copying
\
Leveraging the serverless capabilities of AWS Batch with Fargate compute environment, we efficiently executed a task to copy S3 objects from a source bucket to a destination bucket.\
\
**Methodology:**\
\
**Environment Setup:**
- Launched an EC2 instance.
- Installed Docker and Docker Desktop.
- Created a Python script and a requirements.txt file.
- Generated a Dockerfile using docker init and customized it as needed.\

**Container Image Creation:**
- Created a private ECR repository.
- Created an IAM role with AmazonEC2ContainerRegistryFullAccess permissions and attached it to the EC2 instance.
- Logged in to the ECR.
- Built, tagged, and pushed the Docker image to the ECR repository.\

**AWS Batch Service Configuration:**
- Created a compute environment using Fargate.
- Created a security group for the compute environment with no inbound rules and default outbound rules.
- Created an IAM role with AmazonS3FullAccess permissions for the batch job.
- Created a job queue associated with the compute environment.
- Created a job definition using Fargate orchestration.\

**Batch Job Submission and Verification:**
- Submitted a new batch job using the created job definition.
- Verified the status of the batch job by checking the destination bucket contents and CloudWatch logs.\

### Results
\
The AWS Batch service successfully copied S3 objects from the source bucket to the destination bucket using the Fargate compute environment. The batch job executed as expected, demonstrating the effectiveness of AWS Batch for managing containerized workloads.

### Key Points:
* **Fargate Benefits:** Fargate provides a serverless and scalable solution for running containerized applications.\
* **Job Definition:** The job definition specifies the container image, compute resources, and environment variables.\
* **IAM Roles:** Appropriate IAM roles are essential for granting permissions to access S3 buckets and run ECS tasks.\
* **CloudWatch Logs:** Used for monitoring and troubleshooting batch job execution.\


