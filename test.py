import pytest
import sqlite3
from Part4Final import (
    num_older_than,
    sick_patients,
    parse_data_lab,
    parse_data_patient,
    admission,
    Lab,
    Patient,
    cur,
)


@pytest.mark.parametrize(
    "age, answer",
    [
        (
            51.2,
            3,
        )
    ],
)
def test1(age, answer):
    parse_data_patient(
        "patients.txt"
    )
    patientids = cur.execute("Select patientID from patient").fetchall()
    patient_classes = [Patient(i[0]) for i in patientids]
    assert answer == num_older_than(age, patient_classes)


@pytest.mark.parametrize(
    "lab, gt_lt, value,answer",
    [
        (
            "Pfizelabs:covi2023",
            ">",
            1.8,
            1,
        )
    ],
)
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
