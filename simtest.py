import time

from sim import Entity, Controller, System, MessageQueue

mq = MessageQueue()
sim = System(mq)

class HootController(Controller):
    ATTRITION_DAMAGE_PER_UNIT = 10

    def __init__(self, mq):
        super(HootController, self).__init__(self, mq)
        self.mq.listen("entity_gets_doctor", self)

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
            self.mq.emit("hoot_health_loss", {
                "origin": "ENTI",
                "msg": "Entity %d suffers attrition!" % self.entity.id,
                "importance": " "
            })
        health = self.entity.get_property("health")
        health -= (self.ATTRITION_DAMAGE_PER_UNIT * dt)
        self.entity.update_property("health", health)

        if health <= 10:
            if self.mq:
                self.mq.emit("entity_needs_doctor", {
                    "origin": "ENTI",
                    "entity": self.entity,
                    "msg": "Entity %d calls for medical aid!" % self.entity.id,
                    "importance": "~"
                })

    def notify(self, msg_type, data):
        if msg_type == "entity_gets_doctor":
            if data["id"] == self.entity.id:
                self.entity.update_property("health", 100)
                if self.mq:
                    self.mq.emit("hoot_health_ok", {
                        "origin": "ENTI",
                        "msg": "Entity %d receives a medical kit. Health restored." % self.entity.id,
                        "importance": " "
                    })


class DocController(Controller):

    def __init__(self, mq):
        super(DocController, self).__init__(self, mq)
        self.mq.listen("entity_needs_doctor", self)

    def notify(self, msg_type, data):
        if msg_type == "entity_needs_doctor":
            self.mq.emit("entity_gets_doctor", {
                "origin": "ENTI",
                "id": data["entity"].id,
                "msg": "Entity %d sends a medical kit to Entity %d." % (self.entity.id, data["entity"].id),
                "importance": "~"
            })

    def tick(self, clock, dt):
        pass

hootcontroller = HootController(mq=mq)
hootcontroller.add_requirement("nocturnal")
hootcontroller.add_requirement("hoot")

doccontroller = DocController(mq=mq)
doccontroller.add_requirement("has_doctorate")

sim.add_controller(hootcontroller)
sim.add_controller(doccontroller)

hoot = Entity(mq)
hoot.add_property("nocturnal", True)
hoot.add_property("hoot", 1)
hoot.add_property("health", 100)

hoot.update_property("health", 80)
hoot.get_property("health")


doctor = Entity(mq)
doctor.add_property("has_doctorate", True)

while(1):
    for i in range(0, 23):
        sim.tick(1)
        time.sleep(2)

