Biblo - a Web of Science Analysis process

Includes:
* wosis python package, acts as an bridging interface between WoS Client, wos_parser, and Metaknowledge


For the moment it is probably best to install with:

```bash
$ python setup.py develop
```

This will take care of installing the Biblio example and required dependencies

To run the notebooks you will need a suitable Jupyter Notebook kernel set up.

```bash
pip install jupyter notebook
python -m ipykernel install --user --name biblio --display-name "Python (Biblio)"
```
