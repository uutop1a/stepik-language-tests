# Stepik Selenium language tests

Solution for course 575, lesson 3.6: check that the product page has a visible add-to-basket button while the browser requests a selected language.

Install Python dependencies: `pip install pytest selenium`. Chrome must be installed for the standard run:

```bash
pytest --language=es test_items.py
pytest --language=fr test_items.py
```

The `browser` fixture reads `--language` and passes it to Chrome. On a machine with Edge instead of Chrome, set `COURSE_BROWSER=edge` before running the same commands. The French button reads `Ajouter au panier`.
