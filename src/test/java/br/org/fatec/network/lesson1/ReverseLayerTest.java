package br.org.fatec.network.lesson1;

import java.util.LinkedList;
import java.util.List;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class ReverseLayerTest {

  @Test
  void send() {
    ReverseLayer reverseLayer = new ReverseLayer();
    List<String> result = new LinkedList<>();
    String message = "abc";
    reverseLayer.getBottomSide().addListener(result::add);
    reverseLayer.getTopSide().next(message);
    assertEquals(result.get(0), "cba");
  }

  @Test
  void receive() {
    ReverseLayer reverseLayer = new ReverseLayer();
    List<String> result = new LinkedList<>();
    String message = "abc";
    reverseLayer.getTopSide().addListener(result::add);
    reverseLayer.getBottomSide().next(message);
    assertEquals(result.get(0), "cba");
  }
}