import pandas as pd
import random
from pathlib import Path

def generate_5g_qos_data(num_samples=1000, output_file="data/simulated_5g_qos.csv"):
    service_types = ["URLLC", "eMBB", "mMTC"]
    zones = ["Urban", "Suburban", "Rural"]

    rows = []

    for _ in range(num_samples):
        service = random.choice(service_types)
        zone = random.choice(zones)

        if service == "URLLC":
            latency = random.uniform(1, 15)
            throughput = random.uniform(20, 150)
            packet_loss = random.uniform(0.0, 1.0)
        elif service == "eMBB":
            latency = random.uniform(10, 40)
            throughput = random.uniform(100, 1000)
            packet_loss = random.uniform(0.0, 2.0)
        else:  # mMTC
            latency = random.uniform(20, 100)
            throughput = random.uniform(1, 20)
            packet_loss = random.uniform(0.0, 5.0)

        if zone == "Urban":
            throughput *= random.uniform(0.9, 1.1)
            latency *= random.uniform(0.9, 1.1)
        elif zone == "Suburban":
            throughput *= random.uniform(0.8, 1.0)
            latency *= random.uniform(1.0, 1.2)
        else:  # Rural
            throughput *= random.uniform(0.6, 0.9)
            latency *= random.uniform(1.1, 1.5)

        availability = max(95.0, min(99.999, random.uniform(98.0, 99.999)))

        rows.append({
            "service_type": service,
            "zone": zone,
            "latency_ms": round(latency, 2),
            "throughput_mbps": round(throughput, 2),
            "packet_loss_pct": round(packet_loss, 3),
            "availability_pct": round(availability, 3)
        })

    df = pd.DataFrame(rows)

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    return df

if __name__ == "__main__":
    df = generate_5g_qos_data()
    print(df.head())
    print(f"\nDataset generated with {len(df)} samples.")
