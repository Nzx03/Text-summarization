import yaml
from pathlib import Path

path=Path("config/Config.yaml")
with open(path,'r') as f:
    content=yaml.safe_load(f)
    print(content)