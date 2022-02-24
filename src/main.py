from simulator import EvolutionSimulator as Simulator

def main():
	"""
	Main function.
	"""
	sim = Simulator(3, 2, 1)
	sim.run()

if __name__ == "__main__":
	main()
