$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$python = Get-Command python -ErrorAction SilentlyContinue

if (-not $python) {
    throw "Python was not found. Install Python and try again."
}

Write-Host "Installing backend dependencies..."
& $python.Source -m pip install -r (Join-Path $projectRoot "backend\requirements.txt")
if ($LASTEXITCODE -ne 0) {
    throw "Could not install backend dependencies."
}

$backend = Start-Process `
    -FilePath $python.Source `
    -ArgumentList "app.py" `
    -WorkingDirectory (Join-Path $projectRoot "backend") `
    -PassThru

$frontend = Start-Process `
    -FilePath $python.Source `
    -ArgumentList "-m http.server 8000" `
    -WorkingDirectory (Join-Path $projectRoot "frontend") `
    -PassThru

Write-Host "Backend: http://localhost:5001"
Write-Host "Frontend: http://localhost:8000"
Write-Host "Press Ctrl+C to stop this launcher."

try {
    Start-Process "http://localhost:8000"
    Wait-Process -Id $backend.Id
}
finally {
    if (-not $backend.HasExited) {
        Stop-Process -Id $backend.Id -Force
    }
    if (-not $frontend.HasExited) {
        Stop-Process -Id $frontend.Id -Force
    }
}
