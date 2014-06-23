class Entity(object):
    def __init__(self, system=None, **kwargs):
        self.id = id(self)
        self.properties = kwargs
        self.observer = system
        print "[ENTI][*] Entity %d Created" % self.id

    def add_property(self, key, value):
        if key in self.properties:
            raise Exception("Property already exists.")
        self.properties[key] = value

        print "[ENTI][ ] Property-Value Pair %s:%s added to Entity %d" % (key, str(value), self.id)
        if self.observer:
            self.observer.notify(self)


    def update_property(self, key, value):
        if key not in self.properties:
            raise Exception("Property doesn't exist.")
        self.properties[key] = value
        print "[ENTI][ ] Property-Value Pair %s:%s updated in Entity %d" % (key, str(value), self.id)

    def get_property(self, key):
        if key not in self.properties:
            raise Exception("Property doesn't exist.")
        print "[ENTI][ ] Property-Value Pair %s:%s fetched from Entity %d" % (key, str(self.properties[key]), self.id)
        return self.properties[key]

    def attach_system(self, sim):
        self.observer = sim
        sim.notify(self)


class Controller(object):
    def __init__(self, entity=None, requirements=[]):
        self.id = id(self)
        self.entity = entity
        self.requirements = requirements
        print "[CTRL][*] Controller %d Created" % self.id

    def attach_entity(self, entity):
        self.entity = entity
        print "[CTRL][-] Entity %d attached to Controller %d" % (entity.id, self.id)

    def add_requirement(self, key):
        self.requirements.append(key)
        print "[CTRL][ ] Requirement '%s' attached to Controller %d" % (key, self.id)

    def entity_meets_requirements(self, entity):
        return set(self.requirements).issubset(set(entity.properties.keys()))

    def tick(self, clock, dt):
        raise NotImplementedError()


class System(object):
    def __init__(self):
        self.entities = []
        self.controllers = []
        self.entity_controllers = {}
        self.clock = 0

    def add_controller(self, controller):
        self.controllers.append(controller)
        print "[SIM_][-] Controller %d registered with Simulation" % controller.id

    def auto_attach_controllers(self, entity):
        for controller in self.controllers:
            if controller.entity_meets_requirements(entity):
                self.attach_controller(entity, controller)
                print "[AUTO][*] Controller %d attached to Entity %d after meeting requirements" % (controller.id, entity.id)

    def attach_controller(self, entity, controller):
        self.entity_controllers[entity.id].append(controller)

    def tick(self, dt):
        print "\n[SIM_] Simulation ticks forward to hour %d" % self.clock
        for entity in self.entity_controllers:
            for controller in self.entity_controllers[entity]:
                controller.tick(self.clock, dt)

        self.clock += 1
        self.clock = self.clock % 24

    def notify(self, entity):
        if entity not in self.entities:
            self.entities.append(entity)
            print "[SIM_][-] Simulation observing Entity %d" % entity.id

        if entity.id in self.entity_controllers:
            del self.entity_controllers[entity.id]
            print "[SIM_][ ] Controllers for Entity %d destroyed after property change" % entity.id
        self.entity_controllers[entity.id] = []
        self.auto_attach_controllers(entity)

