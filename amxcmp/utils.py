import csv
from email.errors import HeaderDefect
import time
from tqdm import tqdm


def amxcmp(file):
    success, failure = [], []
    csv_file = open(file, "r")
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    started_at = time.monotonic()
    with open(file, mode="r") as csv_file:
        length = len(csv_file.readlines())

    header = next(csv.reader(open(file, "r")))

    if not validHeader(header):
        raise ValueError("Please Provide Valid Header in csv file.")

    for row in tqdm(csv_reader, total=length - 1):
        iccid = isValidIccid(row["ICCID"])
        imsi = isValidImsi(row["IMSI"])
        msisdn = isValidMsisdn(row["MSISDN"])
        reason = " / ".join(
            [
                msg
                for msg in [
                    iccid["errorMessage"],
                    imsi["errorMessage"],
                    msisdn["errorMessage"],
                ]
                if msg
            ]
        )
        if iccid["ValidIccid"] and imsi["ValidImsi"] and msisdn["ValidMsisdn"]:
            success.append(
                {
                    "ICCID": row["ICCID"],
                    "IMSI": row["IMSI"],
                    "MSISDN": row["MSISDN"],
                    "EID": generateEid("52", row["IMSI"]),
                }
            )

        else:
            failure.append(
                {
                    "ICCID": row["ICCID"],
                    "IMSI": row["IMSI"],
                    "MSISDN": row["MSISDN"],
                    "REASON": reason,
                }
            )

        line_count += 1
    csv_file.close()
    total_time = time.monotonic() - started_at
    return total_time, line_count, success, failure


def isValidImsi(imsi):
    result = imsi.isdigit() and len(imsi) == 15
    if result:
        return {"ValidImsi": result, "errorMessage": ""}
    return {
        "ValidImsi": result,
        "errorMessage": "IMSI should be length of 15 and Should not contain any Alphabets",
    }


def isValidIccid(iccid):
    result = iccid.isdigit() and len(iccid) == 19
    if result:
        return {"ValidIccid": result, "errorMessage": ""}
    return {
        "ValidIccid": result,
        "errorMessage": "ICCID should be length of 19 and Should not contain any Alphabets",
    }


def isValidMsisdn(msisdn):
    result = msisdn.isdigit() and len(msisdn) == 12
    if result:
        return {"ValidMsisdn": result, "errorMessage": ""}
    return {
        "ValidMsisdn": result,
        "errorMessage": "MSISDN should be length of 12 and Should not contain any Alphabets",
    }


def create_failure_csv(file, data, field_name):
    with open(file, mode="w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_name)
        writer.writeheader()
        for row in data:
            writer.writerow(
                {
                    "iccid": row["ICCID"],
                    "imsi": row["IMSI"],
                    "msisdn": row["MSISDN"],
                    "reason": row["REASON"],
                }
            )


def create_success_csv(file, data, field_name) -> None:
    with open(file, mode="w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_name)
        for row in data:
            writer.writerow(
                {
                    "iccid": row["ICCID"],
                    "imsi": row["IMSI"],
                    "msisdn": row["MSISDN"],
                    "diccid": "",
                    "dimsi": "",
                    "dmsisdn": "",
                    "eid": row["EID"],
                    "sim_type": "",
                }
            )


def validHeader(header):
    h = ["IMSI", "ICCID", "MSISDN", "eID"]
    for i in h:
        if i not in header:
            return False
    return True


def generateEid(country_code, imsi):
    return country_code + "0" * 15 + imsi



def create_success_bss_csv(file, data, field_name) -> None:
    with open(file, mode="w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_name)
        for row in data:
            writer.writerow(
                {
                    "msisdn": row["MSISDN"],
                    "imsi": row["IMSI"],
                    "iccid": row["ICCID"]
                }
            )