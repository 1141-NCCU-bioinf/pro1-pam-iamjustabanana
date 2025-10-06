import numpy as np
import pandas as pd

# 根據作業圖片 TABLE 3.1 修正後的胺基酸頻率表
AA_FREQ = {
    'G': 0.089, 'A': 0.087, 'L': 0.085, 'K': 0.081, 'S': 0.070, 
    'V': 0.065, 'T': 0.058, 'P': 0.051, 'E': 0.050, 'D': 0.047, 
    'R': 0.041, 'N': 0.040, 'F': 0.040, 'Q': 0.038, 'I': 0.037, 
    'H': 0.034, 'C': 0.033, 'Y': 0.030, 'M': 0.015, 'W': 0.010
}

def generate_pam(x, input_path, output_path):
    print(f"Reading file from: {input_path}")
    # 使用空白分隔，並跳過註釋
    df = pd.read_csv(input_path, delim_whitespace=True, index_col=0, comment='#')
  
#    print(f"原始數據形狀: {df.shape}")
#    print(f"欄位: {df.columns.tolist()}")
    
    df = df.loc[df.columns]  # 確保是方陣
    
    aa_order = df.columns.tolist()
    #print(f"氨基酸順序: {aa_order}")
    
    M1 = df.values / 10000.0
    #print("M1 矩陣:")
    #print(M1)

    Mx = np.linalg.matrix_power(M1, x)

    pam_matrix = np.zeros_like(Mx, dtype=int)
    for i, aa_i in enumerate(aa_order):
        fi = AA_FREQ[aa_i]
        for j, aa_j in enumerate(aa_order):
            fj = AA_FREQ[aa_j]          
            
            odds = Mx[i][j] / (fi)
            
            pam_matrix[i][j] = np.round(10 * np.log10(odds)).astype(int)
            
    pam_df = pd.DataFrame(pam_matrix, index=aa_order, columns=aa_order)
    pam_df.to_csv(output_path, sep=' ', index=True, header=True)
    print(f"\nPAM{x} 矩陣已保存到: {output_path}")
    return pam_df