AudioManager audioManager = (AudioManager) getSystemService(
				Context.AUDIO_SERVICE);
				  
volumePicker = (NumberPicker) findViewById(R.id.volume_picker);
volumePicker.setMinValue(0);
volumePicker.setMaxValue(audioManager.getStreamMaxVolume(
				AudioManager.STREAM_MUSIC));
