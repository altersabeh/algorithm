import algorithm.utils.errors.parameters.NegativeParameterError;

public class Raise {
    public static void main(String[] args) {
        var err = new NegativeParameterError("length", -1.0);
        System.out.println(err);
    }
}
