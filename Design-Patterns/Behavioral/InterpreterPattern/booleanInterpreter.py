from abc import ABC, abstractmethod
import re

# Expression base class
class Expression(ABC):
    @abstractmethod
    def interpret(self) -> bool:
        pass

# Terminal expression
class BooleanValue(Expression):
    def __init__(self, value: bool):
        self.value = value

    def interpret(self) -> bool:
        return self.value

# Non-terminal expressions
class AndExpression(Expression):
    def __init__(self, expr1: Expression, expr2: Expression):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self) -> bool:
        return self.expr1.interpret() and self.expr2.interpret()

class OrExpression(Expression):
    def __init__(self, expr1: Expression, expr2: Expression):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self) -> bool:
        return self.expr1.interpret() or self.expr2.interpret()

class NotExpression(Expression):
    def __init__(self, expr: Expression):
        self.expr = expr

    def interpret(self) -> bool:
        return not self.expr.interpret()

# Tokenizer
def tokenize(expression: str):
    return re.findall(r'\bTrue\b|\bFalse\b|\bAND\b|\bOR\b|\bNOT\b|\(|\)', expression)

# Recursive Parser
def parse_expression(tokens):
    def parse_or(tokens):
        expr = parse_and(tokens)
        while tokens and tokens[0] == 'OR':
            tokens.pop(0)
            right = parse_and(tokens)
            expr = OrExpression(expr, right)
        return expr

    def parse_and(tokens):
        expr = parse_not(tokens)
        while tokens and tokens[0] == 'AND':
            tokens.pop(0)
            right = parse_not(tokens)
            expr = AndExpression(expr, right)
        return expr

    def parse_not(tokens):
        if tokens and tokens[0] == 'NOT':
            tokens.pop(0)
            return NotExpression(parse_not(tokens))
        else:
            return parse_primary(tokens)

    def parse_primary(tokens):
        token = tokens.pop(0)
        if token == 'True':
            return BooleanValue(True)
        elif token == 'False':
            return BooleanValue(False)
        elif token == '(':
            expr = parse_or(tokens)
            if not tokens or tokens.pop(0) != ')':
                raise ValueError("Missing closing parenthesis")
            return expr
        else:
            raise ValueError(f"Unexpected token: {token}")

    return parse_or(tokens)

# Test driver
if __name__ == "__main__":
    input_expr = "NOT (True AND False) OR True"
    tokens = tokenize(input_expr)
    expr_tree = parse_expression(tokens)
    result = expr_tree.interpret()
    print(f"{input_expr} = {result}")
