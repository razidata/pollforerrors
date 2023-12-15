import unittest

import app


class TestLambdaHandler(unittest.TestCase):
    def test_handler_with_valid_url(self):
        # Test with a known website
        event = {"url": "https://www.reddit.com/"}
        result = app.lambda_handler(event, None)
        self.assertIn("statusCode", result)
        self.assertEqual(result["statusCode"], 200)
        self.assertIsInstance(result["body"], str)


if __name__ == "__main__":
    unittest.main()
