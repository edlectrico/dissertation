@Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity);

    //Get the stored parameters in the mobile
    Bundle bundle = getIntent().getExtras();
    userPrefs = bundle.getParcelable(getResources().
				getString(R.string.view_params));
    
    //Initializing an interface button
    btnNext = (Button) findViewById(R.id.button_next);
    
    //Calling different needed methods
    redrawViews();
    initializeServices(TAG);
    addListeners();
  }
  
  
  @Override
  public void redrawViews() {
    btnNext.setMinimumWidth(userPrefs.getButtonWidth());
    btnNext.setMinimumHeight(userPrefs.getButtonHeight());
    btnNext.setTextColor(userPrefs.getButtonTextColor());
    btnNext.setTextSize(userPrefs.getButtonTextSize());
  }
