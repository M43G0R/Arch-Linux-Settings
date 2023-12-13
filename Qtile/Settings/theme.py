import json
import os

themeName = "cyberpunk"

fileJson = os.path.join(os.path.dirname(__file__), f"themes/{themeName}.json")

with open(fileJson) as f:
  array = json.load(f)
def get_theme(themeName):
  return array[themeName]