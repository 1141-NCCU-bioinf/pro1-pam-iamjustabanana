import os
import pandas as pd


def _read_with_fallback(path):
    try:
        df = pd.read_csv(path, sep='\t', index_col=0, comment='#', engine='python')
        if df.shape[1] == 1:
            raise ValueError("Only one column read with sep='\t', fallback to whitespace")
        return df
    except Exception as e:
        print(f"Fallback for {path}: {e}")
        df = pd.read_csv(path, delim_whitespace=True, index_col=0, comment='#', engine='python')
        return df


def check(path):
    print(f"Checking: {path}")
    df = _read_with_fallback(path)
    print(f"shape: {df.shape}")
    print(f"columns (first 10): {df.columns.tolist()[:10]}")
    print(f"dtypes:\n{df.dtypes}\n")


if __name__ == '__main__':
    repo_root = os.path.dirname(os.path.dirname(__file__))
    for fname in ['mut.txt', 'pam250.txt']:
        path = os.path.join(repo_root, 'example', fname)
        check(path)
