from datetime import datetime
import pytest
import sqlite3


con = sqlite3.connect("part44.db")
cur = con.cursor()


def parse_data_lab(filename: str) -> None:
    cur.execute(
        "CREATE TABLE lab (UniqueID INTEGER PRIMARY KEY AUTOINCREMENT, PatientID TEXT NOT NULL, AdmissionID TEXT NOT NULL, LabName TEXT, LabValue REAL, LabUnits TEXT, LabDateTime TEXT)"
    )
    first_line = 0
    with open(filename, "r") as data:
        for line in data:
            if first_line == 0:
                first_line = 1
                continue
            p = line.split("\t")
            p[-1] = p[-1][:-1]
            cur.execute(
                "INSERT INTO lab (PatientID, AdmissionID, LabName, LabValue, LabUnits, LabDateTime) VALUES (?, ?, ?, ?,?,?)",
                p,
            )


def parse_data_patient(filename: str) -> None:
    cur.execute(
        "CREATE TABLE patient (PatientID TEXT PRIMARY KEY, PatientGender TEXT, PatientDateofBirth TEXT, PatientRace TEXT, PatientMaritalStatus TEXT, PatientLanguage TEXT, PatientPopulationPercentageBelowPoverty TEXT)"
    )
    first_line = 0
    with open(filename, "r") as data:
        for line in data:
            if first_line == 0:
                first_line = 1
                continue
            p = line.split("\t")
            p[-1] = p[-1][:-1]
            cur.execute("INSERT INTO patient VALUES (?, ?, ?, ?, ?, ?, ?)", p)


class Lab:
    def __init__(self, UniqueID: str) -> str:
        self.uniqueid = UniqueID

    @property
    def labname(self):
        labname = cur.execute(
            """select LabName from lab where UniqueID = ?""", (self.uniqueid,)
        ).fetchone()
        return labname[0]

    @property
    def patient_id(self):
        patient_id = cur.execute(
            """select PatientID from lab where UniqueID = ?""", (self.uniqueid,)
        ).fetchone()
        return patient_id[0]

    @property
    def value(self):
        value = cur.execute(
            """select LabValue from lab where UniqueID = ?""", (self.uniqueid,)
        ).fetchone()
        return value[0]

    @property
    def unit(self):
        unit = cur.execute(
            """select LabUnits from lab where UniqueID = ?""", (self.uniqueid,)
        ).fetchone()
        return unit[0]

    @property
    def labdate(self):
        labdate = cur.execute(
            """select LabDateTime from lab where UniqueID = ?""", (self.uniqueid,)
        ).fetchone()
        return datetime.strptime(labdate[0], "%Y-%m-%d %H:%M:%S.%f")


class Patient:
    def __init__(self, patient_id: str) -> str:
        self.patient_id = patient_id

    @property
    def gender(self):
        gender = cur.execute(
            """select PatientGender from patient where PatientID= ?""",
            (self.patient_id,),
        ).fetchone()
        return gender[0]

    @property
    def race(self):
        race = cur.execute(
            """select PatientRace from patient where PatientID = ?""",
            (self.patient_id,),
        ).fetchone()
        return race[0]

    @property
    def dob(self):
        dob = cur.execute(
            """select PatientDateofBirth from patient where PatientID = ?""",
            (self.patient_id,),
        ).fetchone()
        return datetime.strptime(dob[0], "%Y-%m-%d %H:%M:%S.%f")

    @property
    def Age(self):
        age = (datetime.now() - self.dob).total_seconds() / 31536000
        return age

    @property
    def labss(self):
        labss = cur.execute(
            """select UniqueID from lab where PatientID = ?""", (self.patient_id,)
        ).fetchall()
        labs_attend = [Lab(i[0]) for i in labss]
        return labs_attend


def num_older_than(age: float, list_of_patients: str) -> float:
    num = 0
    for patient in list_of_patients:
        if patient.Age >= age:
            num = num + 1
    return num


def sick_patients(
    lab_n: str, gt_lt: str, value: float, list_labs_final: list[str]
) -> list[str]:
    patient_ids = []
    for lab in list_labs_final:
        if gt_lt == ">":
            if lab.labname == lab_n and (lab.value >= value):
                patient_ids.append(lab.patient_id)

        elif gt_lt == "<":
            if lab.labname == lab_n and (lab.value <= value):
                patient_ids.append(lab.patient_id)
        else:
            raise ValueError("gt_lt is expected to be '<' or '>'")
    return list(set(patient_ids))


def admission(patient_id_: str, list_patient: str) -> int:
    for i in list_patient:
        if i.patient_id == patient_id_:
            a = i
            break

    min_date_time = min([i.labdate for i in a.labss])
    # print("First Chronological Lab:", min_date_time)
    dob = a.dob
    age_file = min_date_time - dob
    years = age_file.total_seconds() / 31536000
    return round(years)
