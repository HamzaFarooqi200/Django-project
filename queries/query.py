from models import Patient, Hospital, Doctor, MedicalRecord, Nurse
from django.db.models import Max, Count, Avg, Sum, Min
from django.db.models.functions import TruncMonth
from datetime import timedelta, date, timezone, datetime

# **Task 1**

# - Retrieve all patients admitted on a specific date.

pateints =  Patient.objects.filter(date_admitted = '2024-08-15 06:25:40.006197')

# - Get the names of all doctors who have patients with a specific diagnosis.

patients_with_diagnosis = Patient.objects.filter(patientsrecords__diagonses__icontains='Flu')
doctors_with_patients = Doctor.objects.filter(doctors__in=patients_with_diagnosis).distinct()
doctor_names = doctors_with_patients.values_list('name')
print(doctor_names)

# - Find all patients treated by a particular nurse.

pateints = Patient.objects.filter(nurse='1')

# - Retrieve the contact number of the doctor for a given patient.

doc_number =  Patient.objects.get(id=1).doctor.values_list('contact_number', flat=True)

# - Get the total number of patients admitted to the hospital.

total_patients = Patient.objects.count()

# - Find the patients who are not assigned to any nurse.

patients = Patient.objects.filter(nurse__isnull=True)

# - Retrieve the names of nurses who have patients with a specific prescription.

rec = Patient.objects.filter(patientsrecords__prescription__icontains="drink")
nurse = Nurse.objects.filter(nurses__in=rec)

# - Get the average age of patients in the hospital.

averageAge = Patient.objects.all().aggregate(Avg('age'))

# - Find the most recently admitted patient.

recent = Patient.objects.all().aggregate(Max('date_admitted'))

# - Retrieve all doctors who have more than five patients.

doctors = Doctor.objects.annotate(num_patients=Count('doctors')).filter(num_patients__gt=5)

# - Find the patients who have been admitted for more than a week.


one_week_ago = timezone.now() - timedelta(weeks=1)
patients = Patient.objects.filter(date_admitted__lte=one_week_ago)

# - Get the number of patients assigned to each nurse.

nurses = Nurse.objects.annotate(num_patients=Count('nurses'))

# - Retrieve the names of patients who have a specific doctor.

pat = Patient.objects.filter(doctor__id = 1)
p = pat.values_list('name',flat=True)

# - Find the doctors who specialize in a specific medical field.

doc = Doctor.objects.filter(specialization = "Heart")

# - Get the names of patients treated by a doctor with a specific specialization.

pat = Patient.objects.filter(doctor__in=Doctor.objects.filter(specialization = "Heart")).values_list('name', flat=True)

# - Find the nurses who have not been assigned any patients.

nurse = Nurse.objects.exclude(id__in=Patient.objects.values_list('nurse_id', flat=True)).values_list('name', flat=True)

# - Retrieve the latest medical record for a given patient.

rec = MedicalRecord.objects.filter(patient=1).latest('id')

# - Get the names of patients with a specific diagnosis.

name = Patient.objects.filter(patientsrecords__diagonses__icontains='Heart').values_list('name', flat=True)

# - Find the doctors who have patients of a certain age group.

name =  Doctor.objects.filter(doctors__age__gte=20,doctors__age__lte=40).values_list('name', flat=True)

# - Retrieve all patients with a specific prescription.

pat = Patient.objects.filter(patientsrecords__prescription ='Panadol')

# - Find the nurses who have patients with a specific age.

name =  Nurse.objects.filter(nurses__age__gte=20,nurses__age__lte=40).values_list('name', flat=True)

# - Get the total number of medical records in the system.

records = MedicalRecord.objects.all()

# - Retrieve the names of patients treated by a nurse with a specific contact number.

patients = Patient.objects.filter(nurse__contact_number='036217863784687')

# - Find the patients who are treated by more than one doctor.

pat = Patient.objects.annotate(num_doc=Count('doctor')).filter(num_doc__gt=1)

