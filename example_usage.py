from client import BellStateEntanglementCircuit

def run_example():
    print("=== GenPark Bell State Entanglement Example ===")
    circuit = BellStateEntanglementCircuit()
    print("Bell Pair:", circuit.benchmark_bell_pair())

if __name__ == "__main__":
    run_example()
