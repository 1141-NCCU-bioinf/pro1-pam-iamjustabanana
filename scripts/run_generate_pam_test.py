import os
import sys
repo_root = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, repo_root)
from hw1 import generate_pam

mut_path = os.path.join(repo_root, 'example', 'mut.txt')
pam250_path = os.path.join(repo_root, 'example', 'pam250.txt')

out1 = os.path.join(repo_root, 'tmp_pam1.tsv')
out250 = os.path.join(repo_root, 'tmp_pam250.tsv')

print('Generating PAM1 from mut.txt...')
generate_pam(1, mut_path, out1)
print('Wrote', out1)

print('Generating PAM250 from pam250.txt (x=250)...')
generate_pam(250, pam250_path, out250)
print('Wrote', out250)
