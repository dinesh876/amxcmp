import csv
import time
from tqdm import tqdm


def amxcmp(file):
    success,failure = [], []
    csv_file = open(file,"r")
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    started_at = time.monotonic()
    pbar = tqdm(total=3)
    for row in csv_reader:
        iccid = isValidIccid(row["iccid"])
        imsi = isValidImsi(row["imsi"])
        msisdn = isValidMsisdn(row["msisdn"])
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
              {"ICCID": row["iccid"], "IMSI": row["imsi"], "MSISDN": row["msisdn"]}
            )
        else:
            failure.append(
                 {
                    "ICCID": row["iccid"],
                    "IMSI": row["imsi"],
                    "MSISDN": row["msisdn"],
                    "REASON": reason,
                }
              )

        line_count += 1
        pbar.update(1)
    csv_file.close()
    total_time = time.monotonic() - started_at
    return total_time,line_count,success,failure


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
        writer.writeheader()
        for row in data:
            writer.writerow(
                {"iccid": row["ICCID"], "imsi": row["IMSI"], "msisdn": row["MSISDN"]}
            )