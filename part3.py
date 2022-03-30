import datetime
import pytest


class patient:
    def __init__(self, dob, gender, race, patient_id):
        self.gender = gender
        self.race = race
        self.dob = dob
        self.patient_id = patient_id
        pass

    @property
    def age(self):
        age = (
            datetime.datetime.now()
            - datetime.datetime.strptime(self.dob, r"%Y-%m-%d %H:%M:%S.%f")
        ).total_seconds() / 31536000
        return age


class lab:
    def __init__(self, value, unit, labname):
        self.value = float(value)
        self.unit = unit
        self.labname = labname


def parse_data_lab(filename: str) -> list[lab]:
    list_objects = []
    first_line = 0
    with open(filename, "r") as data:
        for line in data:

            if first_line == 0:
                first_line = 1
                continue
            p = line.split("\t")
            list_objects.append(lab(p[3], p[4], p[2]))
    return list_objects


def parse_data_patient(filename: str) -> list[patient]:
    list_objects = []
    first_line = 0
    with open(filename, "r") as data:
        for line in data:
            if first_line == 0:
                first_line = 1
                continue
            p = line.split("\t")
            list_objects.append(patient(p[2], p[1], p[3], p[0]))
    return list_objects


def num_older_than(age: float, list_of_patients) -> float:
    num = 0
    for patient in list_of_patients:
        if patient.age >= age:
            num = num + 1
            pass
        pass
    return num


def sick_patients(lab: str, gt_lt: str, value: float, list_labs) -> int:
    output = []
    for labs in list_labs:
        if gt_lt == ">":
            if labs.labname == lab and labs.value >= value:
                output.append(labs)
                pass
        elif gt_lt == "<":
            if labs.labname == lab and labs.value <= value:
                output.append(labs)
        else:
            raise ValueError("gt_lt is expected to be '<' or '>'")
    return len(output)


def admission(patient_id: str, list_patient) -> patient:
    for patients in list_patient:
        if patients.patient_id == patient_id:
            break
    return patients


if __name__ == "__main__":
    list_patients = parse_data_patient("PatientCorePopulatedTable.txt")
    print(num_older_than(51.2, list_patients))
    list_labs = parse_data_lab("LabsCorePopulatedTable.txt")
    print(sick_patients("METABOLIC: ALBUMIN", ">", 5.95, list_labs))
    patient1 = admission("FB2ABB23-C9D0-4D09-8464-49BF0B982F0F", list_patients)
    print(patient1.age, patient1.dob, patient1.race)
