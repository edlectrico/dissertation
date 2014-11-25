private void modifyOntologyKnowldege() {
  // Adding a new class
  adaptUI.getOntologyManager().createClass(NAMESPACE + "Test");
  // Adding a new individual for the new class
  adaptUI.createIndividual("test", NAMESPACE, "Test");

  // Adding a new relationship between the new class
  // and the User class
  adaptUI.createObjectProperty(NAMESPACE + "test", 
	"hasObjectPropertyWith" + NAMESPACE + "User");

  // Creating a new datatype property for the 'test' 
  // invididual. Adding a new value for 'test'
  adaptUI.createDatatypeProperty(NAMESPACE + "test", 
	"hasDatatypeProperty");
  adaptUI.addDataTypePropertyValue(NAMESPACE + "test", 
	"hasDatatypeProperty", "string_value");
  
  // Creating a new datatype property for User
  adaptUI.createDatatypeProperty(NAMESPACE + "User", 
	"userHasTest");
  
  // Declaring a precedent and conseequent for adding
  // a new rule
  final String precedent = "adaptui:Test(?t) ^ 
	adaptui:User(?u) ^ hasDatatypeProperty(?t, ?value) ^ 
	swrb:equals(?value, 'string_value')";
  final String consequent = "userHasTest(?u, 'true')";
  
  adaptUI.createRule("testRule", antecedent, consequent);
}


