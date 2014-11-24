@Override
protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  setContentView(R.layout.default_layout);

  // These declarations are needed if we want to
  // manipulate the elements from the default_layout
  layout = (GridLayout) findViewById(R.id.layout);
  textView = (TextView) findViewById(R.id.textView);
  button = (Button) findViewById(R.id.button);
  editText = (EditText) findViewById(R.id.editText);

  // Declaring the AdaptUI instance
  adaptUI = new AdaptUI(ADAPTUI_NAMESPACE, views);

  // Loading the required ontology
  adaptUI.loadOntologyFromFile(ONT_PATH, ONTOLOGY_FILE);

  // Adapting the UI elements with the corresponding
  // stored values in the ontology
  button.setBackgroundColor(adaptUI.adaptViewBackgroundColor(
	ADAPTUI_NAMESPACE, button.getClass().
	getSimpleName()));
  button.setTextColor(adaptUI.adaptViewTextColor(
	ADAPTUI_NAMESPACE, button.getClass().
	getSimpleName()));
  button.setTextSize(adaptUI.adaptViewTextSize(
	ADAPTUI_NAMESPACE, button.getClass().
	getSimpleName()));
  editText.setBackgroundColor(adaptUI.adaptViewBackgroundColor(
	ADAPTUI_NAMESPACE, editText.getClass().
	getSimpleName()));
  textView.setBackgroundColor(adaptUI.adaptViewBackgroundColor(
	ADAPTUI_NAMESPACE, textView.getClass().
	getSimpleName()));
  //...
}
