#!/usr/bin/env python3
import importlib
import sys


def check_dependencies() -> None:
    
    # not sure if I'll use request, remove if not
    required = ["pandas", "numpy", "matplotlib.pyplot", "requests"]
    missing = []
    installed = {}

    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    for pkg in required:
        try:
            module = importlib.import_module(pkg)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {pkg} ({version} - Ready)")
            installed[pkg] = module

        except ImportError as e:
            print(f"[MISSING] {pkg} - {e}")  # Maybe change to custom msg
            missing.append(pkg)

    if missing:
        print("\n--- ERROR: MISSING DEPENDENCIES ---")
        print("To install via pip:\n\tpip install -r requirements.txt")
        print("To install via Poetry:\n\tpoetry install")
        sys.exit(1)  # signalizes error and stops execution at MAIN
    
    return installed


def loading() -> None:
    
    libs = check_dependencies()

    pd = libs['pandas']
    np = libs['numpy']
    plt = libs['matplotlib.pyplot']

    print("\nAnalyzing Matrix data...")
    
    data_pts = 1000
    matrix_signals =  np.random.normal(loc=50, scale=15, size=data_pts)
    time_series = np.arange(data_pts)

    data_frame = pd.DataFrame({
            'Signal_ID': time_series,
            'Intensity': matrix_signals
        })

    summary = data_frame['Intensity'].describe()

    print("Generating visualization...")
    
    plt.figure(figsize=(10, 6))
    plt.hist(
            data_frame['Intensity'],
            bins=30,
            color='#FF1493',
            edgecolor='black'
    )
    plt.title("Matrix Signal Intensity Distribution")
    plt.xlabel("Intensity")
    plt.ylabel("Frequency")
    plt.grid(axis='y', alpha=0.3)

    save_path = "matrix_analysis.png"
    plt.savefig(save_path)

    print("Analysis complete!")
    print(f"Results saved to: {save_path}")


if __name__ == '__main__':
    loading()
