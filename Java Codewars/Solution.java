/*Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

Examples
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"*/


import java.lang.StringBuilder;
class Solution{

  static String toCamelCase(String s){

s=s.replace('_','-');
System.out.println(s);
String[] splits = s.split("-");
String result=""+splits[0];
  for(int i =1 ; i<splits.length; i++)
  {
    String first = ""+splits[i].charAt(0);
    result+=first.toUpperCase();
    result+=splits[i].substring(1,splits[i].length());
  }
  return result;
}
}