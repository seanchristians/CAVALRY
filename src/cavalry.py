import os, json
from cavalry import errors


class Secrets:
    def __init__(self, file, *, create=False):
        if os.path.exists(file):
            self.file = file
        elif not os.path.exists(file) and create:
            self.file = file
            with open(file, "w") as f:
                f.write(json.dumps({"_directories": {}}))
        else:
            errors.missing_secrets_file(file)

        with open(self.file, "r") as f:
            self.data = json.loads(f.read())

        # Update existing .secrets.json from older versions
        if "_directories" not in self.data.keys():
            self.data["_directories"] = {}

    def commit(self):
        with open(self.file, "w") as f:
            f.write(json.dumps(self.data))

    def store(self, project, *, key=None, value=None, directory=None):
        if (key and not value) or (value and not key):
            errors.incomplete_attribute(key, value)
        elif key and value:
            if project in self.data:
                self.data[project][key] = value
            else:
                self.data[project] = {key: value}

        if directory:
            self.data["_directories"][directory] = project

    def load(self, project, *keys):
        vars = {}
        allProjects = []

        if not project:  # Find projects on $pwd
            pwd = os.getcwd().split("/")

            for i, dir in enumerate(pwd):
                path = "/".join(pwd[: i + 1])

                if path in self.data["_directories"]:
                    allProjects.append(self.data["_directories"][path])

        elif not project in self.data:
            errors.missing_project(project)

        else:
            allProjects.append(project)

        for project in allProjects:
            if len(keys) > 0:
                for k in keys:
                    if k in self.data[project]:
                        vars[k] = self.data[project][k]
            else:
                for k, v in self.data[project].items():
                    vars[k] = v

        return vars

    def delete(self, project, *keys):
        if not project in self.data:
            errors.missing_project(project)

        if len(keys) > 0:
            for k in keys:
                if not k in self.data[project]:
                    errors.missing_key(project, k)

                self.data[project].pop(k)
        else:
            self.data.pop(project)

    def list(self, *allProjects):
        def list_all_projects():
            vars = list(self.data.keys())
            vars.remove("_directories")
            return vars

        if len(allProjects) == 0:
            return list_all_projects()

        vars = []
        for project in allProjects:
            if project and project != "_directories" and project in self.data.keys():
                vars += [f"${k}={v}" for k, v in self.data[project].items()]
            elif not project:
                vars += list_all_projects()

        return vars
