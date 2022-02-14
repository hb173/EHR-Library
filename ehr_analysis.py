import datetime


"""
Complexity: for fucntion Parse Data is O1+O1+ON(N+1)+O(1) 
O(3) + O(N^2)+O(N) 
Dropping 3 and N 
= 0(N^2) as our complexity of this function.

"""


def parse_data(filename: str) -> list:
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


def num_older_than(age: int, data: dict[str, list[str]]) -> int:
    num = 0  # O(1)
    for line in data[1:]:  # (N)
        # print(line)
        age_file = datetime.datetime.now() - datetime.datetime.strptime(
            line[2], r"%Y-%m-%d %H:%M:%S.%f"
        )  # O(1)
        years = age_file.total_seconds() / 31536000  # O(1)
        # print(years)
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
    lab: str, gt_lt: str, value: float, data: dict[str, list[str]]
) -> list[str]:
    output = []  # O(1)
    for line in data[1:]:  # (N)
        # print(line)
        if gt_lt == ">":  # O(1)
            if (line[2] == lab) and (float(line[3]) > value):  # O(2)
                output.append(line[0])  # O(1)
        elif gt_lt == "<":  # O(1)
            if (line[2] == lab) and (float(line[3]) < value):  # O(2)
                output.append(line[0])  # O(1)
        # elif gt_lt == "=":
        # if (line[2] == lab) and (float(line[3]) == value):
        # output.append(line[0])
    if output:
        finaloutput = list(set(output))  # O(1)
    else:
        finaloutput = "Enter valid argument"  # O(1)
    return finaloutput  # O(1)


if __name__ == "__main__":
    data = parse_data("PatientCorePopulatedTable.txt")
    print(num_older_than(51.2, data))
    data = parse_data("LabsCorePopulatedTable.txt")
    print(sick_patients("METABOLIC: ALBUMIN", ">", 4.0, data))
