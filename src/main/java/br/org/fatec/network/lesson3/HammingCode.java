package br.org.fatec.network.lesson3;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Function;

public class HammingCode {

  int size;

  static class ParityIndexGenerator {

    int index;
    int size;

    public ParityIndexGenerator(int index, int size) {
      this.index = index;
      this.size = size;
    }

    public void subscribe(Function<Integer, ?> observer) {
      for (int startAt = index; startAt <= size; startAt += (index * 2)) {
        int stopAt = startAt + index;
        for (int i = startAt; i < stopAt; i += 1) {
          observer.apply(i);
        }
      }
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

    void subscribe(Function<Parity, ?> observer) {
      for (int i = 1; Math.pow(2, i) <= size; i += 1) {
        observer.apply(new Parity((int) Math.pow(2, i), size));
      }
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
