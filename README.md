# Lambda Function for Storing Form Data in DynamoDB

This Lambda function is designed to store form data submitted through an API into a DynamoDB table. It can be used to handle data submissions from a website or application form.

## Setup

To use this Lambda function, you will need to set up the following:

### 1. DynamoDB Table

Create a DynamoDB table named 'your_table_name' with the following schema:

- ID (Number): The unique identifier for each record.
- Email (String): The email address of the user.
- Message (String): The message submitted by the user.
- Name (String): The name of the user.

### 2. AWS Lambda

Create an AWS Lambda function and paste the provided code into the function's code editor. Make sure to configure the necessary permissions for the Lambda function to access 
DynamoDB.

### 3. IAM Permissions 
Ensure the Lambda function has appropriate IAM roles attached, granting it the necessary permissions to write data to the 'your_table_name' DynamoDB table. Verify that the IAM policy allows the Lambda function to access the specific DynamoDB resources, enabling smooth data storage operations.

### 4. API Gateway

Set up an API Gateway endpoint to handle the incoming requests.

## Usage

Once the setup is complete, the Lambda function will automatically store the form data into the DynamoDB table when invoked.

## Example

An example usage of this Lambda function could be a contact form on a website. When a user submits their contact information, this function can be triggered to store the data securely in DynamoDB.
