
<h1 align="center">

<img src="https://img.shields.io/static/v1?label=PYSTEPFUNCTIONDIAGRAM%20POR&message=bates&color=7159c1&style=flat-square&logo=ghost"/>

<h3> <p align="center">PYSTEPFUNCTIONDIAGRAM </p> </h3>

<h3> <p align="center"> ================= </p> </h3>

>> <h3> Resume </h3>

<p> The pyStepFunctionDiagram library aims to generate a diagram that shows the functions present in a Python script and their dependencies. The diagram displays functions that are called by other functions, indicating the direction of execution flow.

To use the library, just call the sfnDiagram function passing the path to the directory where the Python scripts are located. The function will examine the Python files present in the directory and generate the diagram for each of them. If a function depends on another, the diagram will display an arrow pointing from the dependent function to the function it depends on. If the functions are not chained, the diagram will display only one block.

The diagram is printed on the terminal, in ASCII art format, using plain characters to create the boxes and arrows. This makes the library very simple and portable, allowing it to be used on any operating system without the need to install additional dependencies. </p>

>> <h3> How install </h3>

```
pip install pyStepFunctionDiagram

```

>> <h3> How Works </h3>

```

from pyStepFunctionDiagram import *


sfnDiagram('path')


```

>> <h3> Output </h3>

```
O arquivo __init__.py não possui dependências entre as funções.

Diagrama de dependências para o arquivo hello.py:
  +--------------------------+
  |  This is dependences     |
  +--------------------------+

  +----------------+      +-----------------+
  |  World         | ---> |  hello          |
  +----------------+      +-----------------+

```