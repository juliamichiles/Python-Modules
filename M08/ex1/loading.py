#!/usr/bin/env python3
import importlib
import sys

required = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computation",
    "matplotlib.pyplot": "Visualization"
}


def get_versions(installed: dict) -> dict:

    versions = {}

    for pkg, module in installed.items():

        if pkg == "matplotlib.pyplot":
            parent_module = sys.modules.get(module.__package__)
            version = getattr(parent_module, "__version__", "unknown")
        else:
            version = getattr(module, "__version__", "unknown")
        versions[pkg] = version

    return versions


def check_dependencies() -> dict:

    missing = []
    installed = {}

    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    for pkg in required.keys():
        try:
            module = importlib.import_module(pkg)
            installed[pkg] = module

        except ImportError:
            missing.append(pkg)

    if missing:
        print("LOADING STATUS: Missing dependencies detected.")
        print("\n--- ERROR: MISSING DEPENDENCIES ---")
        print(f"The following packages are missing: {', '.join(missing)}")
        print("To install via pip:\n\tpip install -r requirements.txt")
        print("To install via Poetry:\n\tpoetry install")
        sys.exit(1)  # signalizes error and stops execution at MAIN

    return installed


def loading() -> None:

    libs = check_dependencies()
    versions = get_versions(libs)

#    if "poetry" in sys.prefix.lower():
#        print(
#                "\nPoetry Details: Uses pyproject.toml to enforce"
#                " deterministic lockfiles and nested dependency tracking."
#        )
#    else:
#        print(
#                "\nPip Details:  Uses a flat, global or virtualenv"
#                " tracking system via requirements.txt."
#        )

    for pkg, desc in required.items():
        version = versions[pkg]
        if pkg == "matplotlib.pyplot":
            n_pkg = "matplotlib"
        else:
            n_pkg = pkg
        print(f"[OK] {n_pkg} ({version}) - {desc} ready")

    pd = libs['pandas']
    np = libs['numpy']
    plt = libs['matplotlib.pyplot']
    data_pts = 1000

    print("\nAnalyzing Matrix data...")
    print(f"Processing {data_pts} data points...")
    print("Generating visualization...")

    matrix_signals = np.random.normal(loc=50, scale=15, size=data_pts)
    data_frame = pd.DataFrame(matrix_signals, columns=['Data'])
    data_frame['Time'] = np.arange(len(data_frame))

    # plt.figure(facecolor='black')
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
    plt.close()

    print("Analysis complete!")
    print(f"Results saved to: {save_path}")


if __name__ == '__main__':
    loading()
