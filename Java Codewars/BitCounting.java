// Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.
// Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
public class BitCounting {

	public static int countBits(int n){
		// Show me the code!
//      int n;
//        
//         Scanner s = new Scanner(System.in);
//         System.out.print("Enter any decimal number:");
//         n = s.nextInt();
        int count = 0, a;
         String x = "";
        while(n > 0)
        {
            a = n % 2;
            if(a == 1)
            {
                count++;
            }
            x = a + "" + x;
            n = n / 2;
        }
       return count;
	}
	
}