import click
import sys
from .utils import amxcmp, create_success_csv, create_cmp_failure_csv,create_bss_failure_csv, create_success_bss_csv
from .stats import Result
import os
import uuid
from pathlib import Path


@click.command()
@click.option("--file", "-f", required=True, help="Path to input csv file")
@click.option("--aircontrol-file", "-af", default=None, help="Path to Aircontrol Success file")
@click.option("--bss-file", "-bf", default=None, help="Path to BSS Success file")
@click.option("--cmp-error-file", "-ce", default=None, help="Path to CMP Error file")
@click.option("--bss-error-file", "-be", default=None, help="Path to BSS Error file")
def cli(file, aircontrol_file, bss_file, cmp_error_file, bss_error_file):
    try:
        total_time, line_count, success, failure = amxcmp(file)
        print(success)
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
                for s in success:
                    temp  = aircontrol_file.split('/')
                    newdir = ('/').join(temp[:-1]) + '/' + s
                    check_dir = os.path.isdir(newdir)
                    if not check_dir:
                        os.makedirs(newdir,mode=0o766) 
                    file_name = ('_').join((Path(aircontrol_file).stem ,s,uuid.uuid4().hex)) + '.csv'
                    new_file = newdir + '/' + file_name
                    create_success_csv(new_file, success[s], success_fields)
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
                for s in success:
                    newdir = os.path.join(os.getcwd(),s) 
                    check_dir = os.path.isdir(newdir)
                    if not check_dir:
                        os.makedirs(newdir,mode=0o766) 
                    file_name = ('_').join(("aircontrol_success" ,s,uuid.uuid4().hex)) + '.csv'
                    new_file = newdir + '/' + file_name
                    create_success_csv(new_file, success[s], success_fields)
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
                for s in success:
                    print(s)
                    temp  = bss_file.split('/')
                    newdir = ('/').join(temp[:-1]) + '/' + s
                    check_dir = os.path.isdir(newdir)
                    if not check_dir:
                        os.makedirs(newdir,mode=0o766) 
                    file_name = ('_').join((Path(bss_file).stem ,s,uuid.uuid4().hex)) + '.csv'
                    new_file = newdir + '/' + file_name
                    create_success_bss_csv(new_file, success[s], success_fields)
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
                for s in success:
                    newdir = os.path.join(os.getcwd(),s) 
                    check_dir = os.path.isdir(newdir)
                    if not check_dir:
                        os.makedirs(newdir,mode=0o766) 
                    file_name = ('_').join(("bss_success" ,s,uuid.uuid4().hex)) + '.csv'
                    new_file = newdir + '/' + file_name
                    create_success_bss_csv(new_file, success[s], success_fields)
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
