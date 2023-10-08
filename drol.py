import os
import subprocess
import random
import argparse

# Define a list of insults for the "sir" option
insults = ["Maggot", "Scumbag", "Joker", "Worm", "Punk", "Slacker"]

# Function to run a Docker Compose command and handle output


def run_docker_compose(service_dir, command):
    os.chdir(service_dir)
    try:
        result = subprocess.run(
            command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        if result.returncode == 0:
            return "[{}] - Started.".format(service_dir), result.stdout.strip()
        else:
            return "[{}] - Failed to start.".format(service_dir), result.stderr.strip()
    except Exception as e:
        return "[{}] - Failed to start.".format(service_dir), str(e)

# Function to start services


def start_services(services, insult=""):
    status_messages = []
    for service in services:
        status_messages.append("[{}] - Starting...".format(service))
        command = "docker-compose up -d"
        result, output = run_docker_compose(service, command)
        status_messages.append(result)
        status_messages.append(output)
    if insult:
        status_messages.append(insult)
    return status_messages

# Function to check status of services


def check_status(services, insult=""):
    status_messages = []
    for service in services:
        status_messages.append("[{}] - Checking... {}".format(service, insult))
        command = "docker-compose ps -a"
        result, output = run_docker_compose(service, command)
        if "Up" in output and "Exited" not in output:
            status_messages.append("[{}] - Running.".format(service))
        else:
            status_messages.append("[{}] - Stopped.".format(service))
            status_messages.append("Check the logs.")
    return status_messages

# Main function for command-line interface


def main():
    parser = argparse.ArgumentParser(description="Docker Compose CLI tool")
    parser.add_argument("option", choices=[
                        "start", "status", "sir"], help="Select an option")
    args = parser.parse_args()

    insult = insults[random.randint(0, len(insults) - 1)]

    with open("services.txt", "r") as file:
        services = [line.strip() for line in file]

    sir_flag = False

    if args.option == "sir":
        sir_flag = True

    if args.option == "start":
        status_messages = start_services(services, insult if sir_flag else "")
    elif args.option == "status":
        status_messages = check_status(services, insult if sir_flag else "")
    else:
        status_messages = ["Invalid option. Use 'start', 'status', or 'sir'"]

    for message in status_messages:
        print(message)


if __name__ == "__main__":
    main()
