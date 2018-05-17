/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pregunta3;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.CallableStatement;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextField;
/**
 *
 * @author Andres
 */
public class Pregunta3 extends JPanel{

    private ArrayList<Integer> N;
    private ArrayList<String> esp;
    
    public Pregunta3(){
        setFocusable(true);
        N = new ArrayList<Integer>();
        esp = new ArrayList<String>();
    }
    
    public void AddN(Integer n){
        N.add(n);
    }
    
    public ArrayList<Integer> GetN(){
        return N;
    }
    
    public void AddEsp(String s){
        esp.add(s);
    }
    public ArrayList<String> GetEsp(){
        return esp;
    }
    
    public void SetValues(Integer id1, Integer id2) throws ClassNotFoundException, SQLException{
        
        Class.forName("com.mysql.jdbc.Driver");
        Connection con = DriverManager.getConnection("jdbc:mysql://quilla.lab.inf.pucp.edu.pe/a20152131?useSSL=false","a20152131","JajaSaludos");
        String sql = "{call CANT_NOMBRE_MED_ESP(?, ?, ?, ?, ?, ?)}";
        CallableStatement stmt = con.prepareCall(sql);
        
        stmt.registerOutParameter("_CANTIDAD_ESP1", java.sql.Types.INTEGER);
        stmt.registerOutParameter("_NOMBRE_ESP1", java.sql.Types.VARCHAR);
        stmt.registerOutParameter("_CANTIDAD_ESP2", java.sql.Types.INTEGER);
        stmt.registerOutParameter("_NOMBRE_ESP2", java.sql.Types.VARCHAR);
        stmt.setInt("_ID_ESPECIALIDAD1", id1);
        stmt.setInt("_ID_ESPECIALIDAD2", id2);
        
        stmt.executeUpdate();
        
        //AddEsp("BICA");
        AddEsp(stmt.getString(2));
        AddEsp(stmt.getString(4));
        //AddN(5);
        AddN(stmt.getInt(1));
        AddN(stmt.getInt(3));
        
        con.close();
    }
    
    public void paint(Graphics g){
        super.paint(g);
        int n = 0;
        g.drawLine(210, 150, 210, 420);
        g.drawLine(610, 150, 610, 420);
        g.drawLine(100, 380, 650, 380);
        if (N.size()>0){
            for (int i=0; i<N.size(); i++)
                n = n + N.get(i);
            for (int i=0; i<N.size(); i++){
                g.fillRect(210, 150+(i+1)*130/(N.size()+1)+i*50*2/N.size(), 400*N.get(i)/n, 50*2/N.size());
                g.drawString(N.get(i).toString(), 630, 150+(i+1)*130/(N.size()+1)+i*50*2/N.size()+25*2/(1+N.size()));
                g.drawString(esp.get(i), 80, 150+(i+1)*130/(N.size()+1)+i*50*2/N.size()+25*2/(1+N.size()));
            }            
        }
        N.clear();
        esp.clear();                        
    }
    
    public static void main(String[] args) {
        JFrame marco = new JFrame();
        Pregunta3 p = new Pregunta3();
        p.setLayout(null);

        JLabel label = new JLabel();
        label.setBounds(30, 70, 180, 30);
        label.setText("ID de la Segunda Especialidad: ");
        p.add(label);
        
        JLabel label1 = new JLabel();
        label1.setBounds(30, 30, 180, 30);
        label1.setText("ID de la Primera Especialidad: ");
        p.add(label1);
        
        JTextField texto = new JTextField();
        texto.setBounds(230,30,35,30);
        p.add(texto);
        
        JTextField texto1 = new JTextField();
        texto1.setBounds(230,70,35,30);
        p.add(texto1);
        
        JButton generador = new JButton("Generar Grafico");
        generador.setBounds(300,70,130,30);
        generador.addActionListener(new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                Integer id1 = Integer.parseInt(texto.getText());
                Integer id2 = Integer.parseInt(texto1.getText());
                try {
                    p.SetValues(id1, id2);
                } catch (ClassNotFoundException ex) {
                    Logger.getLogger(Pregunta3.class.getName()).log(Level.SEVERE, null, ex);
                } catch (SQLException ex) {
                    Logger.getLogger(Pregunta3.class.getName()).log(Level.SEVERE, null, ex);
                }
                p.repaint();
            }
        });
        marco.add(generador);
        
        marco.add(p);
        marco.setSize(750,500);
        marco.setVisible(true);
    }  
}
