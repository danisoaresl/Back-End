import os
import unittest

def is_done(path):
    if not os.path.exists(path):
        return False
    with open(path) as _f:
        contents = _f.read()
    if "yes" in contents.lower():
        return True
    elif "no" in contents.lower():
        return False

class TestIsDone:

    def setup(self):
        self.tmp_file = "/tmp/test_file"

    def teardown(self):
        if os.path.exists(self.tmp_file):
            os.remove(self.tmp_file)

    def write_tmp_file(self, content):
        with open(self.tmp_file, "w") as _f:
            _f.write(content)

    def test_yes(self):
        self.write_tmp_file("yes")
        assert is_done(self.tmp_file) is True

    def test_no(self):
        self.write_tmp_file("no")
        assert is_done(self.tmp_file) is False

if __name__ == "__main__":
    unittest.main()
