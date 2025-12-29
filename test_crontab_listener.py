import unittest
from unittest.mock import patch, MagicMock, mock_open
import json
import socket
import sys
import os

# Add the current directory to sys.path
sys.path.insert(0, os.path.dirname(__file__))

from crontab_listener import CrontabManager, MessageListener

class TestCrontabManager(unittest.TestCase):

    def setUp(self):
        self.manager = CrontabManager()

    @patch('crontab_listener.subprocess.run')
    def test_get_crontab_success(self, mock_run):
        """Test successful crontab reading."""
        mock_run.return_value = MagicMock(returncode=0, stdout='* * * * * command\n', stderr='')
        result = self.manager.get_crontab()
        self.assertEqual(result, '* * * * * command\n')
        mock_run.assert_called_once()

    @patch('crontab_listener.subprocess.run')
    def test_get_crontab_no_crontab(self, mock_run):
        """Test reading when no crontab exists."""
        mock_run.return_value = MagicMock(returncode=1, stdout='', stderr='no crontab for user')
        result = self.manager.get_crontab()
        self.assertEqual(result, '')

    @patch('crontab_listener.subprocess.run')
    def test_set_crontab_success(self, mock_run):
        """Test successful crontab writing."""
        mock_run.return_value = MagicMock(returncode=0, stdout='', stderr='')
        self.manager.set_crontab('* * * * * new_command\n')
        mock_run.assert_called_once()

    @patch('crontab_listener.subprocess.run')
    def test_add_job_valid(self, mock_run):
        """Test adding a valid cron job."""
        mock_run.return_value = MagicMock(returncode=0, stdout='* * * * * old_command\n', stderr='')
        self.manager.add_job('0 9 * * *', '/path/to/script.py')
        # Verify set_crontab was called with updated content

    def test_add_job_invalid_schedule(self):
        """Test adding job with invalid schedule."""
        with self.assertRaises(ValueError):
            self.manager.add_job('invalid schedule', 'command')

    @patch('crontab_listener.subprocess.run')
    def test_remove_job_with_pattern(self, mock_run):
        """Test removing jobs matching a pattern."""
        mock_run.return_value = MagicMock(returncode=0, stdout='* * * * * command1\n* * * * * command2\n', stderr='')
        removed = self.manager.remove_job('command1')
        self.assertEqual(removed, 1)

    def test_validate_schedule_valid(self):
        """Test valid cron schedule validation."""
        self.assertTrue(self.manager._validate_schedule('0 9 * * 1'))
        self.assertTrue(self.manager._validate_schedule('*/5 * * * *'))

    def test_validate_schedule_invalid(self):
        """Test invalid cron schedule validation."""
        self.assertFalse(self.manager._validate_schedule('invalid'))
        self.assertFalse(self.manager._validate_schedule('0 9'))  # Too few parts

    def test_list_jobs(self):
        """Test listing and parsing cron jobs."""
        with patch.object(self.manager, 'get_crontab', return_value='# Comment\n0 9 * * 1 /path/to/script\n'):
            jobs = self.manager.list_jobs()
            self.assertEqual(len(jobs), 1)
            self.assertEqual(jobs[0]['command'], '/path/to/script')

class TestMessageListener(unittest.TestCase):

    def setUp(self):
        self.listener = MessageListener()

    def test_handle_message_add_valid(self):
        """Test handling add action with valid data."""
        with patch.object(self.listener.crontab, 'add_job') as mock_add:
            result = self.listener.handle_message('{"action": "add", "schedule": "0 9 * * *", "command": "test"}')
            self.assertEqual(result['status'], 'ok')
            mock_add.assert_called_once_with(schedule='0 9 * * *', command='test', comment=None)

    def test_handle_message_add_with_comment(self):
        """Test handling add action with comment."""
        with patch.object(self.listener.crontab, 'add_job') as mock_add:
            result = self.listener.handle_message('{"action": "add", "schedule": "0 9 * * *", "command": "test", "comment": "Test job"}')
            mock_add.assert_called_once_with(schedule='0 9 * * *', command='test', comment='Test job')

    def test_handle_message_remove(self):
        """Test handling remove action."""
        with patch.object(self.listener.crontab, 'remove_job', return_value=2) as mock_remove:
            result = self.listener.handle_message('{"action": "remove", "pattern": "old"}')
            self.assertEqual(result['status'], 'ok')
            self.assertEqual(result['removed'], 2)

    def test_handle_message_list(self):
        """Test handling list action."""
        with patch.object(self.listener.crontab, 'list_jobs', return_value=[{'command': 'test'}]) as mock_list:
            result = self.listener.handle_message('{"action": "list"}')
            self.assertEqual(result['status'], 'ok')
            self.assertEqual(result['jobs'], [{'command': 'test'}])

    def test_handle_message_get(self):
        """Test handling get action."""
        with patch.object(self.listener.crontab, 'get_crontab', return_value='crontab content') as mock_get:
            result = self.listener.handle_message('{"action": "get"}')
            self.assertEqual(result['status'], 'ok')
            self.assertEqual(result['crontab'], 'crontab content')

    def test_handle_message_set(self):
        """Test handling set action."""
        with patch.object(self.listener.crontab, 'set_crontab') as mock_set:
            result = self.listener.handle_message('{"action": "set", "content": "new content"}')
            self.assertEqual(result['status'], 'ok')
            mock_set.assert_called_once_with('new content')

    def test_handle_message_unknown_action(self):
        """Test handling unknown action."""
        result = self.listener.handle_message('{"action": "unknown"}')
        self.assertEqual(result['status'], 'error')
        self.assertIn('Unknown action', result['message'])

    def test_handle_message_invalid_json(self):
        """Test handling invalid JSON."""
        result = self.listener.handle_message('invalid json')
        self.assertEqual(result['status'], 'error')
        self.assertIn('Invalid JSON', result['message'])

    def test_handle_message_missing_field(self):
        """Test handling missing required field."""
        result = self.listener.handle_message('{"action": "add", "schedule": "0 9 * * *"}')  # Missing command
        self.assertEqual(result['status'], 'error')
        self.assertIn('Missing field', result['message'])

if __name__ == '__main__':
    unittest.main()