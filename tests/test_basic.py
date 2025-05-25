import os
import sys
from pathlib import Path
import types

sys.path.append(str(Path(__file__).resolve().parents[1]))

dotenv_stub = types.SimpleNamespace(load_dotenv=lambda *args, **kwargs: None)
sys.modules.setdefault('dotenv', dotenv_stub)
telegram_stub = types.SimpleNamespace(Update=object)
telegram_ext_stub = types.SimpleNamespace(ApplicationBuilder=object, CommandHandler=object, ContextTypes=types.SimpleNamespace(DEFAULT_TYPE=object))
sys.modules.setdefault('telegram', telegram_stub)
sys.modules.setdefault('telegram.ext', telegram_ext_stub)
from whattsanddrops.main import main


def test_main_prints_message(monkeypatch, capsys):
    monkeypatch.setenv('TELEGRAM_TOKEN', 'dummy')
    main()
    captured = capsys.readouterr()
    assert 'Hello, I am your bot!' in captured.out
