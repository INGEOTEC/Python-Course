def replace_vars(var, rhs):
    """Replace the variables on the right hand side of the equation
    >>> d = {'a': 23.3}
    >>> replace_vars(d, "12 + a * 2")
    '12 + 23.3 * 2'
    """


def eval_expr(var, expr):
    """Evaluation an expression
    >>> d = {'a': 32}
    >>> eval_expr(d, "a + 1")
    33
    >>> eval_expr(d, "c = a + 1")
    >>> d
    {'a': 32, 'c': 33}
    """


def split_lhs_rhs(expr):
    """Split the equation into left and right hand side.
    >>> split_lhs_rhs(" 12 + a ")
    (None, '12 + a')
    >>> split_lhs_rhs(" c = 12 + a ")
    ('c', '12 + a')
    """


def eval_command(var, expr):
    """Commands
    >>> d = dict()
    >>> eval_command(d, "exit")
    False
    >>> eval_command(d, "a = 12 + 3")
    True
    >>> d
    {'a': 15}
    >>> eval_command(d, "b = a * 2")
    True
    >>> d
    {'a': 15, 'b': 30}
    >>> eval_command(d, "b")
    30
    True
    """
    if "exit" in expr:
        return False
    else:
        val = eval_expr(var, expr)
        if val is not None:
            print(val)
    return True


def main():
    var = {}
    flag = True
    while flag:
        expr = input("=> ")
        flag = eval_command(var, expr)


if __name__ == "__main__":
    main()