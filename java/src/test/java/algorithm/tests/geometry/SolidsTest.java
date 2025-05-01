package algorithm.tests.geometry;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.function.Executable;

import algorithm.geometry.solids.Cylinder;
import algorithm.geometry.solids.Sphere;
import algorithm.tests.fixtures.Helper;
import algorithm.utils.errors.parameters.NegativeParameterError;
import algorithm.utils.errors.parameters.ZeroParameterError;

@DisplayName("Solids Figures Test Suite")
public class SolidsTest {
    @Nested
    @DisplayName("Cylinder Test Suite")
    class CylinderTest {
        @Test
        @DisplayName("Cylinder Negative or Zero Radius Test")
        void newCylinder_negativeOrZeroRadius_throwsException() {
            Executable negativeCylinder = () -> new Cylinder(-1, 2);
            Executable zeroCylinder = () -> new Cylinder(0, 2);
            assertThrows(NegativeParameterError.class, negativeCylinder);
            assertThrows(ZeroParameterError.class, zeroCylinder);
        }

        @Test
        @DisplayName("Cylinder Negative or Zero Height Test")
        void newCylinder_negativeOrZeroHeight_throwsException() {
            Executable negativeCylinder = () -> new Cylinder(2, -1);
            Executable zeroCylinder = () -> new Cylinder(2, 0);
            assertThrows(NegativeParameterError.class, negativeCylinder);
            assertThrows(ZeroParameterError.class, zeroCylinder);
        }

        @Test
        @DisplayName("Cylinder Radius Test")
        void cylinderRadius_returnsCorrectValue() throws Exception {
            Cylinder cylinder = new Cylinder(3.0, 5.0);
            double actual = cylinder.getRadius();
            double expected = 3.0;
            assertEquals(expected, actual, Helper.errorMessage(actual, expected));
        }

        @Test
        @DisplayName("Cylinder Height Test")
        void cylinderHeight_returnsCorrectValue() throws Exception {
            Cylinder cylinder = new Cylinder(3.0, 5.0);
            double actual = cylinder.getHeight();
            double expected = 5.0;
            assertEquals(expected, actual, Helper.errorMessage(actual, expected));
        }

        @Test
        @DisplayName("Cylinder Volume Test")
        void cylinderVolume_returnsCorrectValue() throws Exception {
            Cylinder cylinder = new Cylinder(3.0, 5.0);
            double actual = cylinder.volume();
            double expected = Math.PI * Math.pow(3.0, 2) * 5.0;
            assertEquals(expected, actual, Helper.errorMessage(actual, expected));
        }

        @Test
        @DisplayName("Cylinder Surface Area Test")
        void cylinderSurfaceArea_returnsCorrectValue() throws Exception {
            Cylinder cylinder = new Cylinder(3.0, 5.0);
            double actual = cylinder.surfaceArea();
            double expected = 2 * Math.PI * 3.0 * (3.0 + 5.0);
            assertEquals(expected, actual, Helper.errorMessage(actual, expected));
        }
    }

    @Nested
    @DisplayName("Sphere Test Suite")
    class SphereTest {
        @Test
        @DisplayName("Sphere Negative or Zero Radius Test")
        void newSphere_negativeOrZeroRadius_throwsException() {
            Executable negativeSphere = () -> new Sphere(-1);
            Executable zeroSphere = () -> new Sphere(0);
            assertThrows(NegativeParameterError.class, negativeSphere);
            assertThrows(ZeroParameterError.class, zeroSphere);
        }

        @Test
        @DisplayName("Sphere Radius Test")
        void sphereRadius_returnsCorrectValue() throws Exception {
            Sphere sphere = new Sphere(3.0);
            double actual = sphere.getRadius();
            double expected = 3.0;
            assertEquals(expected, actual, Helper.errorMessage(actual, expected));
        }

        @Test
        @DisplayName("Sphere Volume Test")
        void sphereVolume_returnsCorrectValue() throws Exception {
            Sphere sphere = new Sphere(3.0);
            double actual = sphere.volume();
            double expected = (4.0 / 3.0) * Math.PI * Math.pow(3.0, 3);
            assertEquals(expected, actual, Helper.errorMessage(actual, expected));
        }

        @Test
        @DisplayName("Sphere Surface Area Test")
        void sphereSurfaceArea_returnsCorrectValue() throws Exception {
            Sphere sphere = new Sphere(3.0);
            double actual = sphere.surfaceArea();
            double expected = 4 * Math.PI * Math.pow(3.0, 2);
            assertEquals(expected, actual, Helper.errorMessage(actual, expected));
        }
    }
}
