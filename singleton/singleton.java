class Singleton {

    private static Singleton single_instance = null;
    public String s;

    private Singleton() {
        s = "Luiz Filipy";
    }

    public static Singleton getInstance() {
        if (single_instance == null)
            single_instance = new Singleton();
        return single_instance;
    }
}

class Main {
    public static void main(String args[]) {
        Singleton x = Singleton.getInstance();
        System.out.println("s " + x.s);

        Singleton y = Singleton.getInstance();
        System.out.println("s " + y.s);

        x.s = "Filipy";

        System.out.println("s " + x.s);
        System.out.println("s " + y.s);
    }
}