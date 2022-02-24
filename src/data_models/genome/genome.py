from dataclasses import dataclass

from genome_sequence import GenomeSequence


@dataclass
class Genome:
	sequences: list[GenomeSequence]

	@classmethod
	def from_genetic_string(cls, genetic_string: str) -> 'Genome':
		"""
		Creates a Genome from a genetic string.

		:param genetic_string: The genetic string to create the genome from.
		:return: A Genome object.
		"""
		sequences = []
		for sequence in genetic_string.split('.'):
			sequences.append(GenomeSequence.from_sequence(sequence))
		return cls(sequences)

	def to_genetic_string(self) -> str:
		"""
		Returns the genetic string of the genome.

		:return: The genetic string of the genome.
		"""
		return '.'.join([sequence.sequence for sequence in self.sequences])
