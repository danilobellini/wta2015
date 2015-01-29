import ast

def locals_from_exec(code):
  """ Run code in a qualified exec, returning the resulting locals dict """
  namespace = {}
  exec(code, {}, namespace)
  return namespace

def pseudo_import(fname):
  """ Namespace dict from assignments in the file without ``__import__`` """
  is_d_import = lambda n: isinstance(n, ast.Name) and n.id == "__import__"
  is_assign = lambda n: isinstance(n, ast.Assign)
  is_valid = lambda n: is_assign(n) and not any(map(is_d_import, ast.walk(n)))
  with open(fname, "r") as f:
    astree = ast.parse(f.read(), filename=fname)
  astree.body = [node for node in astree.body if is_valid(node)]
  return locals_from_exec(compile(astree, fname, mode="exec"))
