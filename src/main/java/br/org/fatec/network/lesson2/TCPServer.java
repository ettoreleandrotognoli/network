package br.org.fatec.network.lesson2;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class TCPServer {

  static class Mirror implements Runnable {

    protected InputStream inputStream;
    protected OutputStream outputStream;

    public Mirror(InputStream inputStream, OutputStream outputStream) {
      this.inputStream = inputStream;
      this.outputStream = outputStream;
    }

    public Mirror(Socket socket) throws IOException {
      this(socket.getInputStream(), socket.getOutputStream());
    }

    @Override
    public void run() {
      try {
        while (true) {
          this.outputStream.write(this.inputStream.read());
        }
      } catch (IOException ex) {
        ex.printStackTrace();
        return;
      }
    }
  }

  public static void main(String... args) throws Exception {
    ServerSocket serverSocket = new ServerSocket(8001);
    while (true) {
      Socket socket = serverSocket.accept();
      Thread thread = new Thread(new Mirror(socket));
      thread.start();
    }
  }
}
