from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import (
    TaskType,
    Position,
    Task,
)


class PositionModelTest(TestCase):
    def setUp(self) -> None:
        self.worker = get_user_model().objects.create_user(
            username="test_worker",
            password="worker1qazcde3",
        )
        self.client.force_login(self.worker)

    def test_position_str(self) -> None:
        position = Position.objects.create(
            name="Test Position",
        )

        self.assertEquals(
            str(position),
            f"{position.name}"
        )

    def test_update_position_with_valid_data(self) -> None:
        position = Position.objects.create(
            name="Test Position",
        )
        new_name = "Test Position Updated"
        response = self.client.post(
            reverse("manager:position-update", kwargs={"pk": position.id}),
            data={"name": new_name},
        )

        self.assertEquals(response.status_code, 302)

    def test_update_position_with_not_valid_data(self) -> None:
        position = Position.objects.create(
            name="Test Position",
        )
        new_name = "Test Position !@#$%^"
        response = self.client.post(
            reverse("manager:position-update", kwargs={"pk": position.id}),
            data={"name": new_name},
        )

        self.assertEquals(response.status_code, 200)

    def test_delete_position(self) -> None:
        position = Position.objects.create(
            name="Test Position",
        )
        response = self.client.post(
            reverse("manager:position-delete", kwargs={"pk": position.id})
        )

        self.assertEquals(response.status_code, 302)
        self.assertFalse(
            Position.objects.filter(id=position.id).exists()
        )


class WorkerModelTest(TestCase):
    def setUp(self) -> None:
        self.worker = get_user_model().objects.create_user(
            username="test_worker",
            password="worker1qazcde3",
            first_name="Test First",
            last_name="Test Last",
        )
        self.client.force_login(self.worker)

    def test_worker_str(self) -> None:
        self.assertEquals(
            str(self.worker),
            f"{self.worker.username} ({self.worker.first_name} "
            f"{self.worker.last_name})"
        )

    def test_create_worker_with_position(self) -> None:
        username = "test_worker_create"
        password = "worker1qazcde3"
        position = Position.objects.create(
            name="Test Position",
        )

        worker = get_user_model().objects.create_user(
            username=username,
            password=password,
            position=position,
        )

        self.assertEquals(worker.username, username)
        self.assertTrue(worker.check_password(password))
        self.assertEquals(worker.position, position)

    def test_delete_worker(self) -> None:
        position = Position.objects.create(
            name="Test Position",
        )
        worker = get_user_model().objects.create_user(
            username="test_worker_delete",
            password="worker1qazcde3",
            position=position,
        )
        response = self.client.post(
            reverse("manager:worker-delete", kwargs={"pk": worker.id})
        )

        self.assertEquals(response.status_code, 302)
        self.assertFalse(
            get_user_model().objects.filter(id=worker.id).exists()
        )

    def test_worker_get_absolute_url(self) -> None:
        self.assertEquals(
            self.worker.get_absolute_url(),
            "/workers/1/"
        )


class TaskTypeModelTest(TestCase):
    def setUp(self) -> None:
        self.worker = get_user_model().objects.create_user(
            username="test_worker",
            password="worker1qazcde3",
        )
        self.client.force_login(self.worker)

    def test_task_type_str(self) -> None:
        task_type = TaskType.objects.create(
            name="Test Task Type"
        )

        self.assertEquals(
            str(task_type),
            f"{task_type.name}"
        )

    def test_update_task_type(self) -> None:
        task_type = TaskType.objects.create(
            name="Test Task Type"
        )
        new_name = "Test Task Type Updated"
        response = self.client.post(
            reverse("manager:task-type-update", kwargs={"pk": task_type.id}),
            data={"name": new_name}
        )

        self.assertEquals(response.status_code, 302)

    def test_delete_task_type(self) -> None:
        task_type = TaskType.objects.create(
            name="Test Task Type"
        )
        response = self.client.post(
            reverse("manager:task-type-delete", kwargs={"pk": task_type.id}),
        )

        self.assertEquals(response.status_code, 302)
        self.assertFalse(
            TaskType.objects.filter(id=task_type.id).exists()
        )


class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        task_type = TaskType.objects.create(
            name="Test Task Type"
        )
        Task.objects.create(
            name="Test Task",
            description="Test Description",
            deadline="2023-12-12",
            is_completed=False,
            priority="Low",
            task_type=task_type,
        )

    def setUp(self) -> None:
        self.worker = get_user_model().objects.create_user(
            username="test_worker",
            password="worker1qazcde3",
        )
        self.client.force_login(self.worker)

    def test_task_str(self) -> None:
        task = Task.objects.get(id=1)

        self.assertEquals(
            str(task),
            task.name
        )

    def test_task_get_absolute_url(self) -> None:
        task = Task.objects.get(id=1)

        self.assertEquals(
            task.get_absolute_url(),
            "/tasks/1/"
        )
