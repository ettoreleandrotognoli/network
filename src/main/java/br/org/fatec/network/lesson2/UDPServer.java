package br.org.fatec.network.lesson2;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class UDPServer {

  public static void main(String... args) throws Exception {
    DatagramSocket server = new DatagramSocket(8001);
    byte[] inputBuffer = new byte[1024];
    while (true) {
      DatagramPacket received = new DatagramPacket(inputBuffer, inputBuffer.length);
      server.receive(received);
      String message = new String(received.getData());
      InetAddress address = received.getAddress();
      int port = received.getPort();
      System.out.println(String.format("%s:%d >>> %s", address.toString(), port, message));
      DatagramPacket toSend = new DatagramPacket(inputBuffer, inputBuffer.length, address, port);
      server.send(toSend);
    }
  }
}
