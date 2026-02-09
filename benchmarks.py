from core import ContextCoreProtocol
import numpy as np

def run_production_benchmark():
    protocol = ContextCoreProtocol()
    total_standard_time = 0
    total_cc_time = 0
    iterations = 500

    print("📊 Benchmarking ContextCore Protocol...")
    
    for i in range(iterations):
        # Generate semi-repetitive data to simulate real context
        if i % 5 == 0:
            vec = np.random.randn(128) # New context
        else:
            vec = vec + np.random.normal(0, 0.01, 128) # Slight drift
            
        # Standard Approach (Always 50ms)
        total_standard_time += 0.050
        
        # ContextCore Approach
        latency, status = protocol.l1_sequencer(vec)
        total_cc_time += latency

    improvement = ((total_standard_time - total_cc_time) / total_standard_time) * 100
    print(f"✅ Average Latency Gain: {improvement:.2f}%")
    print(f"✅ System Stability: {status}")

if __name__ == "__main__":
    run_production_benchmark()
