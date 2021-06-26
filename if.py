
indian=["somosa","dal","naan"]
chinese=["soup","fried rice","egg role"]
italian=["pizza","pasta","risotto"]

dish=input("Please enter a dish name:")
dish=str.lower(dish)
if dish in indian:
    print("indian")
elif dish in chinese:
    print("chinese")
elif dish in italian:
    print("italian")
else:
    print("No knowledge")