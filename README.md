# Line-ending sensitivity in `dist_meta`

To try it out:

```bash
python3 -m venv venv
venv/bin/pip install --upgrade pip
venv/bin/pip install dist_meta mistletoe
venv/bin/python3 ./test.py
```

Or run `./test.sh`.

# Expected

The wheel name followed by how many metadata entries it has.

# Result

ValueError:

```
...
  File "/../venv/lib/python3.9/site-packages/dist_meta/metadata.py", line 117, in loads
    field_name, field_value = divide(line, ':')
  File "/.../venv/lib/python3.9/site-packages/domdf_python_tools/utils.py", line 556, in divide
    raise ValueError(f"{sep!r} not in {string!r}")
ValueError: ':' not in '\r'
```