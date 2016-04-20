package pack;

import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Arrays;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JPasswordField;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

import com.opencsv.CSVReader;;

public class UiCSVConverter implements ActionListener {
	
	JFrame mainFrame;
	JLabel hostLabel,userLabel,passLabel,dictLabel,logLabel;
	JButton btnUpload,btnClear;
	JTextField txtHost,txtUser,txtDictPath;
	JPasswordField txtPwd;
	JPanel controlPanel;
	JTextArea commentTextArea;
	JScrollPane scrollPane;
	int flag;
	
	public static void main(String[] args) throws SQLException, ClassNotFoundException, IOException {
		
		UiCSVConverter uc=new UiCSVConverter();
		uc.initializeFrm_Lbl_Btn_DictTxt();

	}

	public void initializeFrm_Lbl_Btn_DictTxt()	{
		mainFrame = new JFrame("Postgres Coverter");
		mainFrame.setSize(400,400);
	    mainFrame.setLayout(new GridLayout(3, 1));
		mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		mainFrame.setLayout(null);
		placeComponents(mainFrame);
		mainFrame.setVisible(true);
		
		 controlPanel = new JPanel();
	      controlPanel.setLayout(new FlowLayout());

	      mainFrame.add(controlPanel);
	      mainFrame.setVisible(true);  
	      
	      commentTextArea = new JTextArea("Logs will be Displayed here",10,35);

	      JScrollPane scrollPane = new JScrollPane(commentTextArea);   
	      controlPanel.setBounds(-50, 200, 500, 300);
	      controlPanel.add(scrollPane);        
	      mainFrame.setVisible(true);  
		 
	}
	
