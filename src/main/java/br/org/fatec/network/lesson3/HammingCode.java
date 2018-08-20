package br.org.fatec.network.lesson3;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;

public class HammingCode {

  int size;

  static class ParityIndexGenerator {

    int index;
    int size;

    public ParityIndexGenerator(int index, int size) {
      this.index = index;
      this.size = size;
    }

    public Stream<Integer> stream() {
      return Stream.iterate(index, it -> it + (index * 2))
          .limit((int) Math.ceil(size / (2.0 * index)))
          .flatMap(it -> Stream.iterate(it, i -> i + 1).limit(index));
    }

    public int getIndex() {
      return index;
    }

    public int getSize() {
      return size;
    }
  }

  static class ParityGenerator {
    int size;

    public ParityGenerator(int size) {
      this.size = size;
    }

    public Stream<Parity> stream() {
      return Stream.iterate(1, it -> it + 1)
          .limit((int) Math.ceil(Math.log(size)))
          .map(it -> (int) Math.pow(2, it))
          .map(it -> new Parity(it, size));
    }
  }

  static class Parity {

    public boolean paritOf(String code) {
      boolean parityBit = false;
      ParityIndexGenerator generator = new ParityIndexGenerator(index, size);
      return parityBit;
    }

    int index;
    int size;

    public Parity(int index, int size) {
      this.index = index;
      this.size = size;
    }

    public int getIndex() {
      return index;
    }
  }

  List<Parity> parityList = null;

  public HammingCode(int size) {
    if (size <= 0) {
      throw new RuntimeException(String.format("%d is a valid size for hamming code", size));
    }
    this.size = size;
    this.parityList = new ArrayList<>((int) Math.ceil(Math.log(size)));
  }

  boolean check(String code) {
    if (code.length() != this.size) {
      throw new RuntimeException("Code with invalid size");
    }
    return false;
  }
}
