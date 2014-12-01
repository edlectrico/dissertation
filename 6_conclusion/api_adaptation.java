public void adapt(){
  AdaptUI adaptUI = new AdaptUI(namespace, views);

  // Current API
  adaptUI.addClass(namespace, className);
  adaptUI.addIndividualMembership(namespace, 
		indName, className);
  adaptUI.addDataTypePropertyValue(namespace, 
		indName, dataPropName, value);
  adaptUI.addObjectProperty(namespace, 
		indName1, indName2, objPropName);

  // Future API
  Individual ind = adaptUI.createIndividual(namespace);
  ind.putClass(className);
  ind.putName(indName);
  ind.putDatatypeProperty(dataProperty);
  ind.putObjectProperty(objProperty);
}
