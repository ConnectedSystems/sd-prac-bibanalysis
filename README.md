Web of Science analysis process used to collect data and create figures for a paper on software best practices in
Integrated Environmental Modeling.

For the moment it is probably best clone and install:

```bash
$ git clone https://github.com/ConnectedSystems/sd-prac-bibanalysis.git

$ cd sd-prac-bibanalysis
$ python setup.py develop
```

Key dependencies include:

* WOS Client, a SOAP-based client for Web of Science, developed by E. Bacis (@enricobacis)[https://github.com/enricobacis]
* wos_parser, a parser for Web of Science XML data, developed by T. Achakulvisut (@titipata)[https://github.com/titipata]
* Metaknowledge, a Python library for bibliometric research, developed at (Networks Lab)[https://github.com/networks-lab/metaknowledge]
* (wosis)[https://github.com/ConnectedSystems/wosis], acts as an bridging interface between the above.
