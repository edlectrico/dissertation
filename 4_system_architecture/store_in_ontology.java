private void storeUserPreferencesIntoOntology() {
    ontManager.addDataTypePropertyValue(
	getAudios().get(0), "audioHasVolume", volumeLevel);
    ontManager.addDataTypePropertyValue(
	getDisplays().get(0), "displayHasBrightness", 
	userPrefs.getBrightness());  
    ontManager.addDataTypePropertyValue(
	getLights().get(0), "contextHasLight", userPrefs.getLuxes());
    //...and so forth
}
