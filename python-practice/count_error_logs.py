error = {}

with open("app.log") as f:
    for line in f:
        if "error" in line.lower():
            key = line.strip()
            error[key] = error.get(key,0) + 1
print(error)