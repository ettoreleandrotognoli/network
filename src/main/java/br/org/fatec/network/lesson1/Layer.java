package br.org.fatec.network.lesson1;

public interface Layer<T, B> {

  LayerInterface<T> getTopSide();

  LayerInterface<B> getBottomSide();
}
