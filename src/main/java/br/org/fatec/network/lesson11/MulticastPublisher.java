package br.org.fatec.network.lesson11;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.InetAddress;
import java.net.MulticastSocket;
import java.net.NetworkInterface;

public class MulticastPublisher {
  private MulticastSocket socket;
  private InetAddress group;
  private byte[] buf;

  public void multicast(String message) throws IOException {
    socket = new MulticastSocket();
    socket.setNetworkInterface(NetworkInterface.getByIndex(1));
    group = InetAddress.getByName("230.0.0.0");
    buf = message.getBytes();

    DatagramPacket packet
        = new DatagramPacket(buf, buf.length, group, 8001);
    socket.send(packet);
    socket.close();
  }

  public static void main(String... args) throws Exception {
    new MulticastPublisher().multicast("teste");
  }
}