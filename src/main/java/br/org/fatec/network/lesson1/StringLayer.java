package br.org.fatec.network.lesson1;

public class StringLayer extends BaseLayer<String, String> {

  @Override
  void send(String pack) {
    fireDownStreamPack(pack);
  }

  @Override
  void receive(String pack) {
    fireUpStreamPack(pack);
  }
}
