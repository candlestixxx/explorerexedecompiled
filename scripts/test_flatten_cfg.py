import unittest
import os
import sys
import io
import contextlib
from flatten_cfg import main

class TestFlattenCFG(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_data"
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        for f in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, f))
        os.rmdir(self.test_dir)

    def test_valid_main_function(self):
        filepath = os.path.join(self.test_dir, "test_main.c")
        with open(filepath, "w") as f:
            f.write("int main() { return 0; }\n")

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            result = main(filepath)

        output = f.getvalue()
        self.assertEqual(result, 0)
        self.assertIn("Found function: main", output)

    def test_nested_loops_and_gotos(self):
        filepath = os.path.join(self.test_dir, "test_loops.c")
        with open(filepath, "w") as f:
            f.write("""
            void test() {
            L_START:
                goto L_END;
            L_END:
                return;
            }
            """)

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            result = main(filepath)

        output = f.getvalue()
        self.assertEqual(result, 0)
        self.assertIn("Found function: test", output)
        self.assertIn("[Mock] Found LABEL", output)
        self.assertIn("[Mock] Found GOTO", output)

    def test_missing_file(self):
        filepath = os.path.join(self.test_dir, "nonexistent.c")
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            result = main(filepath)

        output = f.getvalue()
        self.assertEqual(result, 1)
        self.assertIn(f"ERROR: {filepath} not found.", output)

if __name__ == "__main__":
    unittest.main()
