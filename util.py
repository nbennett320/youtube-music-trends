import re

def to_snake_case(s: str):
  return re.sub(r'(?<!^)(?=[A-Z])', '_', re.sub(r'\s|\/|\.|\-', '', s)).lower()

