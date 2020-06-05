a = { 'x' : 1, 'y' : 2, 'z' : 3 }
b = { 'u' : 1, 'v' : 2, 'w' : 3, 'x'  : 1, 'y': 2 }
 
set( a.keys() ) & set( b.keys() )       # Output set(['y', 'x'])
 
set( a.items() ) & set( b.items() ) 