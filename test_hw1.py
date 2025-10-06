import sys
from hw1 import generate_pam
import os

def main():
    # 設定檔案路徑
    repo_root = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(repo_root, 'example', 'mut.txt')
    output_path = os.path.join(repo_root, 'pam250.txt')
    
    # 生成 PAM250 矩陣
    generate_pam(250, input_path, output_path)
    print(f"PAM250 矩陣已生成到 {output_path}")

if __name__ == '__main__':
    main()