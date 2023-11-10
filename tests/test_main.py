import unittest
from main import app

class TestApp(unittest.TestCase):
    def setUp(self):
        # set up a testing client
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        # Test the index route
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_task_route(self):
        # Test the add_task route (passing)
        response = self.app.post('/add_task', data={'task': 'Test Task'})
        self.assertEqual(response.status_code, 302)  # 302 is the HTTP status code for a redirect

        # Check if the task is added by following the redirect
        redirect_response = self.app.get(response.headers['Location'])
        self.assertIn(b'Test Task', redirect_response.data)

    def test_remove_task_route(self):
        # Add a task to test removal (passing)
        self.app.post('/add_task', data={'task': 'Task to Remove'})

        # Test the remove_task route (passing)
        response = self.app.get('/remove_task/0')
        self.assertEqual(response.status_code, 302)  # 302 is the HTTP status code for a redirect

        # Check if the task is removed
        self.assertNotIn(b'Task to Remove', response.data)

    def test_nonexistent_route(self):
        # Test a nonexistent route (passing)
        response = self.app.get('/nonexistent_route')
        self.assertEqual(response.status_code, 404)

    def test_invalid_add_task_route(self):
        # Test the add_task route with invalid data (failing)
        response = self.app.post('/add_task', data={'invalid_key': 'Invalid Task'})
        self.assertEqual(response.status_code, 400)  # 400 is the HTTP status code for a bad request

        # Check if the task is not added
        self.assertNotIn(b'Invalid Task', response.data)

if __name__ == '__main__':
    unittest.main()