# class: blueprint or template of an object that we want to create (fruits could be a class!) a combination of properties and the functions
# objects: real elements that we will use within code (banana,apples,grapes, etc could all be objects of the fruit class)

# classes start with a capital letter, functions are all lowercase

# the init() function creates all the initial properties that you can change later for a class
# it gets automatically called 

# every function we create/attribute we apply for an object of a class must only apply for that specific object. 
# to create that differentiation, we use the keyword "self"

# we can list some proprties to be assigned to the ""

class Fruit():
    def __init__(self,colour,shape,taste,preference):
        self.colour=colour
        self.shape=shape 
        self.taste=taste
        self.preference=preference 
    
    # setter and getter functions can help restrict the control over the class/creating an encapsulation. 
    # setter can only let you set functions, getter can only retrieve and show you certain data

    # getter function 
    def get_shape(self):
        # we 
        return self.shape 
    # self.shape is a property within the init function

    # setter function
    def set_shape(self,newshape):
        self.shape=newshape 

    # custom function: increase preference 
    def increase_pref(self):
        self.preference+=1 
        # a faster way of adding/subtracting/multiplying a value to a variable itself 

    def fruitshow(self):
        print("Hello, I am a fruit with the colour {}, the shape {}, the taste {}, and the preference {},".format(self.colour,self.shape,self.taste,self.preference))

# we are about to create our first fruit object: apple

# r4eo create an dobject first, write the name
apple=Fruit("red","circle","good",5)

# now that wr've created apple, using any function within the class will now return data from the "self" that is apple 
apple.fruitshow() 



    
    

    






