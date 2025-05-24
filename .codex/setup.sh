#!/bin/bash
set -e

echo "[*] Installing uv package manager..."
curl -LsSf https://astral.sh/uv/install.sh | sh

export PATH="$HOME/.cargo/bin:$HOME/.local/bin:$PATH"

echo "[*] Installing Python dependencies from pyproject.toml..."
uv sync

echo "[*] Setup complete. You can now run 'python bot.py'"