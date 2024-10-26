import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class Project {
    public static void main(String[] args) throws Exception {
    	
    	if (args.length !=2){
    		System.err.println("usuage: project");
    		System.exit(-1);
    	}
        Configuration conf = new Configuration();
        
        Job job = Job.getInstance(conf, "Fraud Detection");
        job.setJarByClass(Project.class);  
        
        job.setMapperClass(FraudDetectionMapper.class);
        job.setReducerClass(FraudDetectionReducer.class);
        
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(DoubleWritable.class);
        
        FileInputFormat.addInputPath(job, new Path(args[0]));  
        FileOutputFormat.setOutputPath(job, new Path(args[1])); 

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}




