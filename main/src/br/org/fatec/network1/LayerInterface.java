package br.org.fatec.network1;

public interface LayerInterface<P> extends LayerListener<P> {


    void next(P pack);

    void addListener(LayerListener<P> listener);


}
