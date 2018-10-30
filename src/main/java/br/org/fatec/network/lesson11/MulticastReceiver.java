package br.org.fatec.network.lesson11;

import java.net.DatagramPacket;
import java.net.InetAddress;
import java.net.MulticastSocket;
import java.net.NetworkInterface;

public class MulticastReceiver {
  protected MulticastSocket socket = null;
  protected byte[] buf = new byte[256];

  public void run() throws Exception {
    socket = new MulticastSocket(8001);
    InetAddress group = InetAddress.getByName("230.0.0.0");
    socket.setNetworkInterface(NetworkInterface.getByIndex(1));
    socket.joinGroup(group);
    while (true) {
      DatagramPacket packet = new DatagramPacket(buf, buf.length);
      socket.receive(packet);
      String received = new String(packet.getData(), 0, packet.getLength());
      System.out.println(String.format("%s:%d -> %s",
          packet.getAddress().getHostAddress(),
          packet.getPort(),
          received));
      if ("end".equals(received)) {
        break;
      }
    }
    socket.leaveGroup(group);
    socket.close();
  }

  public static void main(String... args) throws Exception {
    new MulticastReceiver().run();
  }
}