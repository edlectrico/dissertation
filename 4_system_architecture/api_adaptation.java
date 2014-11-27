private static final NAMESPACE = 
	"http://www.morelab.deusto.es/ontologies/adaptui.owl#"

@Override
protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  setContentView(R.layout.activity);

  Button button = (Button) findViewById(R.id.button1);
  
  AdaptUI adaptUI = new AdaptUI();
  
  List<String> buttons = adaptUI.getIndividualsOfClass(
					NAMESPACE, "Button");

  button.setBackgroundColor(adaptUI.adaptViewBackgroundColor(
					buttons.get(0));
}
