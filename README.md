# brainwave-backend

1. Start virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install the dependencies

```bash
pip install -r requirements.txt
```

3. Start the server

```bash
uvicorn api:app --reload
```

4. Docs would be available on http://localhost:8000/docs#/ 