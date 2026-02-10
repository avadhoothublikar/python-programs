import boto3

s3 = boto3.client("s3")

response = s3.list_objects(
    Bucket = "postgresql-db",
    Prefix = "dev-db/"
)

for obj in response.get("Contents", []):
    print(obj["Key"], obj ["Size"])

# initcontainer:
# - name: s3-object
#   image: aws-cli
#   command:
#     - aws s3 cp s3:bucket_name/tmp/abc.txt /data/abc.txt
# volumeMounts:
#     - name: data
#       mountPath: /data


