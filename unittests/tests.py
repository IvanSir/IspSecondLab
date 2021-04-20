import unittest
import main


class TestFunction(unittest.TestCase):

    def test_json_sum_str(self):
        dumped = main.json_seria.dumps(main.summing)
        loaded = main.json_seria.loads(dumped)
        self.assertEqual(loaded(2, 8), main.summing(2, 8))
        self.assertEqual(loaded(17.2, 13.5), main.summing(17.2, 13.5))
        self.assertNotEqual(loaded(10, 8), main.summing(1, 5))
        self.assertRaises(TypeError, lambda: loaded("json", "error"))

    def test_json_sum_file(self):
        main.json_seria.dump(main.summing)
        loaded = main.json_seria.load()
        self.assertEqual(loaded(16, -5), main.summing(16, -5))
        self.assertEqual(loaded(11, 2.6), main.summing(11, 2.6))
        self.assertNotEqual(loaded(10, 8), main.summing(1, 5))
        self.assertRaises(TypeError, lambda: loaded("json", "error"))

    def test_pickle_sum_str(self):
        dumped = main.pickle_seria.dumps(main.summing)
        loaded = main.pickle_seria.loads(dumped)
        self.assertEqual(loaded(2, 8), main.summing(2, 8))
        self.assertEqual(loaded(17.2, 13.5), main.summing(17.2, 13.5))
        self.assertNotEqual(loaded(10, 8), main.summing(1, 5))
        self.assertRaises(TypeError, lambda: loaded("pickle", "error"))

    def test_pickle_sum_file(self):
        main.pickle_seria.dump(main.summing)
        loaded = main.pickle_seria.load()
        self.assertEqual(loaded(16, -5), main.summing(16, -5))
        self.assertEqual(loaded(11, 2.6), main.summing(11, 2.6))
        self.assertNotEqual(loaded(10, 8), main.summing(1, 5))
        self.assertRaises(TypeError, lambda: loaded("pickle", "error"))

    def test_toml_sum_str(self):
        dumped = main.toml_seria.dumps(main.summing)
        loaded = main.toml_seria.loads(dumped)
        self.assertEqual(loaded(2, 8), main.summing(2, 8))
        self.assertEqual(loaded(17.2, 13.5), main.summing(17.2, 13.5))
        self.assertNotEqual(loaded(10, 8), main.summing(1, 5))
        self.assertRaises(TypeError, lambda: loaded("toml", "error"))

    def test_toml_sum_file(self):
        main.toml_seria.dump(main.summing)
        loaded = main.toml_seria.load()
        self.assertEqual(loaded(-124, 11), main.summing(-124, 11))
        self.assertEqual(loaded(11.2, 2.6), main.summing(11.2, 2.6))
        self.assertNotEqual(loaded(1, 8), main.summing(1, 0))
        self.assertRaises(TypeError, lambda: loaded("toml", "error"))

    def test_yaml_sum_str(self):
        dumped = main.yaml_seria.dumps(main.summing)
        loaded = main.yaml_seria.loads(dumped)
        self.assertEqual(loaded(2, 8), main.summing(2, 8))
        self.assertEqual(loaded(17.2, 13.5), main.summing(17.2, 13.5))
        self.assertNotEqual(loaded(10, 8), main.summing(1, 5))
        self.assertRaises(TypeError, lambda: loaded("yaml", "error"))

    def test_yaml_sum_file(self):
        main.yaml_seria.dump(main.summing)
        loaded = main.yaml_seria.load()
        self.assertEqual(loaded(16, -5), main.summing(16, -5))
        self.assertEqual(loaded(11, 2.6), main.summing(11, 2.6))
        self.assertNotEqual(loaded(10, 8), main.summing(1, 5))
        self.assertRaises(TypeError, lambda: loaded("yaml", "error"))


