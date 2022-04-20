from datetime import datetime
import pytest


class Patient:
    def __init__(self, patient_id, gender, race, dob, labss):
        self.patient_id = patient_id
        self.gender = gender
        self.race = race
        self.dob = datetime.strptime(dob, "%Y-%m-%d %H:%M:%S.%f")
        self.labss = labss
        pass

    @property
    def Age(self):
        age = (datetime.now() - self.dob).total_seconds() / 31536000
        return age


class Lab:
    def __init__(self, labname:str, value:float, unit:str, labdate:str):
        self.labname = labname
        self.value = float(value)
        self.unit = unit

        self.labdate = datetime.strptime(labdate, "%Y-%m-%d %H:%M:%S.%f")


def parse_data_lab(filename) -> list[Lab]:
    patient_lab = {}
    first_line = 0
    with open(filename, "r") as data:
        for line in data:
            if first_line == 0:
                first_line = 1
                continue
            p = line.split("\t")
            p[-1] = p[-1][:-1]
            p_id = p[0]
            p_lab = Lab(p[2], p[3], p[4], p[5])
            if p_id in patient_lab:
                patient_lab[p_id].append(p_lab)
            else:
                patient_lab[p_id] = [p_lab]

    return patient_lab


def parse_data_patient(pat_filename: str, lab_filename: str) -> list[Patient]:
    patient_lab = parse_data_lab(lab_filename)
    pat_objects = {}
    first_line = 0
    with open(pat_filename, "r") as data:
        for line in data:
            if first_line == 0:
                first_line = 1
                continue
            p = line.split("\t")
            p[-1] = p[:-1]
            p_lab_att = patient_lab[p[0]]

            pat_objects[p[0]] = Patient(p[0], p[1], p[3], p[2], p_lab_att)

    return pat_objects


def num_older_than(age: float, list_of_patients:str) -> float:
    num = 0
    list_of_patients = list(list_of_patients.values())
    for patient in list_of_patients:
        if patient.Age >= age:
            num = num + 1
    return num


def sick_patients(lab_n: str, gt_lt: str, value: float, list_labs: str) -> int:
    output = 0
    list_labs_final = []
    for labs in list_labs:
        for k in list_labs[labs]:
            list_labs_final.append(k)

    for lab in list_labs_final:
        print(type(lab))
        if gt_lt == ">":
            if lab.labname == lab_n and (lab.value >= value):
                output += 1

        elif gt_lt == "<":
            if lab.labname == lab_n and (lab.value <= value):
                output += 1
        else:
            raise ValueError("gt_lt is expected to be '<' or '>'")
    return output


def admission(patient_id: str, list_labs, list_patient:str) -> int:
    # list of all lab date time for patient id specified
    date_time = []
    patient = list_patient[patient_id]
    lab = list_labs[patient_id]
    for i in lab:
        date_time.append(i.labdate)
    # first chronological admission of patient id
    min_date_time = min(date_time)
    # print("First Chronological Lab:", min_date_time)
    dob = patient.dob
    age_file = min_date_time - dob
    years = age_file.total_seconds() / 31536000
    return round(years)


if __name__ == "__main__":
    list_patients = parse_data_patient("pcp.txt", "lcp.txt")
    print(num_older_than(51.2, list_patients))
    list_labs = parse_data_lab("lcp.txt")
    #print(type(list_labs))
    #print(admission("FB2ABB23-C9D0-4D09-8464-49BF0B982F0F", list_labs, list_patients))
    #print(sick_patients("URINALYSIS: RED BLOOD CELLS", ">", 1.8, list_labs))



