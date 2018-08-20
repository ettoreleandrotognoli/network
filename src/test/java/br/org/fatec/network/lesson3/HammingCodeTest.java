package br.org.fatec.network.lesson3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.junit.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertIterableEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class HammingCodeTest {

  @Test
  public void makeParityIndexes() {
    List<Integer> result = new ArrayList<>(8);
    HammingCode.ParityIndexGenerator generator = new HammingCode.ParityIndexGenerator(1, 15);
    generator.stream().forEach(result::add);
    assertIterableEquals(result, Arrays.asList(1, 3, 5, 7, 9, 11, 13, 15));

    result.clear();
    generator = new HammingCode.ParityIndexGenerator(2, 15);
    generator.stream().forEach(result::add);
    assertIterableEquals(result, Arrays.asList(2, 3, 6, 7, 10, 11, 14, 15));

    result.clear();
    generator = new HammingCode.ParityIndexGenerator(4, 15);
    generator.stream().forEach(result::add);
    assertIterableEquals(result, Arrays.asList(4, 5, 6, 7, 12, 13, 14, 15));

    result.clear();
    generator = new HammingCode.ParityIndexGenerator(8, 15);
    generator.stream().forEach(result::add);
    assertIterableEquals(result, Arrays.asList(8, 9, 10, 11, 12, 13, 14, 15));
  }

  @Test
  public void makeParities() {
    List<HammingCode.Parity> result = new ArrayList<>(4);
    HammingCode.ParityGenerator generator = new HammingCode.ParityGenerator(15);
    generator.stream().forEach(result::add);
    for (int i = 0; i < result.size(); i += 1) {
      assertEquals(result.get(i).getIndex(), Math.pow(2, i));
    }
    assertEquals(4, result.size());

    result = new ArrayList<>(4);
    generator = new HammingCode.ParityGenerator(7);
    generator.stream().forEach(result::add);
    for (int i = 0; i < result.size(); i += 1) {
      assertEquals(result.get(i).getIndex(), Math.pow(2, i));
    }
    assertEquals(3, result.size());
  }

  @Test
  public void parityCheck() {

    HammingCode.Parity parity = new HammingCode.Parity(1, 7);
    assertTrue(parity.check("0000000"));
    assertTrue(parity.check("1010000"));
    assertTrue(parity.check("1010101"));

    assertFalse(parity.check("0000001"));
    assertFalse(parity.check("1000000"));
    assertFalse(parity.check("1010100"));
  }

  @Test
  public void hammingCheck() {
    HammingCode hammingCode = new HammingCode(7);
    assertFalse(hammingCode.check("0000100"));
    assertTrue(hammingCode.check("0000000"));
    hammingCode = new HammingCode(15);
    assertFalse(hammingCode.check("000100101010101"));
    assertTrue(hammingCode.check("001100101010101"));
  }

  @Test
  public void fix() {
    HammingCode hammingCode = new HammingCode(7);
    assertEquals("0000000", hammingCode.fix("0000100"));
    hammingCode = new HammingCode(15);
    assertEquals("001100101010101", hammingCode.fix("000100101010101"));
  }
}
