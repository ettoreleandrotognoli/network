package br.org.fatec.network1;

public class ReverseLayer extends BaseLayer<String, String> {
    @Override
    public void send(String pack) {
        StringBuilder stringBuilder = new StringBuilder(pack);
        fireDownStreamPack(stringBuilder.reverse().toString());
    }

    @Override
    public void receive(String pack) {
        StringBuilder stringBuilder = new StringBuilder(pack);
        fireUpStreamPack(stringBuilder.reverse().toString());
    }
}
