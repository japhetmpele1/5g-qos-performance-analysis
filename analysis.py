import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def load_data(file_path="data/simulated_5g_qos.csv"):
    return pd.read_csv(file_path)

def compute_summary(df):
    overall_summary = df[["latency_ms", "throughput_mbps", "packet_loss_pct", "availability_pct"]].describe()
    by_service = df.groupby("service_type")[["latency_ms", "throughput_mbps", "packet_loss_pct", "availability_pct"]].mean()
    by_zone = df.groupby("zone")[["latency_ms", "throughput_mbps", "packet_loss_pct", "availability_pct"]].mean()
    return overall_summary, by_service, by_zone

def save_summary(overall_summary, by_service, by_zone, output_dir="data"):
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)

    overall_summary.to_csv(output / "overall_summary.csv")
    by_service.to_csv(output / "summary_by_service.csv")
    by_zone.to_csv(output / "summary_by_zone.csv")

def plot_latency_by_service(df, output_dir="data"):
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 5))
    df.boxplot(column="latency_ms", by="service_type")
    plt.title("Latency Distribution by 5G Service Type")
    plt.suptitle("")
    plt.xlabel("Service Type")
    plt.ylabel("Latency (ms)")
    plt.tight_layout()
    plt.savefig(output / "latency_by_service.png")
    plt.close()

def plot_throughput_by_zone(df, output_dir="data"):
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)

    avg_throughput = df.groupby("zone")["throughput_mbps"].mean()

    plt.figure(figsize=(8, 5))
    avg_throughput.plot(kind="bar")
    plt.title("Average Throughput by Zone")
    plt.xlabel("Zone")
    plt.ylabel("Throughput (Mbps)")
    plt.tight_layout()
    plt.savefig(output / "throughput_by_zone.png")
    plt.close()

def plot_packet_loss_by_service(df, output_dir="data"):
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)

    avg_packet_loss = df.groupby("service_type")["packet_loss_pct"].mean()

    plt.figure(figsize=(8, 5))
    avg_packet_loss.plot(kind="bar")
    plt.title("Average Packet Loss by Service Type")
    plt.xlabel("Service Type")
    plt.ylabel("Packet Loss (%)")
    plt.tight_layout()
    plt.savefig(output / "packet_loss_by_service.png")
    plt.close()

def run_full_analysis(file_path="data/simulated_5g_qos.csv"):
    df = load_data(file_path)

    overall_summary, by_service, by_zone = compute_summary(df)
    save_summary(overall_summary, by_service, by_zone)

    plot_latency_by_service(df)
    plot_throughput_by_zone(df)
    plot_packet_loss_by_service(df)

    return overall_summary, by_service, by_zone
