import ast
import operator

class CalculatorTools:
    # Allowed operators for safe mathematical evaluation
    _operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.Mod: operator.mod,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos,
    }

    @classmethod
    def calculate(cls, operation: str) -> str:
        """Safely calculates the result of a mathematical expression using AST parsing."""
        try:
            tree = ast.parse(operation, mode="eval")
            result = cls._eval_node(tree.body)
            return str(round(result, 2))
        except Exception as e:
            return f"Error: Invalid mathematical expression '{operation}'. Detail: {str(e)}"

    @classmethod
    def _eval_node(cls, node):
        if isinstance(node, ast.Constant):  # Numbers
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError(f"Unsupported constant type: {type(node.value)}")
        elif isinstance(node, ast.BinOp):
            op_type = type(node.op)
            if op_type not in cls._operators:
                raise ValueError(f"Unsupported binary operator: {op_type}")
            left = cls._eval_node(node.left)
            right = cls._eval_node(node.right)
            return cls._operators[op_type](left, right)
        elif isinstance(node, ast.UnaryOp):
            op_type = type(node.op)
            if op_type not in cls._operators:
                raise ValueError(f"Unsupported unary operator: {op_type}")
            operand = cls._eval_node(node.operand)
            return cls._operators[op_type](operand)
        else:
            raise ValueError(f"Unsupported AST node: {type(node)}")
