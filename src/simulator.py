from typing import Optional


class EvolutionSimulator:
	def __init__(self, fitness_function, mutation_rate, max_generations):
		"""
		Take in a fitness function, mutation rate, and max generations, and create the simulation.
		:param fitness_function: TODO
		:param mutation_rate: TODO
		:param max_generations: TODO
		"""
		self.fitness_function = fitness_function
		self.mutation_rate: float = mutation_rate
		self.max_generations: Optional[int] = max_generations

	def simulate_day(self) -> None:
		...

	def simulate_week(self) -> None:
		...

	def simulate_month(self) -> None:
		...

	def simulate_year(self) -> None:
		...

	def run_full_simulation(self) -> None:
		...

	def simulate_x_generations(self, generations: int) -> None:
		for _ in range(generations):
			self.simulate_day()
