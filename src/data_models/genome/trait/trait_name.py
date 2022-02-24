from __future__ import annotations

from enum import Enum, unique


@unique
class TraitName(Enum):
	"""
	Enum for storing the possible values for a trait.

	Values should be lower-cased and should be unique.
	"""
	SIZE = 'size'
	SPEED = 'speed'
	ENERGY = 'energy'
	VISION = 'vision'
	SIGHT = 'sight'
	HEALTH = 'health'
	ALTRUISM = 'altruism'
	COOPERATION = 'cooperation'
	ATTRACTIVENESS = 'attractiveness'
	FERTILITY = 'fertility'
	ENJOYMENT_FROM_SEX = 'sex_enjoyment'
	MUTATION = 'mutation'
