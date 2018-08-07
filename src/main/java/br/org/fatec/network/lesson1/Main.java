package br.org.fatec.network.lesson1;

public class Main {

  public static void main(String... args) {
    StringLayer aStringLayer = new StringLayer();
    ReverseLayer aReverseLayer = new ReverseLayer();
    CharLayer aCharLayer = new CharLayer();

    LayerHelper.connectAll(aStringLayer, aReverseLayer, aCharLayer);

    StringLayer bStringLayer = new StringLayer();
    ReverseLayer bReverseLayer = new ReverseLayer();
    CharLayer bCharLayer = new CharLayer();

    LayerHelper.connectAll(bStringLayer, bReverseLayer, bCharLayer);

    LayerHelper.crossover(aCharLayer, bCharLayer);

    aCharLayer.getBottomSide().addListener(System.err::println);
    bCharLayer.getBottomSide().addListener(System.err::println);

    aStringLayer.getTopSide().addListener(it -> System.out.println("A: " + it));
    bStringLayer.getTopSide().addListener(it -> System.out.println("B: " + it));

    aStringLayer.send("message from a");
    bStringLayer.send("message from b");
  }
}
