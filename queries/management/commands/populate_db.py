import random

from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Doctor, Hospital, MedicalRecord, Nurse, Patient


class Command(BaseCommand):
    help = "Populate the database with fake data"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create doctors
        for _ in range(random.randint(5, 10)):
            Doctor.objects.create(
                name=fake.name(),
                specialization=fake.job(),
                contact_number=fake.phone_number(),
            )

        # Create nurses
        for _ in range(random.randint(5, 10)):
            Nurse.objects.create(name=fake.name(), contact_number=fake.phone_number())

        # Create patients
        doctors = list(Doctor.objects.all())
        nurses = list(Nurse.objects.all())

        for _ in range(random.randint(5, 10)):
            patient = Patient.objects.create(
                name=fake.name(),
                age=random.randint(1, 100),
                nurse=random.choice(nurses),
            )
            patient.doctor.set(
                random.sample(doctors, k=random.randint(1, len(doctors)))
            )
            patient.save()

        # Create hospitals
        patients = list(Patient.objects.all())
        for _ in range(random.randint(5, 10)):
            hospital = Hospital.objects.create(
                patient=random.choice(patients), nurse=random.choice(nurses)
            )
            hospital.doctor.set(
                random.sample(doctors, k=random.randint(1, len(doctors)))
            )

        # Create medical records
        for patient in Patient.objects.all():
            MedicalRecord.objects.create(
                patient=patient, diagonses=fake.text(), prescription=fake.text()
            )

        self.stdout.write(self.style.SUCCESS("Database populated successfully!"))
