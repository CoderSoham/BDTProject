import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;

public class FraudDetectionMapper extends Mapper<Object, Text, Text, DoubleWritable> {

    private Text transactionType = new Text();  
    private DoubleWritable amount = new DoubleWritable();  
    
    @Override

    public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
        String[] fields = value.toString().split(",");
        
        if (fields[0].equals("Time")) { 
        	return;
         
        }
        
        try{
        	int classIndex = fields.length-1; 
        	String classValue = fields[classIndex];
        	double amountValue =  Double.parseDouble(fields[classIndex - 1]);
        	if(classValue.equals("1")){
        		transactionType.set("Fraud");
        	}
        	else{
        		transactionType.set("Legitimate");
        	}
        	amount.set(amountValue);
        	context.write(transactionType,amount);
        }
        catch(NumberFormatException e){
        	System.err.println("number format for inout:"+value.toString ());
        }
        catch(ArrayIndexOutOfBoundsException e){
        	System.err.println("Array index out of bounds forinput:" + value.toString());
        }
        
        
    }
}