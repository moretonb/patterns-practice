import unittest
import json
from deepdiff import DeepDiff
from app.tests.base import api_client
from app.tests.data.task_builder import TaskBuilder
from app.src.data.tasks.commands.delete_task import delete_task

class WhenGetTaskList(unittest.TestCase):
    def setUp(self):
        self.expected_task = TaskBuilder().create().build()
        self.response = api_client.get('/tasks/')
        self.tasks = json.loads(self.response.data.decode('utf-8').replace("'", "\""))

    def tearDown(self):
        delete_task(self.expected_task["id"])

    def test_then_the_status_code_is_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_then_the_body_contains_the_expected_tasks(self):
        expected_body = {'tasks': [self.expected_task]}
        self.assertEqual(DeepDiff(expected_body, self.tasks), {})
