
#############################################################################################################################
#   filename:pyStepFunctionDiagram.py                                                       
#   created: 2023-05-03                                                              
#   import your librarys below                                                    
#############################################################################################################################


import os
import ast

def find_functions(tree):
    """
    Retorna uma lista com as funções encontradas no nó AST passado como parâmetro.
    """
    functions = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append(node)
    return functions

def check_dependencies(tree):
    """
    Verifica se há dependências entre as funções no nó AST passado como parâmetro.
    Retorna uma lista de tuplas com as dependências encontradas, no formato (funcao1, funcao2).
    """
    dependencies = []
    functions = find_functions(tree)
    for func in functions:
        for node in ast.walk(func):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                for func2 in functions:
                    if func2.name == node.func.id:
                        dependencies.append((func, func2))
    return dependencies

def draw_dependency_diagram(dependencies):
    """
    Desenha o diagrama de dependências a partir da lista de tuplas de dependências.
    """
    if dependencies:
        print("  +--------------------------+")
        print("  |  This is dependences     |")
        print("  +--------------------------+")
    for dependency in dependencies:
        print("\n  +----------------+      +-----------------+")
        print("  |  {:<13} | ---> |  {:<13}  |".format(dependency[0].name, dependency[1].name))
        print("  +----------------+      +-----------------+")

def sfnDiagram(dir_path):
    """
    Examina todos os arquivos Python encontrados no diretório passado como parâmetro
    e desenha o diagrama de dependências das funções definidas em cada arquivo.
    """
    for filename in os.listdir(dir_path):
        if filename.endswith('.py'):
            filepath = os.path.join(dir_path, filename)
            with open(filepath, 'r') as file:
                code = file.read()
                tree = ast.parse(code)
                dependencies = check_dependencies(tree)
                if dependencies:
                    print(f"Diagrama de dependências para o arquivo {filename}:")
                    draw_dependency_diagram(dependencies)
                else:
                    print(f"O arquivo {filename} não possui dependências entre as funções.")
                print()


   