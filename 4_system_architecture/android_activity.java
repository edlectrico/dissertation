  public class ExampleActivity extends Activity {
    
    private Button button;
    
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Here we can initialize components for this activities,
        // such as buttons, text views, etc.
        
        button = (Button) findViewById(R.id.button_example);
    }
}
