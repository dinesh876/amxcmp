import click
import sys

print("hello")

@click.command()
@click.option("--file","-f",default=None,help="Path to input csv file")
@click.option("--output-file","-o",default=None,help="Path to Success file")
@click.option("--error-file","-e",default=None,help="Path to Error file")
@click.argument("url")
def cli(file,output_file,error_file):
     print(file,output_file,error_file)