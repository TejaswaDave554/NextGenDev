public class Printer {

    public void print(int a) {
        System.out.println("Printing integer: " + a);
    }

    public void print(double a) {
        System.out.println("Printing double: " + a);
    }

    public void print(String a) {
        System.out.println("Printing string: " + a);
    }

    public void print(String a, String b) {
        System.out.println("Printing two strings: " + a + " and " + b);
    }

    public static void main(String[] args) {
        Printer printer = new Printer();
        
        printer.print(10);
        printer.print(3.14);
        printer.print("Hello");
        printer.print("Hello", "World");
    }
}
