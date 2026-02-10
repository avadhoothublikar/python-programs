import subprocess

result = subprocess.run(["kubectl", "get", "pods", "-n", "production3-training"],
text=True
)

#print("STDOUT:")
print(result.stdout)

