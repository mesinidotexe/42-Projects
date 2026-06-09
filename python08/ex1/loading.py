def dependencies() -> bool:
    print('LOADING STATUS: Loading Programs...')
    print()

    print('checking dependencies:')
    try:
        import numpy
        print(f'[OK] numpy {numpy.__version__}')
    except ImportError:
        print('[ERROR] numpy not found')
        print('Use pip install numpy to solve the issue')
        print('Run this code in a virtual enviroment')
        return False
    try:
        import pandas
        print(f'[OK] pandas {pandas.__version__}')
    except ImportError:
        print('[ERROR] pandas not found')
        print('Use pip install pandas to solve the issue')
        return False
    try:
        import requests
        print(f'[OK] requests {requests.__version__}')
    except ImportError:
        print('[ERROR] requests not found')
        print('Use pip install requests to solve the issue')
        return False
    try:
        import matplotlib
        print(f'[OK] matplotlib {matplotlib.__version__}')
    except ImportError:
        print('[ERROR] matplotlib not found')
        print('Use pip install matplotlib to solve the issue')
        return False
    return True


if __name__ == '__main__':
    # pip install -r requirements.txt
    # ou
    # poetry install
    if dependencies():
        print()

        print('Processing 1000 data points...')
        import numpy
        data = numpy.random.rand(1000)

        print('Analyzing Matrix data...')
        import pandas
        df = pandas.DataFrame(data, columns=["values"])

        print('Generating visualization...')
        import matplotlib.pyplot as plt
        plt.plot(df["values"])
        plt.savefig("matrix_analysis.png")
        print()

        print('Analysis complete!')
        print('Results saved to: matrix_analysis.png')
