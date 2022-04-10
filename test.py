import pytest
from assingmentone import (
    parse_data,
    num_older_than,
    sick_patients,
    admission,
    parse_data,
)


@pytest.mark.parametrize(
    "age, filename, answer",
    [
        (
            51.2,
            "Patients.txt",
            3,
        )
    ],
)
def test1(age, filename, answer):
    data = parse_data(filename)
    assert answer == num_older_than(age, data)


@pytest.mark.parametrize(
    "lab, gt_lt, value,filename,answer",
    [
        (
            "Pfizelabs:covi2023",
            ">",
            1.8,
            "index.txt",
            ["728"],
        )
    ],
)
def test_2(lab, gt_lt, value, filename, answer):
    data = parse_data(filename)
    assert answer == sick_patients(lab, gt_lt, value, data)


@pytest.mark.parametrize(
    "patient_id, filename, filename1, answer",
    [
        (
            "928",
            "index.txt",
            "patients.txt",
            77,
        )
    ],
)
def test_3(patient_id, filename, filename1, answer):
    lab_data = parse_data(filename)
    patient_data = parse_data(filename1)

    assert answer == admission(patient_id, lab_data, patient_data)
