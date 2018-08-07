package br.org.fatec.network1;

import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertIterableEquals;

class CharLayerTest {

    @Test
    void send() {
        CharLayer layer = new CharLayer();
        List<Character> result = new LinkedList<>();
        String message = "abc";
        layer.getBottomSide().addListener(result::add);
        layer.getTopSide().next(message);
        assertIterableEquals(Arrays.asList(new Character[]{'a', 'b', 'c', null}), result);
    }

    @Test
    void receive() {
        CharLayer layer = new CharLayer();
        List<String> result = new LinkedList<>();
        String message = "abc";
        layer.getTopSide().addListener(result::add);
        Arrays.asList(new Character[]{'a', 'b', 'c', null}).forEach(layer.getBottomSide()::next);
        layer.getTopSide().next(message);
        assertEquals(message, result.get(0));
    }
}