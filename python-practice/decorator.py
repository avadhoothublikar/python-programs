def log_execution(func):
    def wrapper():
        print("Logs of app1")
        func()
    return wrapper

@log_execution
def deployment_log():
    print("Deployed app1")

deployment_log()