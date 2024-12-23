import unittest
from dependency_visualizer import DependencyVisualizer

class TestDependencyVisualizer(unittest.TestCase):
    def setUp(self):
        self.visualizer = DependencyVisualizer("/usr/bin/dot", "pkg1", "output/graph")

    def test_get_dependencies(self):
        deps = self.visualizer.get_dependencies()
        self.assertEqual(deps, ["pkg2", "pkg3"])

    def test_generate_graph(self):
        self.visualizer.dependencies = {"pkg1": ["pkg2"], "pkg2": ["pkg3"], "pkg3": []}
        result = self.visualizer.generate_graph()
        self.assertIn("Graph saved", result)

if __name__ == "__main__":
    unittest.main()
