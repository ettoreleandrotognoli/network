package br.org.fatec.network.lesson11;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.InterfaceAddress;
import java.net.NetworkInterface;
import java.util.Enumeration;

public class BroadcastClient {

  private static DatagramSocket socket = null;

  public static void main(String... args) throws IOException {
    Enumeration<NetworkInterface> interfaces = NetworkInterface.getNetworkInterfaces();
    while (interfaces.hasMoreElements()) {
      NetworkInterface netInterface = interfaces.nextElement();
      for (InterfaceAddress address : netInterface.getInterfaceAddresses()) {
        InetAddress broadcastAddress = address.getBroadcast();
        if(broadcastAddress == null){
          continue;
        }
        System.out.println(broadcastAddress.getHostAddress());
        broadcast("Hello", address.getBroadcast());
      }
    }
  }

  public static void broadcast(String broadcastMessage, InetAddress address) throws IOException {
    socket = new DatagramSocket();
    socket.setBroadcast(true);

    byte[] buffer = broadcastMessage.getBytes();

    DatagramPacket packet = new DatagramPacket(buffer, buffer.length, address, 8001);
    socket.send(packet);
    socket.close();
  }
}