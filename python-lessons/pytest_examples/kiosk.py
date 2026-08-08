class CoffeKiosk:
    """A kiosk that brews expresso with sufficient water and beans
    Example:
    >>> MaryCaffe = Kiosk(100, 50)
    >>> MarrCaffe.brew_expresso()
    >>> print(MarrCaffe.beans)
    82
    >>> print(MarrCaffe.water)
    20
    >>> ZakCaffe = Kiosk(17, 50)
    >>> ZakCaffe.brew_expresso
    Insufficient ingredients!
    """
    def __init__(self, beans_grams, water_ml):
        """
        Args:
            beans: quantity of beans provided to make the expresso
            water: quantity of water provided to make the expresso
        """
        self.beans = beans_grams
        self.water = water_ml
    
    def brew_expresso(self):
        if self.beans < 18 or self.water < 30:
            raise ValueError("Insufficient ingredients!")
        
        self.beans -= 18
        self.water -= 30

    