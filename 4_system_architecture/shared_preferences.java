//Creating a shared preference
  SharedPreferences  mPrefs = getPreferences(MODE_PRIVATE);

  //Saving data
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

  --------------------------------------------------------

  //If we desing our own class
  public class CustomImplementation implements Parcelable {

  private int intAttribute;
  private float floatAttribute;
  
  public UserMinimumPreferences(int intAttr, float floatAttr) {
    super();
    this.intAttribute 	= intAttr;
    this.floatAttribute = floatAttr;
  }
  
  public CustomImplementation(Parcel in) { 
    readFromParcel(in); 
  }
  
  public static Parcelable.Creator<CustomImplementation> getCreator() {
    return CREATOR;
  }
  
  @Override
  public void writeToParcel(Parcel dest, int flags) {
    dest.writeInt(intAttribute);
    dest.writeFloat(floatAttribute);
  }
  
  private void readFromParcel(Parcel in) {   
    intAttribute   = in.readInt();
    floatAttribute = in.readFloat();
  }
