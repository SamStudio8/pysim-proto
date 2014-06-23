import time

from sim import Entity, Controller, System, MessageQueue

mq = MessageQueue()
sim = System(mq)

class HootController(Controller):
    ATTRITION_DAMAGE_PER_UNIT = 0.5

    def tick(self, clock, dt):
        if clock > 18 or clock < 7:
            if self.entity.properties["hoot"]:
                if self.mq:
                    self.mq.emit("hoot_hoot", {
                        "origin": "ENTI",
                        "msg": "Entity %d hoots!" % self.entity.id,
                        "importance": " "
                    })
        if self.mq:
            self.mq.emit("hoot_health_ok", {
                "origin": "ENTI",
                "msg": "Entity %d suffers attrition!" % self.entity.id,
                "importance": " "
            })
        health = self.entity.get_property("health")
        self.entity.update_property("health", health - (self.ATTRITION_DAMAGE_PER_UNIT * dt))

        if clock == 0:
            if self.mq:
                self.mq.emit("hoot_health_ok", {
                    "origin": "ENTI",
                    "msg": "Entity %d receives a medical kit. Health restored." % self.entity.id,
                    "importance": " "
                })
            self.entity.update_property("health", 100)

hootcontroller = HootController(mq=mq)
hootcontroller.add_requirement("nocturnal")
hootcontroller.add_requirement("hoot")

sim.add_controller(hootcontroller)

hoot = Entity(mq)
hoot.add_property("nocturnal", True)
hoot.add_property("hoot", 1)
hoot.add_property("health", 100)

hoot.update_property("health", 80)
hoot.get_property("health")

while(1):
    for i in range(0, 23):
        sim.tick(1)
        time.sleep(2)

