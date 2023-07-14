from django.test import TestCase

from manager.forms import WorkerCreationForm
from manager.models import Position


class WorkerFormTest(TestCase):
    def test_worker_creation_form_is_valid(self) -> None:
        position = Position.objects.create(name="Test Position")
        form_data = {
            "username": "test_worker",
            "password1": "worker1qazcde3",
            "password2": "worker1qazcde3",
            "first_name": "Test First",
            "last_name": "Test Last",
            "position": position,
            "bio": "Test Bio",
        }
        form = WorkerCreationForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEquals(form.cleaned_data, form_data)
