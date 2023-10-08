# drol-sergeant

## Drol Sergeant
#### The sergeant who is also a drol, who'll make sure your containers sound off

This Docker Compose CLI Tool is a Python script that allows you to manage and monitor multiple Docker Compose services from the command line. It provides options for starting services, checking their status, and even adding a touch of humor with insults when desired.
### Features

- Start multiple Docker Compose services in a specified order.
- Check the status of Docker Compose services.
- Add a touch of humor by enabling the "sir" option.

### Prerequisites

- Python 3.6 or higher.
- Docker installed and running on your system.
- Docker Compose installed on your system.

### Installation

1. Clone this repository to your local machine:
```bash
git clone https://github.com/APoniatowski/drol-sergeant.git
```

2. Navigate to the project directory:
```bash
cd drol-sergeant
```

## Usage

#### Command-Line Options
- `start`: Start Docker Compose services.
```bash
python drol.py start
```
- `status`: Check the status of Docker Compose services.
```bash
python drol.py status
```
- `sir`: Check the status of Docker Compose services.
```bash
python drol.py start sir
```
#### or 
```bash
python drol.py status sir
```

## Configuration

1. Create a file named `services.txt` in the project directory and list the names of the services you want to manage, one per line.

    Example `services.txt`:
```txt
service1
service2
service3
```
2. Customize the list of insults in the script by modifying the `insults` list.

## Unit Testing

The project includes unit tests for key functions using the `unittest` framework. You can run the tests using the following command:
```bash
python -m unittest drol_test.py
```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Implement your changes and write unit tests if necessary.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.

## License

This project is licensed under the BSD License - see the LICENSE file for details.
