public class Main {
  private final static String ADAPTUI = "original/adaptui.owl";
  private static final String NAMESPACE = 
		"http://www.morelab.deusto.es/ontologies/adaptui.owl#";

  public static void main(String[] args) {
    AdaptUI adaptUI = new AdaptUI();

    // Loading the ontology through the ontology manager
    adaptUI.loadOntologyFromFile(new FileInputStream(
    	new File(ADAPTUI)));
    // TODO: create a new class

    // TODO: create a new individual of the created class

    // TODO: create a new datatype property for the individual

    // TODO: create a new object property for the individual

    // TODO: create a new SWRL rule

    // TODO: modify a Button instance background color

    // Storing the ontology modifications
    try {
      adaptUI.saveOntology("stored/test.owl");
    } catch (OntologySavingException e) {
      e.printStackTrace();
    }		
  }
  // Check methods
  // ...
  // checkClassInsertion(NAMESPACE, className);
  // ...
}
