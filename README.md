pysim-proto
===========

Prototyping structures for some form of simulator.

    python simtest.py

    [CTRL][*] Controller 140540494570000 Created
    [CTRL][ ] Requirement 'nocturnal' attached to Controller 140540494570000
    [CTRL][ ] Requirement 'hoot' attached to Controller 140540494570000
    [SIM_][-] Controller 140540494570000 registered with Simulation
    [ENTI][*] Entity 140540494570128 Created
    [SIM_][-] Simulation observing Entity 140540494570128
    [CTRL][-] Entity 140540494570128 attached to Controller 140540494570000
    [ENTI][ ] Property-Value Pair nocturnal:True added to Entity 140540494570128
    [SIM_][ ] Controllers for Entity 140540494570128 destroyed after property change
    [ENTI][ ] Property-Value Pair hoot:1 added to Entity 140540494570128
    [SIM_][ ] Controllers for Entity 140540494570128 destroyed after property change
    [AUTO][*] Controller 140540494570000 attached to Entity 140540494570128 after meeting requirements
    [ENTI][ ] Property-Value Pair health:100 added to Entity 140540494570128
    [SIM_][ ] Controllers for Entity 140540494570128 destroyed after property change
    [AUTO][*] Controller 140540494570000 attached to Entity 140540494570128 after meeting requirements
    [ENTI][ ] Property-Value Pair health:80 updated in Entity 140540494570128
    [ENTI][ ] Property-Value Pair health:80 fetched from Entity 140540494570128

    [SIM_] Simulation ticks forward to hour 0
    [ENTI][ ] Entity 140540494570128 hoots
    [ENTI][ ] Entity 140540494570128 suffers attrition!
    [ENTI][ ] Property-Value Pair health:80 fetched from Entity 140540494570128
    [ENTI][ ] Property-Value Pair health:79.5 updated in Entity 140540494570128
    [ENTI][ ] Entity 140540494570128 receives a medical kit.
    [ENTI][ ] Property-Value Pair health:100 updated in Entity 140540494570128

    [SIM_] Simulation ticks forward to hour 1
    [ENTI][ ] Entity 140540494570128 hoots
    [ENTI][ ] Entity 140540494570128 suffers attrition!
    [ENTI][ ] Property-Value Pair health:100 fetched from Entity 140540494570128
    [ENTI][ ] Property-Value Pair health:99.5 updated in Entity 140540494570128

    [SIM_] Simulation ticks forward to hour 2
    [ENTI][ ] Entity 140540494570128 hoots
    [ENTI][ ] Entity 140540494570128 suffers attrition!
    [ENTI][ ] Property-Value Pair health:99.5 fetched from Entity 140540494570128
    [ENTI][ ] Property-Value Pair health:99.0 updated in Entity 140540494570128

    ...
