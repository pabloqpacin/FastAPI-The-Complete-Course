# 00-oop_game

> [!NOTE]
> Info en [../CURSO.md](/CURSO.md)


Jugar:

```bash
python3 ./main.py
  # Hero has equipped a weapon!
  # *Grumbling...
  # -----
  # Zombie: 10 HP left!
  # Hero: 10 HP left!
  # Zombie attacks for 1 damage.
  # Hero attacks for 6 damage.
  # -----
  # Zombie: 4 HP left!
  # Hero: 9 HP left!
  # Zombie attacks for 1 damage.
  # Hero attacks for 6 damage.
  # -----
  # Hero wins!
```

Contra el zombie se gana fácil, contra el ogro está chungo. ¿Quieres probar?

```bash
sed -i '/# ogre =.*/s/^# //' ./main.py
sed -i '/hero_battle(hero,zombie)/s/zombie/ogre/' ./main.py

python3 00-oop_game/main.py
  # Hero has equipped a weapon!
  # Ogre is slamming hands all around.
  # -----
  # Ogre: 20 HP left!
  # Hero: 10 HP left!
  # Ogre attacks for 3 damage.
  # Hero attacks for 6 damage.
  # Ogre attack has increased by 4!
  # -----
  # Ogre: 14 HP left!
  # Hero: 7 HP left!
  # Ogre attacks for 7 damage.
  # Hero attacks for 6 damage.
  # -----
  # Ogre wins!
```

<!-- Posibles mejoras... -->

