from sim import Entity, Controller, System

sim = System()

hootcontroller = Controller()
hootcontroller.add_requirement("nocturnal")
hootcontroller.add_requirement("hoot")

sim.add_controller(hootcontroller)

hoot = Entity()
hoot.attach_system(sim)
hoot.add_property("nocturnal", True)
hoot.add_property("hoot", 0)
hoot.add_property("health", 100)

hoot.update_property("health", 80)
hoot.get_property("health")


