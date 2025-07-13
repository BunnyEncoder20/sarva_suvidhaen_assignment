# sarva_suvidhaen_assignment

## Project Init

1. setting up git repo
```cmd
echo "# sarva_suvidhaen_assignment" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/BunnyEncoder20/sarva_suvidhaen_assignment.git
git push -u origin main
```

2. make a venv (I used uv) and actiavte it:
```cmd
uv venv
source .venv/bin/activate
```

3. Init FastAPI project
- Command installs:
    1. fastapi
    2. psycopg (Postgres Driver)
    3. dotenv (for env variables)
    4. sqlalchemy (ORM)
```cmd
uv pip install "fastapi[standard]" "psycopg[binary]" python-dotenv sqlalchemy
```

4. Made .env and config.py
    - for loading all env variables from single src of truth - the config file. (also don't need to load all env in each and every file which needs it)

5. Installed Alembic (For DB migration)
```cmd
uv pip install alembic
```

6. Make a requirements.txt file
```cmd
uv pip freeze > requirements.txt
```


### Imp Cmds used
```cmd
lsof -i :8000
kill -9 <PID>
```
