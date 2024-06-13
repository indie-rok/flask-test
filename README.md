### creat venv

```
 python3 -m venv myprojectenv
```

### running venv

```
source myprojectenv/bin/activate
```

### installing req

```
pip install -r requirements.txt
```

### Running local

```
flask --debug run --host 0.0.0.0  --port 6001
```

### running prod

```
gunicorn --config gunicorn_config.py app:app
```
