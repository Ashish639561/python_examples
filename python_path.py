from pathlib import Path
print(__file__)
f_path=Path(__file__)
print(type(f_path))
com_path=f_path.resolve()
print(com_path)
print(Path(__file__).resolve().parent.parent)
