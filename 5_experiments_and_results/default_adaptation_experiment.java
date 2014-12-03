public class ActivityExample extends Activity {
  private GridLayout layout;
  private TextView textView;
  private Button button;
  private EditText editText;

  private static final String ONTOLOGY_FILE = "adaptui.owl";
  private static final String ONT_PATH = "/sdcard/ontologies/";
  private static final String ADAPTUI_NAMESPACE = 
	"http://www.morelab.deusto.es/ontologies/adaptui.owl#";

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.main_activity);
	
    layout = (GridLayout) findViewById(R.id.layout);
    textView = (TextView) findViewById(R.id.textView);
    button = (Button) findViewById(R.id.button);
    editText = (EditText) findViewById(R.id.editText);
    // Initializing the framework
    AdaptUI adaptUI = new AdaptUI(ADAPTUI_NAMESPACE, views);
    // Simulating context change with a listener
    button.setOnClickListener(new OnClickListener() {
    @Override
    public void onClick(View v) {
      // TODO: Change layout color (the name of the  
      // class is "Background")
			
      // TODO: Change button size (text size), and  
      // background and text color
			
      // TODO: Change edit text size (text size), and  
      // background and text color
			
      // TODO: Change text view size (text size), and  
      // background and text color
      }
    });
	
    adaptUI.loadOntologyFromFile(ONT_PATH, ONTOLOGY_FILE);
}
