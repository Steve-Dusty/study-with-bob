"""
Math Parser - Uses SymPy for symbolic mathematics
"""
from typing import Dict, Any, Optional
import sympy as sp
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    convert_xor
)

class MathParser:
    """Parse and compare mathematical expressions using SymPy"""
    
    def __init__(self):
        # Transformations for parsing expressions
        self.transformations = (
            standard_transformations +
            (implicit_multiplication_application, convert_xor)
        )
    
    def parse_expression(self, expr_str: str) -> Optional[sp.Expr]:
        """
        Parse a string into a SymPy expression.
        
        Handles common notations:
        - x^2 or x**2 for powers
        - 2x for 2*x
        - sin(x), cos(x), etc.
        """
        try:
            # Clean up common notations
            expr_str = expr_str.replace('^', '**')
            expr_str = expr_str.replace('÷', '/')
            expr_str = expr_str.strip()
            
            # Parse with transformations
            expr = parse_expr(
                expr_str,
                transformations=self.transformations
            )
            
            return expr
            
        except Exception as e:
            print(f"Error parsing expression '{expr_str}': {e}")
            return None
    
    def compare_expressions(
        self,
        expr1_str: str,
        expr2_str: str
    ) -> Dict[str, Any]:
        """
        Compare two mathematical expressions for equivalence.
        
        Returns:
            {
                "equivalent": bool,
                "simplified_form1": str,
                "simplified_form2": str,
                "error": Optional[str]
            }
        """
        try:
            # Parse both expressions
            expr1 = self.parse_expression(expr1_str)
            expr2 = self.parse_expression(expr2_str)
            
            if expr1 is None or expr2 is None:
                return {
                    "equivalent": False,
                    "error": "Could not parse one or both expressions"
                }
            
            # Simplify both
            simplified1 = sp.simplify(expr1)
            simplified2 = sp.simplify(expr2)
            
            # Check if equivalent
            difference = sp.simplify(simplified1 - simplified2)
            equivalent = difference == 0
            
            return {
                "equivalent": equivalent,
                "simplified_form1": str(simplified1),
                "simplified_form2": str(simplified2),
                "difference": str(difference) if not equivalent else None
            }
            
        except Exception as e:
            return {
                "equivalent": False,
                "error": f"Comparison error: {str(e)}"
            }
    
    def expand_expression(self, expr_str: str) -> Optional[str]:
        """Expand an expression (e.g., (x-1)^2 -> x^2 - 2x + 1)"""
        try:
            expr = self.parse_expression(expr_str)
            if expr is None:
                return None
            
            expanded = sp.expand(expr)
            return str(expanded)
            
        except Exception as e:
            print(f"Error expanding: {e}")
            return None
    
    def factor_expression(self, expr_str: str) -> Optional[str]:
        """Factor an expression"""
        try:
            expr = self.parse_expression(expr_str)
            if expr is None:
                return None
            
            factored = sp.factor(expr)
            return str(factored)
            
        except Exception as e:
            print(f"Error factoring: {e}")
            return None
    
    def solve_equation(self, equation_str: str, variable: str = 'x') -> Dict[str, Any]:
        """
        Solve an equation for a variable.
        
        Example: "2*x + 5 = 13" -> x = 4
        """
        try:
            # Split on equals sign
            if '=' in equation_str:
                left, right = equation_str.split('=')
                left_expr = self.parse_expression(left.strip())
                right_expr = self.parse_expression(right.strip())
                
                if left_expr is None or right_expr is None:
                    return {"error": "Could not parse equation"}
                
                # Solve left = right
                equation = sp.Eq(left_expr, right_expr)
                solutions = sp.solve(equation, sp.Symbol(variable))
                
                return {
                    "solutions": [str(sol) for sol in solutions],
                    "solution_count": len(solutions)
                }
            else:
                # Assume it's an expression to solve for zero
                expr = self.parse_expression(equation_str)
                if expr is None:
                    return {"error": "Could not parse expression"}
                
                solutions = sp.solve(expr, sp.Symbol(variable))
                
                return {
                    "solutions": [str(sol) for sol in solutions],
                    "solution_count": len(solutions)
                }
                
        except Exception as e:
            return {"error": f"Solve error: {str(e)}"}
    
    def differentiate(self, expr_str: str, variable: str = 'x') -> Optional[str]:
        """Calculate derivative"""
        try:
            expr = self.parse_expression(expr_str)
            if expr is None:
                return None
            
            derivative = sp.diff(expr, sp.Symbol(variable))
            return str(derivative)
            
        except Exception as e:
            print(f"Error differentiating: {e}")
            return None
    
    def integrate(self, expr_str: str, variable: str = 'x') -> Optional[str]:
        """Calculate integral"""
        try:
            expr = self.parse_expression(expr_str)
            if expr is None:
                return None
            
            integral = sp.integrate(expr, sp.Symbol(variable))
            return str(integral)
            
        except Exception as e:
            print(f"Error integrating: {e}")
            return None
    
    def validate_expression(self, expr_str: str) -> Dict[str, Any]:
        """
        Validate if a string is a valid mathematical expression.
        """
        expr = self.parse_expression(expr_str)
        
        if expr is None:
            return {
                "valid": False,
                "error": "Could not parse expression"
            }
        
        return {
            "valid": True,
            "expression": str(expr),
            "variables": [str(sym) for sym in expr.free_symbols]
        }

