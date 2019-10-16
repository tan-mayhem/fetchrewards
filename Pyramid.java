import java.util.*;

class Pyramid {
	public static void main(String[] args) {
		String str = args[0].toLowerCase();
		/* Check for null string */
		if(str.equals(""))
			System.out.println("false");

		int arr[] = new int[26];
		List <Integer> sorted = new ArrayList <>();
		int flag = 0;

		for(char c: str.toCharArray()) {
			arr[c - 'a']++;
		}

		for(int i : arr) {
			if(i > 0)
				sorted.add(i);
		}
		/* Sort the array list */
		Collections.sort(sorted);
		/* Check for pyramid word */
		for(int i = 0; i < sorted.size(); i++) {
			if(sorted.get(i) != i+1) {
				System.out.println("false");
				flag = 1;
				break;
			}
		}
		/* Return true if it is a pyramid word */
		if(flag == 0)
			System.out.println("true");
	}
}
