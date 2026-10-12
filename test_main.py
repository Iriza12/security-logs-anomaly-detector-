
import subprocess
import sys
import unittest


class TestLoginLogAnalyzer(unittest.TestCase):

    def run_analyzer(self):
        return subprocess.run(
            [sys.executable, "main.py"],
            capture_output=True,
            text=True,
            check=True
        )

    def test_bob_triggers_alert(self):
        result = self.run_analyzer()
        self.assertIn(
            "ALERT: bob had 3 failed login attempts.",
            result.stdout
        )

    def test_alice_does_not_trigger_alert(self):
        result = self.run_analyzer()
        self.assertNotIn("ALERT: alice", result.stdout)


if __name__ == "__main__":
    unittest.main()
