from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Student


class StudentCRUDTests(APITestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            roll_number="STU001",
            course="Computer Science",
            age=20,
        )
        self.list_create_url = reverse("student-list-create")
        self.detail_url = reverse("student-detail", kwargs={"pk": self.student.pk})

    def test_get_all_students(self):
        """Test GET /api/students/ (List students)"""
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["roll_number"], "STU001")

    def test_post_create_student(self):
        """Test POST /api/students/ (Create new student)"""
        payload = {
            "first_name": "Jane",
            "last_name": "Smith",
            "email": "jane.smith@example.com",
            "roll_number": "STU002",
            "course": "Data Science",
            "age": 22,
        }
        response = self.client.post(self.list_create_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 2)
        self.assertEqual(response.data["email"], "jane.smith@example.com")

    def test_get_student_by_id(self):
        """Test GET /api/students/<id>/ (Retrieve student by ID)"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.student.id)
        self.assertEqual(response.data["first_name"], "John")

    def test_put_update_student(self):
        """Test PUT /api/students/<id>/ (Full update of student)"""
        payload = {
            "first_name": "Johnny",
            "last_name": "Doe Updated",
            "email": "johnny.updated@example.com",
            "roll_number": "STU001",
            "course": "Software Engineering",
            "age": 21,
        }
        response = self.client.put(self.detail_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.student.refresh_from_db()
        self.assertEqual(self.student.first_name, "Johnny")
        self.assertEqual(self.student.course, "Software Engineering")
        self.assertEqual(self.student.age, 21)

    def test_patch_partial_update_student(self):
        """Test PATCH /api/students/<id>/ (Partial update of student)"""
        payload = {
            "course": "Artificial Intelligence",
        }
        response = self.client.patch(self.detail_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.student.refresh_from_db()
        self.assertEqual(self.student.course, "Artificial Intelligence")
        # Ensure other fields remain unchanged
        self.assertEqual(self.student.first_name, "John")

    def test_delete_student(self):
        """Test DELETE /api/students/<id>/ (Delete student by ID)"""
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Student.objects.filter(pk=self.student.pk).exists())

    def test_get_student_not_found(self):
        """Test GET with non-existent student ID returns 404"""
        invalid_url = reverse("student-detail", kwargs={"pk": 99999})
        response = self.client.get(invalid_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
