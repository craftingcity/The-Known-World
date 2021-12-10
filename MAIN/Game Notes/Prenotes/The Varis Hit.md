---
tags: encounter, monster
aliases:
---
# Description
This is an Ambush by a group of Drow who are very very good at what they do.

This is the encounter with [[The Whitimore]] that the current party is going to encounter. It is tailored to beat the main threats as best they can, i.e. the Whitimore are going to target Varis first at all times, lock down Grod to the best of their ability (see nets and paralysis poison), and engage Bardaux and Amashod up close. They will not engage if the party has the *iron horn of valhalla* available, and will attempt to swipe it if necessary.

This is a Deadly encounter for a 4 player party of level 13 characters. It is worth 20,400 experience points. 1 Cap, 1 Healer, 3 Bruiser, 4 Sniper.

## Insults and Phrases
https://www.elfdict.com/
- "You stay right there scaled one"; "halld~e mori*h*loc~e"
- "I'll shoot the wizard"; "qui*h*tan o istar"
- "Form up! Form up! Lets do this right!"; ""
# Stats
remove me
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
*multiattack* - three longsword attacks
*aggressive* - "As a bonus action, the creature can move up to its speed toward a hostile creature that it can see."
*leadership* - "As an action the creature utters a command. For 1 minute, whenever nonhostile creatures that it can see within 30 feet of it makes an attack roll or saving throw the creature can add a d4 to its roll provided it can hear and understand the creature. A creature can benefit from only one Leadership die at a time. This effect ends if the leader is incapacitated."

healer
> alchemisty/divine healer; crossbow of healing and spells

12 AAD
16 AC
+4 STAT
64 HP
+3 PRF
*healing bolt* - As an action, the creature fires an injector bolt at an ally within range. They regain 2d4+2 hp. (5)
*boosting bolt* As an action, the creature fires an injector bolt at an ally within range. They gain +5ft speed and +2d4 melee weapon damage for 18 seconds. (2)
*spellcasting* - The Healer is a 9th level caster, uses WIS (DC 15, +7 attack, +4 SAM) has access to the following spells.
- cantrips; dancing lights, light, guidance, sacred flame, thaumaturgy
- 1st level (4); healing word, command, faerie fire, guiding bolt
- 2nd level (3); hold person, invisibility, moonbeam
- 3rd level (3); beacon of hope, counterspell, haste
- 4th level (1); banishment

bruiser
30 AAD
18 AC
+7 STAT
96 HP
+3 PRF

*multiattack* - 3 scimitar attacks
*net attack* - The creature makes an attack with its wire net (restrain on hit, DC 14 strength or 15 slash).
*well prepared* - The creature has resistance to two types of non-weapon damage. 

ranged/poison
12 AAD
14 AC
+6 avgSTAT
40 HP
+3 PRF
*multiattack* - two longbow bow attacks
*assasinate* - "During its first turn, the creature has advantage on attack rolls against any creature that hasn't taken a turn. Any hit the creature scores against a surprised creature is a critical hit."
*shadow stealth* - "While in dim light or darkness, the creature can take the Hide action as a bonus action."
*sneak attack* - Once per turn, the assassin deals an extra 24 (7d6) damage when it hits a target with a weapon attack and has advantage on the attack roll, or when the target is within 5 feet of an ally of the assassin that isn't incapacitated and the creature doesn't have disadvantage on the attack roll.
- harmful poisioned attack; +63 poison damage, two time use
- paralitic poison attack; dc 16 CON save or paralyzed save ends, one time use

```statblock
name: Whitimore Captain
size: Medium
type: humainoid
subtype: drow
alignment: chaotic evil
ac: 19
hp: 122
hit_dice: 27d8
speed: 30ft
stats: [20, 14, 16, 10, 15, 17]
skillsaves:
    - Stealth: 7
senses: darkvision (60ft)
languages: undercommon, elvish
cr: 10
actions:
	- [Longsword +1, The Captain makes a longsword attack (+10 to hit, 1d10 + 6 slashing damage).]
    - [Multiattack, The Captain makes three longsword attacks.]
    - [Aggresive, As a bonus action, the creature can move up to its speed toward a hostile creature that it can see.]
	- [Leadership, As an action the creature utters a command. For 1 minute, whenever nonhostile creatures that it can see within 30 feet of it makes an attack roll or saving throw the creature can add a d4 to its roll provided it can hear and understand the creature. A creature can benefit from only one Leadership die at a time. This effect ends if the leader is incapacitated.]
legendary_actions:
    - [Longsword (1), The Captain makes one longsword attack.]
    - [Combo Shot (2), The Captain makes a grapple attack. If it succeeds, an ally within 30ft may use their reaction to make a ranged weapon attack against the target.]
reactions:
    - [Trip, When a creature exits the Captian's combat range, it makes a DEX saving throw. If it fails, it falls prone where it exited combat range.]
    - ...
```

```statblock
name: Whitimore Healer
size: Meduim
type: humaniod
subtype: drow
alignment: chaotic evil
ac: 16
hp: 64
hit_dice: 14d8
speed: 30ft
stats: [9, 15, 11, 15, 19, 17]
skillsaves:
    - Stealth: 7
senses: darkvision 60ft
languages: undercommon, elvish
cr: 8
spells:
    - The Healer is a 9th level caster, uses WIS (DC 15, +7 attack) has access to the following spells
    - 1st level (4): healing word, command, faerie fire, guiding bolt
	- 2nd level (3): hold person, invisibility, moonbeam
	- 3rd level (3): beacon of hope, counterspell, haste
	- 4th level (1): banishment
actions:
	- [Spiked bolt, As an action, the healer makes a bolt-thrower attack (+5 to hit, 1d8+2 peircing damage).]
    - [Healing bolt, As an action, the creature fires an injector bolt at an ally within range. They regain 2d4+2 hp. Five uses.]
	- [Boosting Bolt, As an action, the creature fires an injector bolt at an ally within range. They gain +5ft speed and +2d4 melee weapon damage for 18 seconds. Two uses.]
```

```statblock
name: Whitimore Bruiser
size: meduim
type: humainoid
subtype: drow
alignment: chaotic evil
ac: 18
hp: 96
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

```statblock
name: string
size: string
type: string
subtype: string
alignment: string
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