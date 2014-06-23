pysim-proto
===========

Prototyping structures for some form of simulator.

    python simtest.py

    [_MQ_][!] Message Queue Created.
    [SIM_][!] Simulator Created.
    [_MQ_][!] <sim.System object at 0x7f90b7e0a510> now listening for entity_new_property message types
    [CTRL][*] Controller 140259536971152 Created
    [_MQ_][!] <__main__.HootController object at 0x7f90b7e0a590> now listening for entity_gets_doctor message types
    [CTRL][ ] Requirement 'nocturnal' attached to Controller 140259536971152
    [CTRL][ ] Requirement 'hoot' attached to Controller 140259536971152
    [CTRL][*] Controller 140259536971344 Created
    [_MQ_][!] <__main__.DocController object at 0x7f90b7e0a650> now listening for entity_needs_doctor message types
    [CTRL][ ] Requirement 'has_doctorate' attached to Controller 140259536971344
    [SIM_][-] Controller 140259536971152 registered with Simulation
    [SIM_][-] Controller 140259536971344 registered with Simulation
    [ENTI][*] Entity 140259536971408 Created
    [ENTI][ ] Property-Value Pair nocturnal:True added to Entity 140259536971408
    [SIM_][-] Simulation observing Entity 140259536971408
    [ENTI][ ] Property-Value Pair hoot:1 added to Entity 140259536971408
    [SIM_][ ] Controllers for Entity 140259536971408 destroyed after property change
    [SIM_][!] Controller 140259536971152 attached to Entity 140259536971408 after meeting requirements
    [ENTI][ ] Property-Value Pair health:100 added to Entity 140259536971408
    [SIM_][ ] Controllers for Entity 140259536971408 destroyed after property change
    [SIM_][!] Controller 140259536971152 attached to Entity 140259536971408 after meeting requirements
    [ENTI][ ] Property-Value Pair health:80 updated in Entity 140259536971408
    [ENTI][ ] Property-Value Pair health:80 fetched from Entity 140259536971408
    [ENTI][*] Entity 140259536971472 Created
    [ENTI][ ] Property-Value Pair has_doctorate:True added to Entity 140259536971472
    [SIM_][-] Simulation observing Entity 140259536971472
    [SIM_][!] Controller 140259536971344 attached to Entity 140259536971472 after meeting requirements
    [SIM_][#] Simulation ticks forward to hour 0
    [ENTI][ ] Entity 140259536971408 hoots!
    [ENTI][ ] Entity 140259536971408 suffers attrition!
    [ENTI][ ] Property-Value Pair health:80 fetched from Entity 140259536971408
    [ENTI][ ] Property-Value Pair health:70 updated in Entity 140259536971408
    [SIM_][#] Simulation ticks forward to hour 1
    [ENTI][ ] Entity 140259536971408 hoots!
    [ENTI][ ] Entity 140259536971408 suffers attrition!
    [ENTI][ ] Property-Value Pair health:70 fetched from Entity 140259536971408
    [ENTI][ ] Property-Value Pair health:60 updated in Entity 140259536971408
    [SIM_][#] Simulation ticks forward to hour 2
    [ENTI][ ] Entity 140259536971408 hoots!
    [ENTI][ ] Entity 140259536971408 suffers attrition!
    [ENTI][ ] Property-Value Pair health:60 fetched from Entity 140259536971408
    [ENTI][ ] Property-Value Pair health:50 updated in Entity 140259536971408
    [SIM_][#] Simulation ticks forward to hour 3
    [ENTI][ ] Entity 140259536971408 hoots!
    [ENTI][ ] Entity 140259536971408 suffers attrition!
    [ENTI][ ] Property-Value Pair health:50 fetched from Entity 140259536971408
    [ENTI][ ] Property-Value Pair health:40 updated in Entity 140259536971408
    [SIM_][#] Simulation ticks forward to hour 4
    [ENTI][ ] Entity 140259536971408 hoots!
    [ENTI][ ] Entity 140259536971408 suffers attrition!
    [ENTI][ ] Property-Value Pair health:40 fetched from Entity 140259536971408
    [ENTI][ ] Property-Value Pair health:30 updated in Entity 140259536971408
    [SIM_][#] Simulation ticks forward to hour 5
    [ENTI][ ] Entity 140259536971408 hoots!
    [ENTI][ ] Entity 140259536971408 suffers attrition!
    [ENTI][ ] Property-Value Pair health:30 fetched from Entity 140259536971408
    [ENTI][ ] Property-Value Pair health:20 updated in Entity 140259536971408
    [SIM_][#] Simulation ticks forward to hour 6
    [ENTI][ ] Entity 140259536971408 hoots!
    [ENTI][ ] Entity 140259536971408 suffers attrition!
    [ENTI][ ] Property-Value Pair health:20 fetched from Entity 140259536971408
    [ENTI][ ] Property-Value Pair health:10 updated in Entity 140259536971408
    [ENTI][~] Entity 140259536971408 calls for medical aid!
    [ENTI][~] Entity 140259536971472 sends a medical kit to Entity 140259536971152.
    [ENTI][ ] Property-Value Pair health:100 updated in Entity 140259536971408
    [ENTI][ ] Entity 140259536971408 receives a medical kit. Health restored.
    [SIM_][#] Simulation ticks forward to hour 7
    [ENTI][ ] Entity 140259536971408 suffers attrition!
    [ENTI][ ] Property-Value Pair health:100 fetched from Entity 140259536971408
    [ENTI][ ] Property-Value Pair health:90 updated in Entity 140259536971408
    [SIM_][#] Simulation ticks forward to hour 8
