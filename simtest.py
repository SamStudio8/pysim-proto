import time

from sim import Entity, Controller, System, MessageQueue

sim = System()
mq = MessageQueue()

class HootController(Controller):
    ATTRITION_DAMAGE_PER_UNIT = 0.5

    def tick(self, clock, dt):
        if clock > 18 or clock < 7:
            if self.entity.properties["hoot"]:
                print "[ENTI][ ] Entity %d hoots" % (self.entity.id)
        print "[ENTI][ ] Entity %d suffers attrition!" % self.entity.id
        health = self.entity.get_property("health")
        self.entity.update_property("health", health - (self.ATTRITION_DAMAGE_PER_UNIT * dt))

        if clock == 0:
            print "[ENTI][ ] Entity %d receives a medical kit." % self.entity.id
            self.entity.update_property("health", 100)

hootcontroller = HootController()
hootcontroller.add_requirement("nocturnal")
hootcontroller.add_requirement("hoot")

sim.add_controller(hootcontroller)

hoot = Entity(sim, mq)
hootcontroller.attach_entity(hoot)
hoot.add_property("nocturnal", True)
hoot.add_property("hoot", 1)
hoot.add_property("health", 100)

hoot.update_property("health", 80)
hoot.get_property("health")

#while(1):
#    for i in range(0, 23):
#        sim.tick(1)
#        time.sleep(2)

