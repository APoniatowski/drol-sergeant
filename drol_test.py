import unittest
from unittest.mock import patch, Mock
import drol


class TestDockerComposeTool(unittest.TestCase):
    @patch('subprocess.run')
    def test_run_docker_compose(self, mock_run):
        mock_run.return_value.returncode = 0
        mock_run.return_value.stdout = "Docker Compose started successfully"
        service_dir = '/path/to/service'
        command = 'docker-compose up -d'

        result, output = drol.run_docker_compose(
            service_dir, command)

        self.assertEqual(result, "[{}] - Started.".format(service_dir))
        self.assertEqual(output, "Docker Compose started successfully")

    def test_start_services(self, mock_run):
        # Prepare a list of services and an insult
        services = ['service1', 'service2', 'service3']
        insult = "Maggot"

        # Prepare a mock subprocess.run to simulate Docker Compose
        mock_run.side_effect = [
            Mock(returncode=0, stdout="Service 1 started."),
            Mock(returncode=0, stdout="Service 2 started."),
            Mock(returncode=1, stderr="Service 3 failed to start."),
        ]

        # Call the start_services function
        status_messages = drol.start_services(services, insult)

        # Check if the function returns the expected status messages
        expected_messages = [
            "[service1] - Starting...",
            "[service1] - Started.",
            "[service2] - Starting...",
            "[service2] - Started.",
            "[service3] - Starting...",
            "[service3] - Failed to start.",
            "Maggot"  # Insult message
        ]
        self.assertEqual(status_messages, expected_messages)

    def test_check_status(self, mock_run):
        # Prepare a list of services and an insult
        services = ['service1', 'service2', 'service3']
        insult = "Scumbag"

        # Prepare a mock subprocess.run to simulate Docker Compose
        mock_run.side_effect = [
            Mock(returncode=0, stdout="service1   Up 10 seconds"),
            Mock(returncode=0, stdout="service2   Up 20 seconds"),
            Mock(returncode=1, stderr="service3   Exited (1) 30 seconds ago"),
        ]

        # Call the check_status function
        status_messages = drol.check_status(services, insult)

        # Check if the function returns the expected status messages
        expected_messages = [
            "[service1] - Checking... Scumbag",
            "[service1] - Running.",
            "[service2] - Checking... Scumbag",
            "[service2] - Running.",
            "[service3] - Checking... Scumbag",
            "[service3] - Stopped.",
            "Check the logs."  # Log message for the stopped service
        ]
        self.assertEqual(status_messages, expected_messages)


if __name__ == '__main__':
    unittest.main()
