import platform
import datetime


def greet():
    print("=" * 50)
    print("        Welcome to Jenkins CI/CD Demo")
    print("=" * 50)


def system_info():
    print("\nSystem Information")
    print("-" * 20)
    print(f"Operating System : {platform.system()}")
    print(f"OS Version       : {platform.release()}")
    print(f"Python Version   : {platform.python_version()}")
    print(f"Current Time     : {datetime.datetime.now()}")


def security_tasks():
    print("\nCybersecurity Learning Goals")
    print("-" * 30)

    tasks = [
        "Learn Jenkins",
        ]

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def summary():
    print("\nPipeline Status")
    print("-" * 20)
    print(" Repository cloned successfully")
    print(" Python script executed")
    print(" Jenkins build completed successfully")


if __name__ == "__main__":
    greet()
    system_info()
    security_tasks()
    summary()

    print("\n Hello from Jenkins! Your first pipeline works.")
