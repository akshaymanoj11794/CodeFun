// A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

// Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
import java.util.*;
public class PangramChecker {
  public boolean check(String sentence){
    //code
    Set<String> a = new HashSet<String>();
    String sl= sentence.toLowerCase();
    System.out.println(sl);

    for(int i =0 ; i<sl.length() ; i++)
    {
    char c= sl.charAt(i);
    if(c>=97 && c<123)
      a.add(""+c);

    }
          System.out.println(a.toString());

    if(a.size()==26)
      return true;
    
    return false;
    
  }
}