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


def parse_data(filename: str, type) -> list[str]:
    list_objects = []
    first_line = 0
    with open(filename, "r") as data:
        for line in data:
            # print("in")
            if first_line == 0:
                first_line = 1
                continue
            p = line.split("\t")
            if type == "Patient":
                list_objects.append(patient(p[2], p[1], p[3], p[0]))  # O(1)
            else:
                list_objects.append(lab(p[3], p[4], p[2]))
    return list_objects


def num_older_than(age: float, list_of_patients) -> float:
    num = 0
    for patient in list_of_patients:
        if patient.age >= age:
            num = num + 1
            pass
        pass
    return num


def sick_patients(lab: str, gt_lt: str, value: float, list_labs) -> list[str]:
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


def admission(patient_id: str, list_patient) -> int:
    for patients in list_patient:
        if patients.patient_id == patient_id:
            return patients.dob, patients.age, patients.race, patients.gender


if __name__ == "__main__":
    list_patients = data = parse_data("PatientCorePopulatedTable.txt", type="Patient")
    print(num_older_than(51.2, list_patients))
    list_labs = parse_data("LabsCorePopulatedTable.txt", type)
    print(sick_patients("METABOLIC: ALBUMIN", ">", 5.95, list_labs))
    list_patients = parse_data("PatientCorePopulatedTable.txt", type="Patient")
    print(
        admission(
            "DB22A4D9-7E4D-485C-916A-9CD1386507FB",
            list_patients,
        )
    )
