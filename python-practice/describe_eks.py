import boto3

eks = boto3.client("eks")

paginator = eks.get_paginator("list_clusters")

for page in paginator.paginate():
    for cluster_name in page["clusters"]:
        print(cluster_name)