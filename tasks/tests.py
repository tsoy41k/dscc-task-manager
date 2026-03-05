from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task


class TaskTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_user_login(self):
        login = self.client.login(username='testuser', password='testpass123')
        self.assertTrue(login)

    def test_create_task(self):
        task = Task.objects.create(
            title="Test task",
            description="Test description",
            completed=False,
            user=self.user
        )
        self.assertEqual(task.title, "Test task")

    def test_update_task(self):
        task = Task.objects.create(
            title="Old title",
            user=self.user
        )
        task.title = "New title"
        task.save()
        self.assertEqual(task.title, "New title")

    def test_delete_task(self):
        task = Task.objects.create(
            title="Delete task",
            user=self.user
        )
        task_id = task.id
        task.delete()
        self.assertFalse(Task.objects.filter(id=task_id).exists())

    def test_task_list_page(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)