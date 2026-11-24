import os
import shutil

entry = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
os.makedirs(out_dir, exist_ok=True)
shutil.copyfile(entry, os.path.join(out_dir, "entry.txt"))
