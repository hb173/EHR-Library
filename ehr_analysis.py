import datetime
import pytest


"""
Complexity: for fucntion Parse Data is O1+O1+ON(N+1)+O(1) 
O(3) + O(N^2)+O(N) 
Dropping 3 and N 
= 0(N^2) as our complexity of this function.
"""


def parse_data(filename: str) -> list[list[str]]:
    with open(filename, "r") as data:  # O(1)
        lines = []  # O(1)
        for line in data:  # (N)
            p = line.split("\t")  # O(N)
            lines.append(p)  # O(1)
    return lines  # O(1)


"""
Complexity: for fucntion num_older_than is 
0(1)+O(1)+O(N)(O1+O1)+O(1)+O(2)+O(1)
we drop the constant factor
= O(N) as our complexity of this function.

"""


def num_older_than(age: float, data: list[list[str]]) -> float:
    num = 0  # O(1)
    for line in data[1:]:  # (N)

        age_file = datetime.datetime.now() - datetime.datetime.strptime(
            line[2], r"%Y-%m-%d %H:%M:%S.%f"
        )  # O(1)
        years = age_file.total_seconds() / 31536000  # O(1)

        if years > age:  # O(1)
            num = num + 1  # O(2)"""
    return num  # O(1)


"""
Complexity: for sick_patients is:
= O(1)+O(1)+O(N)(O(1)+O(2)+O(1)+O(1)+O(2)+O(1)+O(1)+O(2)+(O)1)+O(1)
= O(2)+O(N)+O(2N)+O(N)+O(N)+O(2N)+O(N)+O(N)+O(2N)+O(N)+O(1)
= O(3)+O(12N)
We drop the constant factor
=0(N) as our complexity of this function.
"""


def sick_patients(
    lab: str, gt_lt: str, value: float, data: list[list[str]]
) -> list[str]:
    output = []
    for line in data[1:]:
        if gt_lt == ">":
            if (line[2] == lab) and (float(line[3]) > value):
                output.append(line[0])
        elif gt_lt == "<":
            if (line[2] == lab) and (float(line[3]) < value):
                output.append(line[0])
        else:
            raise ValueError("gt_lt is expected to be '<' or '>'")
    return output


def admission(
    patient_id: str, lab_data: list[list[str]], patient_data: list[list[str]]
) -> int:
    # list of all lab date time for patient id specified
    date_time = []

    for i in range(len(lab_data)):
        # header is counted and hence we look at all i values above 0
        if i != 0:
            if lab_data[i][0] == patient_id:
                lab_date_time = lab_data[i][-1].rstrip("\n")

                date_time.append(
                    datetime.datetime.strptime(lab_date_time, r"%Y-%m-%d %H:%M:%S.%f")
                )

    # first chronological admission of patient id
    min_date_time = min(date_time)
    # print("First Chronological Lab:", min_date_time)

    dob = None
    for i in patient_data:
        if patient_id == i[0]:
            dob = i[2]
    age_file = min_date_time - datetime.datetime.strptime(dob, r"%Y-%m-%d %H:%M:%S.%f")
    years = age_file.total_seconds() / 31536000

    return round(years)


if __name__ == "__main__":
    data1 = parse_data("PatientCorePopulatedTable.txt")
    print(num_older_than(51.2, data1))
    data = parse_data("LabsCorePopulatedTable.txt")
    patient_data = parse_data("PatientCorePopulatedTable.txt")
    lab_data = parse_data("LabsCorePopulatedTable.txt")

    print(sick_patients("METABOLIC: ALBUMIN", ">", 5.95, data))
    print(admission("81C5B13B-F6B2-4E57-9593-6E7E4C13B2CE", lab_data, patient_data))
