#!/usr/bin/env python3

import os
import ast
import cProfile
from pylint.lint import Run

class ComplexityAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.complexity = 0

    def visit_For(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_While(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_If(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_With(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_Try(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def get_complexity(self):
        return self.complexity

def analyze_code_complexity(code):
    tree = ast.parse(code)
    analyzer = ComplexityAnalyzer()
    analyzer.visit(tree)
    return analyzer.get_complexity()

def analyze_file(filename):
    with open(filename, 'r') as file:
        code = file.read()
        complexity = analyze_code_complexity(code)
        print(f"File: {filename}, Complexity: {complexity}")

        # Run pylint
        results = Run(['', filename])
        print(results.linter.stats['global_note'])

def analyze_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                analyze_file(file_path)

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    profiler = cProfile.Profile()
    profiler.enable()
    analyze_folder(folder_path)
    profiler.disable()
    profiler.print_stats()
