public class CustomImplementation implements Parcelable {
  private int intAttribute;
  private float floatAttribute;

  public UserMinimumPreferences(int intAttr, float floatAttr) {
    super();
    this.intAttribute = intAttr;
    this.floatAttribute = floatAttr;
  }

  public CustomImplementation(Parcel in) { 
    readFromParcel(in); 
  }

  public static Parcelable.Creator<CustomImplementation> getCreator() {
    return CREATOR;
  }

  // Writing in the Parcelable object
  @Override
  public void writeToParcel(Parcel dest, int flags) {
    dest.writeInt(intAttribute);
    dest.writeFloat(floatAttribute);
  }

  // Reading from the Parcelable object
  private void readFromParcel(Parcel in) {   
    intAttribute = in.readInt();
    floatAttribute = in.readFloat();
  }
