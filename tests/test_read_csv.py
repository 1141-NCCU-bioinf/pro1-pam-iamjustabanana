import os
import pandas as pd


def _read_with_fallback(path):
    # 嘗試使用 sep='\t'（跟 hw1_ref.py 相同），若失敗使用 delim_whitespace=True
    try:
        df = pd.read_csv(path, sep='\t', index_col=0, comment='#', engine='python')
        # If it read everything into one column, treat as failure and fall back
        if df.shape[1] == 1:
            raise ValueError("Only one column read with sep='\t', fallback to whitespace")
        return df
    except Exception:
        df = pd.read_csv(path, delim_whitespace=True, index_col=0, comment='#', engine='python')
        return df


def test_read_mut_txt():
    repo_root = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(repo_root, 'example', 'mut.txt')
    df = _read_with_fallback(path)

    cols = [c.strip() for c in df.columns.tolist()]
    # 檢查前幾個欄名是否為期待的氨基酸
    assert cols[:5] == ['A', 'R', 'N', 'D', 'C']
    # 至少有 20 個欄位與 20 個列（20 種氨基酸）
    assert df.shape[0] >= 20 and df.shape[1] >= 20


def test_read_pam250_txt():
    repo_root = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(repo_root, 'example', 'pam250.txt')
    df = _read_with_fallback(path)

    cols = [c.strip() for c in df.columns.tolist()]
    assert cols[:5] == ['A', 'R', 'N', 'D', 'C']
    assert df.shape[0] >= 20 and df.shape[1] >= 20
