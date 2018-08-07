package br.org.fatec.network.lesson1;

public class LayerHelper {
  public static void connectAll(Layer... layers) {
    Layer lastLayer = layers[0];
    for (int i = 1; i < layers.length; i += 1) {
      Layer layer = layers[i];
      lastLayer.getBottomSide().addListener(layer.getTopSide());
      layer.getTopSide().addListener(lastLayer.getBottomSide());
      lastLayer = layers[i];
    }
  }

  public static void crossover(Layer a, Layer b) {
    a.getBottomSide().addListener(b.getBottomSide());
    b.getBottomSide().addListener(a.getBottomSide());
  }
}
