import fileinput
from datetime import datetime
"""
F1 Started at 19:00:01
F1 Started at 19:00:01
F1 Ended at 19:00:01
F2 Started at 19:00:02
F2 Ended at 19:00:03
F3 Started at 19:00:03
F3 Ended at 19:00:04
F1 Ended at 19:00:04
F1 Started at 19:00:01, Elapsed time = 3 sec
"""
logstack = [];
ident = 0;
msgstack = [];
for idx, line in enumerate( fileinput.input() ):
	#print line
	blocks = line.split();
	if idx == 0 :
		logstack.append(blocks);
	else:
		top = logstack[-1];
		#print top
		#print blocks
		#print top[0]
		#print blocks[0]
		if ( top[0] == blocks[0] ): #same method header
			if ( top[1] == "Started" and blocks[1] == "Ended" ):
				logstack.pop()
				start_time = datetime.strptime( top[3], '%H:%M:%S')
				end_time   = datetime.strptime( blocks[3], '%H:%M:%S')
				msg = "%s%s Started at %s, Elapsed time = %s sec"%("\t"*ident,top[0], top[3], (end_time-start_time).seconds )
				msgstack.append( msg )
				print msg
				ident-=1
			if ( top[1] == "Started" and blocks[1] == "Started" ):
				logstack.append( blocks )
				ident+=1
		else:
			#different method call
			logstack.append( blocks )
			ident+=1
			
#while len(msgstack) > 0 :
#	print msgstack[-1];
#	msgstack.pop();
				
				
		

	
