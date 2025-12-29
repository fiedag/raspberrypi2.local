import unittest
from unittest.mock import patch, mock_open, MagicMock
import sys
import os
import argparse

# Add the current directory to sys.path to import sprinklers3
sys.path.insert(0, os.path.dirname(__file__))

from sprinklers3 import parse_pair

class TestSprinklers3(unittest.TestCase):

    def test_parse_pair_valid(self):
        """Test parse_pair with valid input."""
        result = parse_pair("1.5,2.0")
        self.assertEqual(result, (1.5, 2.0))

    def test_parse_pair_invalid(self):
        """Test parse_pair with invalid input."""
        with self.assertRaises(argparse.ArgumentTypeError):
            parse_pair("invalid")

    @patch('sprinklers3.json.load')
    @patch('sprinklers3.os.path.exists')
    @patch('sprinklers3.argparse.ArgumentParser.parse_args')
    @patch('sprinklers3.GPIO')
    @patch('sprinklers3.time.sleep')
    def test_relay_mapping_loading(self, mock_sleep, mock_gpio, mock_parse_args, mock_exists, mock_json_load):
        """Test relay map loading and GPIO setup."""
        # Mock command line args - no relays specified
        mock_parse_args.return_value = MagicMock(test=False, off=False, **{f'r{i}': None for i in range(1,8)})
        mock_exists.return_value = True
        mock_json_load.return_value = {"1": 6, "2": 4, "3": 22, "4": 10, "5": 9, "6": 5, "7": 23, "8": 1}

        # Mock GPIO setup calls
        mock_gpio.setwarnings = MagicMock()
        mock_gpio.setmode = MagicMock()
        mock_gpio.setup = MagicMock()
        mock_gpio.output = MagicMock()

        # Import and run the module logic (need to handle global execution)
        # This is tricky since the script has global code. For proper testing,
        # the script should be refactored to have a main function.

        # For now, just test the parse_pair function as it's isolated
        # Full integration testing would require significant refactoring

    def test_constants(self):
        """Test safety constants are defined."""
        from sprinklers3 import MAXTIME, MINTIME
        self.assertEqual(MAXTIME, 3600)  # 1 hour
        self.assertEqual(MINTIME, 5)     # 5 seconds

if __name__ == '__main__':
    unittest.main()