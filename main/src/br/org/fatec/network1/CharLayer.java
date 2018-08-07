package br.org.fatec.network1;

public class CharLayer extends BaseLayer<String, Character> {

    @Override
    void send(String pack) {
        for (char c : pack.toCharArray()) {
            fireDownStreamPack(c);
        }
        fireDownStreamPack(null);
    }

    StringBuilder buffer = new StringBuilder();

    @Override
    void receive(Character pack) {
        if (pack != null) {
            buffer.append(pack);
            return;
        }
        fireUpStreamPack(buffer.toString());
        buffer = new StringBuilder();
    }
}
