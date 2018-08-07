package br.org.fatec.network.lesson1;

import java.util.LinkedList;
import java.util.List;

public abstract class BaseLayer<U, D> implements Layer<U, D> {

  private List<LayerListener<U>> upStreamList = new LinkedList<>();
  final private LayerInterface<U> topSide = new LayerInterface<U>() {
    @Override
    public void next(U pack) {
      send(pack);
    }

    @Override
    public void addListener(LayerListener<U> listener) {
      upStreamList.add(listener);
    }
  };
  private List<LayerListener<D>> downStreamList = new LinkedList<>();
  final private LayerInterface<D> bottomSide = new LayerInterface<D>() {
    @Override
    public void next(D pack) {
      receive(pack);
    }

    @Override
    public void addListener(LayerListener<D> listener) {
      downStreamList.add(listener);
    }
  };

  abstract void send(U pack);

  abstract void receive(D pack);

  protected void fireDownStreamPack(D pack) {
    for (LayerListener<D> listener : downStreamList) {
      listener.next(pack);
    }
  }

  protected void fireUpStreamPack(U pack) {
    for (LayerListener<U> listener : upStreamList) {
      listener.next(pack);
    }
  }

  @Override
  public LayerInterface<U> getTopSide() {
    return topSide;
  }

  @Override
  public LayerInterface<D> getBottomSide() {
    return bottomSide;
  }
}
