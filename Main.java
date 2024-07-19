import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException{
        Frame frame = new Frame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
        frame.setSize(1080, 720);
        frame.setResizable(true);
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        try{
            runCV();
        }
        catch(Exception e){
            System.out.println("Exception");
        }
    }

    public static void runCV() throws Exception{
        Process process = Runtime.getRuntime().exec("cvPractice.py");
    }
}