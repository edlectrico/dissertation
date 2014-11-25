private void modifyOntologyKnowldege() {
    
  List<String> classes = (List<String>) ontManager.getClassList();
  System.out.println("Classes: " + classes.size());
  // Prints 'Classes: 18'

  // Any modification of the ontology knowledge is
  // performed through the OntologyManager instance,
  // which can be accessed through AdaptUI
  adaptUI.getOntologyManager().createClass(NAMESPACE + "Test");

  classes = (List<String>) ontManager.getClassList();
  System.out.println("Classes: " + classes.size());
  // Prints 'Classes: 19'
}

// OntologyManager class method
public void createClass(final String clz){
  OWLDataFactory factory = ontology.getOWLOntologyManager()
	.getOWLDataFactory();
  // Creating the class
  OWLClass clazz = factory.getOWLClass(IRI.create(clz));

  // This is necessary to make the ontology use
  // the new class, otherwise it would not refresh
  // the ontology
  OWLAxiom declareC = factory.getOWLDeclarationAxiom(clazz);
  manager.addAxiom(ontology, declareC);
}
