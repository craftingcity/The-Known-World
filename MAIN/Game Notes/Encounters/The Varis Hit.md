---
tags: encounter, monster
aliases:
---
# Description
This is an ambush by a group of Elite Drow. This is a Deadly encounter for a 4 player party of level 13 characters. It is worth 20,400 experience points. 

1 Captain, 1 Healer, 3 Bruiser, 4 Sniper.

This is the encounter with [[The Whitimore]] that the current party is going to encounter. It is tailored to beat the main threats as best they can, i.e. the Whitimore are going to target Varis first at all times, lock down Grod to the best of their ability (see nets and paralysis poison), and engage Bardaux and Amashod up close. They will not engage if the party has the *iron horn of valhalla* available, and will attempt to swipe it if necessary.

## Insults and Phrases
https://www.elfdict.com/
- "You stay right there scaled one"; "halld~e mori*h*loc~e"
- "I'll shoot the wizard"; "qui*h*tan o istar"
- "Form up! Form up! Lets do this right/beautiful!"; "ohtapanna! ohtapanna! carty~e sina vanima!"
- "bow warrior / spell warrior / axe warrior"; "peng daug/ daug oluhtu/ hathol daug"
# Stats

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
	- Athletics: 13
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
	- [The Captain gets two legendary actions per round]
    - [Longsword (1), The Captain makes one longsword attack.]
    - [Combo Shot (2), The Captain makes a grapple attack. If it succeeds, an ally within 30ft may use their reaction to make a ranged weapon attack against the target.]
	- [Regroup (1), The Captain points to an ally within 60 feet, they use their reaction to move their speed toward him.]
reactions:
    - [Trip, When a creature exits the Captian's combat range, it makes a DEX saving throw. If it fails, it falls prone where it exited combat range.]
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
hit_dice: 21d8
speed: 30 ft
stats: [24, 18, 17, 12, 10, 8]
skillsaves:
    - Stealth: +9
damage_resistances: see below
senses: darkvision 60ft
languages: undercommon, elvish
cr: 8
traits:
    - [Well Prepared, The Bruiser has resistance to two types of elemental damage.]
actions:
    - [Multiattack, As an action, the Bruiser makes three Wicked Scimitar attacks.]
    - [Wicked Scimtar, Melee Weapon Attack: +10 to hit, 2d6+7]
	- [Takedown, As an action, the Bruiser makes two grapple or push attacks: ]
	- [Wire Net, As an action, the Brusier makes a wire net attack. (+10 to hit, restrained on hit; DC 14 strength check or 15 slashing damage removes the condition)]
```

```statblock
name: Whitimore Assassin
size: medium
type: humaniod
subtype: drow
alignment: chaotic evil
ac: 14
hp: 41
hit_dice: 10d8
speed: 30ft
stats: [12, 22, 11, 15, 13, 12]
skillsaves:
    - Stealth: 9
senses: darkvision 60ft
languages: undercommon, elvish
cr: 7
traits:
    - [Assasinate, During its first turn, the creature has advantage on attack rolls against any creature that hasn't taken a turn. Any hit the creature scores against a surprised creature is a critical hit.]
	- [Sneak Attack, Once per turn, the assassin deals an extra 24 (7d6) damage when it hits a target with a weapon attack and has advantage on the attack roll, or when the target is within 5 feet of an ally of the assassin that isn't incapacitated and the creature doesn't have disadvantage on the attack roll.]
actions:
    - [Longbow, As an action, the Assassin makes a longbow attack (+9 to hit, 1d8+6 peircing damage).]
    - [Multiattack, As an action, the Assassin makes two longbow attacks.]
	- [Harmful Poison, As a bonus action, the Assassin applies a harmful poision to their next arrow. When struck, the target takes an additional 63 (8d6+35) poision damage. Two uses.]
	- [Paralitic Poison, As a bonus action, the Assassin applies a paralitic poison to their next arrow. When struck, the target is paralized unless they succeed on a DC 16 Constitution saving throw ]
    - [Shadow Stealth, While in dim light or darkness, the creature can take the Hide action as a bonus action.]
```