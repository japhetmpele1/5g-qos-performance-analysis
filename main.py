from generate_data import generate_5g_qos_data
from analysis import run_full_analysis

def main():
    print("Generating simulated 5G QoS dataset...")
    generate_5g_qos_data(num_samples=1500)

    print("Running performance analysis...")
    overall_summary, by_service, by_zone = run_full_analysis()

    print("\n=== Overall Summary ===")
    print(overall_summary)

    print("\n=== Mean QoS by Service Type ===")
    print(by_service)

    print("\n=== Mean QoS by Zone ===")
    print(by_zone)

    print("\nAnalysis complete. Results saved in the data/ folder.")

if __name__ == "__main__":
    main()
