from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Attraction:
	"""
	Attraction type, stores the expected values of the trait.
	"""
	trait: str
	lower_bound: Optional[float] = None
	upper_bound: Optional[float] = None
	potential_values: Optional[list[str]] = None
