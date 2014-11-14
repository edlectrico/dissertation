static final int MAX_BRIGHTNESS = 1F;
static final int MIN_BRIGHTNESS = 0;

brightnessPicker = (NumberPicker) findViewById(R.id.brightness_picker);
brightnessPicker.setMinValue(MIN_BRIGHTNESS);

WindowManager.LayoutParams layoutParams = getWindow().getAttributes();
layoutParams.screenBrightness = MAX_BRIGHTNESS;
getWindow().setAttributes(layoutParams);

currentBrightness = android.provider.Settings.System.
			getInt(getContentResolver(), 
			android.provider.Settings.System.
			SCREEN_BRIGHTNESS,-1);

brightnessPicker.setMaxValue(currentBrightness);
