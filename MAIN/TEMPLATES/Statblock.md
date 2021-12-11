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
saves:
    - str: 3
skillsaves:
    - string: number
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
    - [string, string]
actions:
    - [string, string]
legendary_actions:
    - [string, string]
reactions:
    - [string, string]
```