# - Get the names of doctors who have treated patients with a specific prescription.

doc = Doctor.objects.filter(doctors__patientsrecords__prescription__icontains='Panadol').values_list('name', flat=True)

# - Find the patients who have not been assigned to any doctor.

pat = Patient.objects.filter(doctor__isnull=True)

# - Retrieve the doctors who have patients admitted on a specific date.


spec_date = date(2024,9,23)
doc = Doctor.objects.filter(doctors__date_admitted__date=spec_date).values_list('name', flat=True)

# - Get the number of patients admitted each month.

patients_per_month = Patient.objects.annotate(month=TruncMonth('date_admitted')).values('month').annotate(count=Count('id')).order_by('month')

# - Find the patients with the highest age in the hospital.

maxi = Patient.objects.aggregate(max_age=Max('age'))['max_age']
pat = Patient.objects.filter(age = maxi)

# - Retrieve all nurses who have patients admitted on a specific date.

nurse = Nurse.objects.filter(nurses__date_admitted = spec_date).values_list('name',flat=True)

# - Find the doctors who have patients with a specific age.

doctors = Doctor.objects.filter(doctors__age=30).values_list('name', flat=True)

# - Get the number of patients treated by each doctor.

doc = Doctor.objects.annotate(num_pat=Count('doctors')).values_list('name','num_pat')

# - Retrieve the names of patients with a specific age.

pat = Patient.objects.filter(age= 20).values_list('name',flat=True)

# - Find the nurses who have patients with a specific diagnosis.

Nurse = Nurse.objects.filter(nurses__patientsrecords__diagonses = "Heart")

# - Get the names of patients treated by a nurse with a specific contact number.

pat = Patient.objects.filter(nurse__contact_number='031548525145').values_list('name', flat=True)

# - Find the doctors who have not been assigned any patients.

doc = Doctor.objects.filter(doctors__isnull=True)

# - Retrieve the patients who have medical records with a specific prescription.

pat = Patient.objects.filter(patientsrecords__prescription__icontains="Panadol")

# - Get the average age of patients treated by each doctor.

doc = Doctor.objects.annotate(avg_age=Avg('doctors__age')).values_list('name', 'avg_age')

# - Find the doctors who have patients with a specific prescription.

doc = Doctor.objects.filter(doctors__patientsrecords__prescription__icontains="Panadol")

# - Retrieve the names of patients treated by a doctor with a specific contact number.

pat = Patient.objects.filter(doctor__contact_number='031548525145').values_list('name', flat=True)

# - Find the nurses who have patients with a specific prescription.

nurse = Nurse.objects.filter(nurses__patientsrecords__prescription__icontains="Panadol")

# - Get the total number of patients treated by nurses in a specific specialization.

doc = Doctor.objects.filter(specialization= 'Heart').annotate(num_pat=Count('doctors')).values_list('name', 'num_pat')

# - Retrieve the patients who have not been assigned to any nurse.

pat = Patient.objects.filter(nurse__isnull=True)

# - Find the doctors who have patients admitted for more than a week.

one_week_ago = timezone.now() - timedelta(weeks=1)
doctors = Doctor.objects.filter(doctors__date_admitted__lte=one_week_ago).distinct()


# - Get the names of patients with a specific diagnosis treated by a specific doctor.

pat = Patient.objects.filter(patientsrecords__diagonses__icontains='Diabetes', doctor__name='Dr. Smith').values_list('name',flat=True)

# - Find the nurses who have patients with a specific age group.

name =  Nurse.objects.filter(nurses__age__gte=20,nurses__age__lte=40)

# - Retrieve the doctors who have patients with a specific diagnosis and age group.

name =  Doctor.objects.filter(doctors__age__gte=20,doctors__age__lte=40,doctors__patientsrecords__diagonses="Heart")

# - Get the number of patients treated by each doctors in a specific specialization.

doc = Doctor.objects.filter(specialization="Cardiology").annotate(num_pat=Count('doctors')).values_list('name','num_pat')