class TestLambda(unittest.TestCase):

    def test_json_triple_str(self):
        dumped = main.json_seria.dumps(main.triple)
        loaded = main.json_seria.loads(dumped)
        self.assertEqual(loaded(2), main.triple(2))
        self.assertEqual(loaded([1, 2, "check"]), main.triple([1, 2, "check"]))
        self.assertNotEqual(loaded(3), main.triple(1))
        self.assertEqual(loaded("ha"), "hahaha")

    def test_json_triple_file(self):
        main.json_seria.dump(main.triple)
        loaded = main.json_seria.load()
        self.assertEqual(loaded(2), main.triple(2))
        self.assertEqual(loaded([1, 2, "check"]), main.triple([1, 2, "check"]))
        self.assertNotEqual(loaded(3), main.triple(1))
        self.assertEqual(loaded("ha"), "hahaha")

    def test_pickle_triple_str(self):
        dumped = main.json_seria.dumps(main.triple)
        loaded = main.json_seria.loads(dumped)
        self.assertEqual(loaded(2), main.triple(2))
        self.assertEqual(loaded([1, 2, "check"]), main.triple([1, 2, "check"]))
        self.assertNotEqual(loaded(3), main.triple(1))
        self.assertEqual(loaded("ha"), "hahaha")

    def test_pickle_triple_file(self):
        main.json_seria.dump(main.triple)
        loaded = main.json_seria.load()
        self.assertEqual(loaded(2), main.triple(2))
        self.assertEqual(loaded([1, 2, "check"]), main.triple([1, 2, "check"]))
        self.assertNotEqual(loaded(3), main.triple(1))
        self.assertEqual(loaded("ha"), main.triple("ha"))

    def test_toml_triple_str(self):
        dumped = main.json_seria.dumps(main.triple)
        loaded = main.json_seria.loads(dumped)
        self.assertEqual(loaded(2), main.triple(2))
        self.assertEqual(loaded(17.2), main.triple(17.2))
        self.assertNotEqual(loaded(3), main.triple(1))
        self.assertEqual(loaded("str"), main.triple("str"))

    def test_toml_triple_file(self):
        main.json_seria.dump(main.triple)
        loaded = main.json_seria.load()
        self.assertEqual(loaded(2), main.triple(2))
        self.assertEqual(loaded([1, 2, "check"]), main.triple([1, 2, "check"]))
        self.assertNotEqual(loaded(3), main.triple(1))
        self.assertEqual(loaded("val"), main.triple("val"))

    def test_yaml_triple_str(self):
        dumped = main.json_seria.dumps(main.triple)
        loaded = main.json_seria.loads(dumped)
        self.assertEqual(loaded(2), main.triple(2))
        self.assertEqual(loaded([1, 2, "check"]), main.triple([1, 2, "check"]))
        self.assertNotEqual(loaded(3), main.triple(1))
        self.assertEqual(loaded("c"), main.triple("c"))

    def test_yaml_triple_file(self):
        main.json_seria.dump(main.triple)
        loaded = main.json_seria.load()
        self.assertEqual(loaded(2), main.triple(2))
        self.assertEqual(loaded([1, 2, "check"]), main.triple([1, 2, "check"]))
        self.assertNotEqual(loaded(3), main.triple(1))
        self.assertEqual(loaded("1"), main.triple("1"))


