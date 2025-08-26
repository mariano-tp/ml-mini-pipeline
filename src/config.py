from dataclasses import dataclass
from pathlib import Path
from typing import Literal, Optional
import yaml

@dataclass
class ModelCfg:
    type: Literal["logreg", "tree"] = "logreg"
    max_depth: Optional[int] = 3

@dataclass
class Cfg:
    random_state: int = 42
    test_size: float = 0.2
    model: ModelCfg = ModelCfg()

def load_cfg(path: str = "config.yaml") -> Cfg:
    p = Path(path)
    if not p.exists():
        return Cfg()
    raw = yaml.safe_load(p.read_text()) or {}
    model = raw.get("model", {}) or {}
    return Cfg(
        random_state=raw.get("random_state", 42),
        test_size=raw.get("test_size", 0.2),
        model=ModelCfg(
            type=model.get("type", "logreg"),
            max_depth=model.get("max_depth", 3),
        ),
    )