	private void placeComponents(JFrame frame) {
		

		hostLabel = new JLabel("Host Name");
		hostLabel.setBounds(10, 10, 80, 25);
		frame.add(hostLabel);

		txtHost = new JTextField(200);
		txtHost.setBounds(130, 10, 260, 25);
		frame.add(txtHost);
		
		userLabel = new JLabel("User Name");
		userLabel.setBounds(10, 40, 80, 25);
		frame.add(userLabel);

		txtUser = new JTextField(200);
		txtUser.setBounds(130, 40, 260, 25);
		frame.add(txtUser);

		passLabel = new JLabel("Password");
		passLabel.setBounds(10, 70, 80, 25);
		frame.add(passLabel);

		txtPwd = new JPasswordField(200);
		txtPwd.setBounds(130, 70, 260, 25);
		frame.add(txtPwd);
		
		dictLabel = new JLabel("Directory path");
		dictLabel.setBounds(10, 100, 130, 25);
		frame.add(dictLabel);

		txtDictPath = new JTextField(200);
		txtDictPath.setBounds(130, 100, 260, 25);
		frame.add(txtDictPath);

		btnUpload = new JButton("Upload");
		btnUpload.setBounds(40, 140, 100, 25);
		frame.add(btnUpload);
		
		btnClear = new JButton("Clear");
		btnClear.setBounds(160, 140, 100, 25);
		frame.add(btnClear);
		
		ActionListener uploadButtonListener = new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {

				JOptionPane.showMessageDialog(null,"                Processing Your Request,\n   Click OK and wait back for process to be done\nYour Logs will be displayed Below after the process");
				
				//JButton source = (JButton) e.getSource();
				String hostname = txtHost.getText();
				String username = txtUser.getText();
				String password = txtPwd.getText();
				String filename1 = txtDictPath.getText();
			
				
				 Connection c = null;
				 Statement stmt = null;
				 
				 String directoryPath = filename1;
				 File[] filesInDirectory = new File(directoryPath).listFiles();
				 
				 commentTextArea.append("\nUploading Started\n");
				 
				 for(File f : filesInDirectory){
					 String filePath = f.getAbsolutePath();
				     String fileExtenstion = filePath.substring(filePath.lastIndexOf(".") + 1,filePath.length());
				     if("csv".equals(fileExtenstion)){
				    	 String filename = filePath;
				    	 String tableName=(String) filename.substring(filename.lastIndexOf("/")+1,filename.indexOf(".")).replaceAll("[^\\w]", "_").toLowerCase();
				    	 
				    	 String strHeader[];
				    	 CSVReader reader;
			    
					    try 
					        {
					    	Class.forName("org.postgresql.Driver");
					        c = DriverManager.getConnection("jdbc:postgresql://"+hostname+":5432/testdb",username, password);
					        stmt = c.createStatement();
					        StringBuilder colNames=new StringBuilder();
					         
					        reader = new CSVReader(new FileReader(filename));
					        
					        String[] row;
					     
					        DatabaseMetaData md = c.getMetaData();
					    	ResultSet rs = md.getTables(null, null, tableName, null);
					    	
					    	if(rs.next())	{
					    		String drpTable="drop table "+tableName+" restrict";
					    		stmt.executeUpdate(drpTable);
					    		
					    	}
					        
					        while ((row = reader.readNext()) != null)	{
					        	
					        	if(reader.getLinesRead()==1)	{
					        		
									System.out.println("Creation of "+tableName+" Started\n");
									
							        String firstRow=Arrays.toString(row);
							        
							        firstRow=firstRow.substring(1,firstRow.lastIndexOf("]"));
							        strHeader=firstRow.split(",");
							        
							        for(int k=0;k<strHeader.length;k++)	{
							        	strHeader[k]=strHeader[k].trim();
							           	strHeader[k]=strHeader[k].replaceAll("[^\\w]", "_");
							           	strHeader[k]=strHeader[k].toLowerCase();
							        	colNames.append(strHeader[k]+",");
							        }
							        colNames.deleteCharAt(colNames.length()-1);
							        
							        for(int i=0;i<strHeader.length;i++)	{
							        	strHeader[i]=strHeader[i].trim();
							           	strHeader[i]=strHeader[i].replaceAll("[^\\w]", "_");
							           	strHeader[i]=strHeader[i].toLowerCase();
							          	if(i == strHeader.length-1){
							          		strHeader[i]=strHeader[i]+" character varying";
							        	}
							        	else
							        		strHeader[i]=strHeader[i]+" character varying,";
							        }
							        
							        StringBuilder sb = new StringBuilder();
							        
							        
							        sb.append("create table ");
							        sb.append("\"");
							        sb.append(tableName);
							        sb.append("\"");
							        sb.append(" (id SERIAL primary key,");
							        for(int k=0;k<strHeader.length;k++)	{
							        	sb.append(strHeader[k]);
							        }
							        sb.append(");");
							       // System.out.println(sb.toString());
							        stmt.executeUpdate(sb.toString());
							        commentTextArea.append("Created : "+tableName+"\n");
							        flag=0;
							    } 
					        	else	{
					        		StringBuilder sb4=new StringBuilder();
					        		for(int i=0;i<row.length;i++)
					        			sb4.append("trim(?),");
					        		sb4.deleteCharAt(sb4.length()-1);
					        		
					        		PreparedStatement ps=c.prepareStatement("insert into "+tableName+" ("+colNames.toString()+") values("+sb4.toString()+")");
					        		for(int j=0;j<row.length;j++)	{
					        			if(row[j].length()==0){
							        		row[j]=null;
							        	}
					        			//System.out.println(ps.toString());
					        			ps.setString(j+1, row[j]);
					        		}
					        		ps.executeUpdate();
					        		flag=1;
					        		
					        	}
					        	
						    }
					        if( flag==1)
					        	commentTextArea.append("Inserted to : "+tableName+"\n");
					        
					}
			        catch (SQLException | IOException | ClassNotFoundException e1) 
			        {
			                JOptionPane.showMessageDialog(null,e1);
			        }
				     }
				     
				 }    
				 commentTextArea.append("Finished Uploading");
				 JOptionPane.showMessageDialog(null,"Uploaded Everyting");   
				
			}
		};
		btnUpload.addActionListener(uploadButtonListener);
		
		ActionListener clearButtonListener=new ActionListener(){
			@Override
			public void actionPerformed(ActionEvent e) {
				clear();
			}
		};
		btnClear.addActionListener(clearButtonListener);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		
	}
	
	
	public void clear() {
//		jtfName.setText("");
		txtHost.setText("");
		txtUser.setText("");
		txtPwd.setText("");
		txtDictPath.setText("");
		
	}

	

	
}
