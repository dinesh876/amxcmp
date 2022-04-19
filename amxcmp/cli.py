import click
import sys
from .utils import amxcmp, create_success_csv, create_cmp_failure_csv,create_bss_failure_csv, create_success_bss_csv
from .stats import Result


@click.command()
@click.option("--file", "-f", required=True, help="Path to input csv file")
@click.option("--aircontrol-file", "-af", default=None, help="Path to Aircontrol Success file")
@click.option("--bss-file", "-bf", default=None, help="Path to BSS Success file")
@click.option("--cmp-error-file", "-ce", default=None, help="Path to CMP Error file")
@click.option("--bss-error-file", "-be", default=None, help="Path to BSS Error file")
def cli(file, aircontrol_file, bss_file, cmp_error_file, bss_error_file):
    try:
        total_time, line_count, success, failure = amxcmp(file)
    except Exception as e:
        print(e)
        sys.exit(1)
    if success:
        if aircontrol_file:
            try:
                success_fields = [
                    "iccid",
                    "imsi",
                    "msisdn",
                    "diccid",
                    "dimsi",
                    "dmsisdn",
                    "eid",
                    "sim_type",
                ]
                create_success_csv(aircontrol_file, success, success_fields)
            except Exception as e:
                print(e)
                sys.exit(1)
        else:
            try:
                success_fields = [
                    "iccid",
                    "imsi",
                    "msisdn",
                    "diccid",
                    "dimsi",
                    "dmsisdn",
                    "eid",
                    "sim_type",
                ]
                create_success_csv("aircontrol_success.csv", success, success_fields)
            except Exception as e:
                print(e)
                sys.exit(1)
            
        if bss_file:
            try:
                success_fields = [
                    "msisdn",
                    "imsi",
                    "iccid",
                ]
                create_success_bss_csv(bss_file, success, success_fields)
            except Exception as e:
                print(e)
                sys.exit(1)
        else:
            try:
                success_fields = [
                    "msisdn",
                    "imsi",
                    "iccid",
                ]
                create_success_bss_csv("bss_success.csv", success, success_fields)
            except Exception as e:
                print(e)
                sys.exit(1)


    if failure:
        if cmp_error_file:
            try:
                failure_fields = ["iccid", "imsi", "msisdn", "reason"]
                create_cmp_failure_csv(cmp_error_file, failure, failure_fields)
            except Exception as e:
                print(e)
                sys.exit(1)
        else:
            try:
                failure_fields = ["iccid", "imsi", "msisdn", "reason"]
                create_cmp_failure_csv("cmp_error.csv", failure, failure_fields)
            except Exception as e:
                print(e)
                sys.exit(1)
        if bss_error_file:
            try:
                failure_fields = ["msisdn", "imsi", "iccid", "reason"]
                create_bss_failure_csv(bss_error_file, failure, failure_fields)
            except Exception as e:
                print(e)
                sys.exit(1)
        else:
            try:
                failure_fields = ["msisdn", "imsi", "iccid", "reason"]
                create_bss_failure_csv("bss_error.csv", failure, failure_fields)
            except Exception as e:
                print(e)
                sys.exit(1)

    display(total_time, line_count, success, failure)


def display(total_time, line_count, success, failure):
    results = Result(total_time, line_count)
    print("Completed!\n")
    print("---------- Results ----------")
    print(f"Success Count        \t{results.success_count(success)}")
    print(f"Failure Count        \t{results.failure_count(failure)}")
    print(f"Total Line Processed \t{results.line_count}")
    print(f"Total time           \t{results.total_time}s")
    print("-----------------------------")
