import ast,unittest
from pathlib import Path
class TestSources(unittest.TestCase):
 def test_valid_python(self):ast.parse(Path("src/fabric_pipeline.py").read_text())
 def test_semantic_model_present(self):self.assertTrue(Path("model/measures.dax").exists())
if __name__=="__main__":unittest.main()