import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;

public class FraudDetectionReducer extends Reducer<Text, DoubleWritable, Text, Text> {
	@Override

    public void reduce(Text key, Iterable<DoubleWritable> values, Context context) throws IOException, InterruptedException {
        double sum = 0.0;
        int count = 0;  

        for (DoubleWritable val : values) {
            sum += val.get();
            count++;  
        }
        
        context.write(key, new Text("Count: " + count + ", Total Amount: " + sum));
    }
}