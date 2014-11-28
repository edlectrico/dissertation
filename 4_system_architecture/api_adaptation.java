private static final NAMESPACE = 
	"http://www.morelab.deusto.es/ontologies/adaptui.owl#"

@Override
protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  setContentView(R.layout.activity);
  
  // Fetch the desired view
  Button button = (Button) findViewById(R.id.button);
  // Initialize an AdaptUI instance
  AdaptUI adaptUI = new AdaptUI();
  // Fetch the desired views instances in the ontology, in
  // this case we want to adapt a button.
  List<String> buttons = adaptUI.getIndividualsOfClass(
					NAMESPACE, "Button");
  // Use Android default View methods to adapt the user
  // interface through retrieving the corresponding value
  // from the ontology
  button.setBackgroundColor(adaptUI.adaptViewBackgroundColor(
					buttons.get(0));
}
