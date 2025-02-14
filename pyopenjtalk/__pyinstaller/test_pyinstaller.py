from pathlib import Path
import pytest
import subprocess

pyi_main = pytest.importorskip("PyInstaller.__main__")


def test_pyinstaller(tmp_path: Path):
    work_dir = tmp_path / "build"
    dist_dir = tmp_path / "dist"
    app_path = Path(__file__).with_name("app.py").resolve()
    app_name = app_path.stem
    exe_path = dist_dir / app_name / app_name
    args = [
        "--workpath",
        str(work_dir),
        "--distpath",
        str(dist_dir),
        "--specpath",
        str(tmp_path),
        str(app_path),
    ]
    pyi_main.run(args)
    subprocess.run(exe_path, check=True)
