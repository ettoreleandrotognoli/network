package br.org.fatec.network.lesson2;

import java.io.DataOutputStream;
import java.net.Socket;
import java.util.Scanner;

public class TCPClient {

  public static void main(String... args) throws Exception {
    Socket socket = new Socket("127.0.0.1", 8001);
    DataOutputStream output = new DataOutputStream(socket.getOutputStream());
    Scanner scanner = new Scanner(socket.getInputStream());
    output.writeUTF("echo...\n");
    System.out.println(scanner.next());
    socket.close();
  }
}
