import argparse
import re


class ReValidator:
    def __init__(self, pattern: str) -> None:
        self.raw_pattern = pattern
        self.pattern = re.compile(pattern)

    def __call__(self, value: str) -> str:
        if not re.match(self.pattern, value):
            raise argparse.ArgumentTypeError(
                f"Value '{value}', does not match pattern '{self.raw_pattern}'"
            )
        return value
