import boto3

ec2 = boto3.client("ec2")

# paginator = ec2.get_paginator("describe_instances")

# for page in paginator.paginate():
#     for reservation in page["Reservations"]:
#         for instance in reservation["Instances"]:
#             print(
#                 instance["InstanceId"],
#                 instance["State"],
#                 instance["InstanceType"]
#             )

# paginator = ec2.get_paginator("describe_instances")

# for page in paginator.paginate(
#     Filters = [
#         {
#             "Name": "instance-state-name",
#             "Values": ["running"]
#         }
#     ]
# ):
#     for reservation in page["Reservations"]:
#         for instance in reservation["Instances"]:
#             print(instance["InstanceId"])

paginator = ec2.get_paginator("describe_instances")

for page in paginator.paginate(
    Filters = [
        {
            "Name": "instance-state-name",
            "Values": ["stopped"]
        }
    ] 
):
    for reservation in page["Reservations"]:
        for instance in reservation["Instances"]:
            print(instance["InstanceId"])