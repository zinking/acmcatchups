
firstOrEmpty lst = if not (null lst ) then head lst else "emtpy"

lst1 +++ lst2 = if null lst1 
                   then lst2
                   else (head lst1):(tail lst1 +++ lst2 )