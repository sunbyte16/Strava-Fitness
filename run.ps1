Param(
    [string]$Port = "8501"
)

$ErrorActionPreference = "Stop"

function Resolve-Python {
    try { return (Get-Command py -ErrorAction Stop).Source } catch {}
    try { return (Get-Command python -ErrorAction Stop).Source } catch {}
    throw "Python not found. Please install Python 3.10+ and ensure 'py' or 'python' is on PATH."
}

$python = Resolve-Python

if (-not (Test-Path .venv)) {
    & $python -m venv .venv
}

. .\.venv\Scripts\Activate.ps1

pip install --upgrade pip
pip install -r .\requirements.txt

$env:STREAMLIT_SERVER_PORT = $Port
$env:STREAMLIT_BROWSER_GATHER_USAGE_STATS = "false"

streamlit run .\app\streamlit_app.py
