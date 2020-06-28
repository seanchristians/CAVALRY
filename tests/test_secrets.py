import unittest, os, json, sys
import cavalry


class StderrLog:  # Redirect stderr.write from cavalry.errors.err
    def __init__(self):
        self.log = []

    def write(self, data):
        self.log.append(data)

    def flush(self):  # Suppress error 120
        pass


class SecretsTest(unittest.TestCase):
    def get_file(self):
        with open(self.file, "r") as f:
            return json.loads(f.read())

    @classmethod
    def setUpClass(self):
        sys.stderr = StderrLog()
        self.file = ".secrets.json"
        self.secrets = cavalry.Secrets(self.file, create=True)

    @classmethod
    def tearDownClass(self):
        os.remove(self.file)

    def setUp(self):
        pass

    def tearDown(self):
        self.secrets.data = {}

    def test_workflow(self):
        project = "foo"
        key = "bar"
        value = "baz"

        # Store
        self.secrets.store(project, key, value)
        self.assertIn(project, self.secrets.data)
        self.assertIn(key, self.secrets.data[project])
        self.assertEqual(self.secrets.data[project][key], value)

        self.secrets.commit()
        file = self.get_file()
        self.assertIn(project, file)
        self.assertIn(key, file[project])
        self.assertEqual(file[project][key], value)

        # Load
        data = self.secrets.load(project, key)  # Start with one key
        self.assertIn(key, data)
        self.assertEqual(data[key], value)
        self.assertIn(
            key, self.secrets.data[project]
        )  # Make sure load added data to the internal state
        self.assertEqual(self.secrets.data[project][key], value)

        self.secrets.store(project, "biz", "quux")  # Test multiple keys
        data = self.secrets.load(project, key, "biz")
        for k, v in ((key, value), ("biz", "quux")):
            self.assertIn(k, data)
            self.assertEqual(data[k], v)
            self.assertIn(k, self.secrets.data[project])
            self.assertEqual(self.secrets.data[project][k], v)

        # Delete
        self.secrets.delete(project, key)  # Start with one key
        self.assertNotIn(key, self.secrets.data[project])

        self.secrets.store(project, "quuux", "quuuux")  # Test multiple keys
        self.secrets.delete(project, "biz", "quuux")
        for n in ("biz", "quuux"):
            self.assertNotIn(n, self.secrets.data)

        self.secrets.delete(project)
        self.assertNotIn(project, self.secrets.data)

        self.secrets.commit()
        file = self.get_file()
        self.assertNotIn(project, file)

    def test_errors(self):
        self.assertRaises(SystemExit, cavalry.Secrets, ".foo.json")
        self.assertRaises(SystemExit, self.secrets.load, "foo")
        self.secrets.store("foo", "bar", "baz")
        self.assertRaises(SystemExit, self.secrets.load, "foo", "baz")


if __name__ == "__main__":
    secretsTest = unittest.TestLoader().loadTestsFromTestCase(SecretsTest)
    unittest.TextTestRunner(stream=sys.stdout).run(secretsTest)
