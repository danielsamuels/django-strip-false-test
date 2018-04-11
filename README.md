```bash
$ ./manage.py runserver
Unhandled exception in thread started by <function check_errors.<locals>.wrapper at 0x109b41598>
Traceback (most recent call last):
  File "/Users/danielsamuels/Workspace/_other/django-strip-false-test/.venv/lib/python3.6/site-packages/django/utils/autoreload.py", line 225, in wrapper
    fn(*args, **kwargs)
  File "/Users/danielsamuels/Workspace/_other/django-strip-false-test/.venv/lib/python3.6/site-packages/django/core/management/commands/runserver.py", line 112, in inner_run
    autoreload.raise_last_exception()
  File "/Users/danielsamuels/Workspace/_other/django-strip-false-test/.venv/lib/python3.6/site-packages/django/utils/autoreload.py", line 248, in raise_last_exception
    raise _exception[1]
  File "/Users/danielsamuels/Workspace/_other/django-strip-false-test/.venv/lib/python3.6/site-packages/django/core/management/__init__.py", line 327, in execute
    autoreload.check_errors(django.setup)()
  File "/Users/danielsamuels/Workspace/_other/django-strip-false-test/.venv/lib/python3.6/site-packages/django/utils/autoreload.py", line 225, in wrapper
    fn(*args, **kwargs)
  File "/Users/danielsamuels/Workspace/_other/django-strip-false-test/.venv/lib/python3.6/site-packages/django/__init__.py", line 24, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "/Users/danielsamuels/Workspace/_other/django-strip-false-test/.venv/lib/python3.6/site-packages/django/apps/registry.py", line 112, in populate
    app_config.import_models()
  File "/Users/danielsamuels/Workspace/_other/django-strip-false-test/.venv/lib/python3.6/site-packages/django/apps/config.py", line 198, in import_models
    self.models_module = import_module(models_module_name)
  File "/usr/local/Cellar/python/3.6.4_4/Frameworks/Python.framework/Versions/3.6/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/Users/danielsamuels/Workspace/_other/django-strip-false-test/strip/models.py", line 4, in <module>
    class Test(models.Model):
  File "/Users/danielsamuels/Workspace/_other/django-strip-false-test/strip/models.py", line 8, in Test
    strip=False,
  File "/Users/danielsamuels/Workspace/_other/django-strip-false-test/.venv/lib/python3.6/site-packages/django/db/models/fields/__init__.py", line 1042, in __init__
    super().__init__(*args, **kwargs)
TypeError: __init__() got an unexpected keyword argument 'strip'
```
