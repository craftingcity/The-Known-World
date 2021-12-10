---
tags: encounter, monster
aliases:
---
# Description
This is the encounter with [[The Whitimore]] that the current party is going to encounter. It is tailored to beat the main threats as best they can, i.e. the Whitimore are going to target Varis first at all times, lock down Grod to the best of their ability (see nets and paralysis poison), and engage Bardaux and Amashod up close.

## Insults and Phrases
- "You stay right there scaled one"; "halld~e mori*h*loc~e"
- "I'll shoot the wizard"; "qui*h*tan o istar"
# Stats
remove me

party compisition
- captain
- healer
- mage
- bruisers
- snipers

captain
> the big bad, hits hard, hard to hit, lasts long, interesting ability. sick splint mail, shield, hype longsword

42 AAD
19 AC
+5 STAT
122 HP
+4 PRF
legendary resist: 3
legendary actions: 2
- basic attack; 1
- combo shot; 2 (grappled into ally w/in 30 ranged attack)
- trip; 2 (dex save or prone)
*aggressive* - "As a bonus action, the creature can move up to its speed toward a hostile creature that it can see."
*leadership* - "As an action the creature utters a command. For 1 minute, whenever nonhostile creatures that it can see within 30 feet of it makes an attack roll or saving throw the creature can add a d4 to its roll provided it can hear and understand the creature. A creature can benefit from only one Leadership die at a time. This effect ends if the leader is incapacitated."

healer
> alchemisty/divine healer; crossbow of healing and spells

12 AAD
16 AC
+0 STAT
0 HP
35 MBP

mage
12 AAD
14 AC
+0 STAT
0 HP
37 MBP

bruiser
0 AAD
18 AC
+0 STAT
0 HP
41 MBP

ranged/poison
12 AAD
14 AC
+0 STAT
0 HP
37 MBP

```statblock
name: Whitimore Sniper
size: Medium
type: humainoid
subtype: drow
alignment: chaotic evil
ac: number
hp: number
hit_dice: string
speed: string
stats: [number, number, number, number, number, number]
fage_stats: [number, number, number, number, number, number, number, number, number]
saves:
    - <ability-score>: number
skillsaves:
    - <skill-name>: number
damage_vulnerabilities: string
damage_resistances: string
damage_immunities: string
condition_immunities: string
senses: string
languages: string
cr: number
spells:
    - <description>
    - <spell level>: <spell-list>
traits:
    - [<trait-name>, <trait-description>]
    - ...
actions:
    - [<trait-name>, <trait-description>]
    - ...
legendary_actions:
    - [<legendary_actions-name>, <legendary_actions-description>]
    - ...
reactions:
    - [<reaction-name>, <reaction-description>]
    - ...
```