class Tes 
{
	public static boolean chekyer(int x)
	{
	  if (x%4!=0)return false;
      if (x%100!=0)return true;
      if (x%400!=0)return true;
      return false;
	}
	public static void main(String[] args) 
	{   int a[] = {31,28,31,30,31,30,31,31,30,31,30,31};
	    int b[] = {"January","February","March","April","May","June","July","August","September","October","November","December"};
		Scanner key = new Scanner(System.in);
		System.out.println("enter year: ");int yer = key.nextInt();
		if (chekyer(yer))
		{
			a[1] = 29;
		}
        for (int i = 0;i<12 ;i++ )
        {
			System.out.println(b[i]+" "+yer);
            while(cout < a[i])
            {   for (int k =0;k<5 ;k++ )
                {
                   System.out.print(cout+"/t");
				   cout++;
				}
				System.out.println("");
            }
        }
	}
}
