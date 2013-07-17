class Player :

    str name
    int init_skill, init_stamina, init_luck #Initial character traits' values 
	int skill, stamina, luck #Current character traits' values
	int gold, jewels, potions, provisions #Collectible and usable items
    dict items #Equipment list	
	dict experiences #List of experiences with consequences