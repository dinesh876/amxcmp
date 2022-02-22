# assault

A simple CLI tool to convert amx file to CMP format.


## Installation

Install using `pip`:

Download the .whl file from Release and run below command

```
$ pip install amxcmp-<version>-py3-none-any.whl
```

## Usage

The simplest usage of `amxcmp` requires only a amx file to convert CMP format. This is what it would look like:

```
$ amxcmp -f sim.csv

Completed!

---------- Results ----------
Success Count           3
Failure Count           0
Total Line Processed    3
Total time              0.010318530723452568s
-----------------------------
```

If we want to add specify output file path file, we'll use the `-o` option, and we can use the `-e` option to specify error file path that we'd like to make:

```
$ amxcmp -f sim.csv -o /opt/output.csv -e error.csv
Completed!

---------- Results ----------
Success Count           3
Failure Count           0
Total Line Processed    3
Total time              0.010318530723452568s
-----------------------------
```
## Development

For working on `amxcmp`, you'll need to have Python >= 3.7  and [`poetry`] installed. With those installed, run the following command to create a virtualenv for the project and fetch the dependencies:

```
$ poetry install --dev
...
```

Next, activate the virtualenv and get to work:

```
$ poetry shell
...
(amxcmp) $
```
