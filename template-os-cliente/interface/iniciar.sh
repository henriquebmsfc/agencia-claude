#!/bin/bash
PYTHON="$HOME/.pyenv/versions/3.11.15/bin/python3.11"

if [ ! -f "$PYTHON" ]; then
  echo "Python 3.11 não encontrado. Rode: curl https://pyenv.run | bash && pyenv install 3.11"
  exit 1
fi

echo ""
echo "  Interface rodando em http://localhost:3000"
echo "  Ctrl+C para parar"
echo ""

cd "$(dirname "$0")"
"$PYTHON" server.py
