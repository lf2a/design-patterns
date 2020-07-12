abstract class Pessoa {
    public String nome;
    public String sexo;
}

class Homem extends Pessoa {
    public Homem(String nome) {
        this.nome = nome;
        System.out.println("Olá Senhor " + this.nome);
    }
}

class Mulher extends Pessoa {
    public Mulher(String nome) {
        this.nome = nome;
        System.out.println("Olá Senhora " + this.nome);
    }
}

class FactoryPessoa {
    public Pessoa getPessoa(String nome, String sexo) {
        if (sexo.equals("M"))
            return new Homem(nome);
        if (sexo.equals("F"))
            return new Mulher(nome);
        return null;
    }
}

class Main {
    public static void main(String args[]) {
        FactoryPessoa factory = new FactoryPessoa();
        String nome = "Carlos";
        String sexo = "M";
        factory.getPessoa(nome, sexo);

        String nome2 = "Ana";
        String sexo2 = "F";
        factory.getPessoa(nome2, sexo2);
    }
}