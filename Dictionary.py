#Creating a 30-word dictionary using Pydroid 3

DATA = {
"Acceleration" : "the rate at which an object's velocity changes over time; includes both speed and direction.",
"Accuracy" : "the measurement of closeness to a true or standard value",
"Additive Manufacturing" : "A computer-led manufacturing process, also known as 3D printing, in which a machine layers materials, such as plastic, liquid and metal powder, to build three-dimensional objects.",
"Agitator" : "A device, also known as a mixer that puts objects into motion thrpugh shaking or stirring",
"AI" : "acronym for Artificial Intelligence, is the demonstration of cognition by computers and machines",
"Brittleness" : "a mechanical property of an object that measures the degree to which a material will fracture without significant deformation when subjected to stress.",
"CAD" : "Computer-aided Design is the digital creation of two-dimensional drawings and three-dimensional models using a computer system.",
"CAM" : "Computer-aided Manufacturing is a manufacturing method in which software and computer-controlled machines execute high-precision tasks to build products.",
"CNC" : "Computer Numerical Control is a computer-controlled manufacturing process in which progamming dictates tasks to a wide range of factory tools and machinery, from drills to lathes.",
"Code Compliance" : "is the adherance to a standardized area codes, from design standards to specifications and ordinance.",
"Cement" : "a building material that is a powder made of a mixture of calcined limestone and clay; used with water and sand or gravel to make concrete and mortar.",
"Circuit" : "an electric device providing path for current to flow.",
"Component" : "one of the individual parts making up a larger entity",
"Sketch" : "preliminary drawing dor later elaboration",
"Software" : "written programs operating on a computer system",
"Solar energy" : "energy from the sun that is concerted into thermal or electrical energy",
"Speed" : "a rate at which something happens",
"Fulcrum" : "the pivot about which a lever turns.",
"Gear" : "a toothed wheel that engages another toothed mechanism",
"Heat" : "a form of energy transferred by a difference in temperature",
"Hydraulics" : "study of mechanics of fluids",
"Impact" : "a forceful consequence; a strong effect",
"Inclined plane" : "a simple machine for elevating objects",
"Constraint" : "a limitation or restriction",
"Construction" : "the act of building something",
"Lever" : "a simple machine giving a mechanical advantage on a fulcrum",
"Load" : "weight to be borne or conveyed",
"Machine" : "a device for overcoming resistance by applying force",
"Momentum" : "the product of a body's mass and its velocity",
"Motion" : "a change of position not entailing a change of location"
}

def search():
    a = input("Enter a word: ")
    print(DATA[a])
    
while True:
    search()