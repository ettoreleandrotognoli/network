package br.org.fatec.network.lesson2;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class UDPClient {

  public static void main(String... args) throws Exception {
    DatagramSocket client = new DatagramSocket();
    InetAddress address = InetAddress.getLoopbackAddress();
    byte[] outputBuffer = "echo...\n".getBytes();
    byte[] inputBuffer = new byte[1024];
    DatagramPacket toSend = new DatagramPacket(outputBuffer, outputBuffer.length, address, 8001);
    client.send(toSend);
    DatagramPacket receive = new DatagramPacket(inputBuffer, inputBuffer.length);
    client.receive(receive);
    System.out.println(new String(receive.getData()));
    client.close();
  }
}
