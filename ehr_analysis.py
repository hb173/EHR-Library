from datetime import datetime
import pytest
<<<<<<< HEAD
import sqlite3


con = sqlite3.connect("part4.db")
cur = con.cursor()


def parse_data_lab(filename: str) -> None:
    cur.execute(
        "CREATE TABLE lab (UniqueID INTEGER PRIMARY KEY AUTOINCREMENT, PatientID TEXT NOT NULL, AdmissionID TEXT NOT NULL, LabName TEXT, LabValue REAL, LabUnits TEXT, LabDateTime TEXT)"
    )
=======


class Patient:
    def __init__(
        self, patient_id: str, gender: str, race: str, dob: str, labss: str
    ) -> None:
        self.patient_id = patient_id
        self.gender = gender
        self.race = race
        self.dob = datetime.strptime(dob, "%Y-%m-%d %H:%M:%S.%f")
        self.labss = labss
        pass

    @property
    def Age(self) -> int:
        age = (datetime.now() - self.dob).total_seconds() / 31536000
        return int(age)


class Lab:
    def __init__(self, labname: str, value: float, unit: str, labdate: str) -> None:
        self.labname = labname
        self.value = float(value)
        self.unit = unit

        self.labdate = datetime.strptime(labdate, "%Y-%m-%d %H:%M:%S.%f")


def parse_data_lab(filename: str) -> dict[str, list[str]]:
    patient_lab = {}
>>>>>>> main
    first_line = 0
    with open(filename, "r") as data:
        for line in data:
            if first_line == 0:
                first_line = 1
                continue
            p = line.split("\t")
            p[-1] = p[-1][:-1]
<<<<<<< HEAD
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
=======
            p_id = p[0]
            p_lab = Lab(p[2], p[3], p[4], p[5])
            if p_id in patient_lab:
                patient_lab[p_id].append(p_lab)
            else:
                patient_lab[p_id] = [p_lab]

    return patient_lab


def parse_data_patient(pat_filename: str, lab_filename: str) -> dict[str, Patient]:
    patient_lab = parse_data_lab(lab_filename)
    pat_objects = {}
    first_line = 0
    with open(pat_filename, "r") as data:
>>>>>>> main
        for line in data:
            if first_line == 0:
                first_line = 1
                continue
            p = line.split("\t")
<<<<<<< HEAD
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
=======
            p[-1] = p[:-1]
            p_lab_att = patient_lab[p[0]]

            pat_objects[p[0]] = Patient(p[0], p[1], p[3], p[2], p_lab_att)

    return pat_objects


def num_older_than(age: int, list_of_patients: str) -> int:
    num = 0
    list_of_patients = list(list_of_patients.values())
>>>>>>> main
    for patient in list_of_patients:
        if patient.Age >= age:
            num = num + 1
    return num


<<<<<<< HEAD
def sick_patients(
    lab_n: str, gt_lt: str, value: float, list_labs_final: list[str]
) -> list[str]:
    output = 0
    for lab in list_labs_final:
=======
def sick_patients(lab_n: str, gt_lt: str, value: float, list_labs: list[str]) -> int:
    output = 0
    list_labs_final = []
    for labs in list_labs:
        for k in list_labs[labs]:
            list_labs_final.append(k)

    for lab in list_labs_final:
        print(type(lab))
>>>>>>> main
        if gt_lt == ">":
            if lab.labname == lab_n and (lab.value >= value):
                output += 1

        elif gt_lt == "<":
            if lab.labname == lab_n and (lab.value <= value):
                output += 1
        else:
            raise ValueError("gt_lt is expected to be '<' or '>'")
    return output


<<<<<<< HEAD
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
=======
def admission(patient_id: str, list_labs, list_patient: str) -> int:
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
    return int(years)


# if __name__ == "__main__":
#     list_patients = parse_data_patient("pcp.txt", "lcp.txt")
#     print(num_older_than(51.2, list_patients))
#     list_labs = parse_data_lab("lcp.txt")
#     print(admission("FB2ABB23-C9D0-4D09-8464-49BF0B982F0F", list_labs, list_patients))
#     print(sick_patients("URINALYSIS: RED BLOOD CELLS", ">", 1.8, list_labs))
>>>>>>> main
