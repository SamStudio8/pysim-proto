class MessageQueue(object):

    def __init__(self):
        self.listeners = {}

    def listen(self, msg_type, listener):
        if msg_type not in self.listeners:
            self.listeners[msg_type] = []
        self.listeners[msg_type].append(listener)

    def emit(self, msg_type, data):
        # TODO Check for malformed messages...

        # Notify subscribers
        if msg_type in self.listeners:
            for listener in self.listeners[msg_type]:
                listener.notify(data)

        # Print log
        print "[%s][%s] %s" % (data["origin"],
                            data["importance"],
                            data["msg"])

class Entity(object):
    def __init__(self, system=None, mq=None, **kwargs):
        self.id = id(self)
        self.properties = kwargs

        self.observer = None
        self.mq = None

        if system:
            self.attach_system(system)
        if mq:
            self.attach_message_queue(mq)
            self.mq.emit("entity_created", {
                "origin": "ENTI",
                "msg": "Entity %d Created" % self.id,
                "importance": "*"
            })

    def add_property(self, key, value):
        if key in self.properties:
            raise Exception("Property already exists.")
        self.properties[key] = value

        if self.mq:
            self.mq.emit("entity_new_property", {
                "origin": "ENTI",
                "entity": self,
                "msg": "Property-Value Pair %s:%s added to Entity %d" % (key, str(value), self.id),
                "importance": " "
            })
        if self.observer:
            self.observer.notify(self)

    def update_property(self, key, value):
        if key not in self.properties:
            raise Exception("Property doesn't exist.")
        self.properties[key] = value

        if self.mq:
            self.mq.emit("entity_update_property", {
                "origin": "ENTI",
                "msg": "Property-Value Pair %s:%s updated in Entity %d" % (key, str(value), self.id),
                "importance": " "
            })

    def get_property(self, key):
        if key not in self.properties:
            raise Exception("Property doesn't exist.")

        if self.mq:
            self.mq.emit("entity_get_property", {
                "origin": "ENTI",
                "msg": "Property-Value Pair %s:%s fetched from Entity %d" % (key, str(self.properties[key]), self.id),
                "importance": " "
            })
        return self.properties[key]

    def attach_system(self, sim):
        self.observer = sim
        sim.notify(self)

    def attach_message_queue(self, mq):
        self.mq = mq


class Controller(object):
    def __init__(self, entity=None, mq=None, requirements=[]):
        self.id = id(self)
        self.entity = entity
        self.requirements = requirements
        self.mq = None

        if mq:
            self.attach_message_queue(mq)
            self.mq.emit("controller_created", {
                "origin": "CTRL",
                "msg": "Controller %d Created" % self.id,
                "importance": "*"
            })

    def attach_entity(self, entity):
        self.entity = entity
        if self.mq:
            self.mq.emit("controller_entity_attached", {
                "origin": "CTRL",
                "msg": "Entity %d attached to Controller %d" % (entity.id, self.id),
                "importance": "-"
            })

    def add_requirement(self, key):
        self.requirements.append(key)
        if self.mq:
            self.mq.emit("controller_requirement_attached", {
                "origin": "CTRL",
                "msg": "Requirement '%s' attached to Controller %d" % (key, self.id),
                "importance": " "
            })

    def attach_message_queue(self, mq):
        self.mq = mq

    def entity_meets_requirements(self, entity):
        return set(self.requirements).issubset(set(entity.properties.keys()))

    def tick(self, clock, dt):
        raise NotImplementedError()


class System(object):
    def __init__(self, mq):
        self.entities = []
        self.controllers = []
        self.entity_controllers = {}
        self.clock = 0
        self.mq = mq

    def add_controller(self, controller):
        self.controllers.append(controller)
        self.mq.emit("sim_controller_registered", {
            "origin": "SIM_",
            "msg": "Controller %d registered with Simulation" % controller.id,
            "importance": "-"
        })

    def auto_attach_controllers(self, entity):
        for controller in self.controllers:
            if controller.entity_meets_requirements(entity):
                self.attach_controller(entity, controller)
                self.mq.emit("sim_controller_autoattach", {
                    "origin": "SIM_",
                    "msg": "Controller %d attached to Entity %d after meeting requirements" % (controller.id, entity.id),
                    "importance": "!"
                })

    def attach_controller(self, entity, controller):
        self.entity_controllers[entity.id].append(controller)

    def tick(self, dt):
        self.mq.emit("sim_tick", {
            "origin": "SIM_",
            "msg": "Simulation ticks forward to hour %d" % self.clock,
            "importance": "#"
        })
        for entity in self.entity_controllers:
            for controller in self.entity_controllers[entity]:
                controller.tick(self.clock, dt)

        self.clock += 1
        self.clock = self.clock % 24

    def notify(self, entity):
        if entity not in self.entities:
            self.entities.append(entity)
            self.mq.emit("sim_observing_entity", {
                "origin": "SIM_",
                "msg": "Simulation observing Entity %d" % entity.id,
                "importance": "-"
            })

        if entity.id in self.entity_controllers:
            del self.entity_controllers[entity.id]
            self.mq.emit("sim_controllers_destroyed", {
                "origin": "SIM_",
                "msg": "Controllers for Entity %d destroyed after property change" % entity.id,
                "importance": " "
            })
        self.entity_controllers[entity.id] = []
        self.auto_attach_controllers(entity)

