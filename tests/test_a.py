import unittest
import os
import subprocess
from dotenv import load_dotenv
import pathlib as pl
import sys
import time
from package import Spinner

# constants
test_env_path = "tests/.env"


class Test_A(unittest.TestCase):
    """Sample spinning test suite."""

    @classmethod
    def setUpClass(cls):

            # set flag
            cls.wheel_failed=False

            # set expected wheel build path
            load_dotenv(test_env_path)
            whl_path = pl.Path(
                f'dist/{os.getenv("PACKAGE_NAME")}-{os.getenv("VERSION")}-py3-none-any.whl'
            )

            # build wheel
            cls.build_wheel(cls)

            # delete the wheel file if it was created
            whl_path.unlink(missing_ok=True)

    def build_wheel(self):
        # build the wheel and validate result
        with Spinner():
            try:
                subprocess.check_call(
                    [sys.executable, "setup.py", "clean", "bdist_wheel", "--test"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
            except Exception:
                self.wheel_failed = True


    def test_module_execution(self):
        """Test module execution"""
        with Spinner():
            proc = subprocess.Popen(
                [sys.executable, "-m", os.getenv("PACKAGE_NAME")],
                stdout=subprocess.DEVNULL,
            )
            time.sleep(2)
            poll = proc.poll()
            proc.kill()
            proc.wait()
            if poll is not None:
                self.fail("Module dies prematurely.")

    def test_wheel(self):
        if self.wheel_failed:
            self.fail("Wheel build returned non-zero exit status.")
