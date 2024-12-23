import os
import subprocess
import sys
from graphviz import Digraph

class DependencyVisualizer:
    def __init__(self, graphviz_path, package_name, output_file):
        self.graphviz_path = graphviz_path
        self.package_name = package_name
        self.output_file = output_file
        self.dependencies = {}

    def get_dependencies(self):
        # Эмуляция получения зависимостей
        fake_db = {
            "pkg1": ["pkg2", "pkg3"],
            "pkg2": ["pkg4"],
            "pkg3": [],
            "pkg4": ["pkg5"],
            "pkg5": [],
        }
        return fake_db.get(self.package_name, [])

    def resolve_dependencies(self, package, visited=None):
        if visited is None:
            visited = set()
        if package in visited:
            return
        visited.add(package)
        deps = self.get_dependencies()
        self.dependencies[package] = deps
        for dep in deps:
            self.resolve_dependencies(dep, visited)

    def generate_graph(self):
        graph = Digraph()
        for pkg, deps in self.dependencies.items():
            for dep in deps:
                graph.edge(pkg, dep)
        graph.render(filename=self.output_file, format="png", directory=os.path.dirname(self.output_file), cleanup=True)
        return f"Graph saved to {self.output_file}.png"

    def run(self):
        self.resolve_dependencies(self.package_name)
        return self.generate_graph()

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python dependency_visualizer.py <graphviz_path> <package_name> <output_file>")
        sys.exit(1)

    graphviz_path = sys.argv[1]
    package_name = sys.argv[2]
    output_file = sys.argv[3]

    visualizer = DependencyVisualizer(graphviz_path, package_name, output_file)
    print(visualizer.run())
