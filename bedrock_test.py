import os
from litellm import completion

# Set AWS credentials from environment
os.environ["AWS_PROFILE"] = "bedrock-profile"
os.environ["AWS_REGION"] = "us-east-1"

response = completion(
    model="bedrock/us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    messages=[{"role": "user", "content": "Hello, how are you?"}]
)

print(response)
