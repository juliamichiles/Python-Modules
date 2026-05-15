#!/usr/bin/env python3
import importlib
import sys


def check_dependencies() -> dict:

    # not sure if I'll use request, remove if not
    required = {
            "pandas": "Data manipulation",
            "numpy": "Numerical computation",
            # "requests" : "Network access",
            "matplotlib.pyplot": "Visualization"
    }
    missing = []
    installed = {}

    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    for pkg, msg in required.items():
        try:
            module = importlib.import_module(pkg)
            version = getattr(module, "__version__", "unknown")
            if pkg == "matplotlib.pyplot":
                p_pkg = "matplotlib"
            else:
                p_pkg = pkg
            print(f"[OK] {p_pkg} ({version} - {msg} Ready)")
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
    print("Generating visualization...")

    data_pts = 1000
    matrix_signals = np.random.normal(loc=50, scale=15, size=data_pts)
    data_frame = pd.DataFrame(matrix_signals, columns=['Data'])
    data_frame['Time'] = np.arange(len(data_frame))

    plt.plot(
            data_frame['Time'],
            data_frame['Data'],
            color='#FF69B4',
            linewidth=0.5
    )
    plt.title("Matrix Signal Analysis", color='#FF69B4', loc='center')
    plt.axis('off')

    save_path = "matrix_analysis.png"
    plt.savefig(save_path, facecolor='black')

    print("Analysis complete!")
    print(f"Results saved to: {save_path}")


if __name__ == '__main__':
    loading()