# - Find the patients who have been treated by more than one nurse.

pat = Patient.objects.annotate(num_nurse=Count('nurse')).filter(num_nurse__gt=1)

# - Retrieve the names of doctors who have patients with a specific diagnosis and age group.

name =  Doctor.objects.filter(doctors__age__gte=20,doctors__age__lte=40,doctors__patientsrecords__diagonses="Heart").values_list('name', flat=True)



# **Task 2*******************************************************************************




# - Select all patients with their associated doctors and nurses.

pat = Patient.objects.select_related('nurse').prefetch_related('doctor').all()

# - Select all patients admitted after a specific date.

specific_date = datetime(2024, 1, 1)
patients_admitted_after = Patient.objects.filter(date_admitted__gt=specific_date)

# - Count the total number of patients.

pat = Patient.objects.aggregate(count_pat=Count('name'))['count_pat']

# - Count the total number of patients with a specific age.

pat = Patient.objects.filter(age=30).count()

# - Select all patients with their associated doctors and nurses prefetched.

pat = Patient.objects.prefetch_related('doctor','nurse').all()

# - Count the total number of doctors associated with each patient.

pat = Patient.objects.annotate(total_doc=Count('doctor')).values_list('name', 'total_doc')

# - Sum the ages of all patients.

pat = Patient.objects.aggregate(sum_age=Sum('age'))

# - Select all patients along with the number of doctors associated with each.

pat = Patient.objects.annotate(total_doc=Count('doctor')).values_list('name', 'total_doc')

# - Select all patients along with their medical records, if available.

pat = Patient.objects.prefetch_related('patientsrecords').all()

# - Count the total number of nurses associated with each patient.

pat = Patient.objects.annotate(total_nurse=Count('nurse')).values_list('name', 'total_nurse')

# - Select all patients with their associated nurses and the nurses' contact numbers.

pat = Patient.objects.select_related('nurse').values('name', 'nurse__contact_number')

# - Select all patients along with the total number of medical records for each.

pat = Patient.objects.annotate(num_rec=Count('patientsrecords')).values_list('name', 'num_rec')

# - Select all patients with their diagnoses and prescriptions, if available.

pat = Patient.objects.select_related('patientsrecords').values('name','patientsrecords__diagonses', 'patientsrecords__prescription')

# - Count the total number of patients admitted in a specific year.

pat = Patient.objects.filter(date_admitted__year=2024).count()

# - Select all patients along with their doctors' specializations.

pat = Patient.objects.select_related('doctor').values('name', 'doctor__specialization')

# - Select all patients along with the count of medical records for each.

pat = Patient.objects.annotate(num_records=Count('patientsrecords')).values('name', 'num_records')

# - Select all doctors with the count of patients they are associated with.

doc = Doctor.objects.annotate(num_patients=Count('doctors')).values('name', 'num_patients')

# - Select all patients along with the count of nurses they are associated with.

pat = Patient.objects.annotate(num_nurses=Count('nurse')).values('name', 'num_nurses')

# - Annotate the average age of patients.

pat = Patient.objects.aggregate(avg_age=Avg('age'))['avg_age']

# - Annotate the maximum age of patients.

pat = Patient.objects.aggregate(max_age=Max('age'))['max_age']

# - Annotate the minimum age of patients.

pat = Patient.objects.aggregate(min_age=Min('age'))['min_age']

# - Select all patients along with the earliest admission date.

e_date = Patient.objects.aggregate(min_date=Min('date_admitted'))['min_date']
pat = Patient.objects.filter(date_admitted=e_date)

# - Select all doctors with their associated patients prefetched.

doc = Doctor.objects.prefetch_related('doctors').all()

# - Select all nurses with their associated patients prefetched.

nurse = Nurse.objects.prefetch_related('nurses').all()

# - Select all patients along with the count of distinct doctors they are associated with.

pat = Patient.objects.annotate(num_doc=Count('doctor', distinct=True)).values('name', 'num_doc')
