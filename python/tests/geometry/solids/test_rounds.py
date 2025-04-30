import math

import pytest
from fixtures import helper

from algorithm.geometry.solids.rounds import Cylinder, Sphere
from algorithm.utils.errors import NegativeValueError, ZeroValueError


class TestSphere:
    def test_sphere_new_negative_or_zero_radius_returns_error(self):
        with pytest.raises(NegativeValueError):
            Sphere(-1.0)
        with pytest.raises(ZeroValueError):
            Sphere(0.0)

    def test_sphere_radius_returns_correct_value(self):
        sphere = Sphere(3.0)
        actual = sphere.radius
        expected = 3.0
        assert actual == expected, helper.error_message(actual, expected)

    def test_sphere_surface_area_returns_correct_value(self):
        sphere = Sphere(3.0)
        expected = 4 * math.pi * pow(3.0, 2)
        actual = sphere.surface_area()
        assert math.isclose(actual, expected), helper.error_message(actual, expected)

    def test_sphere_volume_returns_correct_value(self):
        sphere = Sphere(3.0)
        expected = (4 / 3) * math.pi * pow(3.0, 3)
        actual = sphere.volume()
        assert math.isclose(actual, expected), helper.error_message(actual, expected)


class TestCylinder:
    def test_cylinder_new_negative_or_zero_radius_returns_error(self):
        with pytest.raises(NegativeValueError):
            Cylinder(-1.0, 3.0)
        with pytest.raises(ZeroValueError):
            Cylinder(0.0, 3.0)

    def test_cylinder_new_negative_or_zero_height_returns_error(self):
        with pytest.raises(NegativeValueError):
            Cylinder(3.0, -1.0)
        with pytest.raises(ZeroValueError):
            Cylinder(3.0, 0.0)

    def test_cylinder_radius_returns_correct_value(self):
        cylinder = Cylinder(3.0, 5.0)
        actual = cylinder.radius
        expected = 3.0
        assert actual == expected, helper.error_message(actual, expected)

    def test_cylinder_height_returns_correct_value(self):
        cylinder = Cylinder(3.0, 5.0)
        actual = cylinder.height
        expected = 5.0
        assert actual == expected, helper.error_message(actual, expected)

    def test_cylinder_surface_area_returns_correct_value(self):
        cylinder = Cylinder(3.0, 5.0)
        expected = 2 * math.pi * 3.0 * (3.0 + 5.0)
        actual = cylinder.surface_area()
        assert math.isclose(actual, expected), helper.error_message(actual, expected)

    def test_cylinder_volume_returns_correct_value(self):
        cylinder = Cylinder(3.0, 5.0)
        expected = math.pi * pow(3.0, 2) * 5.0
        actual = cylinder.volume()
        assert math.isclose(actual, expected), helper.error_message(actual, expected)
