public class SelectionSort{
	public static void main(String[] args){
		int[] input = {1,3,4};
		SelectionSort.selectionAlgo(input);
	}
	public static void selectionAlgo(int [] input){
		for(int i=0;i<input.length;i++){
			int idxSmall = i;
			System.out.println("Im at index "+ i + " of the first loop");
			for(int x=i+1;x < input.length; x++){
			   System.out.println("Im at index  "+ x + " of the second loop");
				if(input[x] < input[idxSmall]){
				    System.out.println("Update the current idxSmall");
					idxSmall = x;
				
				}
			}
			int tmp = input[i];
			input[i] = input[idxSmall];
			input[idxSmall] = tmp;
		}
		
        for(int n=0;n < input.length;n++){
            System.out.println(input[n]);
        }
	}


}

