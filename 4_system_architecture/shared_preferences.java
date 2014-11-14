//Creating a shared preference
SharedPreferences  mPrefs = getPreferences(MODE_PRIVATE);

//Saving data in the editor
Editor editor = mPrefs.edit();
editor.putBoolean("key_name", true); 
editor.putString("key_name", "string value"); 
editor.commit();

//Retreiving data
mPrefs.getBoolean("key_name", null); 
mPrefs.getString("key_name", null);

//Removing data
editor.remove("key_name"); // will delete key name
editor.commit(); // commit changes

