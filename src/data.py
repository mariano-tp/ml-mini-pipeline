from __future__ import annotations
from sklearn.datasets import make_classification
from dataclasses import dataclass
import numpy as np

@dataclass
class Dataset:
    X: np.ndarray
    y: np.ndarray

def make_dataset(n_samples: int = 400, n_features: int = 3, random_state: int = 42) -> Dataset:
    X, y = make_classification(
        n_samples=n_samples,
        n_features=n_features,
        n_informative=3,
        n_redundant=0,
        n_clusters_per_class=1,
        class_sep=1.2,
        random_state=random_state,
    )
    return Dataset(X=X.astype("float32"), y=y.astype("int64"))
