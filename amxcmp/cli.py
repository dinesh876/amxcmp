import click
import sys
from .utils import amxcmp, create_success_csv, create_failure_csv
from .stats import Result


@click.command()
@click.option("--file", "-f", required=True, help="Path to input csv file")
@click.option("--output-file", "-o", default=None, help="Path to Success file")
@click.option("--error-file", "-e", default=None, help="Path to Error file")
def cli(file, output_file, error_file):
    try:
        total_time, line_count, success, failure = amxcmp(file)
    except Exception as e:
        print(e)
        sys.exit(1)
    if success:
        if output_file:
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
                create_success_csv(output_file, success, success_fields)
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
                create_success_csv("success.csv", success, success_fields)
            except Exception as e:
                print(e)
                sys.exit(1)

    if failure:
        if error_file:
            try:
                failure_fields = ["iccid", "imsi", "msisdn", "reason"]
                create_failure_csv(error_file, failure, failure_fields)
            except Exception as e:
                print(e)
                sys.exit(1)
        else:
            try:
                failure_fields = ["iccid", "imsi", "msisdn", "reason"]
                create_failure_csv("error.csv", failure, failure_fields)
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
