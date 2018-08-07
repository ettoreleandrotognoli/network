package br.org.fatec.network1;

public interface Layer<T, B> {

    LayerInterface<T> getTopSide();

    LayerInterface<B> getBottomSide();

}
