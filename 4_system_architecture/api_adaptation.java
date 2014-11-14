private Button button1, button2;
private EditText edit1, edit2;
private TextView textView1, textView2;
private List<View> buttons, editTexts, textViews;

@Override
protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  setContentView(R.layout.activity);

  button1 = (Button) findViewById(R.id.button1);
  //button2, button3...
  buttons.add(button1);
  //...

  //Initializing adaptui
  AdaptuiAdapter adapter = new AdaptuiAdapter(getApplicationContext());

  //Calling different needed methods
  drawViews(adapter)
}

private void drawViews(AdaptuiAdapter adapter){
  adapter.adapt(buttons);
  //The same for other ui components
}
