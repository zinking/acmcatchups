object cci9mergeab {

  def merge_ab( a:List[Int], b:List[Int] ):List[Int]={
  
	def merge_ab_at( al:List[Int], ar:List[Int], b:List[Int] ):List[Int]={
 	    if( ar.isEmpty ) return al ::: b;
 	    if( b.isEmpty ) return al:::ar;
 	    if( b.head < ar.head )  return merge_ab_at( al:::List( b.head ) , ar, b.tail )
 	    else return merge_ab_at( al:::List( ar.head ) , ar.tail, b )
 	}
 	merge_ab_at( Nil, a, b )
  }                                             
   
  //merge_ab( List(1,3), List(2,4) )
  //merge_ab( List(1,3,5,7,9), List(2,4,6,8,10) )
  
  def merge_sort( a:List[Int] ):List[Int]={
  	//println( a.zipWithIndex )
  	def split_merge( a:List[Int] ): List[Int]={
  	    //println( a )
  	    val n = a.length;
  	    if (n < 2) return a
  	    //(al,ar)=a.zipWithIndex.partition( _._2 < a.length/2 );
  	    //val p = a.grouped( n/2+1 ).toList;
            //val p = a.partition( _ < a.head )
  	    return merge_ab(
  	    	   //split_merge(p(0)),split_merge(p(1))
              //split_merge( p._1 ), split_merge( p._2 )
              split_merge( List( a.head) ), split_merge( a.tail )
  	    );
  	}
  	split_merge(a)
  }                                               
  
  def main( args:Array[String] ){
      println( "helloworld" )
      println( merge_sort( List( 14, 13, 12 , 11 ) ) )
      println( merge_sort( List( 14, 13, 12 , 11 , 10, 9, 12, 29, 8, 18, 17 ) ) )
  }
  
}
