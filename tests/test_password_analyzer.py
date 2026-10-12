
import unittest

from password_analyzer import analyze_password, detect_patterns


class TestPasswordAnalyzer(unittest.TestCase):

    def test_common_password_is_weak(self):
        result = analyze_password("password123")
        self.assertEqual(result["strength"], "Weak")
        self.assertIn("Common password detected.", result["patterns"])

    def test_repeated_characters_are_detected(self):
        patterns = detect_patterns("Abc!!!!1111")
        self.assertIn("Repeated-character pattern detected.", patterns)

    def test_sequential_characters_are_detected(self):
        patterns = detect_patterns("Blue12345!Sky")
        self.assertIn("Sequential-character pattern detected.", patterns)

    def test_long_mixed_sample(self):
        result = analyze_password("R8!mQ2#vL9@pT4$x")
        self.assertEqual(result["strength"], "Strong")

    def test_empty_password_is_weak(self):
        result = analyze_password("")
        self.assertEqual(result["strength"], "Weak")

    def test_score_stays_within_range(self):
        for password in ["", "hello", "password123", "R8!mQ2#vL9@pT4$x"]:
            result = analyze_password(password)
            self.assertGreaterEqual(result["score"], 0)
            self.assertLessEqual(result["score"], 100)
	
    def test_detected_patterns_never_receive_strong_rating(self):
        samples = [
            "Abc!!!!1111",
            "Blue12345!Sky",
            "Password123!ExtraLong",
        ]

        for password in samples:
            with self.subTest(password=password):
                result = analyze_password(password)
                if result["patterns"]:
                    self.assertNotEqual(result["strength"], "Strong")

    def test_common_password_with_different_case(self):
        result = analyze_password("PASSWORD123")
        self.assertEqual(result["strength"], "Weak")



if __name__ == "__main__":
    unittest.main()