class TestObject(unittest.TestCase):

    def test_json_circle_str(self):
        dumped = main.json_seria.dumps(main.circle)
        loaded = main.json_seria.loads(dumped)
        self.assertEqual(loaded.square(loaded), main.circle.square())
        self.assertEqual(loaded.radius, main.circle.radius)
        self.assertEqual(loaded.name, main.circle.name)
        self.assertEqual(loaded.samples, main.circle.samples)

    def test_json_circle_file(self):
        main.json_seria.dump(main.circle)
        loaded = main.json_seria.load()
        self.assertEqual(loaded.square(loaded), main.circle.square())
        self.assertEqual(loaded.radius, main.circle.radius)
        self.assertEqual(loaded.name, main.circle.name)
        self.assertEqual(loaded.samples, main.circle.samples)

    def test_pickle_circle_str(self):
        dumped = main.pickle_seria.dumps(main.circle)
        loaded = main.pickle_seria.loads(dumped)
        self.assertEqual(loaded.square(), main.circle.square())
        self.assertEqual(loaded.radius, main.circle.radius)
        self.assertEqual(loaded.name, main.circle.name)
        self.assertEqual(loaded.samples, main.circle.samples)

    def test_pickle_circle_file(self):
        main.pickle_seria.dump(main.circle)
        loaded = main.pickle_seria.load()
        self.assertEqual(loaded.square(), main.circle.square())
        self.assertEqual(loaded.radius, main.circle.radius)
        self.assertEqual(loaded.name, main.circle.name)
        self.assertEqual(loaded.samples, main.circle.samples)


    def test_toml_circle_str(self):
        dumped = main.toml_seria.dumps(main.circle)
        loaded = main.toml_seria.loads(dumped)
        self.assertEqual(loaded.square(loaded), main.circle.square())
        self.assertEqual(loaded.radius, main.circle.radius)
        self.assertEqual(loaded.name, main.circle.name)
        self.assertEqual(loaded.samples, main.circle.samples)

    def test_toml_circle_file(self):
        main.toml_seria.dump(main.circle)
        loaded = main.toml_seria.load()
        self.assertEqual(loaded.square(loaded), main.circle.square())
        self.assertEqual(loaded.radius, main.circle.radius)
        self.assertEqual(loaded.name, main.circle.name)
        self.assertEqual(loaded.samples, main.circle.samples)

    def test_yaml_circle_str(self):
        dumped = main.yaml_seria.dumps(main.circle)
        loaded = main.yaml_seria.loads(dumped)
        self.assertEqual(loaded.square(loaded), main.circle.square())
        self.assertEqual(loaded.radius, main.circle.radius)
        self.assertEqual(loaded.name, main.circle.name)
        self.assertEqual(loaded.samples, main.circle.samples)

    def test_yaml_circle_file(self):
        main.yaml_seria.dump(main.circle)
        loaded = main.yaml_seria.load()
        self.assertEqual(loaded.square(loaded), main.circle.square())
        self.assertEqual(loaded.radius, main.circle.radius)
        self.assertEqual(loaded.name, main.circle.name)
        self.assertEqual(loaded.samples, main.circle.samples)


class TestClass(unittest.TestCase):

    def test_json_figure_str(self):
        dumped = main.json_seria.dumps(main.Figure)
        loaded = main.json_seria.loads(dumped)
        parsed_obj = loaded("circle")
        fig_obj = main.Figure("circle")
        self.assertEqual(parsed_obj.square(), fig_obj.square())
        self.assertEqual(parsed_obj.radius, fig_obj.radius)
        parsed_obj.radius = 10
        fig_obj.radius = 10
        self.assertEqual(parsed_obj.square(), fig_obj.square())


    def test_json_figure_file(self):
        main.json_seria.dump(main.Figure)
        loaded = main.json_seria.load()
        parsed_obj = loaded("ellipse")
        fig_obj = main.Figure("circle")
        self.assertEqual(parsed_obj.square(), fig_obj.square())
        self.assertEqual(parsed_obj.radius, fig_obj.radius)
        parsed_obj.radius = 10
        fig_obj.radius = 10
        self.assertEqual(parsed_obj.square(), fig_obj.square())

    def test_pickle_figure_str(self):
        dumped = main.json_seria.dumps(main.Figure)
        loaded = main.json_seria.loads(dumped)
        parsed_obj = loaded("ellipse")
        fig_obj = main.Figure("circle")
        self.assertEqual(parsed_obj.square(), fig_obj.square())
        self.assertEqual(parsed_obj.radius, fig_obj.radius)
        parsed_obj.radius = 10
        fig_obj.radius = 10
        self.assertEqual(parsed_obj.square(), fig_obj.square())


