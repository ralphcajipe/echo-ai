"""
Tests for app.py using unittest.
Implementation of unit tests that collectively test
the implementation of functions from app.py thoroughly.
"""

import unittest
import gradio
import app


class TestApp(unittest.TestCase):
    def test_openai_api_key(self):
        """Test that the openai_api_key function returns a string"""
        self.assertIsInstance(app.openai_api_key, str)

    def test_start_sequence(self):
        """Test that the start_sequence variable returns a string"""
        self.assertIsInstance(app.start_sequence, str)

    def test_restart_sequence(self):
        """Test that the restart_sequence variable returns a string"""
        self.assertIsInstance(app.restart_sequence, str)

    def test_prompt(self):
        """Test that the prompt variable returns a string"""
        self.assertIsInstance(app.prompt, str)

    def test_read(self):
        """Test that the read function returns a string"""
        self.assertIsInstance(app.read("initial.txt"), str)

    def test_api_request(self):
        """Test that the api_request function returns a string"""
        self.assertIsInstance(app.api_request("Hello"), str)

    def test_chat_brain(self):
        """Test that the chat_brain function returns a tuple"""
        self.assertIsInstance(app.chat_brain("Hello", []), tuple)

    def test_gradio_block(self):
        """Test that the gradio block returns a gradio object"""
        self.assertIsInstance(app.block, gradio.Blocks)
