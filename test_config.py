"""Tests for the connection-status behavior introduced in config.py."""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import config


class ConnectTests(unittest.TestCase):
    def test_connect_prints_status_with_default_key(self):
        output = io.StringIO()

        with redirect_stdout(output):
            config.connect()

        self.assertEqual(output.getvalue(), f"Connecting with {config.API_KEY}\n")

    def test_connect_returns_none(self):
        with redirect_stdout(io.StringIO()):
            result = config.connect()

        self.assertIsNone(result)

    def test_connect_preserves_configured_key_in_output(self):
        for key in ("synthetic-key", "", "key with spaces", "clé-接続"):
            with self.subTest(key=key):
                output = io.StringIO()

                with patch.object(config, "API_KEY", key), redirect_stdout(output):
                    config.connect()

                self.assertEqual(output.getvalue(), f"Connecting with {key}\n")

    def test_connect_reads_current_key_on_each_call(self):
        output = io.StringIO()

        with redirect_stdout(output):
            with patch.object(config, "API_KEY", "first-synthetic-key"):
                config.connect()
                config.connect()
            with patch.object(config, "API_KEY", "second-synthetic-key"):
                config.connect()

        self.assertEqual(
            output.getvalue(),
            "Connecting with first-synthetic-key\n"
            "Connecting with first-synthetic-key\n"
            "Connecting with second-synthetic-key\n",
        )


if __name__ == "__main__":
    unittest.main()
