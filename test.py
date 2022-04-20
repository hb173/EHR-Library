import pytest
from part3ehr import (
    num_older_than,
    sick_patients,
    parse_data_lab,
    parse_data_patient,
    admission,
)


@pytest.mark.parametrize(
    "age, patient_filename, lab_filename, answer",
    [
        (
            45,
            "Patients.txt",
            "index.txt",
            3,
        )
    ],
)
def test1(age, lab_filename, patient_filename, answer):
    data = parse_data_patient(patient_filename, lab_filename)
    assert answer == num_older_than(age, data)


@pytest.mark.parametrize(
    "lab, gt_lt, value,filename,answer",
    [
        (
            "Pfizelabs:covi2023",
            ">",
            1.8,
            "index.txt",
            1,
        )
    ],
)
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
