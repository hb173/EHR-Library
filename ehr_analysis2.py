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


def admission(patient_id: str, data: list[list[str]]) -> int:

    patient = [line for line in data if line[0] == patient_id][0]

    age_file = datetime.datetime.now() - datetime.datetime.strptime(
        patient[-1], r"%Y-%m-%d %H:%M:%S.%f "
    )
    years = age_file.total_seconds() / 31536000

    return round(years)


if __name__ == "__main__":
    data = parse_data("PatientCorePopulatedTable.txt")
    print(num_older_than(51.2, data))
    data = parse_data("LabsCorePopulatedTable.txt")
    print(sick_patients("METABOLIC: ALBUMIN", ">", 5.95, data))
    print(admission("1A8791E3-A61C-455A-8DEE-763EB90C9B2C", data))


@pytest.mark.parametrize(
    "age, filename, answer",
    [
        (
            51.2,
            "PatientCorePopulatedTable.txt",
            77,
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
            "METABOLIC: ALBUMIN",
            ">",
            4.0,
            "LabsCorePopulatedTable.txt",
            [
                "64182B95-EB72-4E2B-BE77-8050B71498CE",
                "0BC491C5-5A45-4067-BD11-A78BEA00D3BE",
                "6E70D84D-C75F-477C-BC37-9177C3698C66",
                "B39DC5AC-E003-4E6A-91B6-FC07625A1285",
                "7FD13988-E58A-4A5C-8680-89AC200950FA",
                "6623F5D6-D581-4268-9F9B-21612FBBF7B5",
                "DDC0BC57-7A4E-4E02-9282-177750B74FBC",
                "35FE7491-1A1D-48CB-810C-8DC2599AB3DD",
                "9C75DF1F-9DA6-4C98-8F5B-E10BDC805ED0",
                "4C201C71-CCED-40D1-9642-F9C8C485B854",
                "7C788499-7798-484B-A027-9FCDC4C0DADB",
                "6985D824-3269-4D12-A9DD-B932D640E26E",
                "016A590E-D093-4667-A5DA-D68EA6987D93",
                "53B9FFDD-F80B-43BE-93CF-C34A023EE7E9",
                "A19A0B00-4C9A-4206-B1FE-17E6DA3CEB0B",
                "80D356B4-F974-441F-A5F2-F95986D119A2",
                "CC9CDA72-B37A-4F8F-AFE4-B08F56A183BE",
                "81C5B13B-F6B2-4E57-9593-6E7E4C13B2CE",
                "25B786AF-0F99-478C-9CFA-0EA607E45834",
                "21792512-2D40-4326-BEA2-A40127EB24FF",
                "56A35E74-90BE-44A0-B7BA-7743BB152133",
                "2EE42DEF-37CA-4694-827E-FA4EAF882BFC",
                "7A025E77-7832-4F53-B9A7-09A3F98AC17E",
                "220C8D43-1322-4A9D-B890-D426942A3649",
                "B5D31F01-7273-4901-B56F-8139769A11EF",
                "DB92CDC6-FA9B-4492-BC2C-0C588AD78956",
                "3E462A8F-7B90-43A1-A8B6-AD82CB5002C9",
                "DA6CECFF-DE13-4C4C-919F-64E1A2B76C9D",
                "03A481F5-B32A-4A91-BD42-43EB78FEBA77",
                "66154E24-D3EE-4311-89DB-6195278F9B3C",
                "D8B53AA2-7953-4477-9EA4-68400EBAAC5C",
                "0A9BA3E4-CF3C-49C4-9774-5EEA2EE7D123",
                "B2EB15FA-5431-4804-9309-4215BDC778C0",
                "69B5D2A0-12FD-46EF-A5FF-B29C4BAFBE49",
                "8D389A8C-A6D8-4447-9DDE-1A28AB4EC667",
                "B70E5A76-F2BC-41E4-B037-CD4D9ABA0967",
                "8AF47463-8534-4203-B210-C2290F6CE689",
                "C65A4ADE-112E-49E4-B72A-0DED22C242ED",
                "49DADA25-F2C2-42BB-8210-D78E6C7B0D48",
                "DB22A4D9-7E4D-485C-916A-9CD1386507FB",
                "FB909FAE-72DD-4F6F-9828-D92183DF185F",
                "6D5DCAC1-17FE-4D7C-923B-806EFBA3E6DF",
            ],
        )
    ],
)
def test_2(lab, gt_lt, value, filename, answer):
    data = parse_data(filename)
    assert answer == sick_patients(lab, gt_lt, value, data)


@pytest.mark.parametrize(
    "patient_id, filename,answer",
    [
        (
            "1A8791E3-A61C-455A-8DEE-763EB90C9B2C",
            "LabsCorePopulatedTable.txt",
            30,
        )
    ],
)
def test_3(patient_id, filename, answer):
    data = parse_data(filename)
    assert answer == admission(patient_id, data)
