public abstract class AbstractActivity extends 
	  Activity implements View.OnClickListener, 
	  View.OnLongClickListener, TextToSpeech.OnInitListener {
  //The ontology individuals
  private List<String> buttons, edits, textViews, audios, 
  displays, noises, lights, backgrounds, devices, contexts;

  /** This methods initializes several classes representing
    * the knowledge in the AdaptUIOnt ontology.
  **/
  public void initOntology() {
    buttons = ontManager.getIndividualOfClass("Button");
    edits = ontManager.getIndividualOfClass("EditText");
    // And so forth with the rest of declared individuals		
    ontology_initialized = true;
  }

  /** This methods gets all the individuals from the ontology
    * and removes all previous values. The only remaining
    * values are the ones in the Adaptation individual.
  **/
  protected void removeAllValuesFromOntology() {
    List <String> views = new ArrayList<String>();
    
    views.add(getButtons().get(0));
    views.add(getEditTexts().get(0));
    views.add(getTextViews().get(0));
    views.add(getBackgrounds().get(0));
    
    // For each view every value is removed
    for (int i = 0; i < views.size(); i++){
      ontManager.removeIndividualMembership(
			views.get(i), "viewHasColor");
      ontManager.removeIndividualMembership(
			views.get(i), "viewHasTextColor");
      ontManager.removeIndividualMembership(
			views.get(i), "viewHasTextSize");
      ontManager.removeIndividualMembership
			(views.get(i), "viewHasWidth");
      ontManager.removeIndividualMembership(
			views.get(i), "viewHasHeight");
    }
    
    // Finally, the membership is also removed
    ontManager.removeIndividualMembership(
			getAudios().get(0), "audioHasVolume");
    ontManager.removeIndividualMembership(
			getAudios().get(0), "audioHasApplicable");
    ontManager.removeIndividualMembership(
			getDisplays().get(0), "displayHasBrightness");
    //...and so forth
  }

  //...
}
