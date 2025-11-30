import yaml, pathlib
p = pathlib.Path('rules/base_rules.yaml')
data = yaml.safe_load(p.read_text())
RULES = data
