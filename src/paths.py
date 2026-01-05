from pathlib import Path

def get_repo_root():
    current = Path(__file__).resolve()

    for parent in [current] + list(current.parents):
        if (parent / ".git").exists() or (parent / "pyproject.toml").exists():
            return parent

    raise RuntimeError("Repo root not found")

REPO_ROOT = get_repo_root()

DATA_DIR = REPO_ROOT / "data"
OUTPUTS_DIR = REPO_ROOT / "outputs"
DOCS_DIR = REPO_ROOT / "docs"
MAPS_DIR = OUTPUTS_DIR / "maps"
