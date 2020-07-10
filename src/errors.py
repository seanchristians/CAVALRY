import sys


def err(msg, code):
    if code > 0:
        sys.stderr.write(msg + "\n")
        sys.exit(code)
    else:
        sys.stderr.write(msg + "\n")


def missing_secrets_file(file):
    err(f"Unable to find secrets file at {file}", 1)


def missing_project(project):
    err(f"Project {project} not found", 2)


def missing_key(project, key):
    err(f"Key {key} in {project} not found", 3)

def incomplete_attribute(key, value):
    err(f"Incomplete attribute \"{key}\":\"{value}\"", 4)

def invalid_project_name(project):
    error(f"Invalid project name \"{project}\"", 5)
