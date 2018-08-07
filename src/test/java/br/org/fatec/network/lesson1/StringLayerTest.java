package br.org.fatec.network.lesson1;

import java.util.LinkedList;
import java.util.List;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class StringLayerTest {

  @Test
  void send() {
    StringLayer layer = new StringLayer();
    List<String> result = new LinkedList<>();
    String message = "message";
    layer.getBottomSide().addListener(result::add);
    layer.getTopSide().next(message);
    assertEquals(result.get(0), message);
  }

  @Test
  void receive() {
    StringLayer layer = new StringLayer();
    List<String> result = new LinkedList<>();
    String message = "message";
    layer.getTopSide().addListener(result::add);
    layer.getBottomSide().next(message);
    assertEquals(result.get(0), message);
  }
}