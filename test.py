import pytest
<<<<<<< HEAD
import sqlite3
from Part4Final import (
=======
from part3ehr import (
>>>>>>> main
    num_older_than,
    sick_patients,
    parse_data_lab,
    parse_data_patient,
    admission,
<<<<<<< HEAD
    Lab,
    Patient,
    cur,
=======
>>>>>>> main
)


@pytest.mark.parametrize(
<<<<<<< HEAD
    "age, answer",
    [
        (
            51.2,
=======
    "age, patient_filename, lab_filename, answer",
    [
        (
            45,
            "Patients.txt",
            "index.txt",
>>>>>>> main
            3,
        )
    ],
)
<<<<<<< HEAD
def test1(age, answer):
    parse_data_patient(
        "patients.txt"
    )
    patientids = cur.execute("Select patientID from patient").fetchall()
    patient_classes = [Patient(i[0]) for i in patientids]
    assert answer == num_older_than(age, patient_classes)


@pytest.mark.parametrize(
    "lab, gt_lt, value,answer",
=======
def test1(age, lab_filename, patient_filename, answer):
    data = parse_data_patient(patient_filename, lab_filename)
    assert answer == num_older_than(age, data)


@pytest.mark.parametrize(
    "lab, gt_lt, value,filename,answer",
>>>>>>> main
    [
        (
            "Pfizelabs:covi2023",
            ">",
            1.8,
<<<<<<< HEAD
=======
            "index.txt",
>>>>>>> main
            1,
        )
    ],
)
<<<<<<< HEAD
def test_2(lab, gt_lt, value, answer):
    parse_data_lab(
        "index.txt"
    )
    listlabs = cur.execute("Select UniqueID from lab").fetchall()
    lab_classes = [Lab(i[0]) for i in listlabs]
    assert answer == sick_patients(lab, gt_lt, value, lab_classes)


@pytest.mark.parametrize(
    "patient_id, answer",
    [
        (
            "928",
            62,
        )
    ],
)
def test_3(patient_id, answer):
    parse_data_patient("patients.txt")
    patientids = cur.execute("Select patientID from patient").fetchall()
    patient_classes = [Patient(i[0]) for i in patientids]
    assert answer == admission(patient_id, patient_classes)
=======
def test_2(lab, gt_lt, value, filename, answer):
    data = parse_data_lab(filename)
    assert answer == sick_patients(lab, gt_lt, value, data)


@pytest.mark.parametrize(
    "patient_id, filename, filename1, answer",
    [
        (
            "977",
            "Patients.txt",
            "index.txt",
            45,
        )
    ],
)
def test_3(patient_id, filename, filename1, answer):
    data = parse_data_patient(filename, filename1)
    lab = parse_data_lab(filename1)
    assert answer == admission(patient_id, lab, data)
>>>>>>> main
