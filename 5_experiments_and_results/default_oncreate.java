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

  // It is impossible to specify any of the values
  // marked with the question mark without explicitly
  // asking the user
  button.setBackgroundColor(?);
  button.setTextColor(?));
  button.setTextSize(?);
  editText.setBackgroundColor(?);
  editText.setTextColor(?);
  editText.setTextSize(?);
  textView.setBackgroundColor(?);
  textView.setTextColor(?);
  textView.setTextSize(?);
}
